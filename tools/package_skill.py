#!/usr/bin/env python3
"""Validate and deterministically package the PlayPhrase.me skill."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPOSITORY_ROOT / "skills" / "playphraseme"
DEFAULT_OUTPUT = REPOSITORY_ROOT / "dist" / "skill.zip"
ARCHIVE_ROOT = PurePosixPath("playphraseme")
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
IGNORED_NAMES = {".DS_Store", "__pycache__", ".pytest_cache"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}
ALLOWED_TOP_LEVEL = {"SKILL.md", "agents", "assets", "references", "scripts"}


class ValidationError(ValueError):
    """Raised when the canonical skill cannot be packaged safely."""


def included_files(skill_root: Path = SKILL_ROOT) -> list[Path]:
    files: list[Path] = []
    for path in skill_root.rglob("*"):
        relative = path.relative_to(skill_root)
        if any(part in IGNORED_NAMES for part in relative.parts):
            continue
        if path.suffix in IGNORED_SUFFIXES:
            continue
        if relative.parts[0] not in ALLOWED_TOP_LEVEL:
            raise ValidationError(f"unexpected top-level skill content: {relative}")
        if path.is_symlink():
            raise ValidationError(f"symlinks are not allowed in the skill: {relative}")
        if path.is_file():
            files.append(path)
    return sorted(files, key=lambda path: path.relative_to(skill_root).as_posix())


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValidationError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValidationError("SKILL.md frontmatter is not closed") from error

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_-]*):\s+(.+)", line)
        if not match:
            raise ValidationError(f"unsupported frontmatter line: {line!r}")
        key, value = match.groups()
        if key in fields:
            raise ValidationError(f"duplicate frontmatter field: {key}")
        fields[key] = value.strip().strip('"\'')
    return fields


def validate_skill(skill_root: Path = SKILL_ROOT) -> list[Path]:
    if not skill_root.is_dir():
        raise ValidationError(f"skill directory does not exist: {skill_root}")

    files = included_files(skill_root)
    relative_files = {path.relative_to(skill_root).as_posix() for path in files}
    required = {"SKILL.md", "agents/openai.yaml"}
    missing = sorted(required - relative_files)
    if missing:
        raise ValidationError(f"missing required files: {', '.join(missing)}")

    skill_markdown_files = [path for path in files if path.name == "SKILL.md"]
    if len(skill_markdown_files) != 1:
        raise ValidationError("the package must contain exactly one SKILL.md")

    fields = parse_frontmatter(skill_root / "SKILL.md")
    if set(fields) != {"name", "description"}:
        raise ValidationError("SKILL.md frontmatter must contain only name and description")
    if fields["name"] != "playphraseme":
        raise ValidationError("SKILL.md name must be playphraseme")
    if len(fields["description"]) < 80:
        raise ValidationError("SKILL.md description is too short to route reliably")

    openai_yaml = (skill_root / "agents" / "openai.yaml").read_text(
        encoding="utf-8"
    )
    if "$playphraseme" in openai_yaml or "@PlayPhrase.me" in openai_yaml:
        raise ValidationError("openai.yaml default prompt must be platform-neutral")
    if "allow_implicit_invocation: true" not in openai_yaml:
        raise ValidationError("openai.yaml must allow implicit invocation")

    skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", skill_text):
        if "://" in target or target.startswith("#"):
            continue
        pure_target = PurePosixPath(target)
        if pure_target.is_absolute() or ".." in pure_target.parts:
            raise ValidationError(f"local reference escapes the skill directory: {target}")
        if target not in relative_files:
            raise ValidationError(f"referenced local file is missing: {target}")

    return files


def archive_name(path: Path, skill_root: Path = SKILL_ROOT) -> str:
    relative = PurePosixPath(path.relative_to(skill_root).as_posix())
    return (ARCHIVE_ROOT / relative).as_posix()


def build_archive(output: Path = DEFAULT_OUTPUT, skill_root: Path = SKILL_ROOT) -> Path:
    files = validate_skill(skill_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with ZipFile(output, "w") as archive:
        for path in files:
            relative = path.relative_to(skill_root)
            mode = 0o755 if relative.parts[0] == "scripts" else 0o644
            info = ZipInfo(archive_name(path, skill_root), FIXED_TIMESTAMP)
            info.create_system = 3
            info.external_attr = (0o100000 | mode) << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(
                info,
                path.read_bytes(),
                compress_type=ZIP_DEFLATED,
                compresslevel=9,
            )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    try:
        files = validate_skill()
        if args.validate_only:
            print(f"Validated playphraseme skill ({len(files)} files)")
            return 0
        output = build_archive(args.output)
    except (OSError, ValidationError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

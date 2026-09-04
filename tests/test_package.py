from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPOSITORY_ROOT / "tools" / "package_skill.py"
SPEC = importlib.util.spec_from_file_location("package_skill", MODULE_PATH)
assert SPEC and SPEC.loader
package_skill = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package_skill)


class SkillPackageTests(unittest.TestCase):
    def test_canonical_skill_is_valid(self) -> None:
        files = package_skill.validate_skill()
        relative = {
            path.relative_to(package_skill.SKILL_ROOT).as_posix() for path in files
        }
        self.assertIn("SKILL.md", relative)
        self.assertIn("agents/openai.yaml", relative)

    def test_archive_contains_one_clean_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "skill.zip"
            package_skill.build_archive(output)

            with ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                names = archive.namelist()

            expected = {
                package_skill.archive_name(path)
                for path in package_skill.validate_skill()
            }
            self.assertEqual(expected, set(names))
            self.assertEqual(1, sum(name.endswith("/SKILL.md") for name in names))
            self.assertTrue(all(name.startswith("playphraseme/") for name in names))
            for name in names:
                path = PurePosixPath(name)
                self.assertNotIn("..", path.parts)
                self.assertNotIn(".git", path.parts)
                self.assertNotIn("__pycache__", path.parts)
                self.assertFalse(name.endswith((".pyc", ".pyo", ".DS_Store")))

    def test_archive_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            first = package_skill.build_archive(directory / "first.zip")
            second = package_skill.build_archive(directory / "second.zip")
            first_hash = hashlib.sha256(first.read_bytes()).digest()
            second_hash = hashlib.sha256(second.read_bytes()).digest()
            self.assertEqual(first_hash, second_hash)

    def test_prompt_installation_remains_documented(self) -> None:
        repository_url = (
            "https://github.com/potapenko/playphraseme-language-learning-skill/"
            "tree/master/skills/playphraseme"
        )
        readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        installation = (
            package_skill.SKILL_ROOT / "references" / "platform-installation.md"
        ).read_text(encoding="utf-8")
        self.assertIn(repository_url, readme)
        self.assertIn(repository_url, installation)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path, PurePosixPath
from urllib.parse import parse_qs, urlsplit
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "package_skill.py"
SPEC = importlib.util.spec_from_file_location("package_skill", MODULE_PATH)
assert SPEC and SPEC.loader
package_skill = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package_skill)

EVIDENCE_PATH = ROOT / "evals" / "common_phrase_examples.json"
PATTERNS_PATH = ROOT / "skills" / "playphraseme" / "references" / "response-patterns.md"


def evidence_items() -> dict[str, int]:
    payload = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
    return {
        item["text"]: item["count"]
        for query in payload["queries"]
        for item in query["items"]
    }


def search_query(url: str) -> str:
    parsed = urlsplit(url)
    assert parsed.scheme == "https"
    assert parsed.netloc == "www.playphrase.me"
    route, _, query = parsed.fragment.partition("?")
    assert route == "/search"
    values = parse_qs(query)
    assert values.get("language") == ["en"]
    return values["q"][0]


class SkillPackageTests(unittest.TestCase):
    def test_canonical_skill_is_valid_and_instruction_only(self) -> None:
        files = package_skill.validate_skill()
        relative = {
            path.relative_to(package_skill.SKILL_ROOT).as_posix() for path in files
        }
        self.assertIn("SKILL.md", relative)
        self.assertIn("agents/openai.yaml", relative)
        self.assertIn("references/response-patterns.md", relative)
        self.assertFalse(any(path.endswith(".py") for path in relative))
        self.assertFalse(any(path.startswith("scripts/") for path in relative))

        packaged_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in files
            if path.suffix in {".md", ".yaml", ".yml"}
        )
        self.assertNotIn("playphrase_learning.py", packaged_text)
        self.assertNotIn("playphrase_url.py", packaged_text)
        self.assertNotIn("python3 scripts/", packaged_text)

    def test_archive_contains_one_clean_skill_without_python(self) -> None:
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
            self.assertFalse(any(name.endswith((".py", ".pyc", ".pyo")) for name in names))
            self.assertFalse(any("/scripts/" in name for name in names))
            for name in names:
                path = PurePosixPath(name)
                self.assertNotIn("..", path.parts)
                self.assertNotIn(".git", path.parts)
                self.assertNotIn("__pycache__", path.parts)

    def test_archive_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            first = package_skill.build_archive(directory / "first.zip")
            second = package_skill.build_archive(directory / "second.zip")
            self.assertEqual(
                hashlib.sha256(first.read_bytes()).digest(),
                hashlib.sha256(second.read_bytes()).digest(),
            )

    def test_readme_leads_with_chatgpt_download(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        release_url = (
            "https://github.com/potapenko/playphraseme-skill/"
            "releases/latest/download/skill.zip"
        )
        repository_url = (
            "https://github.com/potapenko/playphraseme-skill/"
            "tree/master/skills/playphraseme"
        )
        self.assertIn("https://chatgpt.com/skills", readme)
        self.assertLess(readme.index(release_url), readme.index(repository_url))

    def test_gold_evidence_uses_public_gets_and_current_examples(self) -> None:
        payload = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(1, payload["schema-version"])
        self.assertEqual(
            "https://www.playphrase.me/api/v1/learning/common-phrases",
            payload["source"],
        )
        self.assertEqual("2026-09-05", payload["verified-on"])
        self.assertTrue(payload["retention"]["owner"])
        self.assertTrue(payload["retention"]["condition"])

        queries = {query["id"]: query for query in payload["queries"]}
        self.assertEqual({"b2-idioms", "b1-work", "b1-b2-apology"}, set(queries))
        self.assertGreaterEqual(len(queries["b2-idioms"]["items"]), 5)
        for query in payload["queries"]:
            self.assertTrue(query["verified-with"].startswith("GET https://www.playphrase.me/api/v1/learning/"))
            self.assertEqual("en", query["language"])
            self.assertLessEqual(query["limit"], 20)
            self.assertIn("language-level-from", query["filters"])
            self.assertIn("language-level-to", query["filters"])
            for item in query["items"]:
                self.assertEqual(item["text"], item["text"].strip())
                self.assertGreaterEqual(item["count"], 5)

    def test_literal_phrase_links_match_verified_text(self) -> None:
        known = evidence_items()
        documents = (ROOT / "README.md", PATTERNS_PATH)
        pattern = re.compile(
            r"\[([^\]\n]*“([^”]+)”[^\]\n]*)\]"
            r"\((https://www\.playphrase\.me/#/search\?[^)\s]+)\)"
        )
        for document in documents:
            text = document.read_text(encoding="utf-8")
            matches = pattern.findall(text)
            self.assertTrue(matches, document)
            for _label, phrase, destination in matches:
                with self.subTest(document=document.name, phrase=phrase):
                    self.assertIn(phrase, known)
                    self.assertGreaterEqual(known[phrase], 5)
                    self.assertEqual(phrase, search_query(destination))
                    self.assertNotIn("utm_", destination)

    def test_regression_example_contains_five_distinct_links(self) -> None:
        text = PATTERNS_PATH.read_text(encoding="utf-8")
        section = text.split("## Release regression example", 1)[1].split(
            "## Optional exploration", 1
        )[0]
        links = re.findall(
            r"\]\((https://www\.playphrase\.me/#/search\?[^)\s]+)\)", section
        )
        self.assertEqual(5, len(links))
        self.assertEqual(5, len({search_query(link) for link in links}))
        answer = section.split("### Responsibility", 1)[1].split(
            "These five literal", 1
        )[0]
        self.assertNotIn("DNS", answer)
        self.assertNotIn("Python", answer)

    def test_documented_links_are_public_and_tracking_free(self) -> None:
        documents = (ROOT / "README.md", PATTERNS_PATH)
        for document in documents:
            text = document.read_text(encoding="utf-8")
            for destination in re.findall(
                r"\]\((https://www\.playphrase\.me/[^)]+)\)", text
            ):
                parsed = urlsplit(destination)
                self.assertEqual("https", parsed.scheme)
                self.assertEqual("www.playphrase.me", parsed.netloc)
                self.assertNotIn("utm_", destination)


if __name__ == "__main__":
    unittest.main()

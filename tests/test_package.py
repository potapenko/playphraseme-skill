from __future__ import annotations

import hashlib
import importlib.util
import json
import re
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

URL_MODULE_PATH = REPOSITORY_ROOT / "skills/playphraseme/scripts/playphrase_url.py"
URL_SPEC = importlib.util.spec_from_file_location("playphrase_url", URL_MODULE_PATH)
assert URL_SPEC and URL_SPEC.loader
playphrase_url = importlib.util.module_from_spec(URL_SPEC)
URL_SPEC.loader.exec_module(playphrase_url)

COMMON_PHRASE_EVIDENCE_PATH = REPOSITORY_ROOT / "evals/common_phrase_examples.json"


def load_common_phrase_evidence() -> dict:
    return json.loads(COMMON_PHRASE_EVIDENCE_PATH.read_text(encoding="utf-8"))


def common_phrase_evidence_items() -> dict[str, int]:
    payload = load_common_phrase_evidence()
    return {
        item["text"]: item["count"]
        for query in payload["queries"]
        for item in query["items"]
    }


class SkillPackageTests(unittest.TestCase):
    def test_canonical_skill_is_valid(self) -> None:
        files = package_skill.validate_skill()
        relative = {
            path.relative_to(package_skill.SKILL_ROOT).as_posix() for path in files
        }
        self.assertIn("SKILL.md", relative)
        self.assertIn("agents/openai.yaml", relative)
        self.assertIn("references/response-patterns.md", relative)

        skill_text = (package_skill.SKILL_ROOT / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("references/response-patterns.md", skill_text)

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
            "https://github.com/potapenko/playphraseme-skill/"
            "tree/master/skills/playphraseme"
        )
        readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        installation = (
            package_skill.SKILL_ROOT / "references" / "platform-installation.md"
        ).read_text(encoding="utf-8")
        self.assertIn(repository_url, readme)
        self.assertIn(repository_url, installation)

    def test_readme_leads_with_chatgpt_zip_download(self) -> None:
        release_url = (
            "https://github.com/potapenko/playphraseme-skill/"
            "releases/latest/download/skill.zip"
        )
        chatgpt_skills_url = "https://chatgpt.com/skills"
        repository_url = (
            "https://github.com/potapenko/playphraseme-skill/"
            "tree/master/skills/playphraseme"
        )
        readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(release_url, readme)
        self.assertIn(chatgpt_skills_url, readme)
        self.assertLess(readme.index(release_url), readme.index(repository_url))
        self.assertLess(
            readme.index(chatgpt_skills_url), readme.index(repository_url)
        )

    def test_readme_offers_canonical_product_taste_links(self) -> None:
        readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        evidence = load_common_phrase_evidence()
        idioms = next(query for query in evidence["queries"] if query["id"] == "b2-idioms")
        phrases = {item["text"] for item in idioms["items"]}
        expected = {playphrase_url.build_search(phrase)["url"] for phrase in phrases}
        destinations = set(
            re.findall(r"\]\((https://www\.playphrase\.me/[^)]+)\)", readme)
        )
        search_destinations = {
            destination
            for destination in destinations
            if destination.startswith("https://www.playphrase.me/#/search?")
        }
        self.assertTrue(expected.issubset(search_destinations))
        for destination in search_destinations:
            playphrase_url.validate_url(destination)

    def test_retained_common_phrase_example_evidence_is_valid(self) -> None:
        evidence = load_common_phrase_evidence()
        self.assertEqual(1, evidence["schema-version"])
        self.assertEqual(
            "https://www.playphrase.me/api/v1/learning/common-phrases",
            evidence["source"],
        )
        self.assertRegex(evidence["verified-on"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertTrue(evidence["retention"]["owner"])
        self.assertTrue(evidence["retention"]["condition"])

        queries = {query["id"]: query for query in evidence["queries"]}
        self.assertEqual({"b2-idioms", "b1-work", "b1-b2-apology"}, set(queries))
        self.assertEqual(
            {
                "idiom": True,
                "language-level-from": "B2",
                "language-level-to": "B2",
            },
            queries["b2-idioms"]["filters"],
        )
        self.assertEqual(
            {
                "topic": "work",
                "language-level-from": "B1",
                "language-level-to": "B1",
            },
            queries["b1-work"]["filters"],
        )
        self.assertEqual(
            {
                "function": "apology",
                "language-level-from": "B1",
                "language-level-to": "B2",
            },
            queries["b1-b2-apology"]["filters"],
        )

        seen: set[str] = set()
        for query in evidence["queries"]:
            self.assertIn("playphrase_learning.py phrases", query["verified-with"])
            self.assertEqual("en", query["language"])
            self.assertEqual(20, query["limit"])
            self.assertIn("language-level-from", query["filters"])
            self.assertIn("language-level-to", query["filters"])
            for item in query["items"]:
                self.assertEqual(item["text"], item["text"].strip())
                self.assertGreaterEqual(item["count"], 5)
                self.assertNotIn(item["text"], seen)
                seen.add(item["text"])

        documented = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (
                REPOSITORY_ROOT / "README.md",
                REPOSITORY_ROOT / "skills/playphraseme/references/response-patterns.md",
                REPOSITORY_ROOT / "evals/cases.json",
            )
        )
        for text in seen:
            self.assertIn(text, documented)

    def test_documented_common_phrase_links_match_api_evidence_exactly(self) -> None:
        evidence_items = common_phrase_evidence_items()
        link_pattern = re.compile(
            r"\[([^\]\n]*“([^”]+)”[^\]\n]*)\]"
            r"\((https://www\.playphrase\.me/#/search\?[^)\s]+)\)"
        )
        documents = (
            REPOSITORY_ROOT / "README.md",
            REPOSITORY_ROOT / "skills/playphraseme/references/response-patterns.md",
        )
        for document in documents:
            text = document.read_text(encoding="utf-8")
            search_urls = re.findall(
                r"\]\((https://www\.playphrase\.me/#/search\?[^)\s]+)\)", text
            )
            matches = link_pattern.findall(text)
            self.assertEqual(len(search_urls), len(matches), document)
            for _label, phrase, destination in matches:
                with self.subTest(document=document.name, phrase=phrase):
                    self.assertIn(phrase, evidence_items)
                    self.assertGreaterEqual(evidence_items[phrase], 5)
                    self.assertEqual(playphrase_url.build_search(phrase)["url"], destination)
                    decoded = playphrase_url.validate_url(destination)
                    self.assertEqual(phrase, decoded["state"]["q"])

    def test_documented_b1_work_reels_link_matches_public_fixture_scope(self) -> None:
        evidence = load_common_phrase_evidence()
        work = next(query for query in evidence["queries"] if query["id"] == "b1-work")
        self.assertTrue(
            set(work["filters"]).issubset(playphrase_url.COMMON_PHRASE_DEFAULTS)
        )
        expected = playphrase_url.build_reels(
            source="common-phrases",
            language=work["language"],
            filters=work["filters"],
        )["url"]
        patterns = (
            REPOSITORY_ROOT / "skills/playphraseme/references/response-patterns.md"
        ).read_text(encoding="utf-8")
        reels_urls = re.findall(
            r"\]\((https://www\.playphrase\.me/#/reels/[^)\s]+)\)", patterns
        )
        self.assertEqual([expected], reels_urls)
        self.assertEqual(
            work["filters"], playphrase_url.validate_url(expected)["state"]["filters"]
        )

    def test_documented_deep_links_follow_the_public_url_contract(self) -> None:
        documents = (
            REPOSITORY_ROOT / "README.md",
            REPOSITORY_ROOT / "skills/playphraseme/references/response-patterns.md",
        )
        destinations: set[str] = set()
        for document in documents:
            text = document.read_text(encoding="utf-8")
            destinations.update(
                re.findall(r"\]\((https://www\.playphrase\.me/[^)]+)\)", text)
            )

        deep_links = {
            destination
            for destination in destinations
            if destination.startswith("https://www.playphrase.me/#/")
        }
        self.assertGreaterEqual(len(deep_links), 10)
        for destination in deep_links:
            playphrase_url.validate_url(destination)


if __name__ == "__main__":
    unittest.main()

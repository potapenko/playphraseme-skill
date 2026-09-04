from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/playphraseme/scripts/playphrase_url.py"
SPEC = importlib.util.spec_from_file_location("playphrase_url", SCRIPT)
assert SPEC and SPEC.loader
url_builder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = url_builder
SPEC.loader.exec_module(url_builder)


def fragment_query(url: str) -> tuple[str, dict[str, list[str]]]:
    fragment = urlsplit(url).fragment
    route, _, query = fragment.partition("?")
    return route, parse_qs(query)


class URLBuilderTests(unittest.TestCase):
    def test_plain_query_with_spaces_and_apostrophe(self) -> None:
        result = url_builder.build_search("don't stop")
        route, query = fragment_query(result["url"])
        self.assertEqual("/search", route)
        self.assertEqual(["don't stop"], query["q"])

    def test_exact_query_quotes_once(self) -> None:
        first = url_builder.build_search("i love you", exact=True)
        second = url_builder.build_search('"i love you"', exact=True)
        self.assertEqual(first["url"], second["url"])
        self.assertIn("%22i+love+you%22", first["url"])

    def test_wildcard_is_preserved(self) -> None:
        result = url_builder.build_search("hello * world")
        self.assertEqual(["hello * world"], fragment_query(result["url"])[1]["q"])

    def test_grammar_prefix_is_not_duplicated(self) -> None:
        result = url_builder.build_search("gr: go home", grammar=True)
        self.assertEqual("gr: go home", result["state"]["q"])
        with self.assertRaises(url_builder.URLContractError):
            url_builder.build_search("go home", language="fr", grammar=True)

    def test_common_phrases_idiom_and_cefr(self) -> None:
        result = url_builder.build_catalog(
            "common-phrases",
            filters={"idiom": True, "language-level-from": "B1", "language-level-to": "C1"},
        )
        filters = json.loads(fragment_query(result["url"])[1]["filters"][0])
        self.assertEqual(
            {"idiom": True, "language-level-from": "B1", "language-level-to": "C1"},
            filters,
        )

    def test_catalog_defaults_are_removed(self) -> None:
        result = url_builder.build_catalog(
            "common-phrases",
            filters={
                "idiom": False,
                "is-question": False,
                "language-level-from": "A1",
                "language-level-to": "C2",
            },
        )
        self.assertNotIn("filters", fragment_query(result["url"])[1])

    def test_vocabulary_domain_and_part_of_speech(self) -> None:
        result = url_builder.build_catalog(
            "common-words",
            filters={"domain": "American-English", "part-of-speech": "verb"},
        )
        filters = json.loads(fragment_query(result["url"])[1]["filters"][0])
        self.assertEqual("American-English", filters["domain"])
        self.assertEqual("verb", filters["part-of-speech"])

    def test_vocabulary_offensive_and_sort_enums(self) -> None:
        result = url_builder.build_catalog(
            "common-words",
            filters={"offensive-filter": "only", "sort-by": "travel-utility"},
        )
        filters = result["state"]["filters"]
        self.assertEqual("only", filters["offensive-filter"])
        self.assertEqual("travel-utility", filters["sort-by"])
        with self.assertRaises(url_builder.URLContractError):
            url_builder.build_catalog("common-words", filters={"offensive-filter": "all"})

    def test_clip_year_range(self) -> None:
        result = url_builder.build_clip_search(filters={"year": "1990..1999"})
        self.assertEqual({"min": 1990, "max": 1999}, result["state"]["filters"]["year"])

    def test_clip_arrays_and_aliases(self) -> None:
        result = url_builder.build_clip_search(
            filters={"year-range": {"min": 1990, "max": 1999}, "actor": ["brad pitt"], "genre": ["Comedy", "Drama"]}
        )
        self.assertNotIn("actor", result["state"]["filters"])
        self.assertEqual(["brad pitt"], result["state"]["filters"]["cast-actor"])
        self.assertEqual(["Comedy", "Drama"], result["state"]["filters"]["genre"])

    def test_non_english_clip_removes_voice_with_warning(self) -> None:
        result = url_builder.build_clip_search(
            language="fr",
            filters={"voice-detection": ["actor"], "cast-actor": ["actor"]},
        )
        self.assertNotIn("voice-detection", result["state"]["filters"])
        self.assertIn("cast-actor", result["state"]["filters"])
        self.assertTrue(result["warnings"])

    def test_exact_source_conflict_warns(self) -> None:
        result = url_builder.build_clip_search(
            filters={"imdb": "tt7131622", "year": 2019, "director": ["quentin tarantino"]}
        )
        self.assertTrue(any("ineffective" in warning for warning in result["warnings"]))

    def test_reels_english_route_is_explicit(self) -> None:
        result = url_builder.build_reels(source="custom-search", query="break a leg")
        self.assertTrue(result["url"].startswith("https://www.playphrase.me/#/reels/en?"))

    def test_same_language_translation_is_removed(self) -> None:
        result = url_builder.build_reels(language="en", translate_direction="en")
        self.assertNotIn("translate-direction", result["state"])
        self.assertTrue(result["warnings"])

    def test_actor_requires_known_id(self) -> None:
        with self.assertRaises(url_builder.URLContractError):
            url_builder.build_actor("")
        self.assertEqual(
            "https://www.playphrase.me/actor/brad_pitt",
            url_builder.build_actor("brad_pitt")["url"],
        )

    def test_decode_removes_internal_and_unknown_parameters(self) -> None:
        decoded = url_builder.decode_url(
            "https://www.playphrase.me/?recovery-token=outer-secret#/search?language=en&q=hello&auth-token=secret&recorder-mode=true&force_mobile=1"
        )
        self.assertEqual(
            ["auth-token", "force_mobile", "recorder-mode", "recovery-token"],
            decoded["unknown"],
        )
        self.assertNotIn("secret", decoded["url"])
        self.assertEqual(["hello"], fragment_query(decoded["url"])[1]["q"])

    def test_unicode_round_trip(self) -> None:
        original = url_builder.build_search("¿Qué tal? 日本語", language="es")
        decoded = url_builder.decode_url(original["url"])
        self.assertEqual(original["state"], decoded["state"])
        self.assertEqual(original["url"], decoded["url"])

    def test_fragment_query_stays_after_hash(self) -> None:
        result = url_builder.build_search("hello")
        self.assertEqual("", urlsplit(result["url"]).query)
        self.assertIn("?language=en", urlsplit(result["url"]).fragment)

    def test_reserved_characters_round_trip(self) -> None:
        result = url_builder.build_search("rock & roll #100%")
        decoded = url_builder.decode_url(result["url"])
        self.assertEqual("rock & roll #100%", decoded["state"]["q"])
        self.assertEqual(result["url"], decoded["url"])

    def test_validate_rejects_internal_parameters(self) -> None:
        with self.assertRaises(url_builder.URLContractError):
            url_builder.validate_url(
                "https://www.playphrase.me/#/search?language=en&q=hello&auth-token=secret"
            )

    def test_validate_rejects_tracking_parameters(self) -> None:
        with self.assertRaises(url_builder.URLContractError):
            url_builder.validate_url(
                "https://www.playphrase.me/#/search?language=en&q=hello&utm_source=chatgpt"
            )

    def test_public_reels_path_decodes_search_text(self) -> None:
        decoded = url_builder.decode_url(
            "https://www.playphrase.me/reels/en/break%20a%20leg/"
        )
        self.assertEqual("break a leg", decoded["state"]["q"])
        self.assertIn("q=break+a+leg", decoded["url"])

    def test_api_item_uses_text_not_id(self) -> None:
        item = {"id": "common-phrase-record", "text": "break a leg"}
        result = url_builder.build_reels(source="custom-search", query=item["text"])
        self.assertIn("break+a+leg", result["url"])
        self.assertNotIn(item["id"], result["url"])

    def test_cli_emits_warning_to_stderr_and_url_to_stdout(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "clip-search",
                "--language",
                "fr",
                "--filter",
                "voice-detection=someone",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode)
        self.assertTrue(completed.stdout.startswith("https://"))
        self.assertIn("warning:", completed.stderr)


if __name__ == "__main__":
    unittest.main()

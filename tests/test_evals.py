from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "cases.json"
EVIDENCE_PATH = ROOT / "evals" / "common_phrase_examples.json"


def payload() -> dict:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


def case_map() -> dict[str, dict]:
    return {case["id"]: case for case in payload()["cases"]}


class EvalDefinitionTests(unittest.TestCase):
    def test_shape_and_unique_ids(self) -> None:
        data = payload()
        self.assertEqual(3, data["schema-version"])
        self.assertEqual("playphraseme", data["skill"])
        self.assertGreaterEqual(len(data["cases"]), 20)
        ids = [case["id"] for case in data["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        for case in data["cases"]:
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["expected"])
            for turn in case.get("prior-turns", []):
                self.assertIn(turn["role"], {"user", "assistant"})
                self.assertTrue(turn["content"].strip())

    def test_instruction_only_eval_contract_has_no_transport_state_machine(self) -> None:
        data = payload()
        serialized = json.dumps(data, sort_keys=True)
        forbidden = (
            "learning-api-client",
            "print-url",
            "exit-code",
            "direct-web-fetch",
            "playphrase-url-builder",
            "playphrase_learning.py",
            "playphrase_url.py",
        )
        for value in forbidden:
            self.assertNotIn(value, serialized)

        api = data["api-backed-selection-invariants"]
        self.assertEqual("GET", api["method"])
        self.assertEqual(20, api["maximum-limit"])
        self.assertEqual(1, api["maximum-initial-requests"])
        self.assertTrue(api["forbids-private-api"])
        self.assertTrue(api["requires-exact-returned-text"])
        self.assertEqual(5, api["minimum-common-phrase-count"])

    def test_api_only_selection_is_a_first_class_contract(self) -> None:
        contract = payload()["api-only-selection-invariants"]
        for key in (
            "applies-to-all-study-modes",
            "requires-successful-public-api-rows",
            "requires-exact-returned-text-or-word",
            "forbids-synthetic-example-or-link-filler",
            "must-state-shortfall",
            "permits-composed-explanations-translations-and-meaning-choices",
            "user-supplied-text-is-unverified-context",
            "all-offered-examples-including-user-quotes-and-formulas-require-exact-api-row",
            "unverified-user-input-must-not-be-promoted-to-learning-material",
            "explicit-navigation-is-not-example-evidence",
            "reuse-requires-current-record-identity-text-and-corpus-language",
            "historical-documentation-is-not-current-api-evidence",
        ):
            self.assertTrue(contract[key], key)

        cases = case_map()
        for case in cases.values():
            expected = case["expected"]
            self.assertFalse(expected.get("allows-model-selected-language", False))
            event = case.get("runtime-event", {})
            if event.get("learning-api") in {"unavailable", "http-429", "empty-items"}:
                if event.get("established-current-api-rows"):
                    continue
                self.assertEqual(0, expected.get("output-count", 0), case["id"])
                self.assertFalse(expected.get("requires-link-per-phrase", False), case["id"])

    def test_api_only_partial_and_meaning_quiz_boundaries(self) -> None:
        cases = case_map()
        partial = cases["api-only-insufficient-rows"]
        self.assertEqual(len(partial["runtime-event"]["items"]), partial["expected"]["output-count"])
        self.assertTrue(partial["expected"]["must-not-fill-requested-count"])
        self.assertTrue(partial["expected"]["requires-shortfall-notice"])
        quiz = cases["api-only-quiz-meaning-options"]["expected"]
        self.assertTrue(quiz["allows-composed-meaning-options"])
        self.assertTrue(quiz["must-not-generate-new-english-study-phrases"])
        correction = cases["transcript-correction-invites-same-item-repeat"]["expected"]
        self.assertTrue(correction["must-not-compose-corrected-english-target"])
        self.assertTrue(correction["requires-conceptual-missing-article-feedback"])

    def test_user_quotes_and_formulas_do_not_bypass_exact_api_evidence(self) -> None:
        cases = case_map()
        formula = cases["api-only-ellipsis-formula-unavailable"]["expected"]
        self.assertEqual(0, formula["new-example-count"])
        self.assertTrue(formula["must-not-offer-unverified-formula"])
        practice = cases["api-only-user-quoted-practice-unavailable"]["expected"]
        self.assertEqual(0, practice["offered-practice-target-count"])
        self.assertTrue(practice["must-not-treat-user-quote-as-source-evidence"])
        substring = cases["api-only-no-formula-from-substring"]["expected"]
        self.assertTrue(substring["must-not-shorten-or-abstract-api-row"])
        verified = cases["api-only-supplied-quote-verified-practice"]["expected"]
        self.assertEqual(1, verified["offered-practice-target-count"])
        self.assertTrue(verified["requires-exact-api-text-not-merely-user-quote"])
        for case_id in ("exact-quote", "wildcard", "grammar-search"):
            self.assertTrue(cases[case_id]["expected"]["navigation-query-is-not-offered-learning-material"])

    def test_release_prompt_has_api_and_no_api_acceptance(self) -> None:
        cases = case_map()
        available = cases["release-regression-api-available"]
        unavailable = cases["release-regression-api-unavailable"]
        expected_prompt = (
            "Give me 5 useful B2 English idioms for today. Group them by what "
            "they help me express and give me a PlayPhrase.me link for each one."
        )
        self.assertEqual(expected_prompt, available["prompt"])
        self.assertEqual(expected_prompt, unavailable["prompt"])

        success = available["expected"]
        self.assertEqual(
            {"idiom": True, "language-level-from": "B2", "language-level-to": "B2"},
            success["filters"],
        )
        self.assertEqual(5, success["output-count"])
        self.assertTrue(success["requires-link-per-phrase"])
        self.assertTrue(success["requires-common-phrase-source"])
        self.assertTrue(success["requires-exact-returned-text"])

        degraded = unavailable["expected"]
        self.assertEqual(0, degraded["output-count"])
        self.assertEqual("B2", degraded["level"])
        self.assertTrue(degraded["must-not-generate-new-study-examples-or-links"])
        self.assertTrue(degraded["must-not-fill-requested-count"])
        self.assertTrue(degraded["requires-brief-evidence-limitation"])
        self.assertTrue(degraded["must-not-mention-dns-python-tools-or-transport"])
        self.assertTrue(degraded["must-not-claim-common-phrase-or-api-provenance"])

    def test_provenance_request_remains_strict(self) -> None:
        expected = case_map()["explicit-api-ranking-needs-evidence"]["expected"]
        self.assertEqual("slang", expected["filters"]["register"])
        self.assertTrue(expected["must-state-provenance-unavailable"])
        self.assertTrue(expected["must-not-substitute-model-ranking"])
        self.assertTrue(expected["must-not-use-private-api"])

    def test_level_resolution_and_filter_semantics(self) -> None:
        cases = {key: value["expected"] for key, value in case_map().items()}
        unknown = cases["unknown-level-asks-once"]
        self.assertEqual([], unknown["api-paths"])
        self.assertTrue(unknown["requires-one-short-level-question"])
        self.assertTrue(unknown["must-wait-before-returning-candidates"])

        immediate = cases["no-question-uses-task-appropriate-language"]
        self.assertTrue(immediate["requires-common-task-appropriate-language"])
        self.assertNotIn("language-level-from", immediate["filters"])
        self.assertEqual(8, immediate["output-count"])

        imminent = cases["imminent-interview-uses-task-appropriate-language"]
        self.assertTrue(imminent["requires-common-task-appropriate-language"])
        self.assertNotIn("language-level-from", imminent["filters"])
        self.assertEqual("work", imminent["filters"]["topic"])
        self.assertTrue(imminent["must-not-ask-level"])

        remembered = cases["remembered-level-wins"]
        self.assertEqual("C1", remembered["filters"]["language-level-from"])
        self.assertEqual("C1", remembered["filters"]["language-level-to"])
        self.assertTrue(remembered["must-not-repeat-level-question"])

        harder = cases["higher-than-b2-followup"]
        self.assertEqual("C1", harder["filters"]["language-level-from"])
        self.assertEqual("C2", harder["filters"]["language-level-to"])
        self.assertTrue(harder["must-raise-lower-cefr-bound"])

        both = cases["formal-professional-are-independent"]
        self.assertEqual("formal", both["filters"]["formality"])
        self.assertEqual("professional", both["filters"]["register"])
        self.assertTrue(both["requires-and-semantics"])

    def test_phrase_word_and_exact_text_boundaries(self) -> None:
        cases = {key: value["expected"] for key, value in case_map().items()}
        slang = cases["slang-expressions-use-register"]
        self.assertEqual("slang", slang["filters"]["register"])
        self.assertTrue(slang["must-not-use-common-words-as-phrase-proof"])
        self.assertTrue(slang["must-not-put-api-only-filter-in-catalog-url"])

        exact = cases["exact-common-phrase-text"]
        evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
        known = {
            item["text"]: item["count"]
            for query in evidence["queries"]
            for item in query["items"]
        }
        self.assertEqual(exact["api-item"]["count"], known[exact["api-item"]["text"]])
        self.assertTrue(exact["must-not-complete-shorten-or-rewrite-returned-text"])
        self.assertTrue(exact["must-not-use-record-id-in-link"])

    def test_response_patterns_and_product_boundaries(self) -> None:
        cases = {key: value["expected"] for key, value in case_map().items()}
        self.assertTrue(cases["exact-quote"]["requires-encoded-double-quotes"])
        self.assertEqual("hello * world", cases["wildcard"]["query"])
        self.assertEqual("gr: go home", cases["grammar-search"]["query"])
        self.assertTrue(cases["explain-one-phrase"]["requires-first-link-in-first-content-block"])
        self.assertTrue(cases["compare-phrases"]["requires-linked-comparison-set"])
        self.assertTrue(cases["job-interview-lesson"]["requires-explicit-lesson-structure"])
        self.assertEqual(20, cases["job-interview-lesson"]["duration-minutes"])
        self.assertTrue(cases["explicit-interactive-quiz"]["must-wait-for-learner-answer"])
        self.assertTrue(cases["common-phrases-reels"]["must-use-only-public-reels-filters"])
        self.assertTrue(
            cases["model-fallback-does-not-invent-reels-scope"]
            ["must-not-invent-reels-scope"]
        )
        self.assertTrue(cases["reject-private-export"]["must-refuse-bypass"])


if __name__ == "__main__":
    unittest.main()

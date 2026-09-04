from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EvalDefinitionTests(unittest.TestCase):
    def test_behavioral_eval_file_has_required_shape(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        self.assertEqual("playphraseme", payload["skill"])
        cases = payload["cases"]
        self.assertGreaterEqual(len(cases), 12)
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertTrue(case["prompt"].strip())
            self.assertIsInstance(case["expected"], dict)
            self.assertTrue(case["expected"])

    def test_negative_bypass_eval_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        negative = next(case for case in payload["cases"] if case["id"] == "reject-private-export")
        self.assertTrue(negative["expected"]["must-refuse-bypass"])

    def test_response_pattern_eval_contract_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        cases = {case["id"]: case["expected"] for case in payload["cases"]}
        self.assertTrue(
            {
                "explain-one-phrase-response",
                "compare-phrases-response",
                "natural-wording-response",
                "job-interview-response",
                "implicit-job-interview-response",
                "vocabulary-discovery-response",
                "grammar-through-examples-response",
                "explicit-phrase-native-quiz",
            }.issubset(cases)
        )

        one_phrase = cases["explain-one-phrase-response"]
        self.assertTrue(one_phrase["requires-primary-descriptive-link"])
        self.assertTrue(one_phrase["requires-short-nuance"])
        self.assertEqual({"min": 1, "max": 2}, one_phrase["nearby-phrase-count"])

        comparison = cases["compare-phrases-response"]
        self.assertTrue(comparison["requires-linked-comparison-table"])
        self.assertTrue(comparison["requires-same-situation-contrast"])

        natural = cases["natural-wording-response"]
        self.assertTrue(natural["requires-natural-options-first"])
        self.assertEqual({"min": 3, "max": 5}, natural["default-option-count"])
        self.assertTrue(natural["requires-best-fit-recommendation"])

        interview = cases["job-interview-response"]
        self.assertEqual("work", interview["filters"]["topic"])
        self.assertTrue(interview["requires-intent-based-groups"])
        self.assertEqual({"min": 2, "max": 4}, interview["default-group-count"])
        self.assertEqual(
            {"min": 2, "max": 4}, interview["default-phrases-per-group"]
        )
        self.assertTrue(interview["requires-link-per-phrase"])
        self.assertTrue(interview["must-not-use-timeboxed-stages"])
        self.assertTrue(interview["must-not-add-generic-exercises"])
        self.assertTrue(interview["requires-builder-output-unchanged"])
        self.assertTrue(interview["forbids-tracking-parameters"])

        implicit = cases["implicit-job-interview-response"]
        self.assertTrue(implicit["must-recognize-implicit-learning-need"])
        self.assertTrue(implicit["must-not-add-generic-exercises"])

        discovery = cases["vocabulary-discovery-response"]
        self.assertTrue(discovery["requires-scannable-linked-table"])
        self.assertTrue(discovery["must-keep-deeper-explanations-selective"])

        offline = cases["grammar-through-examples-response"]
        self.assertTrue(offline["requires-pattern-table-before-rule"])
        self.assertTrue(offline["requires-documented-url-fallback"])
        self.assertTrue(offline["requires-link-per-pattern"])
        self.assertTrue(offline["must-not-name-unverified-sources"])

        interactive = cases["explicit-phrase-native-quiz"]
        self.assertTrue(interactive["requires-linked-phrase-choices"])
        self.assertTrue(interactive["requires-meaning-or-context-decision"])
        self.assertTrue(interactive["must-wait-for-learner-answer"])
        self.assertTrue(interactive["must-not-reveal-answer-in-same-turn"])


if __name__ == "__main__":
    unittest.main()

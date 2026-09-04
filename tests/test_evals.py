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

    def test_lesson_eval_contract_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        cases = {case["id"]: case["expected"] for case in payload["cases"]}
        self.assertTrue(
            {
                "job-interview-lesson",
                "grammar-lesson-no-browser",
                "same-phrase-different-tone",
                "interactive-quiz",
            }.issubset(cases)
        )

        interview = cases["job-interview-lesson"]
        self.assertEqual("work", interview["filters"]["topic"])
        self.assertEqual({"min": 3, "max": 5}, interview["activity-count"])
        self.assertTrue(interview["requires-active-listening"])
        self.assertTrue(interview["requires-builder-output-unchanged"])
        self.assertTrue(interview["forbids-tracking-parameters"])

        offline = cases["grammar-lesson-no-browser"]
        self.assertTrue(offline["requires-complete-offline-lesson"])
        self.assertTrue(offline["requires-documented-url-fallback"])
        self.assertTrue(offline["must-not-name-unverified-sources"])

        tone = cases["same-phrase-different-tone"]
        self.assertTrue(tone["requires-learner-classification"])
        self.assertTrue(tone["must-not-prelabel-unverified-tone"])

        interactive = cases["interactive-quiz"]
        self.assertTrue(interactive["must-wait-for-learner-answer"])
        self.assertTrue(interactive["must-not-reveal-answer-in-same-turn"])


if __name__ == "__main__":
    unittest.main()

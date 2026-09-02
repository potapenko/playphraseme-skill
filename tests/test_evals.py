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


if __name__ == "__main__":
    unittest.main()

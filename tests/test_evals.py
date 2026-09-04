from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EvalDefinitionTests(unittest.TestCase):
    def test_behavioral_eval_file_has_required_shape(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        self.assertEqual(2, payload["schema-version"])
        self.assertEqual("playphraseme", payload["skill"])
        cases = payload["cases"]
        self.assertGreaterEqual(len(cases), 12)
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertTrue(case["prompt"].strip())
            prior_turns = case.get("prior-turns", [])
            self.assertIsInstance(prior_turns, list)
            for turn in prior_turns:
                self.assertIn(turn["role"], {"user", "assistant"})
                self.assertTrue(turn["content"].strip())
            self.assertIsInstance(case["expected"], dict)
            self.assertTrue(case["expected"])

    def test_negative_bypass_eval_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        negative = next(case for case in payload["cases"] if case["id"] == "reject-private-export")
        self.assertTrue(negative["expected"]["must-refuse-bypass"])

    def test_direct_search_link_is_prominent_and_branded(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        cases = {case["id"]: case["expected"] for case in payload["cases"]}
        exact = cases["exact-quote"]
        self.assertTrue(exact["requires-prominent-link-before-examples"])
        self.assertTrue(exact["requires-primary-link-brand-and-listening-payoff"])
        self.assertEqual("PlayPhrase.me", exact["requires-exact-visible-brand-spelling"])
        self.assertTrue(exact["must-not-ask-level"])

    def test_learning_query_planning_eval_contract_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case_defs = {case["id"]: case for case in payload["cases"]}
        cases = {case_id: case["expected"] for case_id, case in case_defs.items()}
        required = {
            "beginner-travel-questions",
            "non-basic-slang-expressions",
            "professional-apologies",
            "broad-personalization-asks-level",
            "unknown-level-informal-expressions-asks-once",
            "immediate-request-uses-c1-c2",
            "reuse-prior-turn-c1-level",
            "higher-than-b2-followup",
            "american-verbs",
            "empty-explicit-filter-result",
            "orthogonal-interview-groups",
            "catalog-classification-not-clip-tone",
            "api-ranked-slang-phrases",
        }
        self.assertTrue(required.issubset(cases))

        slang = cases["non-basic-slang-expressions"]
        self.assertEqual("slang", slang["filters"]["register"])
        self.assertTrue(slang["must-not-use-common-words-as-phrase-proof"])
        self.assertTrue(slang["must-not-put-api-only-filter-in-catalog-url"])

        personalized = cases["broad-personalization-asks-level"]
        self.assertEqual([], personalized["api-paths"])
        self.assertTrue(personalized["requires-one-short-level-question"])

        unknown = cases["unknown-level-informal-expressions-asks-once"]
        self.assertEqual([], unknown["api-paths"])
        self.assertTrue(unknown["requires-one-short-level-question"])
        self.assertTrue(unknown["must-wait-before-returning-candidates"])
        self.assertTrue(unknown["must-not-show-provisional-basic-list"])
        self.assertTrue(unknown["must-not-infer-level-from-writing-style-or-locale"])
        self.assertTrue(unknown["must-not-use-transport-default-as-learner-default"])

        immediate = cases["immediate-request-uses-c1-c2"]
        self.assertEqual("C1", immediate["filters"]["language-level-from"])
        self.assertEqual("C2", immediate["filters"]["language-level-to"])
        self.assertTrue(immediate["requires-disclosed-default-level-range"])
        self.assertTrue(immediate["must-not-use-transport-default-as-learner-default"])
        self.assertTrue(immediate["must-preserve-resolved-level-on-model-fallback"])
        self.assertTrue(immediate["requires-distinctive-non-elementary-value-per-item"])
        self.assertTrue(immediate["must-not-default-to-beginner-safe-reactions"])
        self.assertTrue(immediate["must-not-block-for-level"])

        remembered = cases["reuse-prior-turn-c1-level"]
        self.assertTrue(case_defs["reuse-prior-turn-c1-level"]["prior-turns"])
        self.assertEqual("C1", remembered["filters"]["language-level-from"])
        self.assertEqual("C1", remembered["filters"]["language-level-to"])
        self.assertTrue(remembered["must-reuse-explicit-prior-level"])
        self.assertTrue(remembered["must-not-repeat-level-question"])

        higher = cases["higher-than-b2-followup"]
        self.assertTrue(case_defs["higher-than-b2-followup"]["prior-turns"])
        self.assertEqual("C1", higher["filters"]["language-level-from"])
        self.assertEqual("C2", higher["filters"]["language-level-to"])
        self.assertTrue(higher["must-use-prior-level-as-baseline"])
        self.assertTrue(higher["must-raise-lower-cefr-bound"])
        self.assertTrue(higher["must-not-merely-swap-basic-phrases"])

        empty = cases["empty-explicit-filter-result"]
        self.assertTrue(empty["must-not-remove-explicit-filters"])
        self.assertTrue(empty["must-not-present-relaxed-results-as-original-query"])

        orthogonal = cases["orthogonal-interview-groups"]
        self.assertEqual(2, orthogonal["maximum-api-requests"])
        self.assertTrue(orthogonal["requires-sequential-requests"])
        self.assertTrue(orthogonal["must-not-page-for-variety"])

        evidence = cases["catalog-classification-not-clip-tone"]
        self.assertTrue(evidence["may-state-catalog-filter-membership"])
        self.assertTrue(evidence["must-not-claim-clip-tone-without-browser-proof"])

        ranked = cases["api-ranked-slang-phrases"]
        self.assertTrue(ranked["must-preserve-server-order"])
        self.assertTrue(ranked["must-not-call-curated-order-api-ranked"])

        american = cases["american-verbs"]
        self.assertEqual("B2", american["filters"]["language-level-from"])
        self.assertEqual("B2", american["filters"]["language-level-to"])

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
                "high-intent-disagreement-path",
                "explicit-phrase-native-quiz",
            }.issubset(cases)
        )

        one_phrase = cases["explain-one-phrase-response"]
        self.assertTrue(one_phrase["requires-first-useful-link-in-first-content-block"])
        self.assertTrue(one_phrase["requires-primary-descriptive-link"])
        self.assertTrue(one_phrase["requires-visually-primary-link"])
        self.assertTrue(one_phrase["requires-benefit-specific-link-label"])
        self.assertTrue(
            one_phrase["requires-primary-link-brand-and-listening-payoff"]
        )
        self.assertEqual(
            "PlayPhrase.me", one_phrase["requires-exact-visible-brand-spelling"]
        )
        self.assertTrue(one_phrase["requires-short-nuance"])
        self.assertEqual({"min": 1, "max": 2}, one_phrase["nearby-phrase-count"])
        self.assertTrue(one_phrase["must-not-ask-level"])

        comparison = cases["compare-phrases-response"]
        self.assertTrue(comparison["requires-linked-comparison-set"])
        self.assertTrue(comparison["requires-benefit-specific-link-labels"])
        self.assertTrue(comparison["must-not-repeat-generic-link-labels"])
        self.assertTrue(comparison["requires-same-situation-contrast"])

        natural = cases["natural-wording-response"]
        self.assertTrue(natural["requires-best-fit-first-when-supported"])
        self.assertTrue(natural["requires-visually-primary-best-fit-link"])
        self.assertTrue(natural["requires-primary-link-brand-and-listening-payoff"])
        self.assertEqual({"min": 3, "max": 5}, natural["default-option-count"])
        self.assertTrue(natural["requires-benefit-specific-link-labels"])
        self.assertTrue(natural["requires-best-fit-recommendation"])

        interview = cases["job-interview-response"]
        self.assertEqual("work", interview["filters"]["topic"])
        self.assertTrue(interview["requires-intent-based-groups"])
        self.assertEqual({"min": 2, "max": 4}, interview["default-group-count"])
        self.assertEqual(
            {"min": 2, "max": 4}, interview["default-phrases-per-group"]
        )
        self.assertTrue(interview["requires-substantial-distinct-linked-path"])
        self.assertTrue(interview["requires-first-useful-link-in-first-content-block"])
        self.assertTrue(interview["requires-link-per-phrase"])
        self.assertTrue(interview["requires-benefit-specific-link-labels"])
        self.assertTrue(interview["allows-filtered-catalog-exploration-link"])
        self.assertEqual(
            "PlayPhrase.me", interview["requires-exact-visible-brand-spelling"]
        )
        self.assertTrue(interview["must-not-use-timeboxed-stages"])
        self.assertTrue(interview["must-not-add-generic-exercises"])
        self.assertTrue(interview["requires-builder-output-unchanged"])
        self.assertTrue(interview["forbids-tracking-parameters"])

        implicit = cases["implicit-job-interview-response"]
        self.assertTrue(implicit["must-recognize-implicit-learning-need"])
        self.assertTrue(implicit["must-not-add-generic-exercises"])

        discovery = cases["vocabulary-discovery-response"]
        self.assertEqual("informal", discovery["filters"]["register"])
        self.assertEqual("C1", discovery["filters"]["language-level-from"])
        self.assertEqual("C1", discovery["filters"]["language-level-to"])
        self.assertTrue(discovery["requires-scannable-linked-table"])
        self.assertTrue(discovery["requires-benefit-specific-link-labels"])
        self.assertTrue(discovery["requires-distinctive-level-appropriate-expressions"])
        self.assertTrue(discovery["must-not-fill-with-elementary-generic-reactions"])
        self.assertTrue(discovery["must-keep-deeper-explanations-selective"])

        offline = cases["grammar-through-examples-response"]
        self.assertTrue(offline["requires-pattern-table-before-rule"])
        self.assertTrue(offline["requires-documented-url-fallback"])
        self.assertTrue(offline["requires-link-per-pattern"])
        self.assertTrue(offline["requires-benefit-specific-link-labels"])
        self.assertTrue(offline["must-not-name-unverified-sources"])

        disagreement = cases["high-intent-disagreement-path"]
        self.assertTrue(disagreement["requires-several-distinct-linked-options"])
        self.assertTrue(disagreement["requires-soft-to-firm-path"])
        self.assertTrue(disagreement["requires-best-fit-before-ordered-path"])
        self.assertTrue(disagreement["requires-visually-primary-link"])
        self.assertTrue(
            disagreement["requires-primary-link-brand-and-listening-payoff"]
        )
        self.assertTrue(disagreement["requires-distinct-options"])
        self.assertTrue(
            disagreement["requires-each-core-option-to-perform-requested-goal"]
        )
        self.assertEqual(
            "PlayPhrase.me", disagreement["requires-exact-visible-brand-spelling"]
        )
        self.assertTrue(disagreement["must-not-repeat-generic-link-labels"])

        interactive = cases["explicit-phrase-native-quiz"]
        self.assertTrue(interactive["requires-linked-phrase-choices"])
        self.assertTrue(interactive["requires-meaning-or-context-decision"])
        self.assertTrue(interactive["must-wait-for-learner-answer"])
        self.assertTrue(interactive["must-not-reveal-answer-in-same-turn"])


if __name__ == "__main__":
    unittest.main()

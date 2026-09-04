from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
URL_MODULE_PATH = ROOT / "skills/playphraseme/scripts/playphrase_url.py"
URL_SPEC = importlib.util.spec_from_file_location("playphrase_url_for_evals", URL_MODULE_PATH)
assert URL_SPEC and URL_SPEC.loader
playphrase_url = importlib.util.module_from_spec(URL_SPEC)
URL_SPEC.loader.exec_module(playphrase_url)

COMMON_PHRASES_API_PATH = "/api/v1/learning/common-phrases"
COMMON_PHRASE_EVIDENCE_PATH = ROOT / "evals/common_phrase_examples.json"


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
        self.assertTrue(exact["requires-user-supplied-text-for-direct-classic-search"])
        self.assertTrue(exact["must-not-ask-level"])
        self.assertTrue(exact["must-not-add-reels-footer"])

        for case_id in ("wildcard", "grammar-english"):
            self.assertTrue(
                cases[case_id]["requires-user-supplied-text-for-direct-classic-search"]
            )

    def test_learning_query_planning_eval_contract_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case_defs = {case["id"]: case for case in payload["cases"]}
        cases = {case_id: case["expected"] for case_id, case in case_defs.items()}
        required = {
            "beginner-travel-questions",
            "non-basic-slang-expressions",
            "professional-apologies",
            "formal-phrases-use-formality",
            "explicit-formal-professional-intersection",
            "broad-personalization-asks-level",
            "unknown-level-informal-expressions-asks-once",
            "immediate-request-uses-c1-c2",
            "reuse-prior-turn-c1-level",
            "higher-than-b2-followup",
            "american-verbs",
            "empty-explicit-filter-result",
            "orthogonal-interview-groups",
            "catalog-classification-not-clip-tone",
            "common-phrase-text-preserved",
            "api-ranked-slang-phrases",
        }
        self.assertTrue(required.issubset(cases))

        slang = cases["non-basic-slang-expressions"]
        self.assertEqual("slang", slang["filters"]["register"])
        self.assertTrue(slang["must-not-use-common-words-as-phrase-proof"])
        self.assertTrue(slang["must-not-put-api-only-filter-in-catalog-url"])

        professional = cases["professional-apologies"]
        self.assertEqual(
            {
                "function": "apology",
                "register": "professional",
                "language-level-from": "B1",
                "language-level-to": "B2",
            },
            professional["filters"],
        )
        self.assertTrue(professional["must-not-add-formality-formal-filter"])

        formal = cases["formal-phrases-use-formality"]
        self.assertEqual(
            {
                "formality": "formal",
                "language-level-from": "B2",
                "language-level-to": "B2",
            },
            formal["filters"],
        )
        self.assertTrue(formal["must-not-add-register-professional-filter"])

        combined = cases["explicit-formal-professional-intersection"]
        self.assertEqual(
            {
                "formality": "formal",
                "register": "professional",
                "language-level-from": "B2",
                "language-level-to": "B2",
            },
            combined["filters"],
        )
        self.assertTrue(combined["requires-both-filters-because-both-were-explicit"])

        preserved = cases["common-phrase-text-preserved"]
        self.assertEqual(5, preserved["minimum-common-phrase-count"])
        self.assertGreaterEqual(preserved["api-item"]["count"], 5)
        self.assertEqual(preserved["api-item"]["text"], preserved["query"])
        self.assertTrue(preserved["requires-common-phrase-source"])
        self.assertTrue(preserved["requires-exact-returned-text"])
        self.assertTrue(preserved["must-not-complete-shorten-or-rewrite-returned-text"])
        self.assertTrue(preserved["must-not-use-classic-search-count-as-membership-proof"])
        evidence = json.loads(COMMON_PHRASE_EVIDENCE_PATH.read_text(encoding="utf-8"))
        evidence_items = {
            item["text"]: item["count"]
            for query in evidence["queries"]
            for item in query["items"]
        }
        self.assertEqual(
            preserved["api-item"]["count"],
            evidence_items[preserved["api-item"]["text"]],
        )

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
        self.assertTrue(immediate["must-not-use-model-written-phrase-fallback"])
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
        self.assertEqual("informal", higher["filters"]["register"])
        self.assertTrue(higher["must-use-prior-level-as-baseline"])
        self.assertTrue(higher["must-raise-lower-cefr-bound"])
        self.assertTrue(higher["must-not-merely-swap-basic-phrases"])

        empty = cases["empty-explicit-filter-result"]
        self.assertTrue(empty["must-not-remove-explicit-filters"])
        self.assertTrue(empty["must-offer-one-specific-relaxation-or-supported-catalog"])
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
        self.assertTrue(american["requires-common-word-source"])
        self.assertTrue(american["must-not-use-common-phrases-for-individual-words"])
        self.assertTrue(american["requires-individual-word-unit"])
        self.assertTrue(american["requires-exact-returned-word"])

    def test_agent_selected_phrase_cases_require_common_phrase_evidence(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        cases = {case["id"]: case["expected"] for case in payload["cases"]}
        invariants = payload["agent-selected-common-phrase-invariants"]
        self.assertEqual(5, invariants["minimum-common-phrase-count"])
        self.assertTrue(invariants["requires-exact-returned-text"])
        self.assertTrue(
            invariants["must-not-use-classic-search-or-browser-as-membership-proof"]
        )
        allowed_api_paths = set(invariants["allowed-api-paths"])
        self.assertEqual(
            {
                COMMON_PHRASES_API_PATH,
                "/api/v1/learning/common-phrases/suggestions",
            },
            allowed_api_paths,
        )
        agent_selected = {
            "suggest-common-phrase",
            "idioms-cefr",
            "beginner-travel-questions",
            "non-basic-slang-expressions",
            "professional-apologies",
            "formal-phrases-use-formality",
            "explicit-formal-professional-intersection",
            "immediate-request-uses-c1-c2",
            "reuse-prior-turn-c1-level",
            "higher-than-b2-followup",
            "orthogonal-interview-groups",
            "common-phrase-text-preserved",
            "api-ranked-slang-phrases",
            "natural-wording-response",
            "job-interview-response",
            "implicit-job-interview-response",
            "vocabulary-discovery-response",
            "common-phrases-reels-continuation",
            "high-intent-disagreement-path",
            "explicit-phrase-native-quiz",
            "explicit-no-extras-response",
        }
        for case_id in sorted(agent_selected):
            with self.subTest(case_id=case_id):
                expected = cases[case_id]
                self.assertTrue(expected["api-paths"])
                self.assertTrue(set(expected["api-paths"]).issubset(allowed_api_paths))
                self.assertTrue(expected["requires-common-phrase-source"])
                self.assertEqual(5, expected["minimum-common-phrase-count"])
                self.assertTrue(expected["requires-exact-returned-text"])
                filters = expected.get("filters", {})
                if set(filters) - set(playphrase_url.COMMON_PHRASE_DEFAULTS):
                    self.assertTrue(expected["must-not-add-reels-footer"])

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
                "common-phrases-reels-continuation",
                "high-intent-disagreement-path",
                "explicit-phrase-native-quiz",
                "explicit-no-extras-response",
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
        self.assertTrue(one_phrase["allows-user-supplied-direct-search"])
        self.assertTrue(one_phrase["must-not-invent-additional-dialogue-line"])
        self.assertTrue(one_phrase["nearby-options-must-be-common-phrase-suggestions"])
        self.assertEqual({"min": 0, "max": 2}, one_phrase["nearby-phrase-count"])
        self.assertTrue(one_phrase["must-not-ask-level"])

        comparison = cases["compare-phrases-response"]
        self.assertTrue(comparison["requires-linked-comparison-set"])
        self.assertTrue(comparison["requires-benefit-specific-link-labels"])
        self.assertTrue(comparison["must-not-repeat-generic-link-labels"])
        self.assertTrue(comparison["requires-same-situation-contrast"])
        self.assertTrue(comparison["must-not-add-reels-footer"])

        natural = cases["natural-wording-response"]
        self.assertTrue(natural["requires-best-fit-first-when-supported"])
        self.assertTrue(natural["requires-visually-primary-best-fit-link"])
        self.assertTrue(natural["requires-primary-link-brand-and-listening-payoff"])
        self.assertEqual({"min": 3, "max": 5}, natural["default-option-count"])
        self.assertTrue(natural["requires-benefit-specific-link-labels"])
        self.assertTrue(natural["requires-best-fit-recommendation"])
        self.assertTrue(natural["requires-common-phrase-source"])
        self.assertEqual(5, natural["minimum-common-phrase-count"])
        self.assertTrue(natural["requires-exact-returned-text"])
        self.assertTrue(natural["must-not-use-model-written-phrase-options"])

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
        self.assertTrue(interview["requires-common-phrase-source"])
        self.assertEqual(5, interview["minimum-common-phrase-count"])
        self.assertTrue(interview["requires-exact-returned-text"])
        self.assertEqual(
            "PlayPhrase.me", interview["requires-exact-visible-brand-spelling"]
        )
        self.assertTrue(interview["must-not-use-timeboxed-stages"])
        self.assertTrue(interview["must-not-add-generic-exercises"])
        self.assertTrue(interview["requires-builder-output-unchanged"])
        self.assertTrue(interview["forbids-tracking-parameters"])

        implicit = cases["implicit-job-interview-response"]
        self.assertTrue(implicit["must-recognize-implicit-learning-need"])
        self.assertTrue(implicit["requires-common-phrase-source"])
        self.assertEqual(5, implicit["minimum-common-phrase-count"])
        self.assertTrue(implicit["requires-exact-returned-text"])
        self.assertTrue(implicit["must-not-add-generic-exercises"])

        discovery = cases["vocabulary-discovery-response"]
        self.assertTrue(discovery["filters"]["idiom"])
        self.assertEqual("B2", discovery["filters"]["language-level-from"])
        self.assertEqual("B2", discovery["filters"]["language-level-to"])
        self.assertTrue(discovery["requires-scannable-linked-table"])
        self.assertTrue(discovery["requires-benefit-specific-link-labels"])
        self.assertTrue(discovery["requires-distinctive-level-appropriate-expressions"])
        self.assertTrue(discovery["requires-common-phrase-source"])
        self.assertEqual(5, discovery["minimum-common-phrase-count"])
        self.assertTrue(discovery["requires-exact-returned-text"])
        self.assertTrue(discovery["must-not-fill-with-elementary-generic-reactions"])
        self.assertTrue(discovery["must-keep-deeper-explanations-selective"])

        reels = cases["common-phrases-reels-continuation"]
        self.assertEqual("common-phrases", reels["reels-source"])
        self.assertEqual(reels["filters"], reels["reels-filters"])
        self.assertEqual(1, reels["maximum-reels-links"])
        self.assertTrue(reels["requires-reels-footer"])
        self.assertTrue(reels["requires-reels-footer-framed-as-optional"])
        self.assertTrue(reels["requires-reels-link-after-learning-content"])
        self.assertTrue(reels["must-not-replace-primary-search-links-with-reels"])
        self.assertTrue(reels["must-not-add-reels-task-or-report-back"])
        self.assertTrue(reels["requires-canonical-reels-url"])
        self.assertTrue(reels["must-use-only-public-reels-filters"])
        self.assertTrue(reels["forbids-tracking-parameters"])
        self.assertTrue(
            set(reels["reels-filters"]).issubset(playphrase_url.COMMON_PHRASE_DEFAULTS)
        )
        built_reels = playphrase_url.build_reels(
            source=reels["reels-source"],
            language="en",
            filters=reels["reels-filters"],
        )
        self.assertEqual(reels["reels-url"], built_reels["url"])
        self.assertEqual(built_reels, playphrase_url.validate_url(reels["reels-url"]))
        self.assertNotIn("utm_", reels["reels-url"])

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
        self.assertTrue(interactive["requires-common-phrase-source"])
        self.assertEqual(5, interactive["minimum-common-phrase-count"])
        self.assertTrue(interactive["requires-exact-returned-text"])
        self.assertTrue(interactive["must-not-add-reels-footer"])

        no_extras = cases["explicit-no-extras-response"]
        self.assertTrue(no_extras["must-not-add-reels-footer"])
        self.assertTrue(no_extras["must-not-add-exploration-links"])

        reels_negative_cases = {
            "exact-quote",
            "compare-phrases-response",
            "unknown-level-informal-expressions-asks-once",
            "orthogonal-interview-groups",
            "professional-apologies",
            "reels-custom-search",
            "explicit-phrase-native-quiz",
            "explicit-no-extras-response",
        }
        for case_id in sorted(reels_negative_cases):
            with self.subTest(reels_negative_case=case_id):
                self.assertTrue(cases[case_id]["must-not-add-reels-footer"])


if __name__ == "__main__":
    unittest.main()

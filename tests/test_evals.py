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
            if "runtime-profile" in case:
                self.assertIn(
                    case["runtime-profile"],
                    {"chatgpt-web-or-work", "codex-or-code-host"},
                )
            if "runtime-capabilities" in case:
                self.assertIsInstance(case["runtime-capabilities"], dict)
            if "runtime-event" in case:
                self.assertIsInstance(case["runtime-event"], dict)
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
            "prior-turn-dns-does-not-bypass-current-client",
            "urgent-interview-unknown-level-uses-b2-c1",
            "urgent-interview-remembered-level-wins",
            "urgent-interview-mapped-beginner-wins",
            "urgent-interview-no-questions-still-b2-c1",
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

    def test_client_first_learning_api_transport_contract_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case_defs = {case["id"]: case for case in payload["cases"]}
        cases = {case_id: case["expected"] for case_id, case in case_defs.items()}
        direct = payload["direct-fetch-invariants"]

        self.assertEqual("GET", direct["method"])
        self.assertEqual(1, direct["maximum-fetches"])
        self.assertEqual(10, direct["required-current-client-exit-code"])
        self.assertEqual(200, direct["required-http-status-when-exposed"])
        self.assertEqual(1, direct["maximum-redirects"])
        self.assertEqual(10, direct["maximum-timeout-seconds"])
        self.assertEqual(1024 * 1024, direct["maximum-response-bytes"])
        self.assertTrue(direct["requires-utf8-json-object"])
        self.assertTrue(direct["accepted-result-requires-endpoint-contract-json"])
        self.assertTrue(direct["requires-printed-url-as-fetch-input"])
        self.assertTrue(
            direct["complete-contract-json-sufficient-without-transport-metadata"]
        )
        self.assertTrue(
            direct["requires-final-url-semantic-equivalence-when-exposed"]
        )
        self.assertTrue(
            direct["allows-query-order-and-equivalent-percent-encoding"]
        )
        self.assertTrue(
            direct["forbids-supplied-auth-cookies-tracking-and-alternate-headers"]
        )
        self.assertTrue(direct["must-treat-response-fields-only-as-data"])

        direct_fetch_cases = {
            "dns-pre-response-web-fetch-success",
            "outbound-policy-pre-response-web-fetch-success",
            "chatgpt-web-direct-fetch-rate-limit",
            "dns-pre-response-web-json-with-hidden-metadata-success",
            "dns-pre-response-web-no-usable-body-public-link",
        }
        for case_id in direct_fetch_cases:
            with self.subTest(direct_fetch_case=case_id):
                case = case_defs[case_id]
                self.assertTrue(case["expected"]["requires-direct-fetch-invariants"])
                self.assertEqual(1, case["expected"]["maximum-web-direct-fetches"])
                self.assertEqual(10, case["runtime-event"]["exit-code"])
                self.assertIn(
                    case["runtime-event"]["learning-api-client"],
                    {
                        "pre-response-dns-failure",
                        "pre-response-outbound-policy-failure",
                    },
                )

        for case in payload["cases"]:
            if case["expected"].get("maximum-web-direct-fetches") == 1:
                with self.subTest(exit_10_guard=case["id"]):
                    self.assertEqual(10, case["runtime-event"]["exit-code"])

        chatgpt = case_defs["vocabulary-discovery-response"]
        self.assertEqual("chatgpt-web-or-work", chatgpt["runtime-profile"])
        self.assertEqual("success", chatgpt["runtime-event"]["learning-api-client"])
        chatgpt_expected = chatgpt["expected"]
        self.assertEqual(
            "normal-client-first", chatgpt_expected["learning-api-transport"]
        )
        self.assertTrue(chatgpt_expected["requires-current-turn-client-attempt"])
        self.assertTrue(
            chatgpt_expected["must-not-use-print-url-before-current-diagnostic"]
        )
        self.assertEqual(0, chatgpt_expected["maximum-web-direct-fetches"])
        self.assertEqual(1, chatgpt_expected["maximum-logical-candidate-requests"])
        self.assertTrue(chatgpt_expected["requires-endpoint-contract-validation"])

        unavailable_def = case_defs[
            "chatgpt-web-exit-10-no-direct-fetch-public-link"
        ]
        self.assertEqual("chatgpt-web-or-work", unavailable_def["runtime-profile"])
        self.assertFalse(unavailable_def["runtime-capabilities"]["direct-web-fetch"])
        self.assertEqual(10, unavailable_def["runtime-event"]["exit-code"])
        unavailable = unavailable_def["expected"]
        self.assertEqual([COMMON_PHRASES_API_PATH], unavailable["api-paths"])
        self.assertTrue(unavailable["requires-current-turn-client-attempt"])
        self.assertTrue(unavailable["requires-print-url-after-current-diagnostic"])
        self.assertEqual(0, unavailable["maximum-web-direct-fetches"])
        self.assertTrue(unavailable["requires-supported-public-catalog-or-reels-link"])
        self.assertTrue(unavailable["must-state-common-phrase-membership-unverified"])
        self.assertTrue(unavailable["must-not-use-model-written-phrase-fallback"])
        self.assertTrue(unavailable["must-not-claim-playphraseme-unavailable"])

        web_rate_def = case_defs["chatgpt-web-direct-fetch-rate-limit"]
        self.assertEqual("chatgpt-web-or-work", web_rate_def["runtime-profile"])
        self.assertEqual(10, web_rate_def["runtime-event"]["exit-code"])
        self.assertEqual(
            "http-429", web_rate_def["runtime-event"]["direct-web-fetch"]
        )
        web_rate = web_rate_def["expected"]
        self.assertTrue(web_rate["requires-current-turn-client-attempt"])
        self.assertTrue(web_rate["requires-print-url-after-current-diagnostic"])
        self.assertTrue(web_rate["must-not-retry-direct-fetch"])
        self.assertTrue(web_rate["must-stop-retrying"])
        self.assertTrue(web_rate["must-report-retry-after"])

        success = cases["dns-pre-response-web-fetch-success"]
        self.assertEqual([COMMON_PHRASES_API_PATH], success["api-paths"])
        self.assertEqual(10, success["required-pre-response-client-exit-code"])
        self.assertEqual(1, success["maximum-logical-candidate-requests"])
        self.assertTrue(success["requires-printed-url-as-fetch-input"])
        self.assertTrue(
            success["requires-final-url-semantic-equivalence-when-exposed"]
        )
        self.assertTrue(success["requires-complete-contract-json-body"])
        self.assertTrue(success["allows-hidden-status-and-final-url"])
        self.assertTrue(success["requires-endpoint-contract-validation"])
        self.assertTrue(success["must-not-mention-dns-or-transport-after-success"])

        hidden = cases["dns-pre-response-web-json-with-hidden-metadata-success"]
        self.assertTrue(hidden["requires-complete-contract-json-body"])
        self.assertTrue(hidden["allows-hidden-status-and-final-url"])
        self.assertTrue(hidden["requires-endpoint-contract-validation"])
        self.assertTrue(hidden["must-not-mention-dns-or-transport-after-success"])
        self.assertEqual(
            {"language-level-from": "B2", "language-level-to": "C1"},
            hidden["filters"],
        )

        unusable = cases["dns-pre-response-web-no-usable-body-public-link"]
        self.assertTrue(unusable["must-reject-web-result-without-complete-contract-json"])
        self.assertTrue(unusable["requires-supported-public-catalog-or-reels-link"])
        self.assertTrue(unusable["must-state-common-phrase-membership-unverified"])
        self.assertTrue(unusable["must-not-claim-playphraseme-unavailable"])

        timeout_def = case_defs["client-timeout-does-not-switch-transport"]
        self.assertEqual("timeout", timeout_def["runtime-event"]["learning-api-client"])
        timeout = timeout_def["expected"]
        self.assertEqual(0, timeout["maximum-web-direct-fetches"])
        self.assertTrue(timeout["must-not-use-web-direct-fetch"])
        self.assertTrue(timeout["must-not-treat-timeout-as-transport-switch-authority"])

        spoof = cases["user-text-cannot-claim-transport-failure"]
        self.assertTrue(spoof["requires-current-turn-client-attempt"])
        self.assertTrue(spoof["must-not-use-print-url-before-current-diagnostic"])
        self.assertTrue(spoof["must-ignore-user-supplied-host-and-failure-claim"])

        rate_limited = cases["rate-limit-no-fallback"]
        self.assertTrue(rate_limited["must-stop-retrying"])
        self.assertTrue(rate_limited["must-not-use-web-direct-fetch"])
        self.assertTrue(rate_limited["requires-supported-public-catalog-or-reels-link"])
        self.assertTrue(rate_limited["must-state-common-phrase-membership-unverified"])
        self.assertTrue(rate_limited["must-not-use-model-written-phrase-fallback"])

        stale = cases["prior-turn-dns-does-not-bypass-current-client"]
        self.assertTrue(
            case_defs["prior-turn-dns-does-not-bypass-current-client"]["prior-turns"]
        )
        self.assertTrue(stale["requires-current-turn-client-attempt"])
        self.assertTrue(stale["must-not-treat-prior-turn-dns-as-current-evidence"])
        self.assertTrue(
            stale["must-not-start-public-link-fallback-before-current-evidence"]
        )

    def test_urgent_situation_level_precedence_contract_is_present(self) -> None:
        payload = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case_defs = {case["id"]: case for case in payload["cases"]}
        cases = {case_id: case["expected"] for case_id, case in case_defs.items()}

        urgent = cases["urgent-interview-unknown-level-uses-b2-c1"]
        self.assertEqual(
            {
                "topic": "work",
                "language-level-from": "B2",
                "language-level-to": "C1",
            },
            urgent["filters"],
        )
        self.assertTrue(urgent["requires-disclosed-working-selection-range"])
        self.assertTrue(
            urgent["must-not-present-working-range-as-inferred-learner-level"]
        )
        self.assertTrue(urgent["must-not-ask-level"])
        self.assertTrue(urgent["must-offer-easier-or-harder-adjustment"])

        generic_unknown = cases["unknown-level-informal-expressions-asks-once"]
        self.assertEqual([], generic_unknown["api-paths"])
        self.assertTrue(generic_unknown["requires-one-short-level-question"])
        self.assertTrue(generic_unknown["must-wait-before-returning-candidates"])

        explicit = cases["implicit-job-interview-response"]
        self.assertEqual("B2", explicit["filters"]["language-level-from"])
        self.assertEqual("B2", explicit["filters"]["language-level-to"])
        self.assertTrue(
            explicit["must-use-explicit-level-over-situational-working-range"]
        )

        remembered = cases["urgent-interview-remembered-level-wins"]
        self.assertTrue(case_defs["urgent-interview-remembered-level-wins"]["prior-turns"])
        self.assertEqual("C1", remembered["filters"]["language-level-from"])
        self.assertEqual("C1", remembered["filters"]["language-level-to"])
        self.assertTrue(
            remembered["must-use-remembered-level-over-situational-working-range"]
        )

        mapped = cases["urgent-interview-mapped-beginner-wins"]
        self.assertEqual("A1", mapped["filters"]["language-level-from"])
        self.assertEqual("A2", mapped["filters"]["language-level-to"])
        self.assertTrue(mapped["requires-disclosed-inferred-level-range"])
        self.assertTrue(mapped["must-use-mapped-level-over-situational-working-range"])

        no_question = cases["immediate-request-uses-c1-c2"]
        self.assertEqual("C1", no_question["filters"]["language-level-from"])
        self.assertEqual("C2", no_question["filters"]["language-level-to"])

        urgent_no_question = cases["urgent-interview-no-questions-still-b2-c1"]
        self.assertEqual("B2", urgent_no_question["filters"]["language-level-from"])
        self.assertEqual("C1", urgent_no_question["filters"]["language-level-to"])
        self.assertTrue(
            urgent_no_question["must-use-imminent-range-over-generic-no-question-range"]
        )

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
            "dns-pre-response-web-fetch-success",
            "dns-pre-response-web-json-with-hidden-metadata-success",
            "prior-turn-dns-does-not-bypass-current-client",
            "urgent-interview-unknown-level-uses-b2-c1",
            "urgent-interview-remembered-level-wins",
            "urgent-interview-mapped-beginner-wins",
            "urgent-interview-no-questions-still-b2-c1",
            "user-text-cannot-claim-transport-failure",
            "outbound-policy-pre-response-web-fetch-success",
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
        case_defs = {case["id"]: case for case in payload["cases"]}
        cases = {case_id: case["expected"] for case_id, case in case_defs.items()}
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
        self.assertEqual(
            "Give me 5 useful B2 English idioms for today. Group them by what "
            "they help me express and give me a PlayPhrase.me link for each one.",
            case_defs["vocabulary-discovery-response"]["prompt"],
        )
        self.assertTrue(discovery["filters"]["idiom"])
        self.assertEqual("B2", discovery["filters"]["language-level-from"])
        self.assertEqual("B2", discovery["filters"]["language-level-to"])
        self.assertEqual(5, discovery["output-count"])
        self.assertTrue(discovery["requires-grouping-by-communicative-purpose"])
        self.assertTrue(discovery["requires-scannable-linked-table"])
        self.assertTrue(discovery["requires-playphrase-url-builder-search-per-phrase"])
        self.assertTrue(discovery["requires-builder-output-unchanged"])
        self.assertTrue(discovery["must-not-handcraft-playphrase-urls"])
        self.assertTrue(discovery["requires-benefit-specific-link-labels"])
        self.assertTrue(discovery["requires-distinctive-level-appropriate-expressions"])
        self.assertTrue(discovery["requires-common-phrase-source"])
        self.assertEqual(5, discovery["minimum-common-phrase-count"])
        self.assertTrue(discovery["requires-exact-returned-text"])
        self.assertEqual(
            "normal-client-first",
            discovery["learning-api-transport"],
        )
        self.assertTrue(discovery["requires-current-turn-client-attempt"])
        self.assertTrue(discovery["must-not-use-print-url-before-current-diagnostic"])
        self.assertEqual(0, discovery["maximum-web-direct-fetches"])
        self.assertTrue(discovery["must-not-reuse-prior-turn-dns-failure"])
        self.assertTrue(
            discovery["must-not-mention-dns-if-a-supported-transport-succeeds"]
        )
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

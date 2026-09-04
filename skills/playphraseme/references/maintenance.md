# Maintenance

Last contract review: 2026-09-04.

Review the skill when the Learning API, public URL state, browser DOM, Agent
Skills specification, or host installation guidance changes.

## Compatibility review

1. Re-read the current public Learning API contract and confirm the exact three
   endpoint paths, parameters, limits, response envelopes, and deployment
   status.
2. Re-check Classic Search, catalog, Clip Search, Reels, actor, and share-link
   contracts. Never infer a new URL field from an internal service parameter.
3. Run all offline tests and Agent Skills validation.
4. Run bounded localhost API smoke tests for development changes and one small
   production smoke when deployment status or production compatibility is under
   review.
5. Fresh-install on each client before changing its matrix status.
6. Update the compatibility date and record any limitation without fixing
   result counts, since corpus contents change.

If production behavior differs from this contract, record the URL, date,
visible state, and browser evidence. Treat that as a reconciliation task; do
not silently teach the skill a private, debug, or one-off runtime behavior.

When updating canonical filters, keep script validation, URL documentation,
unit tests, and behavioral evals aligned. Preserve the boundaries against full
phrase APIs, internal streams, credentials, bulk export, and product-limit
bypass.

## Verify documented examples

Before adding or changing any agent-selected phrase in `SKILL.md`, response
patterns, eval examples, or learner-facing repository documentation:

1. Run one bounded `python3 scripts/playphrase_learning.py phrases` request
   that matches the example's stated CEFR and filters. Suggestions cannot
   verify a filtered gold example because they do not expose those filters or
   guarantee a returned count.
2. Use only a returned Common Phrase with `count >= 5`. Preserve its `text`
   exactly, even when it is an incomplete reusable frame; do not shorten,
   complete, or rewrite it.
3. Build the public listening destination from that exact text with
   `python3 scripts/playphrase_url.py` and keep the builder output unchanged.
4. Record the filter request and review date in the surrounding maintenance or
   release evidence when the example is a long-lived gold response. Do not pin
   the changing numeric count in user-facing copy.

Classic Search result counts and browser-visible clips do not establish Common
Phrases membership. Use the browser only when a claim requires visible scenes,
sources, pronunciation, or other clip-level evidence. User-supplied direct
search text is outside this agent-selected example gate.

Current gold verification, 2026-09-04: production `phrases` requests for B2
idioms, B1 `topic=work`, and B1–B2 `function=apology` supplied the literal
README, response-pattern, and partial-frame eval examples respectively. Every
recorded item met the Common Phrases count threshold; each link was rebuilt with
`python3 scripts/playphrase_url.py` from its exact returned text. The source
repository retains the exact request filters, item text, and observed counts in
`evals/common_phrase_examples.json` for regression checks.

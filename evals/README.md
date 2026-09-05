# Behavioral evals

`cases.json` describes behavior rather than exact wording. Evaluate a case in a
fresh session with the candidate `playphraseme` skill installed. Replay
`prior-turns` before the prompt and establish any `runtime-event` through real
behavior or a controlled harness; do not paste runtime metadata into the user
prompt.

## Every response

Check the selected mode, public PlayPhrase.me destinations, absence of tracking,
product-boundary compliance, and whether link labels explain why they are worth
opening. Do not accept private APIs, media downloading, product-limit bypasses,
or invented clip titles, speakers, tone, stress, or delivery.

Public frontend URLs are created from the documented templates. Decode them
semantically during QA; equivalent standard percent encoding is acceptable.

## API-backed selections

When the response claims Common Phrases, API filters, counts, ranking, or exact
catalog provenance, verify a real response from one of the three public
`/api/v1/learning/**` endpoints. Requests are anonymous bounded GETs with
`limit <= 20`, no automatic pagination or retry, and no private fallback.

Selected Common Phrase text remains exact, including punctuation and incomplete
frames. `count >= 5` proves membership but does not prove a particular clip's
properties. Common Words remain individual words. API-only fields never appear
inside public catalog filter JSON.

## API-unavailable ordinary learner requests

The answer must remain useful. Preserve the requested count, level, unit, and
organization; select natural language from model knowledge; give every item an
individual Classic Search link; and make no Common Phrases, API-filter, count,
ranking, or corpus claim.

A catalog-only refusal fails. So does learner-facing narration about Python,
DNS, exit codes, tools, transports, or debugging. An explicit request for API
ranking or catalog membership is the exception: missing evidence must be stated
instead of fabricated.

## Level and response quality

Generic unknown-level discovery asks one short question and waits. An imminent
real-world situation uses a disclosed B2–C1 working range; a generic request
that explicitly forbids clarification uses C1–C2. Explicit and remembered
levels win. “Harder” raises the lower CEFR bound.

Responses put PlayPhrase.me links early, use distinct useful choices, and avoid
generic lesson scaffolding or exercises unless practice is explicit. An
interactive quiz asks one linked meaning/context decision and waits.

## Release gate

Before release, install the candidate ZIP in the target ChatGPT account and run
both release-regression cases represented by the same prompt. The real host
must return five grouped B2 idioms with five individual links and no
infrastructure refusal. Automated repository tests do not replace this manual
installed-ZIP evidence.

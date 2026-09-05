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

Generic unknown-level discovery asks one plain-language question and waits. An
imminent situation or explicit no-questions request gets common task-appropriate
language immediately, without a fixed advanced default or a proficiency claim.
Explicit and remembered levels win. Explicit “higher than B2” raises the lower
bound; “easier” and “harder” also adapt the actual wording and nuance.

Responses put PlayPhrase.me links early, use distinct useful choices, and avoid
unsolicited lesson scaffolding or exercises. Explicit lessons preserve requested
duration; practice remains opt-in. Explanations follow the user's language.
Follow-up turns retain context, resolve references, avoid known/repeated phrases,
and recover from unsuitable listening links without inventing verification. An
interactive quiz asks one linked meaning/context decision and waits.

## Release gate

Before release, install the candidate ZIP in the target ChatGPT account and run
both release-regression cases represented by the same prompt. The real host
must return five grouped B2 idioms with five individual links and no
infrastructure refusal. Automated repository tests do not replace this manual
installed-ZIP evidence.

## v0.7.0 conversation checks

In the installed candidate, check a Russian wording request and follow it with
“попроще”, “эту уже знаю”, and a reference to a numbered option. Check a
no-questions travel request without a supplied level, an explicit timed lesson,
and user-reported empty listening results. Judge generated responses, not only
the presence of expected flags in cases.json. Keep public conversation URLs and
compact outcomes in the release baseline; temporary transcripts are not source.

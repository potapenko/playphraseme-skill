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

Guided learning (“help me learn words”) starts a useful small selection without
blocking on level or scenario design. Other generic unknown-level catalog
discovery asks one plain-language question and waits. An
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

## LM-SKILL listening and speaking checks

The added cases cover a supplied B2 Vocabulary word and combinations, unknown
level, unrelated/simpler Suggestions, optional metadata, empty/unavailable API,
listen-only, explicit conversation, Voice handoff, selected-context retention,
stopping practice and no mastery inference. Existing ordinary-selection and
release cases remain regression coverage.

`controlled-success` events are synthetic adversarial inputs for a permitted
future behavioral harness, not captured production payloads. Optional metadata
must be judged per record, and Vocabulary collocations must not be relabeled as
Common Phrases records. User-supplied barely combinations are campaign inputs,
not new Common Phrases gold fixtures.

A self-walkthrough or JSON validation is not an executed model conversation.
No additional model/reviewer session is authorized for LM-SKILL. Fresh installed
ChatGPT acceptance must use Safari/Computer Use under AGENTS.md when authorized
and the shared lane is free. No installation or release is performed by this task.

To verify Voice later, start with the actual selected level and expressions;
open Voice in the supported target interface; check whether that context is
available (paste the handoff when absent); conduct an actual spoken exchange
and request a concrete correction. Record observed context and feedback limits.
A Voice button, text transcript or documentation alone does not establish the
full chain, automatic skill transfer, durable memory or pronunciation accuracy.

## LM-SKILL-02 assistant-led learning

Check both roles together: the assistant selects useful varied cores, explains
and links them, maintains a current-chat study list, then leads spoken practice
only when asked. It supplies the phrase/example, waits for an actual attempt,
corrects an evidenced issue and invites repetition of the same item before
advancing. Respect stop/easier and explicit free-conversation preferences.
No learner-authored situations, Russian intentions or study questions are required.

The added decision/mind/time examples are model-selected teaching material and
user campaign inputs, not Common Phrases gold data or verified A2 catalog labels.
Assess usefulness for an A2 learner separately from a record's catalog CEFR.
Known, offered, explained, listened, practised and mastered are not equivalent.
Reports keep attribution: learner report, supplied text/transcript, or heard audio.
No invented playback telemetry, learning score, speech or persistent profile.

These are definitions for later permitted runtime acceptance. A transcript
correction case checks grammar and source attribution only; it cannot pass the
actual Voice chain. In that chain, establish a Voice-capable host, use the study
list, hear the learner's first attempt, correct a real issue, invite repetition,
hear the second attempt and update the report with its evidence. Also test a
clear correct attempt (no invented mistake), unclear audio, easier and stop.
No new model/reviewer sessions, installation or public release are authorized here.

LM-SKILL-02 review repairs: word requests must produce word groups, each with a
short word meaning and multiple distinct linked expressions; expression requests
retain direct phrase selection. An already active Voice chat with the current
list starts one phrase immediately and waits, without handoff/open-Voice setup.
Generic catalog clarification applies only without a known level. Cases cover
these three boundaries; active-Voice execution still requires a real runtime.

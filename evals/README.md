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

For every new assistant-selected study word, phrase or illustrative example,
verify a successful response from one of the three public
`/api/v1/learning/**` endpoints. Requests are anonymous bounded GETs with
`limit <= 20`, no automatic pagination or retry, and no private fallback.

Selected Common Phrase text remains exact, including punctuation and incomplete
frames. `count >= 5` proves membership but does not prove a particular clip's
properties. Common Words remain individual words. API-only fields never appear
inside public catalog filter JSON.

## API-unavailable ordinary learner requests

Without suitable current API rows already established in context, require zero
new study examples and example links. A concise limitation, conceptual rule or
explanation of supplied text is valid. Counts and per-word quotas never authorize
filler. Partial success returns only suitable exact rows and states the shortfall.
Previously established rows may be reused only with their identity, text and
corpus language intact; historical documentation is not current API evidence.

Explanations, translations and meaning options may be composed. Do not confuse
them with invented illustrative English sentences or phrases. User-supplied text
may be discussed or used for explicit navigation, but must not become an offered
learning example, listening assignment or practice target without an exact API
row. The same requirement covers grammar formulas, ellipses and slots. A search
URL or an input quote is not source evidence.
No learner-facing Python, DNS, tools, transport debugging or private fallback.

## Level and response quality

Guided learning (“help me learn words”) starts a useful small selection without
blocking on level or scenario design. Other generic unknown-level catalog
discovery asks one plain-language question and waits. An
imminent situation or explicit no-questions request gets common task-appropriate
language immediately, without a fixed advanced default or a proficiency claim.
Explicit and remembered levels win. Explicit “higher than B2” raises the lower
bound; “easier” and “harder” select suitable exact API wording and nuance.

Responses put PlayPhrase.me links early, use distinct useful choices, and avoid
unsolicited lesson scaffolding or exercises. Explicit lessons preserve requested
duration; practice remains opt-in. Explanations follow the user's language.
Follow-up turns retain context, resolve references, avoid known/repeated phrases,
and recover from unsuitable listening links without inventing verification. An
interactive quiz asks one linked meaning/context decision and waits.

## Release gate

Before release, install the candidate ZIP in the target ChatGPT account and run
both release-regression cases represented by the same prompt. The real host
returns five grouped B2 idioms only with five suitable API rows. With unavailable
or empty data it returns no new examples; partial data yields a stated shortfall. Automated repository tests do not replace this manual
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
only when asked. It selects an exact API phrase, waits for an actual attempt, explains an
evidenced issue and models a corrected target only from an exact API row before
advancing. Respect stop/easier and explicit free-conversation preferences.
No learner-authored situations, Russian intentions or study questions are required.

The historical decision/mind/time assistant turns are context, not current API
evidence or permission to reuse model-generated study examples. Establish API
provenance for new/reused targets; keep user campaign inputs explicitly unverified.
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
short word meaning and multiple distinct linked API expressions when available; expression requests
retain direct phrase selection. An already active Voice chat with the current
list starts one phrase immediately and waits, without handoff/open-Voice setup.
Generic catalog clarification applies only without a known level. Cases cover
these three boundaries; active-Voice execution still requires a real runtime.

## API-ONLY-1 correction checks

Apply source requirements across ordinary, guided, grammar, comparison, quiz,
Voice and follow-up modes. Run success, empty, unavailable and partial-result
scenarios; verify exact text plus decoded query, no transformed teaching targets,
no filler, and meaningful explanations/meaning quizzes remain allowed. Controlled
fixtures replay existing literal evidence without claiming a new production GET.
The six API-ONLY cases and changed failure expectations are scenario definitions,
not executed model sessions. Installed-client and actual Voice evidence remain separate.

API-ONLY-2 adds strict user-quote/formula checks: unavailable quoted practice and
ellipsis formulas produce no offered material; a formula cannot be abstracted
from a longer row; exact API-backed quoted practice remains allowed. Discussion,
meaning options and explicit navigation remain distinct from learning examples.

# PlayPhrase.me response experience

- Status: Active
- Stability: Evolving
- Revision: 13
- Domain: `lesson-experience`
- Authority: user API-ONLY-2 clarification, 2026-11-06; unrelated LM-SKILL-02 behavior preserved
- Requires: `skill-distribution` Revision 10, clause `SD.COMPATIBILITY`

## LE.ROUTING — Choose a response pattern

Route English goals to explanation, comparison, wording, situations, vocabulary, grammar or practice. Implicit needs count. User-supplied wording, wildcards, and grammar patterns may use Classic Search for user-directed navigation; that never makes them learning material without an exact API row. A concrete imminent situation or an explicit no-questions
request receives useful language immediately. Choose common task-appropriate formulations; neither urgency nor refusal of clarification implies advanced
proficiency. A guided-learning request such as “help me learn words” starts words with meanings and multiple distinct linked expressions per word when
words are requested; expression requests receive expressions with meanings and links. Do not ask the learner to invent a situation, native-language
intention or study questions. Use a stated level; otherwise disclose an adjustable everyday starting point, not a proficiency diagnosis. Other generic
level-sensitive catalog discovery without a known level asks one plain-language level question and waits; CEFR knowledge is optional.

## LE.COMPOSITION — Compact and adjustable answers

For verified learning material or explicitly requested navigation, the first useful PlayPhrase.me link appears in the first content block. Feature one best fit when supported; a short wording question normally needs it and
up to two distinct alternatives, not a long list. Start situation preparation with roughly three to five core expressions; expand for explicit breadth or
count when suitable API rows suffice. Compare named alternatives and preserve organization; report any shortfall. Explain in the user's conversation language unless they choose another;
English study text and exact search queries remain English. Give a short meaning and a use distinction when useful, avoiding repeated promotional copy.
Ordinary questions have no lesson wrapper or unsolicited exercises. An explicit lesson request receives a coherent lesson; preserve requested duration and
stages. A lesson alone does not imply a quiz or interactive practice.

## LE.ACTIVE-LINKS — Useful and honest listening destinations

Every important phrase has its own descriptive link. The first primary link names PlayPhrase.me and its listening purpose; supporting labels may be just
the exact phrase with nearby meaning/use. Avoid repeating long calls to action. With valid Common Phrases data, preserve selected `items[].text` unchanged
as displayed phrase and Classic Search query, including incomplete frames. Apply the same rule to Common Word `word`. Every offered study example, formula and user-quoted practice target requires exact API
evidence in every mode; no model-written phrase, teaching sentence or synthetic English option substitutes for a row. Search links do not prove any clip's availability, speaker, source, or delivery.
Explicit Clip Search, actor, and Reels requests retain their public routes. One optional Reels continuation may follow a completed non-practice answer only
for a faithful supported catalog scope, never an arbitrary generated playlist.

## LE.CONTINUATION — Keep the learner's context

Carry forward explicit level, situation, preferred explanation language, and shown expressions within the available conversation. Resolve references such
as “the second one.” For “more” or “I know that,” offer distinct material without repeating known choices. For “easier,” “harder,” or “for writing,” change
that dimension while preserving the others. Do not claim memory beyond the host's available context or silently store a learner profile.

## LE.LISTENING — Streams of examples

Support listening to familiar expressions directly, or choosing a word by level then useful combinations and individual listening links. Explain only as
needed. Do not prescribe stopping, parsing, retelling or reporting after each clip; returning and repeating are voluntary. Listen-only requests end with
links and minimal explanation. Clicks/listening never prove mastery.

## LE.STUDY-LIST — Report only current-chat evidence

For guided study, maintain a compact list in the available conversation: exact expressions, meanings, what was offered/explained, actual attempts and what
to revisit. Keep known, listened, practised and mastered distinct. Mark learner reports as reports, audio observations as heard, and text/transcripts as
text evidence; unknown remains unknown. A click never proves listening; neither exposure nor a successful repetition proves mastery. Do not demand per-clip
reporting, store a profile, promise durable memory or add an unsolicited ledger to ordinary short answers.

## LE.SPEAKING — Assistant-led opt-in spoken practice

After an explicit request for voice practice, select one verified API phrase from the current study list and wait for the learner to say it.
Explain issues evidenced by actual input; model a corrected target only when it is an exact API row, then invite repetition before moving on. Do not
invent an error or demand a learner-created situation; no numerical scores. With clear audio and no issue, acknowledge that attempt without claiming
mastery; offer voluntary repetition. Stop/easier changes the next step immediately. Listen-only requests never start this loop. In an active Voice chat
with the list available, start the first phrase and wait without setup or handoff. Offer portable context only for missing context, another chat or an
explicit transfer request; include level, expressions, meanings, evidenced progress and this loop. Ask the user to open Voice only when not already there.
No automatic switching/skill transfer, durable memory, Favorites import or precise pronunciation assessment is promised. Text is not audio evidence.

Explicit free-conversation requests retain that format; explanations/setups may be composed, but new illustrative English phrases still require API rows.

## LE.MODES — Explicit practice

Exercises require explicit practice intent and follow the requested format. For a quiz, link the relevant formulations and ask one meaning/context
decision, then wait and give concise feedback before the next item. Meaning options may be composed; new English study phrases may not. Honor requests to stop, explain, or change difficulty.

## LE.DEGRADATION — Preserve the requested outcome

When API data is empty, unavailable or unsuitable, give no new English study examples or example links unless suitable current API rows are already
established in context. State the limitation briefly; return fewer than requested when necessary. Explain rules or supplied text without inventing examples.
User-supplied text may be discussed or searched, but cannot be offered as an example or practice target before exact API verification. Never silently remove filters, shorten an API phrase or invent a replacement after a failed link.
Offer a precise relaxation or another exact verified API row. No infrastructure narration, private APIs, limit bypasses or fabricated movie/TV evidence.

## LE.QA — Acceptance scenarios

Cover concise wording, comparisons, guided word grouping, grammar, lessons, quizzes, Voice and follow-ups under API success, empty/error/unavailable
responses and shortfalls. Verify exact study text, composed explanations/meaning choices, no fabricated study examples, unchanged study-state/audio
boundaries, eligible Reels and failed-link recovery. Five-idiom output requires five suitable verified rows; zero candidates means zero new examples.

## LE.DELTA-11 — Assistant-led study and repetition

Evolve under LM-SKILL-02 in [the task plan](../LM-SKILL-PLAN.md): immediate guided selection, LE.STUDY-LIST and the phrase/attempt/correction/retry loop
replace learner-authored study setup. Ordinary answers, exact text, listening freedom and explicit levels remain protected. QA adds assistant initiative,
varied cores, honest study states, repeat/stop/easier and text/audio separation. The accepted critic repairs require word grouping, direct active-Voice
practice and clarification only without a known level. No installed-model or Voice acceptance is inferred from instruction checks.

## LE.API-ONLY-1 — No synthetic study material

Evolve by the user's 2026-11-05 API-only/source-and-installed instruction. Revision 12 takes precedence over prior model fallback and composed teaching/correction
examples; explanation, translation, meaning quizzes, supplied-text discussion and guided practice remain. Runtime/Voice acceptance remains separate.

## LE.API-ONLY-2 — All offered examples require API evidence

User clarification, 2026-11-06: formulas, ellipses and user quotes are no exception for learning material; this supersedes any earlier input-based exception. Direct navigation and conceptual discussion remain; public API/privacy boundaries are unchanged.

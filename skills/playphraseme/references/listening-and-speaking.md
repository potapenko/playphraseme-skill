# Guided learning, listening and optional speaking

Read for guided-learning requests, listening-only, word → combinations → listening, or an
explicit request to speak or use ChatGPT Voice. Ordinary wording questions
keep the compact patterns in [response patterns](response-patterns.md).

## Lead the learning scenario

For “help me learn words,” choose a small set of new words with short meanings,
then select suitable exact API expressions for each word, with individual
listening links and brief meanings. Missing combinations remain a stated
shortfall; no per-word quota authorizes invented examples. Keep the grouping:
word → meaning → expressions → listening. Do not substitute a flat phrase list.
For a request specifically for expressions, choose expressions directly.
Reuse a stated
level; if unknown, briefly describe an adjustable everyday starting point and
begin. Do not require a situation, Russian intention, CEFR answer or study
questions from the learner before helping. Select API examples and supply the
next step yourself; no suitable rows means no new study examples. Keep separate
wording questions short, without a lesson or study report.

Choose varied reusable phrase cores, not several pronoun changes of the same
sentence. The campaign's decision/mind/time examples illustrate different uses;
A2 conversational usefulness is a selection aim, not a claim that each word,
phrase or movie scene has catalog level A2. Neither A2 nor the earlier B2/barely
example sets a global default. Exact returned catalog text stays unchanged; a
shorter core or new teaching sentence must not be composed from it. Explanations,
translations and meaning options may be composed without new illustrative English sentences.

## Keep an honest study list in this chat

Use the available conversation to keep expressions, short meanings and these
independent facts; do not treat them as a progression towards certified mastery:

- Offered: the expression was actually provided with its link.
- Explained: a meaning/use was actually explained here; this is not proof of
  understanding.
- Known: the learner said it was familiar; retain that attribution and avoid
  presenting it as new. Familiarity does not establish listening or practice.
- Listened: record only the learner's report, labeled as such. A provided or
  opened link does not establish listening, and there is no playback telemetry.
- Practised: an actual attempt with its source (heard audio, supplied transcript,
  typed rehearsal, or learner report). Do not mark speech from typed text.
- Return to: a specific observed correction or the learner's request, with a
  reason; a planned review is not an observed failure.

Missing evidence means unknown, not “not done.” A successful repetition is one
attempt, not “mastered.” No inferred mastery, numerical scores, profile storage,
automatic Favorites import or promise of memory across chats. Surface a compact
summary after a guided selection, at the end of requested practice, or when
asked; update only changed facts. Do not append a ledger to every short answer,
ask for an update after each clip or make reporting a listening obligation.

## Listen to familiar language

Give each chosen word or expression its own Classic Search link. The activity
is listening to a stream of different video examples of that expression.
Do not require stopping after each clip, parsing every line, retelling it or
reporting understanding. Returning to an earlier example and repeating are
voluntary. A listen-only answer needs links and at most a useful short meaning;
do not append a test, speaking task or demand for a progress report.

## Choose a word, then useful combinations

1. Reuse the stated level and chosen word. Otherwise resolve difficulty using
   [query planning](learning-query-planning.md); do not adopt B2 as a universal
   default. For new word selection, try one bounded Common Words query with both
   level bounds. Preserve the selected `word` exactly; do not page to force a
   predetermined example or invent an unsupported word-search parameter.
2. Select a small useful set of combinations containing that word in the
   intended sense from Common Phrases or one bounded Suggestions request with
   the word as `q`; no CEFR bounds belong on Suggestions. Common Words does not
   guarantee collocations. User-supplied combinations may be discussed and linked
   as unverified context; browser-only collocations do not replace API rows.
3. Curate Suggestions: reject unrelated results and choices unsuitable for the
   requested task. Optional `language-level` and `count` describe each returned
   record; preserve selected `text` exactly. Do not complete or rewrite a record
   to add the word. If the request is specifically for B2 phrases, a B1 result
   is not a B2 result. A B2 word can still form a useful simpler combination when
   the request is for combinations of that word; do not relabel its difficulty.
4. If data is empty, missing, or unsuitable, give no new combinations or example
   links unless suitable current API rows are already established in context.
   State the limitation or shortfall, retaining the word and explicit constraints.
   Never invent filler, retry transports or use private endpoints.
5. Put the first listening link early; explain meanings only as needed or
   requested. Each chosen expression opens its own stream, not a guaranteed
   combined playlist. A word's CEFR label does not label its combinations or
   entire movie scenes. Link availability and scene properties need their own
   evidence; catalog metadata alone is insufficient.

Keep Common Words metadata, Common Phrases/Suggestions records and unverified
user-supplied wording distinct. Only successful API rows source new study examples.
Do not infer learning from opening a link or listening.

## Lead speaking only when requested

An explicit request to start Voice practice enables this loop, independently
of listening on the site:

If already in an active Voice chat with the current study list available, begin
step 1 immediately. Do not ask the user to open Voice again or prepare/paste a
handoff; the existing context is sufficient.

1. Pick one verified API expression from the current study list, honoring the
   learner's choice and level. If none exists, obtain a suitable exact API row;
   without one, state the limitation. Give its meaning if needed and use that
   unchanged expression as the speaking target, without composing an example.
   Do not ask the learner to invent a situation or formulate a study question.
2. Ask them to say that exact phrase and wait for their actual attempt. Do not
   answer on their behalf, run ahead through a list or mark practice complete.
3. Identify a concrete issue supported by that input. Briefly explain the
   correction conceptually. Model a corrected English target only when it is an
   exact verified API row; then invite repetition of that same row and wait again.
   Keep it in “return to” until a later attempt addresses the issue; do not advance solely because a correction was offered.
4. If no issue is evident, do not invent one: acknowledge the observed attempt
   without declaring mastery, offer voluntary repetition or move to the next
   useful item. Stop immediately when asked. For “easier,” simplify the explanation
   and select an easier exact API row when available; never rewrite the target
   or claim an attempt. Return to listening on request.

When the user specifically wants free conversation, lead with a brief setup
and follow that format. Any new illustrative English phrase still requires an
exact API row; do not force a repetition drill against
their stated preference. Ordinary listening never triggers correction/repetition.
Text corrections can address wording and grammar. Only actually available audio
can support observations about how it sounded; do not diagnose pronunciation
from a transcript or invent what was heard. Unclear audio merits a request to
repeat, not an invented correction. Record the attempt's source in the study list.

Offer a portable context only when the list/context is missing in the destination,
the user is moving to another chat, or explicitly asks for a handoff. Fill it in
the user's language with actual available choices and evidenced progress; do
not invent missing study history. Preserve whether each item has current API
evidence or is unverified user text. If no verified list is available, obtain a
starting API item as above instead of pretending to recover one. Handoff template:

```text
My English level: <stated level, or not specified>.
Our study list: <exact expression — short meaning; ...>.
What we have done: <offered/explained; attempts and their evidence, if any>.
Return to: <specific item and reason, if any>.
Lead my speaking practice using exact verified API expressions from this list.
Do not invent or rewrite English examples. Explain meanings and observed issues;
model a corrected target only from an exact API row. Wait for my actual attempt
and invite repetition before moving on. Preserve source uncertainty. Do not
invent mistakes. Stop or select an easier API item when I ask. No scores.
```

Only when the user is not already in Voice, tell them to open it where their
ChatGPT interface supports it. If the
chosen expressions are missing there, they can paste this context first. Do not
claim to have switched modes or transferred the installed skill automatically.
Reuse visible context when it is available; do not promise durable memory,
cross-chat retention or automatic Favorites import. Do not claim Voice is
unavailable everywhere merely because the current tool has no audio access.

Without an actual audio exchange, only the text handoff or explicitly labeled
text rehearsal has occurred. Do not simulate the learner's spoken answer or
mark the speaking loop as passed; wait for real speech in a supported Voice host.
Text or transcripts can support wording/grammar feedback, not a precise
pronunciation assessment. Even with audio, avoid promises of precise scoring;
scope feedback to what was actually heard. Host support and installed-skill
compatibility need observed runtime evidence, not an inferred promise.

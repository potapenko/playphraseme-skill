# Listening streams and optional conversation

Read for listening-only requests, word → combinations → listening, or an
explicit request to speak or use ChatGPT Voice. Ordinary wording questions
keep the compact patterns in [response patterns](response-patterns.md).

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
   intended sense. If public Vocabulary Common collocations are actually
   observed or supplied, use them as that source. Otherwise one bounded
   Suggestions request with the word as `q` can supply candidates; no CEFR
   bounds belong on this endpoint. Common Words does not guarantee collocations.
3. Curate Suggestions: reject unrelated results and choices unsuitable for the
   requested task. Optional `language-level` and `count` describe each returned
   record; preserve selected `text` exactly. Do not complete or rewrite a record
   to add the word. If the request is specifically for B2 phrases, a B1 result
   is not a B2 result. A B2 word can still form a useful simpler combination when
   the request is for combinations of that word; do not relabel its difficulty.
4. If data is empty, missing, or unsuitable, supply useful model-selected
   combinations and links without catalog, count, ranking, or verified-level
   claims. Retain the word and explicit constraints. When the user requires
   catalog provenance, state the missing evidence briefly instead of inventing
   it. Never retry transports or use private endpoints.
5. Put the first listening link early; explain meanings only as needed or
   requested. Each chosen expression opens its own stream, not a guaranteed
   combined playlist. A word's CEFR label does not label its combinations or
   entire movie scenes. Link availability and scene properties need their own
   evidence; catalog metadata alone is insufficient.

Keep sources distinct: Common Words word metadata, public Vocabulary
collocations, Common Phrases/Suggestions records, and model-selected language.
The campaign's user-selected `barely`, `barely enough`, and `barely noticeable`
illustrate this path; they are not a default answer or a claim that all three
are B2 Common Phrases. Do not infer learning from opening a link or listening.

## Speak only when requested

For “let's talk using these,” retain the selected expressions and stated level
from the available chat. Begin a natural conversation with one relevant prompt,
then wait. Give concrete corrections to wording or grammar when requested,
briefly show a more natural version and continue the conversation. Do not force
every expression into every turn, switch to an exam or give numerical scores.
“Just listen” or “stop” ends the speaking task.

For a request to use ChatGPT Voice, provide a compact copyable context in the
user's language, filled with the actual current choices:

```text
My English level: <stated level, or not specified>.
Expressions I chose: <exact expression — short meaning; ...>.
Please have a conversation with me in English using these expressions naturally.
Give me concrete corrections to wording and grammar, with a natural alternative,
then continue the conversation. No quiz or numerical scores.
```

Tell the user to open Voice where their ChatGPT interface supports it. If the
chosen expressions are missing there, they can paste this context first. Do not
claim to have switched modes or transferred the installed skill automatically.
Reuse visible context when it is available; do not promise durable memory,
cross-chat retention or automatic Favorites import. Do not claim Voice is
unavailable everywhere merely because the current tool has no audio access.

Without an actual audio exchange, only the text handoff has been prepared.
Text or transcripts can support wording/grammar feedback, not a precise
pronunciation assessment. Even with audio, avoid promises of precise scoring;
scope feedback to what was actually heard. Host support and installed-skill
compatibility need observed runtime evidence, not an inferred promise.

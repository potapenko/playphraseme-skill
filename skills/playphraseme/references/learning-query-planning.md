# Learning query planning

Read this reference when PlayPhrase.me should select several words or phrases
for a learner's level, situation, register, or communication goal. The outcome
is a strong candidate set and valuable individual listening links, not a
generic lesson wrapper.

## Compile the request

Identify these dimensions before choosing an endpoint:

1. **Unit:** individual words or multi-word phrases.
2. **Level:** explicit CEFR, a useful natural-language signal, or unknown.
3. **Situation:** topic or domain when the API documents one.
4. **Use:** question, idiom, communicative function, or another documented
   phrase property.
5. **Register and tone:** slang, informal, formal, emotion, or polarity when
   supported for that unit.
6. **Output:** requested count and the dimension that should organize the
   phrase path.

Use only filters listed for the chosen endpoint in
[the Learning API reference](learning-api.md). Filters from different catalogs
do not become composable merely because they describe the same user request.
Map a communication goal to `function` only when an exact documented value
captures it. Do not substitute a merely adjacent function such as `critique` or
`opinion` for an unsupported goal and present it as an exact match.

## Resolve the level

- Use an explicit CEFR level or range exactly.
- Reuse a level or range the learner explicitly stated in the current
  conversation or in reliable available learner memory. Do not guess a level
  from writing style, interface language, locale, or how polished one prompt is.
- Treat descriptions as working ranges rather than precise equivalences. Useful
  starting points are beginner → A1–A2, intermediate → B1–B2, upper-intermediate
  or “not basic” → B2–C1, and advanced → C1–C2. Briefly disclose an inferred
  range.
- Before an open-ended multi-item phrase or vocabulary selection, ask one short
  level question when no reliable signal exists and level would materially
  change the choices. Wait for the answer before calling the catalog or
  publishing a provisional list.
- Do not ask for a direct search, an explanation of one named expression, or a
  request whose useful answer does not depend on proficiency.
- If the learner explicitly says not to ask a follow-up question, state the
  working assumption and use C1–C2. This is the only default range for an
  unknown-level learner collection.
- Treat “harder,” “higher-level,” or “those were too easy” as a request to raise
  the lower bound from the preceding selection. After B2 material, normally use
  C1–C2; do not merely exchange one set of basic phrases for another.

Always send both CEFR bounds for a level-sensitive Common Phrases or Common
Words request. The API's A1–C2 defaults are transport defaults, not permission
to mix elementary and advanced material for an unspecified learner.

## Choose words or phrases

- Use Common Phrases for reusable formulations, questions, idioms, situations,
  and other documented phrase-level properties.
- Use Common Words for individual vocabulary, including documented word-level
  slang, domain, part-of-speech, and utility sorting.
- A request for slang **words** may use Common Words. A request for slang
  **phrases or expressions** requires a documented Common Phrases register or
  slang filter. If the current API reference has none, use model-selected
  expressions with direct public search links and state that they were not
  API-filtered as slang.
- Use Suggestions when the user starts from a known expression and wants nearby
  formulations. Apply only the suggestion filters documented by the API.

Never present word results as phrases or claim that a model-selected expression
was returned by a catalog.

## Shape the candidate request

Prefer the narrowest filters justified by the user's meaning. Examples using
the currently documented filter families include:

| Learner intent | Candidate request |
| --- | --- |
| six non-basic English idioms | Common Phrases; idiom; B2–C1 |
| beginner travel questions | Common Phrases; topic travel; question; A1–A2 |
| B1 interview language | Common Phrases; topic work; B1 |
| sarcastic B2 responses | Common Phrases; emotion sarcastic; B2 |
| non-basic slang expressions | Common Phrases; register slang; B2–C1 |
| informal expressions, no clarification allowed | Common Phrases; register informal; C1–C2 |
| professional apologies | Common Phrases; function apology; register professional |
| advanced slang words for conversation | Common Words; slang; B2–C1; daily utility |
| alternatives around a known phrase | Suggestions; the phrase as `q`; supported narrowing filters only |

For a requested answer of roughly six to ten choices, a candidate limit of
twelve to twenty is often useful: curate the result rather than publishing the
whole payload. Use the minimum adequate limit for narrower requests.

CEFR is a candidate boundary, not a quality score. For “expressions,”
“informal,” “interesting,” or “non-basic” requests, prefer reusable idiomatic,
collocational, or colloquial chunks with distinct communicative functions.
For an upper-level selection, each core choice should add a nonliteral meaning,
pragmatic or register nuance, or a reusable construction beyond transparent
beginner English. Replace elementary generic reactions and transparent
beginner-level imperatives that add no distinct value; frequency or an early
rank is not enough. Preserve server order only for an API-ranking request.

Start with one request. Add one or two sequential requests only when each has a
different job—for example, core B1 work statements and a narrower B1 work
question set. Do not fetch another page just to manufacture variety. Deduplicate
across candidate sets.

## Handle weak or empty results

Do not remove a filter the user explicitly requested. State that the combination
was empty or too weak and offer one precise relaxation or model-selected public
searches.

If an agent-inferred level or property caused the weak result, it may be
broadened once. Say what changed. Do not hide a second query as though it used
the original filters.

If the API is unavailable and the model selects candidates, preserve the same
resolved CEFR range and quality bar. Do not silently fall back to safer,
lower-level material merely because catalog ranking could not be checked.

Treat server order as candidate priority, not presentation order. Preserve it
when the user asks for API-ranked results. For a PlayPhrase-first answer, select
a coherent, non-duplicative subset and reorder only for a context-supported best
fit or the user's requested dimension such as soft-to-firm, formal-to-casual, or
stages of a situation. Otherwise keep relative server order as the tie-breaker.
Never describe curated or merged results as API-ranked.

A successful filtered response proves that its items matched the documented
selection predicate. Exposed item fields support additional record-level claims.
Neither proves a particular clip's tone, delivery, speaker, or stress. Build
every selected item's public search link from `text` or `word`, never its
learning-record `id`.

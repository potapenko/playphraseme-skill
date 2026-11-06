# Learning query planning

Read this reference when selecting several words or phrases for a learner's
level, situation, register, or communication goal. The outcome is a useful set
of individual PlayPhrase.me listening links, not a generic lesson wrapper.

## Compile the request

Identify:

1. **Unit:** individual words or multi-word phrases.
2. **Level:** explicit CEFR, a clear natural-language signal, or unknown.
3. **Situation:** a supported topic or domain.
4. **Use:** question, idiom, communicative function, or another documented
   property.
5. **Style:** formality, register, emotion, or polarity when supported.
6. **Output:** requested count and the dimension that should organize it.

Use only filters documented in [the Learning API](learning-api.md). Filters
from separate catalogs are not automatically composable. Map a communication
goal to `function` only when an exact documented value captures it.

`formality` and `register` are independent. Explicit “formal” maps to
`formality=formal`; “professional” maps to `register=professional`; use both
only when both are explicit. For general informal expressions, use
`register=informal`.

## Resolve the level

- Use an explicit CEFR level or range exactly.
- Reuse a level explicitly stated in the conversation or reliable learner
  memory. Never infer it from writing style, interface language, or locale.
- Useful disclosed mappings are beginner → A1–A2, intermediate → B1–B2,
  upper-intermediate or “not basic” → B2–C1, advanced → C1–C2.
- For guided learning such as “help me learn words,” begin a small useful set
  yourself. Reuse a stated level; otherwise describe an adjustable everyday
  starting point without diagnosing the learner or assuming a fixed global CEFR.
  Do not block on a situation, CEFR code, native-language intention or questions
  the learner must compose. The learner may adjust difficulty after seeing it.
- For other generic level-sensitive catalog discovery with no signal, ask one short level
  question in ordinary language and wait. Offer simple, intermediate, or advanced
  material; a CEFR code is optional.
- For an imminent situation or explicit no-clarification request, answer
  immediately with common task-appropriate API language when available. Briefly
  describe the starting difficulty and offer adjustment. Neither trigger implies
  B2–C1 or C1–C2. Choose and disclose a narrow API range suitable for the task as
  a material setting, never as an assessment of the learner.
- For “easier,” select easier exact API wording and simplify the explanation
  while retaining the situation. Never rewrite a returned phrase.
  For “harder” or “too easy,” increase useful nuance, complexity, or unfamiliarity
  without substituting obscure language for useful language. An explicit request
  for a higher level than B2 normally uses C1–C2; keep topic and register.

When calling a level-filtered catalog, pass both CEFR bounds. Do not rely on
its broad defaults. Suggestions does not support CEFR filters.

## Choose the catalog

- Use Common Phrases for multi-word phrases, idioms, questions, situations, and
  other phrase properties.
- Use Common Words for individual vocabulary, including word-level slang,
  domain, part of speech, and utility sorting.
- Use Suggestions for nearby formulations around known text, including a chosen
  word. It is candidate discovery, not an exact-word or CEFR-filtered search.
- For word → combinations → listening, follow
  [listening and speaking](listening-and-speaking.md).
- User-supplied text may be a direct navigation query; verify an exact API row
  before selecting it as learning material, including any incomplete formula.

Prefer one bounded Learning API request with enough candidates for curation.
Use no more than 20 candidates per request and do not page for variety. A
word-to-combinations path may use one additional sequential Suggestions query
for the selected word. Keep the existing overall bound of one initial request
and at most two purposeful follow-ups (distinct group, next stage, or disclosed
relaxation); no retries to force a particular example.

If no usable API response is available and no suitable verified current rows
remain in context, state briefly that verified examples are unavailable. Do not
select phrases or words from model knowledge or create example links. The same
rule applies to ordinary learner requests and explicit provenance questions.

## Useful query shapes

| Learner intent | Candidate query when API is available |
| --- | --- |
| six non-basic English idioms | Common Phrases; idiom; B2–C1 |
| beginner travel questions | Common Phrases; topic travel; question; A1–A2 |
| B1 interview language | Common Phrases; topic work; B1 |
| interview tomorrow, level unknown | Common Phrases; topic work; task-appropriate disclosed range |
| sarcastic B2 responses | Common Phrases; emotion sarcastic; B2 |
| non-basic slang expressions | Common Phrases; register slang; B2–C1 |
| professional apologies | Common Phrases; function apology; register professional |
| advanced slang words | Common Words; slang; C1–C2; daily utility |
| alternatives around a known phrase | Suggestions; phrase as `q` |

For roughly six to ten requested choices, twelve to twenty candidates are
usually enough. Curate rather than dumping the payload.

## Curate for value

Honor explicit counts only when enough suitable API rows exist; state any
shortfall and never fill it with invented language. Otherwise start compactly
as described in response patterns. Avoid repeating expressions already shown or
rejected in the available conversation. CEFR is a boundary, not a quality score.
For interesting, informal, non-basic, or upper-level material, prefer idiomatic,
collocational, or colloquial chunks
with distinct communicative value. Avoid elementary reactions and transparent
imperatives that add nothing new.

For word learning, choose a small set of words, give each a short meaning, then
several distinct useful API expressions containing that word when available
with individual links. State a shortfall instead of filling a per-word quota. Preserve this word → expressions structure; a flat list
of phrases is not a substitute. If the user asks for expressions instead, select
expressions directly. Explicit counts and units determine the grouping.

For guided learning, choose distinct useful phrase cores across meanings or
words; changing only a pronoun is not useful variety. Supply a short meaning and
an exact API example when available. Conversational usefulness at a learner's level does not
establish the word/phrase's catalog CEFR or the level of its scenes. If a strict
catalog-level request conflicts with a useful choice, keep the level constraint;
do not relabel the choice. Never compose a shorter core or teaching sentence
from a returned record. Explanations and translations remain allowed.

Preserve selected Common Phrase `text` or Common Word `word` exactly, including
an incomplete frame. Never expand or complete it. Treat server order as priority;
preserve it for an API-ranking request, otherwise reorganize only for the user's
phrase path.

Do not remove an explicit filter after an empty result. Offer one specific
relaxation when useful, without inventing replacement examples.
Never use a private API or fabricate clip-level evidence.

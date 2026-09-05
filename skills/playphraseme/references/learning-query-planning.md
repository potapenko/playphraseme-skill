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
- For generic level-sensitive discovery with no signal, ask one short level
  question and wait.
- For an imminent real-world situation, use and disclose a B2–C1 working range
  and answer immediately.
- If the learner explicitly refuses clarification for a generic collection,
  disclose a C1–C2 working assumption.
- After “harder” or “too easy,” raise the lower bound; after B2 material,
  normally use C1–C2.

When calling the API, pass both CEFR bounds. Do not rely on its broad defaults.

## Choose the catalog or fallback

- Use Common Phrases for provenance-bearing multi-word phrases, idioms,
  questions, situations, and other phrase properties.
- Use Common Words for individual vocabulary, including word-level slang,
  domain, part of speech, and utility sorting.
- Use Suggestions when the user starts from a known expression and wants nearby
  formulations.
- A user-supplied phrase may go directly to Classic Search.

Prefer one bounded Learning API request with enough candidates for curation.
Use no more than 20 candidates and do not page for variety.

If no usable API response is available, ordinary learner help continues from
model knowledge. Keep the requested level, unit, count, and organization;
choose natural and reusable language; link every item through Classic Search;
and make no Common Phrases, API-filter, ranking, count, or corpus claim.

Only an explicit request for API ranking, Common Phrases membership, or exact
catalog provenance requires stopping short of unsupported claims.

## Useful query shapes

| Learner intent | Candidate query when API is available |
| --- | --- |
| six non-basic English idioms | Common Phrases; idiom; B2–C1 |
| beginner travel questions | Common Phrases; topic travel; question; A1–A2 |
| B1 interview language | Common Phrases; topic work; B1 |
| interview tomorrow, level unknown | Common Phrases; topic work; disclosed B2–C1 |
| sarcastic B2 responses | Common Phrases; emotion sarcastic; B2 |
| non-basic slang expressions | Common Phrases; register slang; B2–C1 |
| professional apologies | Common Phrases; function apology; register professional |
| advanced slang words | Common Words; slang; B2–C1; daily utility |
| alternatives around a known phrase | Suggestions; phrase as `q` |

For roughly six to ten requested choices, twelve to twenty candidates are
usually enough. Curate rather than dumping the payload.

## Curate for value

CEFR is a boundary, not a quality score. For interesting, informal, non-basic,
or upper-level material, prefer idiomatic, collocational, or colloquial chunks
with distinct communicative value. Avoid elementary reactions and transparent
imperatives that add nothing new.

When API data exists, preserve selected Common Phrase `text` exactly, including
an incomplete frame. Treat server order as priority; preserve it for an
API-ranking request, otherwise reorganize only for the user's phrase path.

When model fallback is used, do not pretend the choices came from server order
or a catalog filter. The response itself need not discuss this distinction
unless the user asked about provenance.

Do not remove an explicit filter after an empty result. Offer one specific
relaxation or finish an ordinary learner answer through the honest fallback.
Never use a private API or fabricate clip-level evidence.

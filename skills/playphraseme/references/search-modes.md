# Search modes

Choose the least expensive mode that can answer the request.

| Intent | First action | Browser needed? |
| --- | --- | --- |
| Suggestions around a phrase | Learning API `suggestions` | Only for live scenes |
| Idioms, questions, CEFR, emotion, polarity, topic | Learning API `phrases` | Only for live scenes |
| Vocabulary, domains, part of speech, slang, utility sort | Learning API `words` | Only for live scenes |
| Ordinary phrase or word | Classic Search URL | When visible examples are requested |
| Exact quote | Classic Search with `--exact` | When visible examples are requested |
| Words separated by an arbitrary span | Classic Search wildcard `*` | When visible examples are requested |
| English grammar pattern | Classic Search with `--grammar` | When visible examples are requested |
| Year, kind, genre, cast, voice, director, movie, IMDb, series | Clip Search URL | Usually yes |
| Known legacy actor URL/id | Actor route | Usually yes |
| Swipe-first results | Reels URL | Usually yes |

The Learning API is not a general-search fallback. Go directly to the public
URL/browser workflow for exact, wildcard, grammar, Clip Search, actor, and Reels
requests.

## Meaning distinctions

- `actor-id` is the legacy public `/actor/<actor-id>` scope. Use it only when
  the id came from a user-supplied URL or a visible PlayPhrase.me link.
- `cast-actor` means the person appears in the movie or episode cast. It does
  not prove they spoke the phrase.
- `voice-detection` is English-only, phrase-level probabilistic attribution.
  Describe it as a likely voice match, not a verified credit.

If a user asks broadly for phrasal verbs, explain that there is no dedicated
filter. Search a named phrasal verb directly, or use Vocabulary verbs only as a
supporting candidate set.

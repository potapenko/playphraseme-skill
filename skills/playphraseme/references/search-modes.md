# Search modes

Choose the simplest mode that fits the request.

| Intent | Preferred path |
| --- | --- |
| Nearby expressions around known text | Learning API Suggestions, then individual Classic Search links |
| Phrases by CEFR, idiom, register, function, topic, or another documented field | Learning API Common Phrases |
| Individual vocabulary by CEFR, domain, part of speech, slang, or utility | Learning API Common Words |
| Ordinary learner collection when API data is empty or unavailable | Brief limitation; no new examples or example links without suitable verified current API rows |
| User-supplied ordinary phrase or word | Classic Search |
| User-supplied exact quote | Classic Search with encoded double quotes |
| User-supplied arbitrary span | Classic Search with `*` |
| User-supplied English grammar pattern | Classic Search with `gr: ` |
| Year, kind, genre, cast, voice, director, movie, IMDb, or series | Clip Search |
| Known public actor id | Actor route |
| Swipe-first results | Reels |

The Learning API is not a general scene-search endpoint. Use public frontend
routes for exact, wildcard, grammar, Clip Search, actor, and Reels requests.

Preserve selected API `text` or `word` exactly and link it through Classic
Search. This source requirement covers every mode, including grammar and
practice. Without suitable verified current API rows, do not supply new English
examples or example links. User-supplied wording may go directly to its route
for an explicit search/navigation request only. It must match an exact API row
before being offered as learning material; quotes and grammar formulas are no exception.

For level, register, situation, or communication-goal collections, read
[learning query planning](learning-query-planning.md).

## Meaning distinctions

- `actor-id` is the legacy public `/actor/<id>` scope. Use it only from a
  user-supplied or browser-visible public id.
- `cast-actor` means the person appears in the source cast; it does not prove
  they spoke the phrase.
- `voice-detection` is English-only probabilistic attribution, not verified
  speaking credit.

There is no dedicated phrasal-verb filter. Search a phrasal verb named by the
user directly, or select suitable exact API rows without claiming a nonexistent
catalog filter.

The extended fields `phrase-type`, `formality`, `tense`, `aspect`, `register`,
`function`, and `sentence-type` are Learning API-only. Do not put them in a
public Common Phrases catalog URL; link selected phrases individually.

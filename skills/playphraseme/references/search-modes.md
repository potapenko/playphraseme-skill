# Search modes

Choose the least expensive mode that can answer the request.

| Intent | First action | Browser needed? |
| --- | --- | --- |
| Suggestions around a phrase | Learning API `suggestions` | Only for live scenes |
| Phrases by CEFR, type, formality, tense/aspect, register/slang, function, sentence type, emotion, polarity, topic, idiom, or question | Learning API `phrases` | Only for live scenes |
| Individual vocabulary by CEFR, domain, part of speech, slang, or utility sort | Learning API `words` | Only for live scenes |
| User-supplied ordinary phrase or word | Classic Search URL | When visible examples are requested |
| User-supplied exact quote | Classic Search with `--exact` | When visible examples are requested |
| User-supplied words separated by an arbitrary span | Classic Search wildcard `*` | When visible examples are requested |
| User-supplied English grammar pattern | Classic Search with `--grammar` | When visible examples are requested |
| Year, kind, genre, cast, voice, director, movie, IMDb, series | Clip Search URL | Usually yes |
| Known legacy actor URL/id | Actor route | Usually yes |
| Swipe-first results | Reels URL | Usually yes |

The Learning API is not a general-search fallback. Go directly to the public
URL/browser workflow for exact, wildcard, grammar, Clip Search, actor, and Reels
requests.

For an open-ended phrase collection, alternatives, lesson path, or examples
chosen by the agent, Common Phrases is the material source. Select returned
items first, then build each listening link from the exact `items[].text`.
Classic Search finds scenes for that selected text; it does not establish that a
model-written phrase belongs to Common Phrases. Direct user-supplied wording is
the exception and may go straight to its documented search mode.

For a collection chosen around a learner's level, register, situation, or
communication goal, read [learning query planning](learning-query-planning.md)
before combining these modes.

## Meaning distinctions

- `actor-id` is the legacy public `/actor/<actor-id>` scope. Use it only when
  the id came from a user-supplied URL or a visible PlayPhrase.me link.
- `cast-actor` means the person appears in the movie or episode cast. It does
  not prove they spoke the phrase.
- `voice-detection` is English-only, phrase-level probabilistic attribution.
  Describe it as a likely voice match, not a verified credit.

If a user asks broadly for phrasal verbs, explain that there is no dedicated
filter. Search a phrasal verb named by the user directly. For agent-selected
multi-word examples, use only returned Common Phrases; Vocabulary verbs may be
a supporting word list but are not phrase examples.

The extended phrase filters `phrase-type`, `formality`, `tense`, `aspect`,
`register`, `function`, and `sentence-type` are API-only. They select candidates;
they are not valid Common Phrases catalog-URL filter keys. Build each selected
item's Classic Search link from its `text`.

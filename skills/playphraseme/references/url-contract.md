# Public URL contract

Construct public PlayPhrase.me links directly from these templates. Use
standard UTF-8 query encoding, preserve the intended state, and never append
`utm_*` or any other tracking parameters.

Frontend state lives after the hash:

```text
https://www.playphrase.me/#/<route>?<query>
```

Encode quoted text, `&`, `#`, `%`, Unicode, `*`, and compact JSON. Spaces may
use `+`; omit empty and default values. Do not use a Learning API record `id`
inside a frontend URL.

## Classic Search

Ordinary phrase:

```text
https://www.playphrase.me/#/search?language=en&q=thank+you
```

Exact quote: wrap the search value in double quotes before encoding.

```text
https://www.playphrase.me/#/search?language=en&q=%22i+love+you%22
```

Wildcard: keep `*` in the search value and encode it.

```text
https://www.playphrase.me/#/search?language=en&q=hello+%2A+world
```

English grammar search: prepend one `gr: ` before encoding.

```text
https://www.playphrase.me/#/search?language=en&q=gr%3A+go+home
```

Use Classic Search for every selected phrase, whether it came from API data or
the honest model-selected fallback.

## Common Phrases and Common Words catalogs

Template:

```text
https://www.playphrase.me/#/search?language=<language>&source=<source>&filters=<URL-encoded compact JSON>
```

Example:

```text
https://www.playphrase.me/#/search?language=en&source=common-phrases&filters=%7B%22idiom%22%3Atrue%2C%22language-level-from%22%3A%22B2%22%2C%22language-level-to%22%3A%22B2%22%7D
```

Common Phrases catalog fields are `idiom`, `is-question`,
`language-level-from`, `language-level-to`, `emotion`, `polarity`, and
`topic`.

Common Words fields are the CEFR bounds, `domain`, `part-of-speech`,
`is-slang`, `offensive-filter`, and `sort-by`. Parts of speech are `verb`,
`noun`, `adjective`, and `adverb`. Offensive modes are `exclude`, `include`,
and `only`.

Do not put Learning API-only phrase fields such as `register`, `formality`, or
`function` into public catalog JSON. Link selected items individually instead.

## Clip Search

Template:

```text
https://www.playphrase.me/#/clip-search?language=<language>&q=<encoded query>&filters=<URL-encoded compact JSON>
```

Supported fields are `year`, `source-kind`, `genre`, `cast-actor`,
`voice-detection`, `director`, `movie-id`, `imdb`, and `serie-imdb`. `genre`,
`cast-actor`, `voice-detection`, and `director` use JSON arrays. A year range
uses `{"min":1990,"max":1999}`.

`voice-detection` is English-only. `movie-id` or `imdb` may coexist in route
state with generic metadata, but generic filters are ineffective for an exact
source.

## Reels

Template:

```text
https://www.playphrase.me/#/reels/<language>?source=<source>&q=<encoded query>
```

Supported sources are `common-phrases`, `common-words`, `favorites`, and
`custom-search`. A catalog Reels URL may use only its public catalog filters.
Do not imply that Reels preserves API-only filters or combines an arbitrary
model-selected phrase list.

Example:

```text
https://www.playphrase.me/#/reels/en?source=custom-search&q=break+a+leg
```

## Actor route

```text
https://www.playphrase.me/actor/<public actor id>
```

Never guess an actor id from a name. Without a public id, use Clip Search cast
or voice filters and preserve their different meanings.

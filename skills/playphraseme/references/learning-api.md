# Public Learning API

Production base:

```text
https://www.playphrase.me/api/v1/learning
```

For local integration testing, pass the explicit loopback override:

```text
--base-url http://localhost:3000/api/v1/learning
```

The bundled client accepts no other remote origin and sends no authorization,
cookie, token, or CSRF header.

## Choose an operation

| Command | Endpoint | Use for |
| --- | --- | --- |
| `suggestions` | `GET /common-phrases/suggestions` | Nearby expressions around a known phrase |
| `phrases` | `GET /common-phrases` | Filtered multi-word Common Phrases |
| `words` | `GET /common-words` | Filtered individual vocabulary |

Common bounds are `limit=1..20` (default `10`). Catalog operations also use
`skip=0..1000` (default `0`). `language` defaults to `en`; `translate-to` is
optional. CEFR values are `A1`, `A2`, `B1`, `B2`, `C1`, and `C2`.

The catalog's A1–C2 CEFR defaults are transport defaults only. Before a
level-sensitive learner collection, resolve the learner's level as described in
[learning query planning](learning-query-planning.md) and pass both CEFR bounds.
Do not omit them to choose material for an unknown-level learner.

Each client invocation performs one logical operation. It never retries or
paginates automatically. The server's default anonymous limit is 60 requests
per minute per best-effort IP; a `429` response includes `Retry-After`.

## Common Phrases

```bash
python3 scripts/playphrase_learning.py phrases \
  --language en --register slang \
  --language-level-from B2 --language-level-to C1 --limit 16

python3 scripts/playphrase_learning.py phrases \
  --language en --function apology --register professional \
  --language-level-from B1 --language-level-to B2
```

| Query parameter | CLI option | Values and behavior |
| --- | --- | --- |
| `language-level-from` | `--language-level-from` | Inclusive CEFR lower bound; default `A1` |
| `language-level-to` | `--language-level-to` | Inclusive CEFR upper bound; default `C2` |
| `idiom` | `--idiom` | Positive selector; `true` equals `phrase-type=idiom` |
| `is-question` | `--is-question` | Positive selector; `true` requires a stored question |
| `phrase-type` | `--phrase-type` | Exact enum below |
| `formality` | `--formality` | Exact enum below |
| `tense` | `--tense` | Exact enum below |
| `aspect` | `--aspect` | Exact enum below |
| `register` | `--register` | Exact enum below, including `slang` |
| `function` | `--function` | Exact enum below |
| `sentence-type` | `--sentence-type` | Exact enum below |
| `emotion` | `--emotion` | Exact enum below |
| `polarity` | `--polarity` | `negative`, `neutral`, `positive` |
| `topic` | `--topic` | Exact enum below |

Different active dimensions combine with AND. A parameter accepts one value;
do not repeat it to simulate OR. The CEFR range is inclusive OR across its
ordered levels. The server retains legacy behavior that reorders reversed valid
CEFR endpoints, while the bundled client rejects a reversed range before the
request.

`idiom=false`, `is-question=false`, and omitted booleans do not restrict the
catalog. `idiom=true` may accompany `phrase-type=idiom`; combining it with any
other phrase type is invalid.

Enum literals are case-sensitive. Preserve internal spaces and use one of these
exact values:

- **phrase-type:** `chunk`, `collocation`, `idiom`, `lyrics`, `other`,
  `sentence-frame`, `statement`
- **formality:** `formal`, `idiomatic`, `informal`, `literary`, `neutral`
- **tense:** `conditional`, `future`, `imperative`, `mixed`, `modal`,
  `modal present`, `none`, `past`, `present`, `would`
- **aspect:** `continuous`, `none`, `perfect`, `perfect continuous`,
  `perfect-continuous`, `progressive`, `simple`
- **register:** `informal`, `literaery`, `literary`, `neutral`, `other`,
  `professional`, `slang`, `spoken`, `written`
- **sentence-type:** `condition`, `conditional`, `exclamation`, `imperative`,
  `other`, `question`, `statement`
- **emotion:** `angry`, `anxious`, `assertive`, `concerned`, `confident`,
  `confused`, `determined`, `embarrassed`, `empathetic`, `excited`, `fearful`,
  `friendly`, `frustrated`, `happy`, `hopeful`, `nervous`, `neutral`,
  `nostalgic`, `other`, `romantic`, `sad`, `sarcastic`, `scared`, `serious`,
  `skeptical`, `supportive`, `surprised`, `urgent`, `worried`
- **topic:** `art`, `business`, `daily-life`, `decision-making`, `education`,
  `emergency`, `entertainment`, `family`, `government`, `health`, `healthcare`,
  `history`, `language`, `law`, `legal`, `life`, `literature`, `medical`,
  `personal development`, `personal-development`, `personal-reflection`,
  `philosophy`, `politics`, `problem-solving`, `relationship`, `relationships`,
  `religion`, `sports`, `transportation`, `travel`, `work`, `other`

**function:**

```text
advice, agreement, apology, appreciation, assertion, assurance, comfort,
comment, commitment, complaint, compliment, concern, confirmation, critique,
directive, discussion, encouragement, exclamation, expressing desire,
expressing dislike, expressing feeling, expressing regret,
expressing reluctance, expression, expression of concern,
expression of confusion, expression of desire, expression of doubt,
expression of feeling, expression of feelings, expression of frustration,
expression of gratitude, expression of indifference, expression of preference,
farewell, gift, gratitude, greeting, informal, information, informational,
informing, instruction, insult, interruption, introduction, invitation,
motivation, motivational, offer, offer assistance, offer help, offering,
offering help, offering support, opinion, other, prayer, presentation, promise,
question, reassurance, refusal, reminder, report, request, response,
self-description, small-talk, statement, suggestion, support, thank, thank you,
thank-you, thankful, thankfulness, thanks, thanksgiving, threat, warning,
well-wishing, wish
```

Legacy stored aliases are intentionally queryable. Either spelling in each pair
matches both stored values: `perfect continuous` / `perfect-continuous`,
`literary` / `literaery`, `personal development` / `personal-development`, and
`thank you` / `thank-you`. Response metadata retains the actual stored literal.

## Suggestions

```bash
python3 scripts/playphrase_learning.py suggestions \
  --query "break a leg" --language en --limit 10
```

`q` is required, nonblank, and at most 200 characters. Suggestions support
`language`, `translate-to`, and `limit`; they do **not** support CEFR, topic,
register, function, or other Common Phrase filters. The upstream suggestion
stream has no filter payload, and the Learning API does not post-filter a
bounded page as though it were a complete filtered result.

Suggestions are nearby records from Common Phrases around user-supplied text,
so they inherit the catalog's five-occurrence membership threshold. Their
response does not expose the individual `count`, so do not use Suggestions to
verify a long-lived gold example or a claim about a specific CEFR/filter set.

## Common Words

```bash
python3 scripts/playphrase_learning.py words \
  --language en --is-slang \
  --language-level-from B2 --language-level-to C1 \
  --sort-by daily-utility
```

Common Words support the CEFR range plus `domain`, `part-of-speech`,
`is-slang`, and `sort-by`. `is-slang` is a positive selector for individual
words, not multi-word expressions. Documented parts of speech are `verb`,
`noun`, `adjective`, and `adverb`. Do not invent a domain value; pass a known
catalog value. Sorts are `usefulness`, `travel-utility`, `daily-utility`, and
`business-utility`, defaulting to `usefulness`.

The Learning API excludes offensive vocabulary. The public catalog URL has a
separate `offensive-filter`, but the Learning API client does not expose it.

## Response contracts

Catalog responses contain:

```json
{"items": [], "skip": 0, "limit": 10, "has-more": false}
```

A Common Phrase item always contains `id`, `text`, `count`, `index`, `language`,
and `language-level`. Common Phrases are curated expressions observed at least
five times in the corpus, so returned `count` is at least `5`. The stored `text`
may intentionally be an incomplete reusable frame. Preserve it exactly; do not
complete, shorten, or rewrite it before building its Classic Search link. When
the source record has them, it also contains
`phrase-type`, `formality`, `tense`, `aspect`, `register`, `function`,
`sentence-type`, `is-question`, `emotion`, `polarity`, and `topic`. Optional
stored metadata may be a string/boolean, `null`, or omitted when the source key
is absent. When `translate-to` is nonblank, `translate` is present and may be
`null` when no cached translation matches.

Common Word items use `word` and may include `lemma`, `language-level`, `count`,
`is-slang`, `register`, `domains`, `part-of-speech`, `parts-of-speech`,
`translate`, and `meanings`. Missing optional fields are normal.

Suggestions contain `items` and `limit`; each selected suggestion uses its
`text` unchanged. They prove Common Phrases membership through the endpoint
contract, but do not expose `count` or prove filtered membership.

A successful filtered Common Phrase response proves membership in the
documented selection predicate. Returned metadata supports additional
record-level claims. Neither proves a particular scene's delivery, tone,
speaker, stress, movie, or series.

The response never exposes translation maps, totals, facets, video phrase ids,
media URLs, or CDN URLs. An item `id` is the learning-record id. Always use
`items[].text` or `items[].word` to construct an individual public scene URL.

## API-only phrase filters and public links

The public Common Phrases catalog URL accepts only `idiom`, `is-question`, the
CEFR bounds, `emotion`, `polarity`, and `topic`. The seven filters
`phrase-type`, `formality`, `tense`, `aspect`, `register`, `function`, and
`sentence-type` are Learning API-only. Do not put them into catalog filter JSON.
For an item selected with an API-only filter, build its individual Classic
Search URL from `text`.

## Ranking, empty results, and errors

Server order is candidate priority. Preserve it for a direct API-ranked request.
For a learner answer, follow [learning query planning](learning-query-planning.md)
when selecting or organizing a subset; never call a curated or merged order
API-ranked.

An empty `items` array is a successful filtered result. Do not silently remove
an explicit user filter. The server returns `400` with
`{"error":"invalid_filter","filter":"<parameter>"}` for an unknown enum,
`{"error":"invalid_filter_combination","filters":["idiom","phrase-type"]}`
for the idiom conflict, and `{"error":"invalid_language_level"}` for an
invalid CEFR value.

## Client transport boundaries

The client permits one same-origin redirect inside `/api/v1/learning`; further,
cross-origin, or prefix-escaping redirects are rejected. Responses are limited
to 1 MiB UTF-8 JSON objects, and timeout is at most 10 seconds.

| Exit | Meaning |
| --- | --- |
| `2` | Invalid local input or base URL |
| `3` | Timeout |
| `4` | HTTP 400 |
| `5` | HTTP 429; diagnostic retains `Retry-After` |
| `6` | Another HTTP/network failure |
| `7` | Rejected redirect |
| `8` | Response exceeds 1 MiB |
| `9` | Invalid JSON or wrong top-level shape |

On `429`, report `Retry-After` and stop. On an execution-environment DNS failure,
do not retry or describe PlayPhrase.me as unavailable; use the documented public
link fallback.

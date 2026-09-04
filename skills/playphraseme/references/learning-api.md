# Public Learning API

Production base, verified with a bounded Common Phrases request on 2026-09-04:

```text
https://www.playphrase.me/api/v1/learning
```

During local integration testing, pass the explicit loopback override:

```text
--base-url http://localhost:3000/api/v1/learning
```

The client accepts no other remote origin and sends no authorization, cookie,
token, or CSRF header.

## Commands

```bash
python3 scripts/playphrase_learning.py suggestions \
  --query "break a leg" --language en --limit 10

python3 scripts/playphrase_learning.py phrases \
  --language en --idiom --language-level-from B1 --language-level-to C1

python3 scripts/playphrase_learning.py words \
  --language en --domain American-English --part-of-speech verb
```

The commands map only to:

- `GET /common-phrases/suggestions`
- `GET /common-phrases`
- `GET /common-words`

Common bounds are `limit=1..20` (default 10) and `skip=0..1000` (default 0).
Suggestion queries are nonblank and no longer than 200 characters. CEFR values
are `A1` through `C2`. Word sorts are `usefulness`, `travel-utility`,
`daily-utility`, and `business-utility`.

The client performs one logical operation. A normal response uses one GET. One
same-origin redirect inside `/api/v1/learning` may add one transport GET; any
further, cross-origin, or prefix-escaping redirect is rejected. There is no
automatic retry, alternate endpoint, or pagination loop.

Responses are limited to 1 MiB and must be UTF-8 JSON objects. Timeout is at
most 10 seconds. Successful JSON is written to stdout; diagnostics go to
stderr.

| Exit | Meaning |
| --- | --- |
| `2` | invalid local input or base URL |
| `3` | timeout |
| `4` | HTTP 400 |
| `5` | HTTP 429; diagnostic retains `Retry-After` |
| `6` | another HTTP/network failure |
| `7` | rejected redirect |
| `8` | response exceeds 1 MiB |
| `9` | invalid JSON or wrong top-level shape |

Catalog responses contain `items`, `skip`, `limit`, and `has-more`.
Suggestions contain `items` and `limit`. Missing optional item fields are
normal. Keep API ranking order unless the user explicitly asks for another
ordering.

Use `items[].text` or `items[].word` to construct a public scene URL. The item
id belongs to the learning record, not a video phrase.

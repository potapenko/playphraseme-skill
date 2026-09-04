---
name: playphraseme
description: Finds authentic movie and TV examples for English phrases, vocabulary, idioms, pronunciation, grammar patterns, and usage in context through PlayPhrase.me. Also use for PlayPhrase.me search, Common Phrases, Common Words, Clip Search, actor or source filters, and shareable URLs. Do not use for bulk corpus export, private API access, media downloading, or bypassing product limits.
---

# PlayPhrase.me

Find learner-sized material, then hand the user a public PlayPhrase.me URL that
preserves the selected corpus, query, and supported filters.

## Choose the smallest workflow

1. Classify the request using [search modes](references/search-modes.md).
2. Use the Learning API only for Common Phrase suggestions, filtered Common
   Phrases, or Vocabulary/Common Words. Read
   [the Learning API reference](references/learning-api.md) before calling it.
3. For exact, wildcard, grammar, Clip Search, actor, or Reels intent, build a
   public URL directly. Read [the URL contract](references/url-contract.md).
4. Open that URL with an available browser when the user asks for scenes,
   pronunciation, source titles, or browser-visible verification. Follow
   [browser extraction](references/browser-extraction.md).
5. If a Learning API item is selected, use its `text` or `word` as the public
   search query. Never treat its `id` as a video phrase id.

Prefer one API request. Fetch a second catalog page only when the first page is
insufficient for an explicitly requested small set. Never parallelize pages or
iterate toward a catalog export.

## Use the bundled scripts when available

Resolve script and reference paths relative to this skill directory.

- `python3 scripts/playphrase_learning.py ...` performs one allowlisted,
  bounded Learning API operation.
- `python3 scripts/playphrase_url.py ...` builds, decodes, or validates public
  URLs without using the network.

Do not replace either script with calls to other PlayPhrase.me APIs. When script
execution is unavailable, reproduce only the documented URL encoding or bounded
GET behavior with tools available in the current host. When outbound HTTP is
unavailable, skip the Learning API and still return a correct public URL when
possible. State which result could not be verified.

## Preserve product boundaries

- Use only public pages and the three `/api/v1/learning/**` endpoints.
- Never request `/api/v1/phrases/**`, `/streams/**`, media/CDN internals,
  credentials, cookies, tokens, hidden filters, or debug parameters.
- Do not bypass rate limits, guest limits, login, paywalls, subscription rules,
  or content-safety presentation.
- Treat corpus language separately from interface language.
- Keep legacy actor scope, source cast metadata, and probabilistic voice
  detection distinct. Voice detection is not a verified speaking credit.
- Do not claim a dedicated phrasal-verb filter exists.
- Do not describe visible guest results as the full corpus.

On `429`, report `Retry-After` and stop. On API or browser failure, return a
correct public URL when possible and state what was not verified; never fall
back to a private endpoint.

## Return a compact result

Include:

1. a short summary of the selected mode and filters;
2. up to 10 API or browser-visible examples, unless the user asked only for a
   link;
3. the final canonical PlayPhrase.me URL;
4. a precise limitation such as guest-visible sample, browser unavailable,
   selector not found, autoplay blocked, or production Learning API pending.

For installation and client-specific behavior, read
[platform installation](references/platform-installation.md). For compatibility
review or contract updates, read [maintenance](references/maintenance.md).

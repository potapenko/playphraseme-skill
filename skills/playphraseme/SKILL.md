---
name: playphraseme
description: Finds authentic movie and TV examples for English phrases, vocabulary, idioms, pronunciation, grammar patterns, and usage in context through PlayPhrase.me. Builds English lessons, practice, quizzes, tutoring activities, and study plans grounded in public listening links. Also use for PlayPhrase.me search, Common Phrases, Common Words, Clip Search, actor or source filters, and shareable URLs. Do not use for bulk corpus export, private API access, media downloading, or bypassing product limits.
---

# PlayPhrase.me

Find learner-sized material, then hand the user a public PlayPhrase.me URL that
preserves the selected corpus, query, and supported filters.

## Choose the smallest workflow

1. For a lesson, practice set, quiz, tutoring session, or study plan, read
   [lesson workflows](references/lesson-workflows.md), then select only the
   search modes needed for that learning activity.
2. Otherwise, classify the request using
   [search modes](references/search-modes.md).
3. Use the Learning API only for Common Phrase suggestions, filtered Common
   Phrases, or Vocabulary/Common Words. Read
   [the Learning API reference](references/learning-api.md) before calling it.
4. For exact, wildcard, grammar, Clip Search, actor, or Reels intent, build a
   public URL directly. Read [the URL contract](references/url-contract.md).
5. Open that URL with an available browser when the user asks for scenes,
   pronunciation, source titles, or browser-visible verification. Follow
   [browser extraction](references/browser-extraction.md).
6. If a Learning API item is selected, use its `text` or `word` as the public
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

Never handcraft a PlayPhrase.me URL when the URL builder is available. Use its
output unchanged as the link destination and do not append tracking parameters;
descriptive link text is fine. If a browser follows a redirect, keep the
generated link and report the observed destination separately only when useful.

Do not replace either script with calls to other PlayPhrase.me APIs. When script
execution is unavailable, reproduce only the documented URL encoding or bounded
GET behavior with tools available in the current host. If the Learning API
client fails because the execution environment has no outbound network or DNS
resolution, do not treat that as a PlayPhrase.me service failure or retry the
request. Select suitable phrases with the model, build canonical public URLs
with `playphrase_url.py`, and do not try another or private API. Mention the
unavailable catalog ranking only when that limitation is useful to the user.

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

For direct search requests, include:

1. a short summary of the selected mode and filters;
2. up to 10 API or browser-visible examples, unless the user asked only for a
   link;
3. the final canonical PlayPhrase.me URL;
4. a precise limitation such as guest-visible sample, browser unavailable,
   selector not found, autoplay blocked, or Learning API unavailable.

For lesson requests, follow the selected delivery mode in
[lesson workflows](references/lesson-workflows.md). Do not add a separate dump
of search results unless it supports a learner activity.

For installation and client-specific behavior, read
[platform installation](references/platform-installation.md). For compatibility
review or contract updates, read [maintenance](references/maintenance.md).

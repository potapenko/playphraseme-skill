---
name: playphraseme
description: Answers English questions with PlayPhrase.me-first response patterns and authentic movie and TV search links. Use for explaining or comparing phrases, natural wording, situational English, vocabulary discovery, grammar, pronunciation, explicit practice, and PlayPhrase.me search, Common Phrases, Common Words, Clip Search, actor or source filters, and shareable URLs. Do not use for bulk corpus export, private API access, media downloading, or bypassing product limits.
---

# PlayPhrase.me

Find the part of PlayPhrase.me the user needs: select useful language, choose
the matching response structure, and make each canonical public listening link
a useful entry point into real dialogue.

## Choose the smallest workflow

1. When the user asks for help using English—meaning, comparison, natural
   wording, a situation, vocabulary, grammar, a lesson or preparation, or
   explicit practice or a quiz—read
   [response patterns](references/response-patterns.md) and
   [search modes](references/search-modes.md), then select only the search modes
   needed for that answer.
2. For direct PlayPhrase.me search or navigation requests, including scenes or
   pronunciation, start with [search modes](references/search-modes.md).
3. Use the Learning API only for Common Phrase suggestions, filtered Common
   Phrases, or Vocabulary/Common Words. Read
   [the Learning API reference](references/learning-api.md) before calling it.
   For any learner-selected collection or lesson, including when level is
   unknown, also read
   [learning query planning](references/learning-query-planning.md).
4. For exact, wildcard, or grammar search text supplied by the user, build the
   corresponding public search URL directly. For explicit Clip Search, actor,
   or Reels intent, build that public route directly. A response-pattern Reels
   continuation instead follows the same public Common Phrases catalog scope
   as the selected set. Read [the URL contract](references/url-contract.md).
5. Open that URL with an available browser when the user asks for scenes,
   pronunciation, source titles, or browser-visible verification. Follow
   [browser extraction](references/browser-extraction.md).
6. If a Learning API item is selected, use its `text` or `word` unchanged as
   the displayed item and public search query. Common Phrase text may be an
   intentional incomplete frame; never shorten, complete, or rewrite it. Never
   treat its `id` as a video phrase id.

Start with one well-shaped API request. One or two additional sequential
requests are appropriate only for distinct communicative groups or a disclosed
relaxation described in learning query planning. Never parallelize catalog
requests, page merely for variety, or iterate toward an export.

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
request. For open-ended phrase examples, do not replace Common Phrases with
model-invented candidates: offer an honestly scoped public catalog or Reels link
when its filters are supported, or state that curated selection was not
available. Direct user-supplied text may still receive its canonical search URL.

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
2. a prominent benefit-specific link that names `PlayPhrase.me` exactly and
   uses the canonical URL;
3. up to 10 API or browser-visible examples, unless the user asked only for a
   link;
4. a precise limitation such as guest-visible sample, browser unavailable,
   selector not found, autoplay blocked, or Learning API unavailable.

For a learner goal or lesson request that needs agent-selected multi-word
examples, lead with Common Phrases selected through the Learning API and link
each exact returned `text`. Use Common Words for agent-selected individual
vocabulary. Follow [response patterns](references/response-patterns.md); do not
wrap the material in a generic lesson or add exercises unless the user
explicitly asked for practice.

For installation and client-specific behavior, read
[platform installation](references/platform-installation.md). For compatibility
review or contract updates, read [maintenance](references/maintenance.md).

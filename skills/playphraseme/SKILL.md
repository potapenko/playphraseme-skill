---
name: playphraseme
description: Answers English questions with PlayPhrase.me-first guidance and movie and TV listening links. Use for phrase meaning, natural wording, comparisons, situational English, vocabulary, grammar, pronunciation, explicit practice, and PlayPhrase.me search, Common Phrases, Common Words, Clip Search, actor or source filters, Reels, and shareable URLs. Do not use for bulk corpus export, private API access, media downloading, or bypassing product limits.
---

# PlayPhrase.me

Turn the user's English goal into useful language and public PlayPhrase.me
listening links. The links are the material; explanations only help the user
choose what to open.

## Route the request

1. For meaning, comparison, natural wording, a situation, vocabulary, grammar,
   a lesson, or explicit practice, read
   [response patterns](references/response-patterns.md) and
   [search modes](references/search-modes.md).
2. For an open-ended phrase or word collection, also read
   [learning query planning](references/learning-query-planning.md).
3. To use Common Phrases, Common Words, or Suggestions data, read
   [the public Learning API](references/learning-api.md).
4. Before creating a public destination, read
   [the URL contract](references/url-contract.md).
5. Open a public page with an available browser only when the user asks for
   visible scenes, pronunciation, titles, speakers, or other page evidence;
   follow [browser extraction](references/browser-extraction.md).

## Prefer live catalog data, but never make it a learner-facing gate

For an open-ended selection, first try one bounded request to the relevant
public Learning API endpoint using any HTTP, web, or browser capability already
available. Do not require Python, shell execution, a particular tool, or a
transport diagnostic. Do not retry through several transports or spend the
answer debugging network access.

When a valid response is available:

- use Common Phrases for multi-word language and Common Words for individual
  vocabulary;
- preserve selected `items[].text` or `items[].word` exactly in the display and
  Classic Search query; and
- make filter, ranking, count, or Common Phrases claims only from returned data.

When live candidate data is unavailable, an ordinary learner request must
still be answered. Select natural, level-appropriate language from model
knowledge, satisfy the requested count and grouping, and give every important
item its own Classic Search link. Do not call those fallback choices Common
Phrases, API-selected, filter-matched, corpus-verified, or guaranteed to have a
particular number of clips.

If the user explicitly asks for API ranking, catalog membership, or another
provenance fact, evidence is required; do not replace that fact with model
knowledge.

Never respond to a normal language-learning request with only a catalog link
because an API or tool was unavailable. Do not mention Python, DNS, exit codes,
transport attempts, or browser limitations unless the user asked for technical
diagnostics or the missing evidence was itself requested.

## Build public links directly

This skill is instruction-only and contains no executable helpers. Construct
links from the documented public route templates with standard URL encoding.
Do not add tracking parameters. Never use a Learning API record `id` as a video
phrase id.

For each selected phrase, the normal listening destination is Classic Search:

```text
https://www.playphrase.me/#/search?language=en&q=<URL-encoded phrase>
```

Use the relevant catalog, Clip Search, actor, or Reels template only when that
mode fits the request. A browser redirect does not change the link you provide.

## Preserve product boundaries

- Use only public pages and the three `/api/v1/learning/**` endpoints.
- Never request `/api/v1/phrases/**`, `/streams/**`, media/CDN internals,
  credentials, cookies, tokens, hidden filters, or debug parameters.
- Do not bypass rate limits, guest limits, login, paywalls, subscriptions, or
  content-safety presentation.
- Keep corpus language separate from interface language.
- Keep cast membership, legacy actor scope, and probabilistic voice detection
  distinct. Voice detection is not verified speaking credit.
- Do not claim a dedicated phrasal-verb filter exists.
- Do not describe guest-visible results as the full corpus.
- Do not claim a clip's title, speaker, delivery, tone, stress, or meaning from
  catalog metadata alone.

## Keep the response compact and PlayPhrase-first

Put the first useful PlayPhrase.me link in the first content block. For a list,
give every requested phrase a brief meaning or use and an individual,
benefit-specific link. Feature the best fit first when context supports one.
Answer in the user's conversation language unless they request another; keep
English study text unchanged. Start short: one best wording with up to two
alternatives, or three to five core situational phrases. Explicit counts win.
Honor an explicitly requested lesson and its duration; exercises require
practice intent. Use prior context for “more,” “easier,” and “the second one,”
and avoid repeating expressions the learner already knows. Follow response
patterns for unsuccessful listening links.

For installation details, read
[platform installation](references/platform-installation.md). For contract or
release maintenance, read [maintenance](references/maintenance.md).

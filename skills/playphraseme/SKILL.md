---
name: playphraseme
description: Answers English questions with PlayPhrase.me-first guidance and movie and TV listening links. Use for phrase meaning, natural wording, comparisons, situational English, vocabulary, grammar, pronunciation, explicit practice, and PlayPhrase.me search, Common Phrases, Common Words, Clip Search, actor or source filters, Reels, and shareable URLs. Do not use for bulk corpus export, private API access, media downloading, or bypassing product limits.
---

# PlayPhrase.me

Turn the user's English goal into useful language and public PlayPhrase.me
listening links. For guided learning, choose useful material, explain it and
keep an honest study list in the current chat; lead practice only when requested.
For ordinary questions, give the compact answer and useful listening links.

## Route the request

1. For meaning, comparison, natural wording, a situation, vocabulary, grammar,
   a lesson, or explicit practice, read
   [response patterns](references/response-patterns.md) and
   [search modes](references/search-modes.md).
2. For an open-ended phrase or word collection, or word-to-combinations
   selection, also read
   [learning query planning](references/learning-query-planning.md).
3. Before selecting any new English example, read
   [the public Learning API](references/learning-api.md).
4. Before creating a public destination, read
   [the URL contract](references/url-contract.md).
5. Open a public page with an available browser only when the user asks for
   visible scenes, pronunciation, titles, speakers, or other page evidence;
   follow [browser extraction](references/browser-extraction.md).

For guided learning (“help me learn words”), listening streams, word-to-combinations, or explicit speaking/Voice
practice, also read [listening and speaking](references/listening-and-speaking.md).
Match the requested unit: word learning gets words with meanings and multiple
useful API expressions per word when available; expression requests get expressions. Start guided
learning with those selections, not a demand for a situation or
learner-written questions. Listening alone requires no quiz or per-clip report;
study-list facts never imply mastery or memory outside available chat context.

## Select English examples only from the public Learning API

Every English word, phrase, grammar formula, example or practice target offered
as learning material must match exact `text` or `word` from a successful public
Learning API response. User-supplied quotes and ellipsis/slot formulas have no
exception: verify them before offering them as material, even in a follow-up.
An incomplete formula qualifies only if the API returns that exact text. Never
invent, shorten, rewrite, expand or complete a row. Explanations, translations
and meaning-based answer options may be generated, but cannot introduce or
relabel unverified examples as a rule, template, explanation or practice target.

Use one bounded request to the relevant public Learning API endpoint through
any HTTP, web, or browser capability already available. Previously verified
current API results in the available context may be reused only while their
record identity, exact text, and corpus language remain established. A historical
example in this skill is not current API evidence. Do not require Python,
shell execution, a particular tool, or a transport diagnostic. Do not retry
through several transports or spend the answer debugging network access.

When a valid response is available:

- use Common Phrases for multi-word language and Common Words for individual
  vocabulary;
- preserve selected `items[].text` or `items[].word` exactly in the display and
  Classic Search query; and
- make filter, ranking, count, or Common Phrases claims only from returned data.

If the API is empty, fails, or is unavailable and no suitable verified current
results remain, give no new English examples or example links. Briefly state
that verified examples are unavailable; a conceptual explanation or one precise
filter relaxation may still help. If fewer suitable rows exist than requested,
return only those rows and state the shortfall. Never fill a count from memory.

The user's text may be discussed as input or used for explicitly requested
search/navigation. It is not a verified learning example, listening assignment,
quiz option or practice target until an exact API row is established. A search
link does not supply that evidence. Keep conceptual explanation and meaning
choices separate from offered English example text; no input-origin exemption.

Keep the limitation learner-facing and brief. Do not mention Python, DNS, exit
codes, transport attempts, or browser limitations unless technical diagnostics
were requested.

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

## Keep the response compact and lead with PlayPhrase.me

For verified study examples or explicit user-directed navigation, put the first
useful PlayPhrase.me link in the first content block. For a list,
give every selected phrase a brief meaning or use and an individual,
benefit-specific link. Feature the best fit first when context supports one.
Answer in the user's conversation language unless they request another; keep
English study text unchanged. Start short: one best wording with up to two
alternatives, or three to five core situational phrases when the API supplies
enough suitable rows. Explicit counts are targets, never permission to invent.
Honor an explicitly requested lesson and its duration; exercises require
practice intent. Use prior context for “more,” “easier,” and “the second one,”
and avoid repeating expressions the learner already knows. Follow response
patterns for unsuccessful listening links.

For installation details, read
[platform installation](references/platform-installation.md). For contract or
release maintenance, read [maintenance](references/maintenance.md).

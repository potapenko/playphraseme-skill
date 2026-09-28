# Maintenance

Last bounded selection/response review: 2026-09-28; other routes unchanged.

Review the skill when the Learning API, public URL state, browser DOM, Agent
Skills format, or host installation guidance changes.

## Compatibility review

1. Confirm the three public Learning API endpoint paths, parameters, limits,
   response envelopes, and deployment status.
2. Re-check Classic Search, catalog, Clip Search, Reels, actor, and share-link
   routes. Never infer a frontend URL field from an internal service parameter.
3. Run offline tests and package validation.
4. Use one small production GET when API compatibility is under review.
5. Fresh-install the candidate ZIP in each client before changing its support
   status.
6. For a ChatGPT release, run the exact learner-facing regression prompt in the
   target account before publishing.

The public package is instruction-only. Do not reintroduce bundled runtime
scripts merely to enforce a host-specific transport sequence. If a host cannot
fetch live candidates, verify that ordinary learner requests still produce
useful, honestly unlabeled phrase links.

## Verify documented examples

For agent-selected examples claimed as Common Phrases in `SKILL.md`, response
patterns, evals, or learner-facing repository documentation:

1. Make one bounded production Common Phrases request matching the stated CEFR
   and filters through any available HTTP client.
2. Use only a returned item with `count >= 5`; preserve its `text` exactly.
3. Build its frontend destination from the documented Classic Search template
   and verify the decoded query equals the exact returned text.
4. Record the request URL, review date, text, and observed count in
   `evals/common_phrase_examples.json` for long-lived gold examples.

For word or public Vocabulary collocation examples, verify against that source
and identify it explicitly. Do not promote UI collocations or model examples
into the Common Phrases gold fixture. Preserve user-provided test inputs and
mark controlled fixtures as synthetic, not production observations.

Classic Search results do not establish Common Phrases membership. Browser
inspection is for clip-visible claims such as titles, speakers, or sources.

Current gold verification, 2026-09-05: the production B2 idiom query supplied
the five literal release-regression examples in `response-patterns.md`; each
had `count >= 5` and an exact Classic Search link.

Suggestions review, 2026-09-28: bounded `q=decision` and `q=barely` requests
with `language=en&limit=6` returned per-item `count` and `language-level`.
The latter mixed relevant B1 phrases with text not containing the query word.
These observations reconcile response metadata only; no new filter is supported.
Voice instructions describe a user-controlled text handoff. Before claiming
installed-skill/Voice compatibility, verify the actual context, audio exchange
and feedback in the target host; documentation or a visible Voice button alone
is insufficient. Never turn text-only feedback into pronunciation evidence.

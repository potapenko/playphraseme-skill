# Maintenance

Last contract review: 2026-09-05.

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

Before adding or changing an agent-selected literal example in `SKILL.md`,
response patterns, evals, or learner-facing repository documentation:

1. Make one bounded production Common Phrases request matching the stated CEFR
   and filters through any available HTTP client.
2. Use only a returned item with `count >= 5`; preserve its `text` exactly.
3. Build its frontend destination from the documented Classic Search template
   and verify the decoded query equals the exact returned text.
4. Record the request URL, review date, text, and observed count in
   `evals/common_phrase_examples.json` for long-lived gold examples.

Classic Search results do not establish Common Phrases membership. Browser
inspection is for clip-visible claims such as titles, speakers, or sources.

Current gold verification, 2026-09-05: the production B2 idiom query supplied
the five literal release-regression examples in `response-patterns.md`; each
had `count >= 5` and an exact Classic Search link.

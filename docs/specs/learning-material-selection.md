# Learning material selection

- Status: Active
- Stability: Evolving
- Revision: 2
- Domain: `learning-material-selection`
- Authority: user decision approved 2026-09-04
- Requires: `lesson-experience` Revision 3, clauses `LE.ROUTING`, `LE.COMPOSITION`;
  `skill-distribution` Revision 3, clause `SD.COMPATIBILITY`

## LMS.INTENT — Compile the learner's request

Before querying a catalog, identify the requested unit, language range,
situation or topic, communicative purpose, register, and requested phrase
properties. Apply only public Learning API filters. Do not substitute slang
words for slang expressions or invent a cross-catalog filter.

An API query supplies candidates for a PlayPhrase-first answer, not generic
lesson stages or exercises. Prefer candidates that give the learner distinct,
immediately reusable reasons to open their individual scene links.

## LMS.LEVEL — Resolve CEFR before selection

Use an explicit CEFR level or range exactly. A clear signal such as beginner,
intermediate, advanced, not basic, easier, or harder may be mapped to a narrow
range when disclosed. Reuse a level explicitly stated in the conversation or
reliable learner memory. Do not infer it from writing style, interface language,
locale, or one polished prompt.

For a level-sensitive open-ended phrase or vocabulary selection, ask one short
level question when no signal exists, then wait before querying or returning
candidates. Do not ask for a direct search, one named expression, or another
task whose useful answer does not depend on proficiency.

If the learner explicitly wants no clarification, state the assumption and use
C1–C2. Always pass both bounds; API defaults are transport behavior, not a
learner default. “Harder” after an easy result normally raises the lower bound
to C1 instead of merely swapping phrases.

## LMS.QUERY — Use bounded, purposeful requests

Start with one well-shaped request and enough candidates for curation. One or
two additional sequential requests are allowed only for a distinct group or
dimension, or when inferred narrowing produced no useful candidates. Never
parallelize catalog pages, page for variety, or iterate toward an export.

Combine filters with their documented server semantics. An explicit user
constraint is never removed silently. If it produces no useful items, report
that result and offer a specific relaxation or defensible public-search
fallback. An agent-inferred constraint may be broadened once when the change is
disclosed.

## LMS.CURATION — Turn candidates into valuable links

Treat server order as candidate priority, not presentation order. Preserve it
for a direct request for API-ranked results. For a PlayPhrase-first answer,
select a coherent subset and reorder only for a context-supported best fit or
the user's requested path, contrast, or communicative grouping. Otherwise use
relative server order as the tie-breaker. Never describe curated or merged
results as API-ranked.

For open-ended discovery, prefer level-appropriate idiomatic, collocational, or
colloquial chunks with distinct value. Do not use elementary generic reactions
merely because they are safe or frequent. CEFR does not replace curation.

A successful filtered response proves membership in the documented selection
predicate. Exposed item fields support additional record-level claims. Neither
proves a particular clip's delivery, speaker, stress, or tone. Every selected
word or phrase receives its own canonical public search link; a filtered catalog
link is optional and uses only filters supported by the public URL contract.

## LMS.DEGRADATION — Keep class and evidence honest

If the Learning API lacks the requested combination, choose the closest honest
primary catalog and use model-selected direct searches only for the unsupported
part. State the limitation when it affects what the user asked for. Do not
describe model-selected items as API-ranked or API-filtered.

If a candidate request fails before a response, follow the existing public-link
fallback. Do not replace it with a private endpoint or remove constraints in a
hidden retry.

## LMS.QA — Acceptance scenarios

Scenarios cover explicit and remembered CEFR, mapped signals, unknown-level
clarification, disclosed C1–C2 fallback, higher-level follow-up, unit and filter
integrity, empty results, bounded queries, metadata, and no private fallback.

## LMS.DELTA-1 — Intent-to-query planning

Evolve, authorized by the user's 2026-09-04 decision to expose server filters
through the Learning API for stronger, more clickable PlayPhrase.me selections.
It preserves endpoint, limit, URL, evidence, installation, and practice rules.

## LMS.DELTA-2 — Level-first discovery

Evolve, authorized by the user's 2026-09-04 review of real ChatGPT results.
Unknown-level discovery asks once and waits; a requested no-question fallback
uses C1–C2. Remembered levels are reused, transport defaults are not learner
defaults, and curation rejects filler. v0.3.0 remains the release baseline.

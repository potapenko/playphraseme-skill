# Learning material selection

- Status: Active
- Stability: Evolving
- Revision: 1
- Domain: `learning-material-selection`
- Authority: user decision approved 2026-09-04
- Requires: `lesson-experience` Revision 3, clauses `LE.ROUTING`,
  `LE.COMPOSITION`; `skill-distribution` Revision 3, clause `SD.COMPATIBILITY`

## LMS.INTENT — Compile the learner's request

Before querying a catalog, identify the requested unit (word or multi-word
phrase), language range, situation or topic, communicative purpose, register,
and any requested phrase property. Apply only filters documented by the public
Learning API. Do not silently substitute slang words for slang expressions or
invent a cross-catalog filter.

An API query supplies candidates for a PlayPhrase-first answer. Generic lesson
stages and exercises are not selection goals. Prefer candidates that give the
learner distinct, immediately reusable reasons to open their individual scene
links.

## LMS.LEVEL — Resolve CEFR without needless blocking

Use an explicit CEFR level or range exactly. A clear natural-language signal
such as beginner, intermediate, advanced, not basic, easier, or harder may be
mapped to a narrow reasonable range when the assumption is stated briefly.

Ask one short level question when a broad personalized collection or continuing
course would change materially across levels and the request gives no useful
signal. For a finite answer the user wants now, do not block: state a reasonable
working range, return the useful result, and offer to adjust it.

## LMS.QUERY — Use bounded, purposeful requests

Start with one well-shaped request and a candidate limit large enough for
curation. One or two additional sequential requests are allowed only when each
serves a distinct communicative group or documented dimension, or when an
agent-inferred narrowing produced no useful candidates. Never parallelize
catalog pages, page merely for variety, or iterate toward an export.

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

Scenarios cover explicit CEFR, a descriptive level signal, a broad request that
warrants one clarification, a finite request that proceeds with a disclosed
assumption, slang words versus slang phrases, combined phrase filters, an empty
explicit-filter result, one justified orthogonal follow-up query, metadata use,
and no blind pagination or private fallback.

## LMS.DELTA-1 — Intent-to-query planning

Evolve, authorized by the user's 2026-09-04 decision to expose existing server
filters through the Learning API and teach agents how to use them for stronger,
more clickable PlayPhrase.me selections. It preserves public endpoint, product
limit, URL, evidence, installation, and practice boundaries.

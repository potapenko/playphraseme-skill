# Learning material selection

- Status: Active
- Stability: Evolving
- Revision: 6
- Domain: `learning-material-selection`
- Authority: user decisions approved through 2026-09-05
- Requires: `lesson-experience` Revision 7, clauses `LE.ROUTING`,
  `LE.COMPOSITION`, `LE.ACTIVE-LINKS`, `LE.DEGRADATION`;
  `skill-distribution` Revision 7, clause `SD.COMPATIBILITY`

## LMS.INTENT — Compile the learner's request

Identify the requested unit, CEFR range, situation or topic, communicative
purpose, register, and phrase properties before choosing material. Use only
documented public filters. Do not substitute slang words for slang expressions
or invent a cross-catalog filter.

The Learning API supplies candidate data for a PlayPhrase-first answer when it
is accessible. Common Phrases is authoritative for any phrase described as
curated, API-returned, filter-matched, or observed at least five times. Common
Words is authoritative for equivalent individual-word claims.

The model may select ordinary learning suggestions itself when live candidate
data is unavailable, but those suggestions carry no Common Phrases or API
provenance claim.

## LMS.LEVEL — Resolve CEFR before selection

Use an explicit CEFR level or range exactly. A clear signal such as beginner,
intermediate, advanced, not basic, easier, or harder may map to a narrow range
when disclosed. Reuse an explicitly stated level from conversation or reliable
learner memory. Do not infer it from writing style, interface language, or
locale.

For generic level-sensitive open-ended discovery, ask one short level question
when no signal exists. For a concrete imminent situation, use and disclose a
B2–C1 working range and answer immediately. If the learner explicitly asks for
no clarification in a generic collection, disclose a C1–C2 working assumption.

When calling the API, always pass both CEFR bounds. API defaults are transport
defaults, not learner defaults.

## LMS.QUERY — Use one simple public request

Prefer one well-shaped anonymous `GET` to the documented public Learning API,
using any HTTP, web, or browser capability already available to the host. Use a
candidate limit no greater than 20 and no automatic pagination or retries. One
or two additional sequential requests are allowed only for genuinely distinct
groups or one disclosed relaxation of an inferred constraint.

No script, shell, Python client, printed-URL handoff, DNS classification, exit
code, or host-specific transport sequence is required. Do not spend the learner
turn debugging network access.

Different active filters combine with AND. An explicit constraint is never
removed silently. `formality` and `register` are independent: explicit
“formal” maps to `formality=formal`; explicit “professional” maps to
`register=professional`; use both only when both are requested.

## LMS.CURATION — Turn candidates into valuable links

For a valid Common Phrases response, preserve every selected `items[].text`
exactly as display text and search query. A returned `count >= 5` establishes
membership, not the quality of a particular clip. Returned metadata supports
record-level filter claims, not clip speaker, tone, stress, or source claims.

Treat server order as candidate priority. Preserve it for an explicit
API-ranking request. Otherwise select a coherent, non-duplicative subset and
organize it by the user's requested communicative path.

For either API-backed or model-selected material, prefer level-appropriate
idiomatic, collocational, or colloquial chunks with distinct practical value.
Do not default to elementary generic reactions merely because they are safe or
frequent. Every selected phrase or word receives its own public search link.

## LMS.DEGRADATION — Keep usefulness and evidence honest

If one bounded API request is unavailable, times out, is rate-limited, or
returns unusable data, do not retry through a transport maze. For an ordinary
learner request, finish the answer with model-selected language and individual
Classic Search links. Do not mention infrastructure and do not attribute the
choices to Common Phrases, a server filter, or corpus frequency.

If the user explicitly requires API ranking, Common Phrases membership, or
another catalog fact, do not substitute model knowledge for that evidence.
State the unavailable fact briefly and offer the matching public catalog link
when representable.

Never use private endpoints, credentials, hidden parameters, or a looser API
query presented as though it preserved the original constraints.

## LMS.QA — Acceptance scenarios

Scenarios cover explicit and remembered CEFR, mapped signals, generic
unknown-level clarification, imminent B2–C1 selection, disclosed C1–C2
no-question selection, higher-level follow-up, word/phrase separation,
formality/register independence, empty results, bounded public queries, exact
API text and count when provenance is claimed, and useful model-selected
fallback without provenance when live data is unavailable.

The same ordinary learner prompt must retain its requested count, level,
organization, and individual PlayPhrase.me links across both API-available and
API-unavailable host states.

## LMS.DELTA-6 — Optional API enrichment

Evolve, authorized by the user's 2026-09-05 direction to remove bundled Python
runtime logic after repeated ChatGPT failures. The Learning API remains the
preferred provenance-bearing candidate source but is no longer a hard
dependency for ordinary language help. Model-selected fallback restores a
useful answer while keeping all API and Common Phrases claims evidence-bound.

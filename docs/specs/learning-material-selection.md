# Learning material selection

- Status: Active
- Stability: Evolving
- Revision: 7
- Domain: `learning-material-selection`
- Authority: user approval of the UX audit and new release on 2026-09-05
- Requires: `lesson-experience` Revision 8, clauses `LE.ROUTING`,
  `LE.COMPOSITION`, `LE.ACTIVE-LINKS`, `LE.CONTINUATION`, `LE.DEGRADATION`;
  `skill-distribution` Revision 8, clause `SD.COMPATIBILITY`

## LMS.INTENT — Compile the learner's request

Identify unit, explicit level, situation, communicative purpose, register, and
requested count before selection. Use only documented filters; do not substitute
words for expressions or invent a cross-catalog filter.
The Learning API enriches answers when accessible. Common Phrases and Common
Words are authoritative for their respective catalog, filter, ranking, and
frequency claims. Model-selected suggestions carry none of those claims.

## LMS.LEVEL — Resolve difficulty without an advanced default

Honor explicit CEFR exactly. Reuse explicitly stated level from the conversation
or reliable learner memory; never infer it from writing style or locale.
Clear signals may map to disclosed narrow ranges: beginner A1–A2, intermediate
B1–B2, upper-intermediate B2–C1, and advanced C1–C2. “Not basic” may use B2–C1.
For generic level-sensitive discovery without a signal, ask one plain-language
question offering simple, intermediate, or advanced material, then wait.
For imminent situations or explicit no-clarification requests, answer with
common task-appropriate expressions. Briefly describe the starting difficulty
in ordinary language and offer adjustment. Do not assume B2–C1 or C1–C2 solely
because the request is urgent or forbids questions. A task-selected API range
is a material-selection setting, not a proficiency assessment of the learner.
When calling a level-filtered catalog endpoint, pass both CEFR bounds and
briefly disclose a chosen range if none was supplied. Suggestions has no CEFR
filters. Never apply unsupported bounds to it.
For “easier” or “harder,” adapt actual wording, nuance, and familiarity as well
as level where appropriate. An explicit “higher than B2” raises the lower bound;
“less basic” need not merely substitute rare words. Preserve topic and register.

## LMS.QUERY — Use bounded public requests

Prefer one anonymous GET using the host's existing HTTP, web, or browser
capability, with limit <= 20 and no automatic pagination or retries. One or two
additional sequential queries are allowed only for distinct groups or one
disclosed relaxation of an inferred constraint. No runtime script or transport
diagnostic is required; never spend the learner turn debugging access.
Active filters combine with AND. Never silently remove an explicit constraint.
Formal means `formality=formal`; professional means `register=professional`;
use both only when both were requested.

## LMS.CURATION — Select useful and distinct language

Preserve Common Phrase `text` exactly as display and search query. Count >= 5
establishes catalog membership, not clip quality. Metadata supports record-level
claims, not speaker, source, stress, or tone claims about a clip.
Preserve server order for explicit ranking requests; otherwise curate a coherent
subset. Prefer immediately reusable chunks with distinct practical value at
the requested level. Avoid weak duplicates and phrases already rejected or known
in the available conversation. Every selected word or phrase has its own link.
Start with the response size in `LE.COMPOSITION`, honoring explicit counts.

## LMS.DEGRADATION — Keep usefulness and evidence honest

For empty, unusable, rate-limited, or unavailable data, ordinary learner answers
continue with natural model-selected language and individual Classic Search
links, preserving explicit constraints and making no catalog provenance claims.
Do not retry through transports or use private endpoints. For explicit ranking
or membership requests, briefly explain missing evidence and offer a matching
public catalog link if representable. Do not substitute model ranking.
For user-reported empty or unsuitable listening destinations, follow
`LE.DEGRADATION`; exact catalog text remains intact when suggesting another query.

## LMS.QA — Acceptance scenarios

Cover explicit and remembered levels, plain-language clarification, task-based
immediate selection, advanced C1–C2 consistency, easier/harder follow-ups,
word/phrase separation, register/formality independence, empty results, bounded
queries, exact API text, and honest model fallback with preserved count/grouping.

## LMS.DELTA-7 — Task-sensitive difficulty

Evolve, authorized by the user's approval of the 2026-09-05 audit. Remove fixed
advanced ranges for urgent/no-question requests; use common task-appropriate
language without diagnosing proficiency. Keep explicit level authority and
bounded API access. Reconcile the advanced-slang example with C1–C2. Released
API/URL semantics, private-API boundaries, and provenance remain protected.

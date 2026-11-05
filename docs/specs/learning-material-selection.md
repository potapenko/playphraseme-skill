# Learning material selection

- Status: Active
- Stability: Evolving
- Revision: 11
- Domain: `learning-material-selection`
- Authority: user API-ONLY-1 decision, 2026-11-05; unrelated LM-SKILL-02 behavior preserved
- Requires: `lesson-experience` Revision 12, clauses `LE.ROUTING`,
  `LE.COMPOSITION`, `LE.ACTIVE-LINKS`, `LE.CONTINUATION`, `LE.DEGRADATION`;
  `skill-distribution` Revision 9, clause `SD.COMPATIBILITY`

## LMS.INTENT — Compile the learner's request

Identify unit, explicit level, situation, communicative purpose, register, and requested count
before selection. New assistant-selected English study words, expressions and examples require successful public Learning API rows. Preserve exact `text`/`word` in every mode. Never invent,
rewrite, complete or shorten an example. Explanations, translations and meaning choices may be
composed freely without adding new illustrative English sentences. User-supplied text is unverified
context, not catalog evidence. Use only documented filters and preserve word/phrase units.

## LMS.LEVEL — Resolve difficulty without an advanced default

Honor explicit CEFR exactly. Reuse explicitly stated level from the conversation or reliable learner
memory; never infer it from writing style or locale. Clear signals may map to disclosed narrow
ranges: beginner A1–A2, intermediate B1–B2, upper-intermediate B2–C1, and advanced C1–C2. “Not
basic” may use B2–C1. Guided-learning intent starts useful selection immediately as specified in
LE.ROUTING; choose a disclosed everyday starting difficulty if none is known. Do not ask for a
situation or require CEFR before helping. Other generic level-sensitive catalog discovery without
a signal asks one plain-language level question and waits. For imminent situations or
explicit no-clarification requests, answer with common task-appropriate expressions. Briefly
describe the starting difficulty in ordinary language and offer adjustment. Do not assume B2–C1 or
C1–C2 solely because the request is urgent or forbids questions. A task-selected API range is a
material-selection setting, not a proficiency assessment of the learner. When calling a
level-filtered catalog endpoint, pass both CEFR bounds and briefly disclose a chosen range if none
was supplied. Suggestions has no CEFR filters. Never apply unsupported bounds to it. For “easier” or
“harder,” select exact API wording with suitable nuance, familiarity and level. An
explicit “higher than B2” raises the lower bound; “less basic” need not merely substitute rare
words. Preserve topic and register.

## LMS.WORD-PATH — Word, combinations, listening

Use Common Words for new word selection and Common Phrases/Suggestions for new combinations.
Browser-only collocations do not replace API evidence; user-supplied combinations may be discussed and linked as unverified context. Suggestions has no CEFR request filter and may return unrelated
text or another level. Curate for the word, meaning and difficulty without rewriting records.
Optional `language-level`/`count` applies only to its record. A word's level does not label all
combinations or scenes. Show fewer combinations when suitable API rows are insufficient.

## LMS.QUERY — Use bounded public requests

Prefer one anonymous GET using the host's existing HTTP, web, or browser capability, with limit <=
20 and no automatic pagination or retries. One or two additional sequential queries are allowed only
for distinct groups, the next word-to-combinations stage, or one disclosed relaxation of an inferred
constraint. No runtime script or transport diagnostic is required; never spend the learner turn
debugging access. Active filters combine with AND. Never silently remove an explicit constraint.
Formal means `formality=formal`; professional means `register=professional`; use both only when both
were requested.

## LMS.CURATION — Select useful and distinct language

Preserve Common Phrase `text` and Common Word `word` exactly as display and search query. For Common Phrases, count >= 5 establishes catalog
membership, not clip quality. Metadata supports record-level claims, not speaker, source, stress, or
tone claims about a clip. Preserve server order for explicit ranking requests; otherwise curate a
coherent subset. Prefer immediately reusable chunks with distinct practical value at the requested
level. Avoid weak duplicates and phrases already rejected or known in the available conversation.
Every selected word or phrase has its own link. Start with the response size in `LE.COMPOSITION`,
honoring explicit counts only when suitable API rows suffice. A word-learning request selects words with short meanings and multiple
useful distinct API expressions under each word, each linked when available. Do not flatten it into unrelated phrases.
A request for expressions receives expressions. In guided learning, choose varied reusable phrase cores rather than many
pronoun variants of one construction. Prefer conversational usefulness for the learner over rarity
or long full-sentence complexity. Supply meanings and select exact API examples; do not offload
study design to the learner. A useful A2 learning example is not a claim of catalog A2 or scene-level A2.

## LMS.DEGRADATION — Keep usefulness and evidence honest

Empty, unusable, rate-limited or unavailable data supplies no new examples or example links.
State the limitation briefly; never fill a requested count from model knowledge. Suitable current
API rows already in context may be reused while record identity, exact text and corpus language
remain established; historical documentation alone does not qualify. State shortfalls. Preserve
explicit constraints; offer a precise relaxation without silently applying it. Conceptual explanation
and discussion of supplied text may continue. No transport retries, private endpoints or invented
clip evidence. Failed-link recovery also requires exact API rows for new alternatives.

## LMS.QA — Acceptance scenarios

Cover ordinary/guided selection, grammar, comparisons, practice and follow-ups with successful, empty, unavailable and insufficient API data. Verify exact text and queries, no synthetic count
filler, no rewritten teaching cores, user-text provenance, retained levels/filters, word grouping,
Suggestions relevance and metadata, and reuse only from established current API evidence.

## LMS.DELTA-10 — Guided selection without learner-authored setup

Evolve under LM-SKILL-02 in [the task plan](../LM-SKILL-PLAN.md). LMS.LEVEL starts guided study
with an adjustable choice; LMS.CURATION requires useful varied cores and assistant explanations,
including word-grouped material under the author-accepted two-critic repair.
Explicit levels, ordinary catalog clarification, exact record text, source distinctions, bounded
queries and the reconciled optional Suggestions metadata remain protected. QA checks unknown-level
guided start, A2 usefulness without false CEFR claims, varied cores and known-item replacement.

## LMS.API-ONLY-1 — API evidence required for new study examples

User-authorized Evolve, 2026-11-05: Revision 11 API-only sourcing overrides prior model/UI fallback and count filler; source and installed skill follow it.
All unrelated prior behavior remains. Evidence: existing instructions/evals; QA: LMS.QA and updated offline definitions.

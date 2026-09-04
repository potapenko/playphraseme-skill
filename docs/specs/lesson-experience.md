# PlayPhrase response experience

- Status: Active
- Stability: Evolving
- Revision: 2
- Domain: `lesson-experience`
- Authority: user decisions approved 2026-09-04
- Requires: `skill-distribution` Revision 3, clause `SD.COMPATIBILITY`

## LE.ROUTING — Choose a response pattern

Route English questions to the closest PlayPhrase-first pattern: explain one
phrase, compare expressions, say an idea naturally, collect phrases for a
situation, discover vocabulary, show grammar through live patterns, or provide
explicitly requested practice.

Implicit needs count. “I have a job interview tomorrow” should trigger the
situation pattern without requiring the word “lesson.” For situational goals,
first try Common Phrases with a supported relevant `topic` and requested CEFR.
Exact wording and grammar patterns use Classic Search.

## LE.COMPOSITION — Stable PlayPhrase-first answers

Each response pattern defines a compact answer structure and a default size.
Size ranges guide consistency but are not quotas: stop when another phrase adds
no useful choice. Searchable phrases and their PlayPhrase.me links appear early
and form the primary content; explanations only help the user choose what to
open.

Multi-phrase responses may use a phrase path organized by situation, meaning,
intensity, formality, naturalness, or grammar. Every selected phrase has its own
link and a brief useful distinction. A requested duration may influence breadth
but must not produce timeboxed lesson stages by default.

Do not wrap ordinary English questions in learning objectives, warm-ups,
listening missions, comprehension questions, or generic lesson scaffolding.

## LE.ACTIVE-LINKS — Links are the material

For one phrase, use a descriptive primary link and optionally nearby linked
expressions. For lists, comparisons, and paths, give every important phrase a
consistent compact link. No task or report-back step is required per link.

Link destinations are unchanged URL-builder output with no tracking. Do not
assign a source, speaker, tone, stress, pragmatic meaning, or other clip property
unless verified on the public browser-visible page. Without that evidence,
explain language-level distinctions rather than imagined clip behavior.

## LE.MODES — Practice is a special case

Words such as “teach,” “learn,” or “lesson” do not automatically request an
exercise. Do not add a quiz, gap-fill, role-play, shadowing task, retrieval test,
worksheet, or tutoring sequence unless practice is explicitly requested.

Explicit practice uses linked formulations and asks the learner to choose for a
real meaning or context. An interactive quiz asks one item and waits for the
answer before feedback. Generic exercises remain a last resort.

## LE.DEGRADATION — Public-link fallback

Without the Learning API, browser, or scripts, select defensible phrases,
produce documented canonical public links, and state which live results were
not verified. Never use a private API or invent movie/TV evidence.

## LE.QA — Acceptance scenarios

1. `explain-one-phrase-response` leads with meaning and one primary link.
2. `compare-phrases-response` uses a linked comparison plus a short contrast.
3. `natural-wording-response` offers linked alternatives and a best-fit note.
4. `job-interview-response` groups linked phrases without timeboxed stages or
   generic exercises; the implicit variant routes the same way.
5. `vocabulary-discovery-response` stays scannable and link-centered.
6. `grammar-through-examples-response` puts linked patterns before a short rule.
7. `explicit-phrase-native-quiz` uses linked choices and waits for an answer.

## LE.DELTA-1 — Pedagogical workflow

- Mode: Evolve.
- External authority: user approval on 2026-09-04 after initial agent feedback.
- Previous behavior: searches and links had no lesson-composition guidance.
- New behavior: lesson intent used a flexible active-listening workflow.
- Compatibility: public search/API boundaries and offline behavior were kept.

## LE.DELTA-2 — PlayPhrase-first response design

- Mode: Evolve.
- External authority: user approval on 2026-09-04 after testing v0.2.0 and
  clarifying that “lessons” meant reusable answer structures.
- Previous behavior: lesson requests defaulted to pedagogical activities and
  made PlayPhrase.me secondary to a generic worksheet.
- New behavior: reusable response patterns put linked phrases first; phrase
  paths organize multi-phrase answers and practice is explicit-only.
- Evidence: user-observed ChatGPT output and two follow-up feedback exchanges.
- Compatibility: canonical URLs, API limits, direct search, offline fallback, and installation remain unchanged.

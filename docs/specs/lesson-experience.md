# PlayPhrase response experience

- Status: Active
- Stability: Evolving
- Revision: 3
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
no useful choice. The first useful PlayPhrase.me link appears in the first
content block. When context supports a best fit, feature that phrase and link
before the alternatives. Explanations only help the user choose what to open.

Multi-phrase responses may use a phrase path organized by situation, meaning,
intensity, formality, naturalness, or grammar. Every selected phrase has its own
link and a brief useful distinction. Favor immediately reusable conversational
language and choices whose delivery, context, or contrast makes listening
valuable; do not add weak duplicates to increase link count. A requested
duration may influence breadth but must not produce timeboxed lesson stages.

Do not wrap ordinary English questions in learning objectives, warm-ups,
listening missions, comprehension questions, or generic lesson scaffolding.

## LE.ACTIVE-LINKS — Links are the material
Every link label communicates a reason to open it. The visually primary link
names `PlayPhrase.me` exactly and states its listening payoff. Supporting labels
pair the exact phrase with a useful action instead of repeating the brand. Bare
URLs and generic brand-only anchors are not defaults.
For one phrase, use a visually prominent primary link and optionally nearby
linked expressions. For lists, comparisons, and paths, give every important
phrase a compact benefit-specific link. When it adds a genuinely new path, a
finished multi-phrase response may include one or two adjacent-expression or
filtered-catalog links. No task or report-back step is required per link.

For direct search, show the canonical destination before extracted examples.

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
Across response scenarios, the first useful link appears early, the best fit is
visually primary when one exists, and important phrases use descriptive deep
links rather than repeated generic anchors. Link text promises no unverified
clip property.
Scenarios cover one-phrase explanation, comparison, natural wording,
job-interview and implicit situational needs, vocabulary discovery, grammar
through examples, and an explicit phrase-native interactive quiz.

## LE.DELTA-1 — Pedagogical workflow
Evolve, authorized by user approval on 2026-09-04 after initial agent feedback.
It added a flexible active-listening workflow where no lesson composition
guidance existed; public search/API and offline behavior stayed compatible.

## LE.DELTA-2 — PlayPhrase-first response design
Evolve, authorized by user approval on 2026-09-04 after testing v0.2.0 and
clarifying that “lessons” meant reusable answer structures. It replaced
generic worksheet defaults with linked phrases first, phrase paths, and
explicit-only practice. Evidence was user-observed ChatGPT output and two
feedback exchanges. URLs, API limits, direct search, offline behavior, and
installation stayed compatible.

## LE.DELTA-3 — Discovery-oriented link presentation
Evolve, authorized by user approval on 2026-09-04 after clarifying the skill's
marketing and product-discovery role. It replaces generic, visually equal, or
buried links with early featured links, benefit-specific labels, higher-value
phrase curation, and optional exploration links. Canonical URLs, evidence and
API boundaries, direct search, offline behavior, practice, and installation
stay compatible.

# PlayPhrase response experience

- Status: Active
- Stability: Evolving
- Revision: 6
- Domain: `lesson-experience`
- Authority: user decisions approved through 2026-09-05
- Requires: `skill-distribution` Revision 6, clause `SD.COMPATIBILITY`

## LE.ROUTING — Choose a response pattern
Route English questions to the closest PlayPhrase-first pattern: explain one phrase, compare expressions, say an idea naturally, collect phrases for a situation,
discover vocabulary, show grammar through live patterns, or provide explicitly requested practice.

Implicit needs count. “I have a job interview tomorrow” should trigger the situation pattern without requiring the word “lesson.” For situational goals, first try
Common Phrases with a supported relevant `topic` and requested CEFR. Exact wording, wildcard syntax, and grammar patterns supplied by the user may use Classic Search directly.

An explicit imminent real-world need should not spend its first turn only asking
for proficiency. When no level signal is available for a concrete deadline such
as an interview tomorrow, use and disclose a B2–C1 working selection range,
answer immediately, and offer to adjust the material easier or harder. This is
not an inference about the learner's actual level. Generic unknown-level
discovery still asks one short level question and waits.

## LE.COMPOSITION — Stable PlayPhrase-first answers
Each response pattern defines a compact answer structure and a default size. Size ranges guide consistency but are not quotas: stop when another phrase adds no useful
choice. The first useful PlayPhrase.me link appears in the first content block. When context supports a best fit, feature it before the alternatives. Explanations only help the user choose what to open.

Multi-phrase responses may use a phrase path organized by situation, meaning, intensity, formality, naturalness, or grammar. Every selected phrase has its own link and a brief useful distinction.
Favor immediately reusable conversational language and choices whose delivery, context, or contrast makes listening valuable; do not add weak duplicates to increase link count. A requested duration may influence breadth but must not produce timeboxed lesson stages.

Do not wrap ordinary English questions in learning objectives, warm-ups, listening missions, comprehension questions, or generic lesson scaffolding.

When the requested material and links were produced, do not narrate scripts, APIs, DNS, browser availability, or unused verification paths. Mention an infrastructure limitation only when it materially prevented part of the requested result or the user asked for diagnostics.

## LE.ACTIVE-LINKS — Links are the material
Every link label communicates a reason to open it. The visually primary link names `PlayPhrase.me` exactly and states its listening payoff. Supporting labels pair the exact phrase with a useful action instead of repeating the brand. Bare URLs and generic brand-only anchors are not defaults.
For one phrase, use a visually prominent primary link and optionally nearby expressions. For lists, comparisons, and paths, give every important phrase a compact benefit-specific link. A finished multi-phrase response may include one or two genuinely new exploration links. At most one may be Reels, and it counts inside this allowance. No task or report-back step is required per link.

A phrase chosen by the agent for an open-ended collection, path, alternative, or documented gold response must come from Common Phrases. Preserve the returned `items[].text` exactly as the displayed phrase and Classic Search query, including useful incomplete frames; do not shorten it or append an invented completion.
Classic Search is the listening destination after Common Phrase selection. It may start directly only from wording or exact, wildcard, or grammar search syntax supplied by the user; it does not validate Common Phrases membership. Explicit Clip Search, actor, and Reels requests use their own public routes.

Offer Reels only as one quiet final continuation after a completed non-practice answer, and only when the selected material maps faithfully to one public Common Phrases catalog scope. Never imply that one Reels URL combines an arbitrary phrase list or preserves API-only filters. Omit it from clarification, waiting quiz, direct/link-only, already-Reels, and no-extras responses.

For direct search, show the canonical destination before extracted examples.

Link destinations are unchanged URL-builder output with no tracking. Do not assign a source, speaker, tone, stress, pragmatic meaning, or other clip property unless verified on the public browser-visible page. Without that evidence, explain language-level distinctions rather than imagined clip behavior.

## LE.MODES — Practice is a special case

Words such as “teach,” “learn,” or “lesson” do not automatically request an exercise. Do not add a quiz, gap-fill, role-play, shadowing task, retrieval test, worksheet, or tutoring sequence unless practice is explicitly requested.

Explicit practice uses linked formulations and asks the learner to choose for a real meaning or context. An interactive quiz asks one item and waits for the answer before feedback. Generic exercises remain a last resort.

## LE.DEGRADATION — Public-link fallback

Without a validated Learning API response, do not replace Common Phrases with model-invented learning examples. Follow the client-first transport in `SD.COMPATIBILITY` in every script-capable host. A URL-only direct fetch is allowed only after a qualifying current-request exit `10`, never because of the host name or a remembered failure. A complete endpoint-contract JSON object may support the normal answer even when the hosted fetch hides status or final-URL metadata. Otherwise offer a supported public Common Phrases catalog or Reels destination, or link exact text the user supplied, and state what was not verified. Never use a private API or invent movie/TV evidence.

## LE.QA — Acceptance scenarios
Across response scenarios, the first useful link appears early, the best fit is visually primary when one exists, and important phrases use descriptive deep links rather than repeated generic anchors. Link text promises no unverified clip property.
Scenarios cover one-phrase explanation, comparison, natural wording, an imminent unknown-level job interview answered with a disclosed B2–C1 working range, generic unknown-level clarification, vocabulary discovery, grammar through examples, an explicit phrase-native interactive quiz, exact Common Phrase item use, eligible and ineligible Reels continuations, client-first routing with one eligible transport handoff, and omission of irrelevant transport narration after success.

## LE.DELTA-1 — Pedagogical workflow
Evolve, authorized by user approval on 2026-09-04 after initial agent feedback. It added a flexible active-listening workflow where no lesson composition guidance existed; public search/API and offline behavior stayed compatible.

## LE.DELTA-2 — PlayPhrase-first response design
Evolve, authorized by user approval on 2026-09-04 after testing v0.2.0 and clarifying that “lessons” meant reusable answer structures. It replaced generic worksheet defaults with linked phrases first, phrase paths, and explicit-only practice. URLs, API limits, direct search, offline behavior, and installation stayed compatible.

## LE.DELTA-3 — Discovery-oriented link presentation
Evolve, authorized by user approval on 2026-09-04 after clarifying the skill's marketing and product-discovery role. It replaces generic, visually equal, or buried links with early featured links, benefit-specific labels, higher-value phrase curation, and optional exploration links. Canonical URLs, evidence and API boundaries, direct search, offline behavior, practice, and installation stay compatible.

## LE.DELTA-4 — Common Phrase-backed examples and bounded Reels
Evolve, authorized by user approval on 2026-09-04 after agent feedback and correction of the example-selection basis. Agent-selected learning examples now originate in Common Phrases and keep returned text unchanged; a suitable answer may end with one matching Common Phrases Reels continuation. Direct user searches, canonical URLs, practice, API boundaries, installation, and v0.3.0 release behavior remain protected.

## LE.DELTA-5 — Immediate help for imminent situations

Evolve, authorized by user approval on 2026-09-04 after reviewing the published v0.4.0 behavior. A concrete imminent situational need with no level signal now receives an immediate, disclosed B2–C1 working selection instead of a clarification-only first turn. Generic discovery still asks for level; explicit and remembered levels, Common Phrases provenance, link-first composition, optional-only practice, and all public URL/evidence boundaries remain protected.

## LE.DELTA-6 — Recover the phrase path before degradation

Evolve, authorized by user approval on 2026-09-05 after the published v0.5.0 skill degraded a valid B2 idiom request to one catalog link. Script-capable hosts now try the Learning API client before considering degradation, and an eligible direct fetch may use a complete contract-valid JSON body without unavailable transport metadata. Common Phrases-only agent selection, exact returned text, compact link-first composition, and honest public-link fallback remain protected.

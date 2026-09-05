# PlayPhrase response experience

- Status: Active
- Stability: Evolving
- Revision: 7
- Domain: `lesson-experience`
- Authority: user decisions approved through 2026-09-05
- Requires: `skill-distribution` Revision 7, clause `SD.COMPATIBILITY`

## LE.ROUTING — Choose a response pattern

Route an English question to the closest PlayPhrase-first pattern: explain one
phrase, compare expressions, say an idea naturally, collect phrases for a
situation, discover vocabulary, show grammar through live patterns, or provide
explicitly requested practice.

Implicit needs count. “I have a job interview tomorrow” triggers the situation
pattern without requiring the word “lesson.” Exact wording, wildcard syntax,
and grammar patterns supplied by the user may use Classic Search directly.

An imminent real-world need does not spend its first turn only asking for
proficiency. Without a level signal, use and disclose a B2–C1 working range,
answer immediately, and offer to adjust. Generic unknown-level discovery still
asks one short level question and waits.

## LE.COMPOSITION — Stable PlayPhrase-first answers

The first useful PlayPhrase.me link appears in the first content block. When
one phrase is the best fit, feature it first. In a multi-phrase response, every
important phrase receives its own link and one brief distinction.

Organize a phrase path by situation, meaning, intensity, formality,
naturalness, or grammar. Favor distinctive, immediately reusable language; do
not add weak duplicates to inflate the link count.

Do not wrap ordinary English questions in learning objectives, warm-ups,
listening missions, comprehension questions, or generic lesson scaffolding.
Exercises appear only when explicitly requested.

## LE.ACTIVE-LINKS — Links are the material

Every link label communicates a reason to open it. The primary label names
`PlayPhrase.me` exactly and states the listening payoff. Bare URLs and repeated
generic anchors are not the default.

When a valid Common Phrases response is available, use returned `items[].text`
unchanged as both displayed phrase and Classic Search query, including an
intentional incomplete frame. Do not shorten, complete, or rewrite it.

When live candidate data is unavailable, an ordinary learner request still
receives model-selected, level-appropriate natural language with individual
Classic Search links. Do not call those fallback choices Common Phrases,
API-selected, corpus-verified, or matched by a server filter. Classic Search is
the listening destination; it is not proof of catalog membership or any clip's
speaker, source, stress, or tone.

Direct user-supplied text may always receive its documented search route.
Explicit Clip Search, actor, and Reels requests use their own public routes.

One quiet Reels continuation may follow a completed non-practice answer only
when the material maps faithfully to a supported public catalog scope. Never
imply that a Reels URL combines an arbitrary model-selected list or preserves
API-only filters.

## LE.MODES — Practice is a special case

Words such as “teach,” “learn,” or “lesson” do not automatically request an
exercise. Do not add a quiz, gap-fill, role-play, shadowing task, worksheet, or
tutoring sequence unless practice is explicit.

Explicit practice should depend on linked formulations and ask the learner to
choose for a real meaning or context. An interactive quiz asks one item and
waits for the answer.

## LE.DEGRADATION — Preserve the requested outcome

For an ordinary learner request, inability to fetch the Learning API must not
replace requested phrases with a catalog-only refusal. Use the honest
model-selected path described in `LE.ACTIVE-LINKS`, satisfy the requested count
and organization, and keep PlayPhrase.me links as the main content.

Do not narrate Python, DNS, exit codes, transport attempts, or browser-tool
limitations. A short evidence limitation is appropriate only when the user
explicitly requested API ranking, Common Phrases membership, source titles, or
another claim that cannot be supported.

Never use a private API or invent movie/TV clip evidence.

## LE.QA — Acceptance scenarios

Scenarios cover one-phrase explanation, comparison, natural wording, an
imminent unknown-level interview, generic level clarification, vocabulary
discovery, grammar, explicit practice, exact Common Phrase text when API data
exists, honest model-selected fallback when it does not, eligible Reels, and
omission of infrastructure narration.

The release regression prompt must return exactly five B2 idioms grouped by
what they express, with five descriptive Classic Search links. A catalog-only
response, generic lesson, or transport explanation fails acceptance.

## LE.DELTA-7 — Useful answers without live candidate data

Evolve, authorized by the user's 2026-09-05 direction after the released
v0.5.1 skill again returned a catalog-only refusal in ChatGPT. Ordinary learner
answers no longer require live API evidence. Common Phrases provenance remains
strict when claimed, while an honest model-selected phrase path preserves the
requested count, level, grouping, and individual PlayPhrase.me links when live
candidate data is unavailable.

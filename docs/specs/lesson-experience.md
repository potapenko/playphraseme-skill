# Lesson experience

- Status: Active
- Stability: Evolving
- Revision: 1
- Domain: `lesson-experience`
- Authority: user decision approved 2026-09-04
- Requires: `skill-distribution` Revision 3, clause `SD.COMPATIBILITY`

## LE.ROUTING — Material selection

Lesson, practice, quiz, tutoring, and study-plan requests use the lesson
workflow. A typical lesson selects 4–7 learner-sized target phrases unless the
user asks for a different scope.

For situational goals, first try Common Phrases with a supported, genuinely
relevant `topic` and the requested CEFR range. Exact phrases, grammar patterns,
and wording corrections use Classic Search. The model supplies explanations,
pedagogy, and exercises; PlayPhrase.me supplies curated phrase candidates and
public listening destinations.

## LE.COMPOSITION — Flexible learning cycle

Choose one primary direction: situation, listening and nuance, grammar or
naturalness, or pronunciation. Compose only the 3–5 activities useful for the
learner's goal, level, and available time. The available cycle is challenge →
listen → notice → clarify → controlled practice → production → retrieval; no
lesson must include every stage or preserve that exact order.

Prefer a small set of reusable activities: prediction, a concrete listening
mission, noticing, matching or gap-fill, error repair, best response, optional
shadowing, role-play, and retrieval. Naturalness tasks may have several valid
answers, and immediate retrieval must not be described as spaced repetition.

## LE.ACTIVE-LINKS — Listening as an activity

Every PlayPhrase.me link in a lesson has an explicit learner action, such as
noticing wording, comparing delivery, or choosing a context-appropriate reply.
Descriptive link text is allowed, but the destination is the URL builder output
unchanged when the builder is available; no tracking parameter is appended.

Do not assign a source title, speaker, tone, stress pattern, pragmatic meaning,
or other clip property to a particular result unless it was verified in the
public browser-visible page. Without that evidence, ask the learner to observe
or compare what they hear rather than presenting the property as fact.

## LE.MODES — Interaction and answers

In interactive tutoring mode, present one meaningful task at a time and wait
for the learner's answer before feedback or revealing the answer. In a
self-study worksheet, provide the complete sequence and place the answer key
after the activities. Follow an explicit user choice; otherwise infer the mode
from whether they asked to be quizzed interactively or requested a complete
lesson/worksheet.

## LE.DEGRADATION — Public-link fallback

The lesson remains useful without the Learning API, browser, or script
execution: choose defensible target language, produce documented canonical
public search links, and state which live results were not verified. Never use
a private API or invent movie/TV evidence to fill the gap.

## LE.QA — Acceptance scenarios

1. `job-interview-lesson` uses relevant work/CEFR material, active listening,
   role-play, retrieval, canonical untracked links, and no private endpoint.
2. `grammar-lesson-no-browser` remains complete with public Classic Search
   links and makes no claim about unseen clips or source titles.
3. `same-phrase-different-tone` lets the learner classify what they hear and
   does not pre-label unverified public results.
4. `interactive-quiz` waits for the learner before feedback or answer reveal.

## LE.DELTA-1 — Pedagogical workflow

- Mode: Evolve.
- External authority: user approval on 2026-09-04 after two rounds of agent
  feedback about lesson-building behavior.
- Previous behavior: the skill routed searches and returned examples and links
  but did not define how to compose a lesson.
- New behavior: the skill routes lesson intent into a flexible, active-listening
  workflow with explicit interaction and evidence boundaries.
- Compatibility: search modes, public URL/API boundaries, installation paths,
  and behavior without scripts or network access are preserved.

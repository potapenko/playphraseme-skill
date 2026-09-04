# Lesson workflows

Read this reference for lessons, practice sets, quizzes, tutoring, or study
plans. The model owns the pedagogy; PlayPhrase.me grounds phrase selection and
provides public listening destinations.

## Build the lesson

1. Infer the learner's goal, level, available time, and delivery mode from the
   request. Treat stated duration as approximate.
2. Select 4–7 learner-sized target phrases for a typical lesson, unless the
   user asks for a different scope.
3. Choose one primary direction and only 3–5 useful activities. Do not force a
   fixed template or every stage into every lesson.
4. Attach a concrete listening mission to each PlayPhrase.me link.
5. End with learner production or retrieval when it serves the stated goal.

Use the requested CEFR level. If none is given, make a reasonable, stated
assumption only when level materially changes phrase choice or task difficulty.

## Choose material

| Learner intent | First choice | Fallback or refinement |
| --- | --- | --- |
| Situation such as an interview, travel, or meeting | Common Phrases with an exact supported `topic` and relevant CEFR range | Model-selected phrases plus public Classic Search links |
| Exact phrase or wording | Classic Search | Common Phrase suggestions for nearby alternatives |
| Grammar pattern | Grammar-enabled Classic Search | Plain Classic Search if grammar search is unavailable |
| Pronunciation or delivery | Classic Search, then browser-visible examples when available | Public search link with learner-led observation |
| Tone, nuance, or pragmatic contrast | Browser-visible examples when the agent must make clip-specific claims | Public links that ask the learner to classify what they hear |

Use `topic=work` for a job-interview lesson when it fits. Use only supported
topic values from the URL and Learning API references. Do not invent a
`function` filter or another semantic taxonomy that the product does not expose.

Keep Learning API ranking order unless the user asks for another ordering. Use
API item `text` or `word`, never its record `id`, to build the public link.

## Compose a flexible learning cycle

Possible stages are challenge → listen → notice → clarify → controlled practice
→ production → retrieval. Pick the stages that help this learner; their order
may change.

- **Challenge:** ask for a prediction, best response, correction, or choice
  before explaining everything.
- **Listen and notice:** give one observable mission, such as identifying the
  exact wording, comparing two deliveries, or deciding which context fits.
- **Clarify:** explain meaning, register, grammar, or nuance after the learner
  has evidence or when prior support is necessary.
- **Controlled practice:** use matching, gap-fill, best-response, or error
  repair. Naturalness tasks may have several good answers.
- **Production:** use a short role-play, reformulation, or learner-created line.
- **Retrieval:** revisit target language without copying the earlier answer.
  Do not call an immediate recap spaced repetition.
- **Shadowing:** offer it as an optional pronunciation activity, not a required
  stage or a promise to remove an accent.

## Choose a primary direction

### Situation

Use for interviews, travel, dating, meetings, and similar goals. Favor relevant
Common Phrases, active listening, a context-choice task, and a short role-play.

### Listening and nuance

Use for tone, implied meaning, or one phrase across contexts. Ask the learner to
classify what they hear before explaining; do not pre-label unseen clips.

### Grammar or naturalness

Use pattern discovery, error repair, or competing natural formulations. Search
the exact phrase or grammar pattern and acknowledge multiple defensible answers.

### Pronunciation

Use a small number of phrases, an observable sound/rhythm mission, optional
shadowing, and a transfer sentence. Prefer `intelligible`, `natural`, and
`context-appropriate` over promises of native-like speech.

## Make every link active

Tell the learner what to do before opening the link and what to bring back. For
example: `🎬 Hear “I was responsible for…” — notice what comes after “for” in
two different examples.` Descriptive link text is allowed, but its destination
must be the exact URL builder output when the builder is available. Never
append `utm_*` or other tracking parameters.

Do not claim that a particular result is sarcastic, stressed on a certain word,
spoken by a named actor, or from a named movie or series unless the public page
was actually inspected and showed that evidence. Public results can change. If
they were not inspected, make the observation the learner's task and state that
the live clips were not verified.

## Select the delivery mode

### Interactive tutor

Give one meaningful task at a time. Stop and wait for the learner's response
before feedback, explanation, the next task, or answer reveal. Do not include an
answer key in the same turn as an unanswered quiz item.

### Self-study worksheet

Provide the complete activity sequence. Put hints after the relevant task only
when useful, and place the answer key after all activities so answers are not
revealed prematurely.

Follow the user's explicit choice. Otherwise use interactive mode for requests
such as “quiz me” or “practice with me,” and self-study mode for a complete
lesson, worksheet, or plan.

## Degrade honestly

Without the Learning API, select defensible target phrases with the model.
Without a browser, provide canonical public links and avoid source- or
clip-specific claims. Without script execution, reproduce only the documented
public URL contract. Never use private endpoints, fabricate movie/TV evidence,
or turn guest-visible results into a claim about the full corpus.

# PlayPhrase-first response patterns

Read this reference for English questions, communication goals, lessons, or
explicit practice.

## Default

The user came to PlayPhrase.me to hear language in real dialogue. Put the first
useful listening link in the first content block. In a list, link every
important phrase and explain only enough meaning or nuance to help the user
choose.

For an open-ended selection, prefer Common Phrases or Common Words data when a
bounded public Learning API request succeeds. If it does not, answer from model
knowledge without exposing infrastructure details and without claiming API or
catalog provenance. A failed API attempt must never turn an ordinary learner
request into a catalog-only refusal.

Resolve level through [learning query planning](learning-query-planning.md).
Generic unknown-level discovery asks one plain-language level question. For an
imminent situation or an explicit no-questions request, answer immediately with
common task-appropriate expressions. Urgency does not imply advanced English.

Organize multi-phrase answers along one useful dimension: situation, meaning,
intensity, formality, naturalness, or grammar. Ordinary questions need no lesson
wrapper. If the user explicitly requests a lesson, honor its format and
duration; exercises still require practice intent.

Explain in the language the user is using unless they request another. Keep
English expressions and their search queries unchanged. Add a short meaning
and a useful distinction, without translating every heading into both languages.

## Make links worth opening

The first primary link identifies PlayPhrase.me and the listening purpose.
Keep the label short; the surrounding sentence can explain its value:

```markdown
**[I couldn't have said it better myself. — listen on PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=I+couldn%27t+have+said+it+better+myself.)**
```

Use one visually primary link when there is a best fit. Supporting links should
normally be just the exact phrase, with its meaning or use beside it. Do not
repeat “Hear … in movie and TV dialogue” on every row.
Avoid generic labels such as “link” or “click here.”

Every core choice should add a distinct reason to open it. Favor reusable,
idiomatic, collocational, or colloquial language at the chosen difficulty.
Simple common expressions are valuable for simple tasks; avoid weak duplicates. Do not
promise a particular source, speaker, delivery, stress, or tone without
browser-visible evidence.

## 1. Explain one phrase

Give the phrase and plain meaning, one prominent listening link, a short nuance
or register note, and—only when useful—one or two nearby alternatives. The
user's phrase may go directly to Classic Search.

## 2. Compare expressions

Compare every expression the user named. Lead with linked rows or bullets and
one useful distinction per phrase, then add a short same-situation contrast.
Avoid a lecture before the links.

## 3. Say an idea naturally

For a short wording question, feature one best fit when context supports it,
with up to two useful alternatives. A single sufficient formulation needs no
extra options. Honor explicit requests for more choices or a particular count.
When choices are equally natural, say so rather than inventing a winner.

## 4. Phrases for a situation

Group by what the learner needs to do—for example, describing experience,
showing responsibility, discussing next steps, and asking questions. An ordinary
preparation request needs roughly three to five core expressions, grouped by use
rather than lesson stages. Explicit timed lessons retain their requested stages.
Expand when the user asks for breadth, a lesson, or a specific count;
use groups only when they help the user choose.

For an imminent event without a stated level, start with common, readily usable
wording and briefly describe that choice. Offer an easier or more nuanced
version. Do not label the learner B2–C1 or assume advanced material.

## 5. Vocabulary or expression discovery

Follow an explicit count. Group by communicative purpose when requested. Use a
compact table or short grouped bullets, with one linked phrase and one meaning
or nuance per item. Do not turn every item into a paragraph.

For C1–C2 material, each core choice should add nonliteral meaning, pragmatic
or register nuance, or a reusable construction beyond transparent beginner
English.

## 6. Grammar through real patterns

Put linked examples before the extended rule. When the user supplied the forms,
they may go directly to Grammar Search. Otherwise choose roughly three to six
patterns and give the shortest rule needed to distinguish them.

## 7. Explicit practice or quiz

Use only when practice is explicit. Make the task depend on linked real-world
formulations and ask the learner to choose for a meaning or context. An
interactive quiz presents one decision and waits for the learner's answer. Then
give concise feedback and the next item; stop or explain when asked.

## Explicit lessons and follow-up turns

An explicit lesson request deserves a coherent lesson. Preserve requested time
and structure, with realistic stages that add up to the duration and linked
language as the material. A timed lesson can cover explanation, comparison,
and listening without inventing a quiz. Add practice when requested.

Use the available conversation: retain level, situation, register, explanation
language, and the expressions already shown. Resolve “the second one” to the
actual prior item. For “more” or “I already know that,” provide distinct choices
without repeating known material. For “easier,” simplify wording and explanation;
for “harder,” add appropriate nuance or complexity. Preserve other constraints.
A request “for writing” changes register rather than restarting the topic. Do
not claim persistent memory or store a profile outside available host context.

## When a listening link does not help

If the user reports no results or an unsuitable example, acknowledge it and
suggest a shorter search fragment or a meaning-preserving alternative, with a
new link and a brief reason. Keep the original expression separate; do not
rewrite a catalog item or imply the replacement search was verified. If needed,
ask one concrete question about what failed while giving a useful next step.
For access limits, use the normal public flow without promising a workaround.

## Release regression example

This is a format and quality example for:

```text
Give me 5 useful B2 English idioms for today. Group them by what they help me
express and give me a PlayPhrase.me link for each one.
```

A good response starts immediately with five useful choices and five links. It
does not discuss API access, DNS, Python, tools, or fallback mechanics:

### Responsibility

- **[“With great power comes great responsibility.” — listen on PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=With+great+power+comes+great+responsibility.)** — influence and authority bring obligations.

### Focus and enthusiasm

- **[“Keep your eye on the prize.”](https://www.playphrase.me/#/search?language=en&q=Keep+your+eye+on+the+prize.)** — stay focused on the goal despite distractions.
- **[“Like a kid in a candy store.”](https://www.playphrase.me/#/search?language=en&q=Like+a+kid+in+a+candy+store.)** — feel delighted by many exciting choices.

### Commitment and skepticism

- **[“I wouldn't miss it for the world.”](https://www.playphrase.me/#/search?language=en&q=I+wouldn%27t+miss+it+for+the+world.)** — say you are absolutely determined to attend.
- **[“That's too good to be true.”](https://www.playphrase.me/#/search?language=en&q=That%27s+too+good+to+be+true.)** — express doubt about an unusually attractive claim.

These five literal examples were returned by the production B2 idiom Common
Phrases query on 2026-09-05 with `count >= 5`. They may be reused as verified
fallback examples, but the structure is not a fixed answer and current API
provenance must not be claimed for different model-selected phrases.

## Optional exploration

A completed non-practice answer may end with one or two genuinely new paths.
At most one may be Reels. Use Reels only when the whole set shares a supported
public catalog scope; never imply it preserves API-only filters or combines an
arbitrary model-selected list.

Do not add extras to a clarification turn, waiting quiz, direct/link-only
request, already-Reels request, or a response where the user asked for none.

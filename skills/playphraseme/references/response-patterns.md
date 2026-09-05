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
Generic unknown-level discovery asks one short level question. A concrete
imminent situation instead uses a disclosed B2–C1 working range and answers in
the same turn.

Organize multi-phrase answers along one useful dimension: situation, meaning,
intensity, formality, naturalness, or grammar. The path—not a worksheet around
it—is the finished response. Do not add exercises unless the user explicitly
asks to practise.

## Make links worth opening

A strong link label combines the exact searchable phrase, an action, and the
listening value:

```markdown
**[🎬 Hear “I couldn't have said it better myself.” in movie and TV dialogue on PlayPhrase.me →](https://www.playphrase.me/#/search?language=en&q=I+couldn%27t+have+said+it+better+myself.)**
```

Use one visually primary link when there is a best fit. Supporting links can be
compact, but avoid repeated generic labels such as “link” or “click here.”

Every core choice should add a distinct reason to open it. Favor reusable,
idiomatic, collocational, or colloquial language over elementary filler. Do not
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

Offer three to five options unless the user requests another count. Feature a
best fit when context supports one, then give linked alternatives and one brief
fit note each. When choices are equally natural, say “Natural options” rather
than inventing a winner.

## 4. Phrases for a situation

Group by what the learner needs to do—for example, describing experience,
showing responsibility, discussing next steps, and asking questions—not by
lesson stages or minutes. For a broad situation, eight to twelve distinct links
across three or four groups is usually enough.

An imminent event with no stated level uses a disclosed B2–C1 working range
immediately. Offer to adjust easier or harder at the end.

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
interactive quiz presents one decision and waits for the learner's answer.

## Release regression example

This is a format and quality example for:

```text
Give me 5 useful B2 English idioms for today. Group them by what they help me
express and give me a PlayPhrase.me link for each one.
```

A good response starts immediately with five useful choices and five links. It
does not discuss API access, DNS, Python, tools, or fallback mechanics:

### Responsibility

- **[🎬 Hear “With great power comes great responsibility.” in movie and TV dialogue on PlayPhrase.me →](https://www.playphrase.me/#/search?language=en&q=With+great+power+comes+great+responsibility.)** — influence and authority bring obligations.

### Focus and enthusiasm

- **[🎬 Hear “Keep your eye on the prize.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=Keep+your+eye+on+the+prize.)** — stay focused on the goal despite distractions.
- **[🎬 Hear “Like a kid in a candy store.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=Like+a+kid+in+a+candy+store.)** — feel delighted by many exciting choices.

### Commitment and skepticism

- **[🎬 Hear “I wouldn't miss it for the world.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=I+wouldn%27t+miss+it+for+the+world.)** — say you are absolutely determined to attend.
- **[🎬 Hear “That's too good to be true.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=That%27s+too+good+to+be+true.)** — express doubt about an unusually attractive claim.

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

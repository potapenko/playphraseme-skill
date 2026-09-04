# PlayPhrase-first response patterns

Read this reference when the user asks an English question, names a
communication goal, or explicitly requests a lesson, practice, or quiz.

## Default principle

The user came to PlayPhrase.me to see and hear real usage. PlayPhrase.me links
are the primary content of the answer. Explanations organize those links and
help the user choose what to open.

- Put the first useful listening link in the first content block.
- When one choice clearly fits best, feature it before the alternatives.
- For multi-word language the agent chooses, select Common Phrases and link
  every important returned `text` to its own public PlayPhrase.me search. Use
  Common Words for agent-selected individual vocabulary.
- Explain only enough meaning, nuance, or contrast to guide exploration.
- Offer nearby phrases when they add a useful choice or progression.
- End a substantial answer with one or two new exploration paths when useful.
- Do not add exercises or lesson scaffolding unless practice is explicit.
- When the requested material and links are complete, do not narrate scripts,
  API calls, DNS, browser availability, or tools that were not needed. Mention a
  limitation only when it prevented requested content or the user asked for
  diagnostics.

For an open-ended multi-item phrase or vocabulary selection, resolve the
learner's level with [learning query planning](learning-query-planning.md)
before choosing material. When generic discovery requires clarification, the
one short level question is the whole turn; the link-first rules begin after
the learner answers. A concrete imminent real-world situation with no reliable
level signal instead uses the disclosed B2–C1 working range defined there and
returns the linked material in the current turn.

Choose the single closest response pattern below. Combine patterns only when
the request genuinely contains separate questions.

The default size ranges below are guidance, not quotas. Stop when another item
would add length without a useful new choice or contrast.

For multi-phrase answers, organize the choices as a phrase path along one clear
dimension: situation, meaning, intensity, formality, naturalness, or grammar.
The path—not a worksheet built around it—is the finished response.

## Make links worth opening

Treat each link as an entry point into the product, not as a citation appended
to generic teaching content. A useful label combines an action, the exact
searchable phrase, and the listening payoff. For example:

`**[🎬 Hear “I couldn't have said it better myself.” in movie and TV dialogue on PlayPhrase.me →](builder output)**`

Use one visually primary link when the answer has a best fit, and spell the
brand `PlayPhrase.me` exactly in that link. Keep supporting links compact, but
do not default to repeated labels such as `PlayPhrase.me`, `link`, or `click
here`: they name the destination without explaining why it is worth opening.
In a list, the whole phrase-and-purpose line may be the link.

Curate for discovery value:

- use Common Phrases as the source for agent-selected multi-word examples,
  alternatives, paths, and gold responses;
- preserve each returned `items[].text` exactly in the display and Classic
  Search query, including a useful incomplete frame;
- never shorten, complete, or rewrite that text to make it look more polished;
  for example, keep a returned `Unfortunately, I won't be able to.` instead of
  inventing an object such as `...attend the meeting`;
- prefer immediately reusable conversational chunks;
- make every core choice independently perform the user's communication goal;
  setup language may support the path but must not replace a core choice;
- choose meaningfully different options rather than near-duplicates;
- favor language whose delivery, context, or contrast becomes clearer across
  several movie and TV scenes;
- when it genuinely helps, include one memorable colloquial option alongside
  safer neutral choices; and
- never add or remove ellipses, slots, punctuation, or other characters in a
  returned Common Phrase; its displayed text and search query stay identical.
  Nonliteral search syntax around direct user-supplied text is a separate case.

Order choices by usefulness or along one explicit phrase-path dimension. More
links are valuable only when each opens a distinct linguistic choice. Never add
padding to hit a count.

If the user requests an ordered path but its best fit belongs in the middle,
feature that phrase once as the hero before the path, then preserve the requested
order. Repeating the same destination inside the path is optional and does not
count as another exploration link.

After a completed non-practice answer, one optional final Reels link may replace
one of the normal exploration links when the selected material shares one public
Common Phrases catalog scope. Use the same supported public filters and frame it
as continued listening, not a task. Do not create a Reels footer for an arbitrary
set, API-only filters, a clarification turn, a waiting quiz, a direct/link-only
answer, an already-Reels request, or a user who asked for no extras.

## 1. Explain one phrase

Use when the user asks what one phrase means or how it is used.

Order:

1. phrase plus a plain-language meaning;
2. one prominent descriptive link such as
   `🎬 Hear “I couldn't have said it better myself.” in movie and TV dialogue on PlayPhrase.me →`;
3. a short nuance or register note;
4. one brief context note; and
5. one or two linked nearby Common Phrases only when they clarify it.

The user's named phrase may go directly to Classic Search. Do not invent an
additional dialogue line and present it as PlayPhrase.me material.

## 2. Compare expressions

Use for “what is the difference?” requests.

Compare every expression the user named. For an open-ended comparison, choose
three to five clearly distinct Common Phrases and preserve their returned text.

Lead with compact linked rows or bullets. Make each exact phrase part of a
benefit-specific link, followed by one useful distinction. Use a table only
when its side-by-side alignment materially improves the comparison; do not
bury identical link labels in a narrow third column.

Follow with a short same-situation contrast showing how the meaning changes.
Avoid a general lecture before the linked comparison.

## 3. Say an idea naturally

Use for “How do I say X?” and textbook-to-natural-English requests.

Offer three to five Common Phrase options when the user does not specify a
count. Preserve every returned text. When the user's context supports a best
fit, lead with `Best fit`, one visually prominent phrase link, and a one-sentence
reason. Then show the alternatives. When several answers are equally natural,
lead with `Natural options` instead of inventing a winner.

For each option show:

1. the formulation and a compact PlayPhrase.me link;
2. one sentence explaining when it fits.

Keep the recommendation and alternatives in the same response block so the
primary link is easy to compare with nearby choices.

## 4. Phrases for a situation or topic

Use for interviews, travel, dating, meetings, and implicit needs such as “I
have an interview tomorrow.” Group the answer by what the user needs to do, not
by generic lesson stages or minutes.

Use [learning query planning](learning-query-planning.md) to resolve level and
turn the situation into one or more bounded candidate sets. When a relevant
supported topic or CEFR filter exists, first try Common Phrases. Use each
selected phrase's text to build its own public search link.

When the user names an imminent real-world event and gives no level signal, say
briefly that the selection uses B2–C1 as a practical working range, then provide
the phrase path immediately. Do not present that range as a diagnosis of the
learner. A final offer to make the choices easier or harder is enough; do not
turn the exception into another intake flow.

For example, an interview path might use groups such as:

- talking about experience;
- showing responsibility or leadership;
- explaining what you want next; and
- asking the interviewer questions.

Within each group, list formulations with compact individual PlayPhrase.me
links and one short note only where choices need differentiation. A requested
duration affects how broad the selection is; it does not require timeboxed
sections, warm-ups, or a closing test.

For a broad situation, three or four functional groups with roughly eight to
twelve distinct phrase links usually provide a useful path. Stop earlier when
the situation is narrow, and never fill a group with weak variants.

## 5. Vocabulary or expression discovery

Use for requests such as “Give me ten informal phrases.” Lead with a scannable
table:

| Linked expression | Meaning or nuance |
| --- | --- | --- |
| benefit-specific phrase link | compact explanation |

If useful, explain only the two or three most interesting or easily confused
items in more depth. Do not give every item a paragraph merely to make the
response resemble a lesson.

Follow an explicit count. Otherwise select roughly eight to ten items, favoring
a coherent set over filling the upper end of the range.

Resolve an explicit or remembered level before returning the list. If it is
unknown and materially affects the selection, ask once and wait; do not show a
basic sample list first. Only when the learner explicitly requests an immediate
answer without clarification, use and disclose the C1–C2 fallback. Within the
resolved range, prefer distinctive reusable expressions over safe elementary
reactions. For C1–C2, each core choice needs nonliteral meaning, pragmatic or
register nuance, or a reusable construction beyond transparent beginner
English; frequency alone does not make it a useful recommendation.

Keep the requested unit honest: a Common Words slang result is a word, not
proof that a multi-word expression was selected as slang. Follow
[learning query planning](learning-query-planning.md) for mixed requests such
as a topic plus slang expressions.

## 6. Grammar through real patterns

Use for grammar questions. When the agent chooses illustrative phrases, select
them from Common Phrases with documented tense, aspect, sentence-type, or phrase
filters and keep their text unchanged. A grammar pattern named by the user may
instead go directly to Grammar Search. Put the PlayPhrase.me material before the
extended rule:

| Linked pattern | Meaning |
| --- | --- | --- |
| benefit-specific pattern link | compact distinction |

Then give the shortest rule needed to distinguish the patterns. Prefer several
characteristic Common Phrases over a long grammar chapter followed by
“additional resources.”

When the user did not name the forms to compare, choose roughly three to six
patterns that expose the useful distinction without becoming a grammar catalog.

## 7. Explicit practice or quiz

Use only when the user clearly asks to practise, be quizzed, or receive an
exercise. The word “lesson” alone is not enough.

Make the task depend on linked Common Phrase choices. For example, give three
returned formulations for different degrees of responsibility and ask
which one matches the learner's real role. Avoid generic gap-fill, matching,
comprehension, shadowing, role-play, or recall tasks that work equally well
without PlayPhrase.me.

For an interactive quiz, present one decision and wait for the answer before
feedback or the next item. If a standalone worksheet is explicitly requested,
keep its tasks phrase-choice-based and place answers at the end.

## Gold-standard mini responses

These examples demonstrate presentation and link hierarchy, not fixed phrase
choices. Every literal linked phrase below was returned by the production
Common Phrases API on 2026-09-04 with `count >= 5`; counts are omitted because
the corpus changes. Rebuild every destination from the exact returned text for
the user's actual selection and language.

### One phrase

**I couldn't have said it better myself.** means “I completely agree with how
you expressed that.”<br>
**[🎬 Hear “I couldn't have said it better myself.” in movie and TV dialogue on PlayPhrase.me →](https://www.playphrase.me/#/search?language=en&q=I+couldn%27t+have+said+it+better+myself.)**

It is a warm, emphatic way to praise both the point and its wording.

### Natural wording with a best fit

For promising a coworker useful follow-up:

**Best fit for ongoing updates**<br>
**[🎬 Hear “I'll keep you in the loop.” in movie and TV dialogue on PlayPhrase.me →](https://www.playphrase.me/#/search?language=en&q=I%27ll+keep+you+in+the+loop.)**<br>
Use it when you will continue sharing new information.

Other precise promises:

- [🎬 Hear “I'll get back to you ASAP.” — promise a quick answer →](https://www.playphrase.me/#/search?language=en&q=I%27ll+get+back+to+you+ASAP.)
- [🎬 Hear “Yeah, I'll get right on it.” — promise immediate action →](https://www.playphrase.me/#/search?language=en&q=Yeah%2C+I%27ll+get+right+on+it.)

### Situational phrase path

#### From a first meeting to follow-up

- **[🎬 Hear “Thank you for agreeing to meet with me.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=Thank+you+for+agreeing+to+meet+with+me.)** — open appreciatively.
- **[🎬 Hear “I think we can work something out.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=I+think+we+can+work+something+out.)** — signal a workable agreement.
- **[🎬 Hear “I look forward to working with you.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=I+look+forward+to+working+with+you.)** — close with future-facing warmth.
- **[🎬 Hear “It's been a pleasure working with you.” in real dialogue →](https://www.playphrase.me/#/search?language=en&q=It%27s+been+a+pleasure+working+with+you.)** — close an established collaboration.

[Keep listening: swipe through B1 work phrases in PlayPhrase.me Reels →](https://www.playphrase.me/#/reels/en?source=common-phrases&filters=%7B%22language-level-from%22%3A%22B1%22%2C%22language-level-to%22%3A%22B1%22%2C%22topic%22%3A%22work%22%7D)

## Link and evidence rules

For a single-phrase response, prefer a large benefit-specific link. For tables
and longer lists, link the phrase or use a compact action label that still says
what the user will hear. A completed multi-phrase answer may end with one or two
adjacent-expression or filtered-catalog links only when they open a new path.
Link text may vary, but each destination must be exact URL-builder output when
the builder is available, with no tracking parameters.

A selected Common Phrase gets its own public search URL rather than only a link
to an undifferentiated catalog. Use its exact API item `text`; use exact `word`
for a Common Word, and never use a record `id` in the URL.

A documented API filter may support a catalog-level statement such as “returned
by the sarcastic Common Phrases filter.” It does not prove that any particular
clip is delivered sarcastically. Do not claim a clip's tone, stress, speaker, or
source unless the public page was inspected and showed it. Without browser
evidence, keep catalog classification separate from clip-level claims.

Without the Learning API, do not present model-written replacements as Common
Phrases. Offer a supported public catalog or Reels destination, or search exact
text the user supplied. Without a browser, avoid clip-specific claims. Without
script execution, reproduce only the documented public URL contract. Never use
private endpoints, fabricate movie/TV evidence, or describe guest-visible
results as the full corpus.

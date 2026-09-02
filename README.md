# PlayPhrase.me for AI agents

Find a word or phrase in real movie and TV dialogue. The skill gives your AI
agent a focused way to search PlayPhrase.me, explain what it found, and share a
link you can open yourself.

Try asking:

> Find how people say “break a leg” in movies.

> Show exact matches for “I love you.”

> Find American-English verbs and open one as Reels.

## Install

### Codex

Paste this into Codex:

```text
$skill-installer Install the playphraseme skill from
https://github.com/potapenko/playphraseme-language-learning-skill/tree/master/skills/playphraseme
```

Then start a new session if needed and ask:

```text
$playphraseme Find natural examples of “piece of cake.”
```

### Claude Code

Copy the `skills/playphraseme` folder to:

```text
~/.claude/skills/playphraseme
```

Start a new session if needed, then use `/playphraseme` in your request.

<details>
<summary>Install with another Agent Skills client</summary>

Give the client this prompt:

```text
Install the Agent Skill from
https://github.com/potapenko/playphraseme-language-learning-skill/tree/master/skills/playphraseme.

Use the personal skills directory supported by this client. Download or clone
the repository into a temporary directory, inspect SKILL.md and the bundled
scripts without executing them, then copy only the playphraseme folder. Validate
SKILL.md against the Agent Skills specification and report the installed path
and invocation syntax. If this client does not support Agent Skills, explain
that instead of making a system-wide installation.
```

Installation paths and invocation syntax vary by client. The skill uses the
open [Agent Skills format](https://agentskills.io/).

</details>

## Use it

Ask normally. The skill chooses the appropriate PlayPhrase.me view and returns
a link alongside the result.

- “Find exact movie quotes containing ‘I knew it.’”
- “Show phrases matching ‘take * off.’”
- “Find English examples of this grammar pattern.”
- “Show idioms between B1 and C1.”
- “Find scenes from the 1990s with this phrase.”
- “Find clips whose cast includes Brad Pitt.”
- “Open these results as Reels.”

It can work with ordinary and exact searches, wildcard phrases, English grammar
patterns, curated phrases, vocabulary, Clip Search filters, actors, and Reels.
When live scenes are needed, it opens the public PlayPhrase.me page through the
agent's browser and returns the final shareable URL.

## Try PlayPhrase.me directly

No skill is required to use the site.

1. Open [PlayPhrase.me](https://www.playphrase.me/).
2. Type a word or phrase, such as `break a leg`.
3. Play the examples to hear the phrase in different scenes.

For an exact match, put the phrase in quotation marks. Use `*` between words
when one or more words may appear in the middle.

[Open “break a leg” on PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=break+a+leg)

## What to expect

The skill uses public PlayPhrase.me pages and a small read-only Learning API. It
does not download clips, expose private APIs, export the corpus, or bypass guest,
subscription, safety, or rate limits. Cast matches and probable voice matches
are also kept separate: appearing in a film does not prove who spoke a line.

The production Learning API is still pending deployment. Public search links
already target `www.playphrase.me`; structured Common Phrases and Vocabulary
requests will become available to installed users after that API is deployed.
Localhost is only used by maintainers for integration testing and is never
required for normal installation.

Search text becomes part of a public URL and may be saved in browser history or
shared messages. Do not include secrets or personal data in a search.

## For developers

Implementation details, test commands, API limits, and contribution rules are
in [CONTRIBUTING.md](CONTRIBUTING.md). Behavioral evals are documented in
[evals/README.md](evals/README.md).

The skill is licensed under the [MIT License](LICENSE).

# Learn with PlayPhrase.me and your AI agent

I build [PlayPhrase.me](https://www.playphrase.me/), and lately people have
started asking me the same question: can it be used inside ChatGPT, Codex,
Claude, or another AI agent?

I think that is a good way to use it. An AI agent can explain a grammar rule,
prepare a lesson, or make a quiz. PlayPhrase.me adds something that a written
explanation cannot: examples you can watch and hear in real movie and TV
dialogue.

This repository connects the two. It contains a small **Agent Skill** that
teaches an AI agent how to search PlayPhrase.me, choose the right kind of
search, and give you a link to the examples it found.

## What you can do with it

Install the skill once, then talk to your agent normally. You do not need to
learn special commands or understand how PlayPhrase.me URLs work.

For example, start a new chat and say:

> Let’s learn five natural phrases for disagreeing politely. Explain each
> phrase, find examples from movies or TV, and give me a short quiz at the end.

The agent can structure the lesson, explain the phrases, and use the skill to
find relevant PlayPhrase.me examples. Open the links, listen to the lines, and
return to the chat when you are ready for the next part.

After watching the examples, continue with:

> Quiz me on those phrases. Give me one question at a time, and include a
> PlayPhrase.me link after each answer.

That is only one possible lesson. You can also ask:

> Explain the difference between “I did” and “I have done,” then find examples
> of both forms in real dialogue.

> Help me learn useful English for a job interview. Make a 20-minute lesson
> with explanations, examples, and practice questions.

> Create a four-week study plan for my level. Whenever we learn a new phrase or
> grammar pattern, use PlayPhrase.me to show how it sounds in context.

> Find natural examples of “break a leg,” explain what it means, and then make
> a small fill-in-the-blank exercise.

You decide what you want to study. The agent decides how to organize the
lesson. The PlayPhrase.me skill helps it find the examples.

## What the skill actually does

The skill is not a separate language course and it does not replace your AI
agent. It is a set of instructions, references, and small helper scripts written
for the agent.

It explains:

- which PlayPhrase.me search to use for a word, exact quote, wildcard phrase,
  grammar pattern, actor, genre, year, or other supported filter;
- how to build a correct, shareable PlayPhrase.me link;
- when to open the public site and inspect the visible scenes;
- how to use the small public Learning API for common phrases and vocabulary;
- which limits must be respected.

In other words, you could explain all of this to the agent yourself in every
new chat. The skill keeps those instructions in one reusable place.

## Install the skill

The folder follows the open [Agent Skills format](https://agentskills.io/).
Installation is slightly different in each AI client.

### Codex

Paste this into Codex:

```text
$skill-installer Install the playphraseme skill from
https://github.com/potapenko/playphraseme-language-learning-skill/tree/master/skills/playphraseme
```

If the skill does not appear immediately, start a new session. You can invoke
it explicitly:

```text
$playphraseme Find natural examples of “piece of cake.”
```

You can also ask for a lesson normally. Codex may select the skill itself when
your request needs PlayPhrase.me examples.

### ChatGPT desktop app

Standalone skills are available in the ChatGPT desktop app. Open **Skills** in
the sidebar, download this repository, and add the `skills/playphraseme` folder
as a personal skill using the option available in your Skills screen.

Once installed, select the skill with `@` or ask ChatGPT to use
PlayPhrase.me in your lesson. Skill availability can depend on your account,
workspace settings, and the ChatGPT surface you are using. See the
[official OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills)
for current details.

### Claude Code

Copy the `skills/playphraseme` folder to:

```text
~/.claude/skills/playphraseme
```

Then invoke it with `/playphraseme`, or ask Claude for a lesson that needs
movie or TV examples. If you created the top-level skills directory during the
current session and the skill does not appear, restart Claude Code.

### Another Agent Skills client

If your AI client can install skills from a Git repository, give it this
prompt:

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

The installation path and invocation syntax vary by client. A client that does
not support the Agent Skills format can still use PlayPhrase.me directly.

## Use PlayPhrase.me without the skill

The skill is optional. To search the site yourself:

1. Open [PlayPhrase.me](https://www.playphrase.me/).
2. Enter a word or phrase, such as `break a leg`.
3. Play the examples to hear the phrase in different scenes.

Put a phrase in quotation marks for an exact match. Use `*` between words when
one or more words may appear in the middle.

[Open “break a leg” on PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=break+a+leg)

## What to expect

The skill uses public PlayPhrase.me pages and a small read-only Learning API.
It does not download clips, expose private APIs, export the corpus, or bypass
guest, subscription, safety, or rate limits.

When live scenes are needed, the agent opens the public PlayPhrase.me page in
an available browser and returns the final shareable URL. If it cannot inspect
the page, it can still give you a correctly constructed search link and tell
you what it was unable to verify.

Cast matches and probable voice matches are kept separate: appearing in a film
does not prove who spoke a line.

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

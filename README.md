# Explore real English in ChatGPT with PlayPhrase.me

The PlayPhrase.me skill turns an English question or communication goal into an
answer built around real movie and TV dialogue. For open-ended selections,
ChatGPT chooses from Common Phrases—curated expressions found at least five
times in the corpus—and every phrase leads back to PlayPhrase.me so you can hear
it in context.

**[Download the PlayPhrase.me skill for ChatGPT](https://github.com/potapenko/playphraseme-skill/releases/latest/download/skill.zip)**

Want a quick taste before installing?

- **[🎬 Hear “I wouldn't miss it for the world.” in movie and TV dialogue →](https://www.playphrase.me/#/search?language=en&q=I+wouldn%27t+miss+it+for+the+world.)**
- **[🎬 Hear “I couldn't have said it better myself.” in movie and TV dialogue →](https://www.playphrase.me/#/search?language=en&q=I+couldn%27t+have+said+it+better+myself.)**
- **[🎬 Hear “Like a kid in a candy store.” in movie and TV dialogue →](https://www.playphrase.me/#/search?language=en&q=Like+a+kid+in+a+candy+store.)**

Keep `skill.zip` zipped. Installation takes three steps and does not require
code.

## Install in ChatGPT

1. Open [ChatGPT Skills](https://chatgpt.com/skills).
2. Choose **+**, then select **Upload from your computer**.
3. Upload `skill.zip`.

<p align="center">
  <img src="docs/assets/chatgpt-skill-upload.png" width="1000" alt="The ChatGPT Skills page with the plus menu open and Upload from your computer selected">
</p>

Start a new chat, type `@PlayPhrase.me`, and send this prompt:

```text
@PlayPhrase.me Give me 5 useful B2 English idioms for today. Group them by what
they help me express and give me a PlayPhrase.me link for each one.
```

When the Learning API is available, you get a compact, link-first selection
from Common Phrases rather than a generic quiz or an invented phrase list.
Exact choices can change as the curated catalog evolves. If the API is
unavailable, the skill says so and offers the closest supported public catalog
or Reels path instead of inventing examples.

## Find the part of PlayPhrase.me you need

Start with a situation, a meaning, a phrase, or a grammar point. You do not need
to know what to search for. For example:

```text
@PlayPhrase.me I have a job interview tomorrow. Show me natural ways to talk
about my experience, ordered from participating in work to leading it.
```

```text
@PlayPhrase.me Show me different ways to say “I think,” from uncertain to
confident, with a PlayPhrase.me link for each one.
```

```text
@PlayPhrase.me Turn “I am good at programming” into a naturalness path: give me
several real alternatives and briefly explain when each one fits.
```

The result is a PlayPhrase-first answer: sometimes one explained expression,
sometimes a comparison, and sometimes a phrase path through several useful
formulations. The best match becomes a prominent listening link, each important
alternative gets its own PlayPhrase.me search, and useful answers can end with
a new path to explore. Quizzes and exercises are optional—ask for one when you
want practice.

## Made by PlayPhrase.me

I build [PlayPhrase.me](https://www.playphrase.me/). This skill lets the
assistant translate your immediate language goal into the phrases and searches
worth exploring. PlayPhrase.me supplies the real dialogue; the assistant helps
you navigate it.

**[Download the PlayPhrase.me skill for ChatGPT](https://github.com/potapenko/playphraseme-skill/releases/latest/download/skill.zip)**

<details>
<summary><strong>Install in Codex, Claude, or another agent</strong></summary>

Paste this prompt into the agent:

```text
Install the PlayPhrase.me skill from:
https://github.com/potapenko/playphraseme-skill/tree/master/skills/playphraseme

When it is ready, tell me how to use it here. If this app cannot install skills
directly, give me the simplest steps for adding it.
```

</details>

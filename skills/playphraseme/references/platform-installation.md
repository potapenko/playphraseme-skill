# Platform installation

This folder follows the open Agent Skills format. The host determines where it
loads skills and how explicit invocation is written.

## ChatGPT

1. Download `skill.zip` from the latest GitHub Release:
   <https://github.com/potapenko/playphraseme-skill/releases/latest>
2. Open ChatGPT and select **Plugins**.
3. Open **Skills**, then choose **Create** or the **+** button.
4. Choose **Upload from your computer** and select `skill.zip`.
5. After installation, invoke it explicitly with `@PlayPhrase.me`, or ask a
   relevant language-learning question and allow ChatGPT to select it
   automatically.

Availability can depend on the ChatGPT account and workspace settings. Do not
claim a particular account has been validated until the upload and invocation
have been smoke-tested there.

## Codex

Personal path:

```text
$HOME/.agents/skills/playphraseme
```

Invoke with `$playphraseme`. Codex may detect a new skill immediately; restart
the session if it does not appear.

## Claude Code

Personal and project paths:

```text
~/.claude/skills/playphraseme
.claude/skills/playphraseme
```

Invoke with `/playphraseme`. The core frontmatter uses only portable Agent
Skills fields, without required Claude-specific extensions.

## Prompt-assisted installation

Codex, Claude, and other agents that can install an Agent Skill from a public
repository can use this prompt:

```text
Install the PlayPhrase.me skill from:
https://github.com/potapenko/playphraseme-skill/tree/master/skills/playphraseme

When it is ready, tell me how to use it here. If this app cannot install skills
directly, give me the simplest steps for adding it.
```

Other clients may use the skill if they load standard `SKILL.md` folders. Do
not claim support without checking that client's current documentation and a
fresh installation.

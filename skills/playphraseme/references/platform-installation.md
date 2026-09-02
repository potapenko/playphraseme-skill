# Platform installation

This folder follows the open Agent Skills format. The host determines where it
loads skills and how explicit invocation is written.

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

## ChatGPT and plugins

Standalone skills are documented for the ChatGPT desktop app, Codex CLI, and
the Codex IDE extension. Skills distributed through plugins are available in
Chat and Work across ChatGPT web, desktop, and mobile. Actual client support
must still be smoke-tested before the compatibility table claims validation.

Other clients may use the skill if they load standard `SKILL.md` folders. Do
not claim support without checking that client's current documentation and a
fresh installation.

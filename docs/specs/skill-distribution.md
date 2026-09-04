# Skill distribution

- Status: Active
- Stability: Evolving
- Revision: 1
- Domain: `skill-distribution`
- Authority: user decision approved 2026-09-04

## SD.CHANNELS — Installation channels

The canonical skill source is `skills/playphraseme/`.

Prompt-based installation remains available for Codex, Claude, and other
compatible Agent Skills hosts. A ready-made `skill.zip` is an additional
installation channel for ChatGPT Web and must not replace or weaken the
prompt-based instructions.

## SD.PACKAGE — Upload package

`make package` produces `dist/skill.zip`. The archive contains exactly one
top-level `playphraseme/` skill directory and only files from the canonical
skill source. It excludes repository metadata, tests, caches, temporary files,
and unrelated documentation.

The package is deterministic: unchanged source files produce byte-identical
archives.

## SD.COMPATIBILITY — Host behavior

The skill keeps its bundled standard-library Python helpers. A host may run
them when script execution and any required network access are available.

When script execution or outbound HTTP is unavailable, the skill still
classifies the requested search mode, constructs a public PlayPhrase.me URL
from the documented contract, explains the selected filters, and uses available
browser or web capabilities when appropriate. It never falls back to private
APIs or bypasses product limits.

ChatGPT explicitly invokes the installed skill with `@PlayPhrase.me`. Codex
uses `$playphraseme`; Claude and other hosts retain their own documented
invocation syntax. Platform syntax must not be mixed in shared UI prompts.

## SD.RELEASE — Non-developer installation

GitHub Releases expose a ready-to-download artifact named `skill.zip`.
Repository documentation presents ChatGPT ZIP upload and prompt-based agent
installation as separate supported paths.

## SD.QA — Acceptance scenarios

1. `make check` passes the existing script tests plus package validation.
2. The archive opens successfully, contains one skill, and contains no junk or
   escaping paths.
3. `SKILL.md` has valid minimal frontmatter with `name: playphraseme` and a
   useful trigger description.
4. Every local path referenced by the packaged skill exists inside the archive.
5. A manual ChatGPT Web smoke test uploads `skill.zip`, shows `PlayPhrase.me`,
   supports `@PlayPhrase.me`, and exercises a public PlayPhrase.me URL.

Manual ChatGPT acceptance is reported separately from automated package
validation and is not claimed until it has actually been performed.

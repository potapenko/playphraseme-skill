# Skill distribution

- Status: Active
- Stability: Evolving
- Revision: 4
- Domain: `skill-distribution`
- Authority: user decisions approved 2026-09-04

## SD.CHANNELS — Installation channels

The canonical skill source is `skills/playphraseme/`.

A ready-made `skill.zip` is the primary public installation path for ChatGPT.
The README and other learner-facing material lead with the direct download,
the shortest supported upload flow, and a first `@PlayPhrase.me` prompt.

Prompt-based installation remains available as a secondary path for Codex,
Claude, and other compatible Agent Skills hosts. Making ChatGPT primary must
not remove or weaken that supported path.

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

When the URL builder is available, public link destinations are its unchanged
output with no tracking. Browser-observed redirects may be reported separately.

When script execution or outbound HTTP is unavailable, the skill still
classifies the requested search mode, constructs a public PlayPhrase.me URL
from the documented contract, explains the selected filters, and uses available
browser or web capabilities when appropriate. It never falls back to private
APIs or bypasses product limits.

The production Learning API is deployed; bounded requests still degrade to
canonical public links when the API or outbound HTTP is unavailable.

ChatGPT explicitly invokes the installed skill with `@PlayPhrase.me`. Codex
uses `$playphraseme`; Claude and other hosts retain their own documented
invocation syntax. Platform syntax must not be mixed in shared UI prompts.

## SD.RELEASE — Non-developer installation

GitHub Releases expose a ready-to-download artifact named `skill.zip`.
The primary README call to action links directly to the latest release asset.
Repository documentation presents ChatGPT ZIP upload first and prompt-based
agent installation as a separate supported path later on the page.

## SD.QA — Acceptance scenarios

1. `make check` passes the existing script tests plus package validation.
2. The archive opens successfully, contains one skill, and contains no junk or
   escaping paths.
3. `SKILL.md` has valid minimal frontmatter with `name: playphraseme` and a
   useful trigger description.
4. Every local path referenced by the packaged skill exists inside the archive.
5. A manual ChatGPT smoke test uploads `skill.zip`, shows `PlayPhrase.me`,
   supports `@PlayPhrase.me`, and exercises a public PlayPhrase.me URL.
6. URL validation rejects tracking parameters; repository QA retains the
   production Common Phrases query evidence for literal examples and verifies
   that their displayed text and Classic Search queries remain exact.

Manual ChatGPT acceptance is reported separately from automated package validation and is not claimed until it has actually been performed. The 2026-09-04 test passed: the installed skill handled an explicit mention and returned public PlayPhrase.me links.
Its response screenshot remains historical repository evidence rather than the current README example. The installation screenshot records the ZIP upload entry point.

## SD.DELTA-2 — ChatGPT-first public installation

- Mode: Evolve.
- External authority: user direction on 2026-09-04 to make ZIP installation the main path for the broader ChatGPT audience and optimize the README for fast installation.
- Previous behavior: ZIP upload was documented as an additional channel beside prompt-assisted installation.
- New behavior: learner-facing material leads with ZIP download and ChatGPT; prompt-assisted installation remains supported below it.
- Compatibility: packaging, skill behavior, Codex invocation, Claude invocation, and other compatible Agent Skills hosts are unchanged.

## SD.DELTA-3 — Canonical links and production API status

- Mode: Evolve.
- External authority: user approval on 2026-09-04 following agent feedback.
- Previous behavior: URL-builder use was advisory and documentation still described the production Learning API rollout as pending.
- New behavior: builder output is immutable, tracking is forbidden, and the production API is documented as deployed after a bounded successful smoke.
- Compatibility: documented no-script, no-browser, and no-network fallbacks; public routes; endpoint allowlist; and product-limit boundaries are preserved.

## SD.DELTA-4 — Current Common Phrases README example

- Mode: Evolve.
- External authority: user approval on 2026-09-04 after correcting example provenance.
- New behavior: README taste links and its starter prompt use verified Common Phrases at an explicit level; the stale response screenshot is no longer presented as the current result.
- Compatibility: ZIP installation, historical smoke evidence, packaging, client invocation, and public API/URL boundaries are unchanged.

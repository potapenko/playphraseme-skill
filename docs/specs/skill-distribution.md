# Skill distribution

- Status: Active
- Stability: Evolving
- Revision: 7
- Domain: `skill-distribution`
- Authority: user decisions approved through 2026-09-05

## SD.CHANNELS — Installation channels

The canonical skill source is `skills/playphraseme/`.

A ready-made `skill.zip` is the primary public installation path for ChatGPT.
The README leads with the direct download, the shortest supported upload flow,
and a first `@PlayPhrase.me` prompt.

Prompt-based installation remains available for Codex, Claude, and other
compatible Agent Skills hosts. ChatGPT-first distribution must not remove that
path.

## SD.PACKAGE — Upload package

`make package` produces `dist/skill.zip`. The archive contains exactly one
top-level `playphraseme/` directory and only canonical skill files. It excludes
repository metadata, tests, caches, temporary files, and unrelated docs.

The public skill is instruction-only: the archive contains no executable
scripts or Python files. Script folders are optional in the Agent Skills format
and are not part of this skill's runtime contract.

The package is deterministic: unchanged source files produce byte-identical
archives.

## SD.COMPATIBILITY — Host behavior

The skill describes the public PlayPhrase.me Learning API and frontend URL
contracts in plain language. A host may use any already-available HTTP, web, or
browser capability to make one bounded public Learning API request. It does not
require a particular tool, shell, Python runtime, DNS diagnostic, exit code, or
transport sequence.

Learning API access is an enrichment path, not a prerequisite for an ordinary
learner answer. When a valid response is available, the skill may describe
selected items as Common Phrases and preserves returned text exactly. When the
host cannot obtain a usable response, it still answers the learner's request
with level-appropriate model-selected language and individual public Classic
Search links. It must not describe those fallback choices as API-returned,
Common Phrases, corpus-verified, or filter-matched.

A request explicitly asking for API ranking, Common Phrases membership, or
catalog provenance still requires API evidence. If that evidence is unavailable,
the skill says so briefly and does not fabricate it.

Public frontend links follow the documented route templates, use standard URL
encoding, and contain no tracking parameters. A host may construct them
directly; no bundled URL-builder execution is required. Browser-observed
redirects may be reported separately when useful.

The skill never uses private APIs, credentials, cookies, alternate hidden
endpoints, bulk export, or product-limit bypasses. It does not expose transport
or infrastructure narration in an ordinary learner response.

ChatGPT explicitly invokes the installed skill with `@PlayPhrase.me`. Codex
uses `$playphraseme`; other hosts retain their documented syntax.

## SD.RELEASE — Non-developer installation

GitHub Releases expose a ready-to-download artifact named `skill.zip`. The
README links directly to the latest release asset. Repository documentation
presents ChatGPT ZIP upload first and prompt-assisted installation afterward.

## SD.QA — Acceptance scenarios

1. `make check` passes package, documentation, and behavioral-contract tests.
2. The archive contains one clean skill, no junk or escaping paths, and no
   `.py`, `.pyc`, or executable helper files.
3. `SKILL.md` has valid minimal frontmatter and every packaged local reference
   exists.
4. Documented frontend URLs contain no tracking and decode to the intended
   route state.
5. A fresh manual ChatGPT test uploads the candidate ZIP and invokes
   `@PlayPhrase.me` with the release regression prompt.
6. The regression prompt returns exactly five B2 idioms, grouped by
   communicative purpose, with one Classic Search link per idiom and no generic
   lesson or infrastructure refusal, whether or not the host can fetch the
   Learning API.
7. Common Phrases or API-filter provenance is claimed only when a valid API
   response was actually observed; fallback selections remain useful and
   honestly unlabeled.

Manual ChatGPT acceptance is separate from automated package validation and is
never claimed until performed against the candidate ZIP in the target account.

## SD.DELTA-7 — Instruction-only runtime

- Mode: Evolve.
- External authority: the user's 2026-09-05 direction to remove bundled Python
  scripts after repeated real ChatGPT failures and to require a useful response
  before release.
- Previous behavior: the skill required a bundled Python client, a special
  transport handoff, and validated API data before it could choose phrases;
  transport failure intentionally degraded to one catalog/Reels link.
- New behavior: the public package is instruction-only. The host chooses its
  available public fetch capability, and ordinary learner answers remain useful
  without API access. Provenance claims remain evidence-bound.
- Compatibility: public endpoint and route shapes, filters, level handling,
  exact API text preservation, product limits, private-API prohibitions,
  ChatGPT ZIP installation, and non-ChatGPT installation channels remain
  protected.

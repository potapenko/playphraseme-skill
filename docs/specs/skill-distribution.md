# Skill distribution

- Status: Active
- Stability: Evolving
- Revision: 10
- Domain: `skill-distribution`
- Authority: user API-ONLY-2 clarification, 2026-11-06; unrelated distribution rules preserved
## SD.CHANNELS — Installation channels

The canonical skill source is `skills/playphraseme/`.

A ready-made `skill.zip` is the primary public installation path for ChatGPT. The README leads with the direct download, the shortest supported upload flow, and a short everyday `@PlayPhrase.me` prompt. Show that users can ask in their own language without specifying filters, CEFR codes, or response structure.

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

Exact successful public Learning API rows are required for every offered
learning example, formula and user-quoted practice target. Preserve exact `text`/`word`.
Empty, failed or unavailable API data gives no new examples or example links;
state the limitation or shortfall without model filler. Suitable current API rows
already in context may be reused only with established identity, exact text and
corpus language. Historical examples alone are not current evidence. User-supplied
text remains input, never learning material before exact API verification. Explanations, translations and meaning choices
may be composed without inventing illustrative English sentences.

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
6. With five suitable API rows, the regression returns five grouped B2 idioms
   and exact individual links. Empty/unavailable data returns no new examples;
   insufficient data returns only suitable rows and states the shortfall.
7. Every new study example has API evidence. Grammar, comparison, practice and
   follow-up requests never bypass that requirement or rewrite returned text.
8. Fresh ChatGPT checks cover changed difficulty defaults, concise answers,
   Russian explanation, context-preserving follow-ups, and explicit timed lessons.

Manual ChatGPT acceptance is separate from automated package validation and is
never claimed until performed against the candidate ZIP in the target account.
## SD.DELTA-8 — Easier first use

Evolve, authorized by the user's approval of the UX audit on 2026-09-05.
README first-use prompts become short everyday requests, including Russian;
release QA adds the changed conversation scenarios. ZIP layout, instruction-only
runtime, invocation syntax, public routes, provenance, and installation channels
remain unchanged. Candidate v0.7.0 requires fresh installed-ZIP ChatGPT evidence.

## SD.API-ONLY-1 — Source and installation consistency

Evolve by the user's 2026-11-05 API-only/source-and-installed instruction.
Revision 9 changes the prior fallback contract; package layout, public routes,
host flexibility and release gates remain. Source checks and offline scenarios
do not establish installed-client acceptance. No release is authorized here.

## SD.API-ONLY-2 — All offered examples require API evidence

User clarification, 2026-11-06: formulas, ellipses and user quotes are no exception for learning material; this supersedes any earlier input-based exception. Direct navigation and conceptual discussion remain; public API/privacy boundaries are unchanged.

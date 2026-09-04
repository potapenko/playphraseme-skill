# Skill distribution

- Status: Active
- Stability: Evolving
- Revision: 6
- Domain: `skill-distribution`
- Authority: user decisions approved through 2026-09-05

## SD.CHANNELS — Installation channels

The canonical skill source is `skills/playphraseme/`.

A ready-made `skill.zip` is the primary public installation path for ChatGPT. The README and other learner-facing material lead with the direct download, the shortest supported upload flow, and a first `@PlayPhrase.me` prompt.

Prompt-based installation remains available as a secondary path for Codex, Claude, and other compatible Agent Skills hosts. Making ChatGPT primary must not remove or weaken that supported path.

## SD.PACKAGE — Upload package

`make package` produces `dist/skill.zip`. The archive contains exactly one top-level `playphraseme/` skill directory and only files from the canonical skill source. It excludes repository metadata, tests, caches, temporary files, and unrelated documentation.

The package is deterministic: unchanged source files produce byte-identical archives.

## SD.COMPATIBILITY — Host behavior

The skill keeps its bundled standard-library Python helpers. A host may run them when script execution and any required network access are available.

When the URL builder is available, public link destinations are its unchanged output with no tracking. Browser-observed redirects may be reported separately.

When script execution is unavailable, the skill still classifies the requested search mode, constructs a public PlayPhrase.me URL from the documented contract, explains the selected filters, and uses available browser or web capabilities when appropriate. It never falls back to private APIs or bypasses product limits.

The Learning API client is the primary transport in every host that can execute
the bundled script, including ChatGPT Web and Work. The skill runs the normal
client command in the current turn and never selects a URL-only path from a
product name, user-supplied claim, or remembered failure. Its boolean phrase
selectors accept both presence flags such as `--idiom` and common explicit
forms such as `--idiom true` without changing the resulting request.

Only the client's distinct exit-10 pre-response DNS or code-execution
outbound-policy failure from that current invocation permits one URL-only
handoff. The skill reruns the same command with `--print-url` and gives its
unchanged production URL to at most one separately available direct-fetch web
or browser transport. Generic network exit 6, a failure from an earlier command
or turn, and every failure after an HTTP response never qualify.

The direct fetch remains the same bounded logical candidate query. It has a
10-second timeout, a 1 MiB UTF-8 JSON body maximum, and at most one redirect.
A complete JSON object matching the endpoint response contract is sufficient
when the hosted fetch tool does not expose status or final-URL metadata. If
status is exposed, it must be HTTP 200. If the final URL is exposed, its
production origin, endpoint, and decoded query parameters must remain equivalent
to the printed URL; harmless query ordering or encoding normalization is allowed. No
authentication, cookies, tracking, or alternate headers are intentionally
added. Search snippets, cached or model-written summaries, HTML, truncated
bodies, changed request semantics, and alternate endpoints do not establish
Learning API results.

The direct-fetch handoff is not used after the client reaches a timeout, HTTP
response, rate limit, redirect-policy rejection, oversized response, invalid
JSON, or other service failure. If the eligible handoff is unavailable or
returns no usable complete JSON object, the skill uses the canonical public-link
fallback.

When direct fetch succeeds, the learner receives the normal result without Python, DNS, or browser implementation details. Those details appear only when all supported candidate transports fail or the user asks for diagnostics.

The production Learning API is deployed; bounded requests still degrade to canonical public links when the supported transports for the current request cannot return a validated response.

ChatGPT explicitly invokes the installed skill with `@PlayPhrase.me`. Codex uses `$playphraseme`; Claude and other hosts retain their own documented invocation syntax. Platform syntax must not be mixed in shared UI prompts.

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
7. A validated URL-only Learning API command performs no network access and rejects a loopback handoff; every script-capable host attempts the normal client first, explicit boolean values produce the same query as presence flags, and direct-fetch scenarios require a current exit `10`, preserve request semantics, and retain `429` stopping behavior.

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

## SD.DELTA-5 — Host-specific Learning API transport

- Mode: Evolve.
- External authority: user approval on 2026-09-04 after reviewing published-skill feedback from a ChatGPT host whose Python environment lacked outbound DNS.
- Previous behavior: hosts normally attempted the Python Learning API request, and a positively identified execution-environment DNS failure degraded immediately even when an independent fetch-capable transport was available.
- New behavior: ChatGPT Web/Work uses URL-only generation plus one direct fetch as its primary path and never tries Python networking; Codex and other code hosts retain the normal client and may use the same handoff once after a qualifying current-request failure. Failure still degrades to existing canonical public links.
- Compatibility: endpoint allowlists, anonymous access, request limits, Common Phrases provenance, `429` stopping behavior, public routes, packaging, and hosts without browser or web fetch remain unchanged.

## SD.DELTA-6 — Client-first Learning API transport

- Mode: Evolve.
- External authority: user approval on 2026-09-05 after a real ChatGPT trace showed that the v0.5.0 URL-only profile discarded a valid request when its web tool exposed no status, final URL, or body.
- Previous behavior: ChatGPT Web/Work skipped the working Python client, used `--print-url` as its primary path, and required web-transport metadata that the host did not guarantee.
- New behavior: every script-capable host runs the normal client first; only a current pre-response exit `10` permits one URL handoff, and a complete contract-valid JSON body may be accepted when hosted fetch metadata is hidden. The client also tolerates explicit boolean literals used by agents.
- Compatibility: endpoint and origin allowlists, request bounds, Common Phrases provenance, exact returned text, `429` stopping, public-link degradation, URL-builder output, and private-API prohibitions are unchanged.

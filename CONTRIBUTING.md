# Contributing

Contributions should preserve the skill's narrow public contract.

## Before changing behavior

Confirm the current PlayPhrase.me public Learning API and URL contracts. A
single production observation does not silently redefine the skill: record the
URL, date, browser-visible evidence, and proposed contract change.

Do not add:

- PlayPhrase.me APIs outside `/api/v1/learning/**`;
- `/streams/**`, media/CDN internals, tokens, cookies, or auth extraction;
- bulk pagination, rate-limit bypass, or paywall/guest-limit bypass;
- internal, debug, recorder, market, or preview URL parameters;
- a claimed phrasal-verb filter;
- cast or voice language that overstates who spoke a phrase.

## Development checks

The scripts must stay compatible with Python 3.10+ using only the standard
library. Run the complete local check:

```bash
make check
```

This runs the tests, validates the canonical skill, and deterministically builds
`dist/skill.zip`. To build only the upload package, run `make package`.

The package is instruction-only. Python is used for repository validation and
packaging, not by the installed skill. Automated tests check packaging and
scenario definitions; they do not run an LLM or replace installed-client QA.
Follow `skills/playphraseme/references/maintenance.md` for live checks and gold
example changes. Public API checks are bounded and only needed when the API
contract or a documented literal example changes.

## Pull requests

Describe the affected mode, tests run, compatibility impact, and any live check
that remains pending. Keep changes to the core portable. Vendor-specific
metadata must remain optional and must not introduce required nonstandard
frontmatter fields.

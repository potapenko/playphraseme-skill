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

The underlying script checks remain:

```bash
python3 -m py_compile \
  skills/playphraseme/scripts/playphrase_url.py \
  skills/playphraseme/scripts/playphrase_learning.py

python3 -m unittest discover -s tests -v
```

Validate `skills/playphraseme/SKILL.md` with `skills-ref validate` when the
reference validator is available. Also run any client-specific validator used
by the release target.

Offline tests must not contact PlayPhrase.me. HTTP behavior uses a loopback
stub. Live production smoke tests are opt-in, bounded, and reserved for reviews
of deployment status or production compatibility. Local integration may pass
the explicit loopback base:

```text
http://localhost:3000/api/v1/learning
```

Do not fix assertions to exact result counts; corpus data changes.

## Pull requests

Describe the affected mode, tests run, compatibility impact, and any live check
that remains pending. Keep changes to the core portable. Vendor-specific
metadata must remain optional and must not introduce required nonstandard
frontmatter fields.

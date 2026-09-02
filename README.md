# PlayPhrase.me Agent Skill

Ask an AI agent:

- “Find how people say ‘break a leg’ in movies.”
- “Show exact matches for ‘I love you’ and give me a shareable link.”
- “Find American-English verbs, then open one as Reels.”

The `playphraseme` skill finds small language-learning sets through the bounded
public PlayPhrase.me Learning API, builds public PlayPhrase.me URLs, and uses a
host browser when live scenes or source details are needed.

## Install with an agent

Copy this prompt into an agent that supports Agent Skills:

```text
Install the Agent Skill from
https://github.com/potapenko/playphraseme-language-learning-skill/tree/master/skills/playphraseme.

First determine which skill directory this agent supports. Download or clone
the repository into a temporary directory, inspect SKILL.md and the bundled
scripts without executing them, then copy only the playphraseme skill folder
into the appropriate personal skills directory. Validate SKILL.md against the
Agent Skills specification, make no changes outside that skill directory, and
report the installed path and how to invoke it. If this client does not support
Agent Skills, do not improvise a system-wide installation; explain the closest
supported manual option.
```

Do not install downloaded scripts with `curl | sh`, `sudo`, or writes to broad
system directories.

### Codex

```text
$skill-installer Install the playphraseme skill from
https://github.com/potapenko/playphraseme-language-learning-skill/tree/master/skills/playphraseme
```

Manual personal path: `$HOME/.agents/skills/playphraseme`. Invoke it as
`$playphraseme`.

### Claude Code

Personal path: `~/.claude/skills/playphraseme`.

Project path: `.claude/skills/playphraseme`.

Invoke it as `/playphraseme`.

Start a new session if the current client does not discover a newly installed
skill.

## What it can do

- Suggest Common Phrases and return small filtered Common Phrase or Vocabulary
  sets.
- Build Classic Search URLs for ordinary, exact, wildcard, and English grammar
  queries.
- Build catalog, Clip Search, actor, and Reels URLs with documented public
  state.
- Distinguish legacy actor scope, source cast metadata, and probabilistic
  phrase-level voice detection.
- Open public results with whatever browser capability the host agent provides.
- Return the final public URL even when live extraction is unavailable.

The skill does not expose the complete phrase-search API, download clips, use
private endpoints, scrape internal services, or bypass guest, subscription,
content-safety, or rate limits. There is no dedicated phrasal-verb filter.

## Bundled command-line tools

The scripts require Python 3.10+ and use the standard library only.

```bash
python3 skills/playphraseme/scripts/playphrase_url.py search \
  --query "I love you" --exact

python3 skills/playphraseme/scripts/playphrase_url.py clip-search \
  --query "break a leg" --filter year=1990..1999

python3 skills/playphraseme/scripts/playphrase_learning.py suggestions \
  --query "break a leg" --language en
```

The published Learning API target is:

```text
https://www.playphrase.me/api/v1/learning
```

It is pending production deployment. Current integration smoke tests must use:

```bash
python3 skills/playphraseme/scripts/playphrase_learning.py suggestions \
  --query "break a leg" \
  --base-url http://localhost:3000/api/v1/learning
```

Only these anonymous GET endpoints are permitted:

- `/api/v1/learning/common-phrases/suggestions`
- `/api/v1/learning/common-phrases`
- `/api/v1/learning/common-words`

The client makes one bounded logical API operation per invocation, does not
send credentials, does not retry automatically, and does not page toward a
bulk export. One same-origin redirect inside the Learning API prefix is allowed
and bounded.

## Compatibility

Last documentation check: **2026-09-02**.

| Client | Format status | Validation status |
| --- | --- | --- |
| Agent Skills standard | Compatible | Local and reference validation required per release |
| Codex CLI / IDE | Standalone skills documented | Fresh-install smoke pending |
| ChatGPT desktop | Standalone skills documented | Fresh-install smoke pending |
| Claude Code | Standard skills and local paths documented | Fresh-install smoke pending |
| ChatGPT Chat/Work web and mobile | Skills via plugins | Plugin packaging is a later milestone |
| Production Learning API | Contracted target | Pending deployment |

Other agents may load the folder if they implement the open Agent Skills
standard. Installation paths and invocation syntax remain client-specific.

## Privacy, security, and rights

Search text becomes part of a public URL and may be saved in browser history,
logs, or shared messages. Do not put secrets or personal data in a query.

Inspect `SKILL.md` and both Python scripts before installation or execution.
The API client rejects arbitrary remote origins, credentials in URLs,
cross-origin redirects, oversized responses, and non-Learning API paths.

PlayPhrase.me results and media remain subject to the site's terms and rights.
This repository provides a workflow and public links; it does not redistribute
the media corpus.

## Development

Run the offline suite:

```bash
python3 -m unittest discover -s tests -v
```

Behavioral eval definitions live in [`evals/cases.json`](evals/cases.json).
Live API tests are intentionally separate from the offline suite.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before changing API or URL behavior.

## License

MIT. See [`LICENSE`](LICENSE).

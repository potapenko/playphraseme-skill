# LM-SKILL — listening streams and optional conversation

## Authority and scope

Execution mode: single-agent in this chat; no nested agents or model sessions.
User-authorized finite packet from Learn chat `01a0e76f-102f-7c00-a847-3cc85fbe45e9`
on 2026-09-28 explicitly says to execute now, save a local plan, check, checkpoint
and push. Its external authority is the user's approved article campaign and
LM-SKILL section of `playphraseme-landings/content/ARTICLE_REWRITE_PLAN.md`, read
only. This plan records that instruction; it does not create additional authority.
Current branch: `master`, initially clean, two existing commits ahead of origin.
Do not change branches, create worktrees, modify Learn/landing, install a skill,
publish a release, change API/backend, or launch further agents.

## Spec Basis and traversal receipt

Mode: Evolve within response experience and learning-material selection, with
reconciliation of the stale Suggestions response description.
Read AGENTS → implementation governance → product-truth core@1 / routing@3 /
change@1 / evidence@1 / delivery@1 → docs/specs/README.md → lesson-experience r8
→ learning-material-selection r7 → skill-distribution r8 (compatibility
dependency), plus candidate v0.7.0 and released v0.6.0. QA and Computer Use routes
were read; coordination@2 applies to the finite receipt to the originating chat.
Closure comprises these three domain contracts and two release records.
Excluded sibling: landing-page and older releases; no landing implementation work.
Supporting resources: canonical SKILL.md, response/query/API/URL/search/maintenance
references, CONTRIBUTING, eval definitions and package/eval tests. This is the
complete bounded response/selection/package context; no backend source needed.

Contract requirements: compact ordinary answers, exact catalog text, explicit
level/count authority, bounded public GETs, honest fallback, opt-in practice,
context limited to the available conversation, no private APIs.
User-authorized delta: streams without per-clip work; word → useful combinations
→ links; explicit-only speaking with a portable context; no numerical exam,
mastery inference, durable memory or unproved Voice compatibility.
Implementation choice: a conditional listening-and-speaking reference, linked
from the existing router, keeps the ordinary response instructions short.

## Reconciled evidence and dispositions

- Production [Suggestions GET](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?q=decision&language=en&limit=6) returned
  `count` and `language-level`: five B1 rows and one B2 row. The blanket claim
  that count is absent is a specification/reference omission; document optional
  record metadata, not CEFR request filters.
- [Suggestions for barely](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?q=barely&language=en&limit=6) returned two relevant B1 records
  and four records without the word. A suggestion is not an exact-word match
  or proof of requested-level filtering. Preserve the literal selected text.
- Common Words B2 requests (limit 20, with and without adverb selection) did not
  return barely in their bounded first page. Do not fabricate an API selection
  or paginate to force the campaign example.
- A read-only Safari observation displayed Barely [B2] and Common collocations
  `barely enough` (118), `barely noticeable` (11), `barely able` (63).
  These are public Vocabulary UI evidence, not Common Phrases API records.
  Continuous playback was reported by the originating method check; this chat
  has not independently replayed it.
- Official Voice documentation was opened at
  https://learn.chatgpt.com/docs/features/voice on 2026-09-28. It describes
  supported desktop voice conversations, account-dependent availability and
  task context; it does not establish installed web-skill/Voice interoperability
  or pronunciation assessment. No such compatibility claim is authorized.
- Safari is reserved by the main chat's method critic. Only a read-only
  getApp observation occurred here; no navigation or input. IAB is not a
  substitute for this repository's Safari-only ChatGPT acceptance rule.

## Task-owned write set and steps

1. This plan; docs/specs/lesson-experience.md (r9) and
   docs/specs/learning-material-selection.md (r8), contract first.
2. skills/playphraseme/SKILL.md; references/response-patterns.md,
   learning-query-planning.md, learning-api.md, maintenance.md, and new
   listening-and-speaking.md under that same canonical skill.
3. evals/cases.json and evals/README.md for requested acceptance scenarios.
4. Validate with make check, skill-creator quick_validate, diff checks and
   focused link decoding. No new test harness or independent model sessions.
5. Record outcomes here, checkpoint only this write set, push current master.
   Build dist/skill.zip as the existing ignored canonical package output.

Protected: package format, released installation channels, ordinary short
questions, requested lessons/quizzes, URL routes, public API request semantics,
language and level routing, provenance and private-data boundaries.

Acceptance: ordinary selection; B2 word/combinations/links; irrelevant or simpler
Suggestions; unavailable/empty API; listen-only; explicit speaking; selected
expressions retained in context; no mastery from clicks. Definition validation
and self-walkthroughs must not be labeled installed-client behavioral acceptance.
Voice audio interaction and fresh installed-ZIP acceptance remain unverified
until performed in the permitted environment. The finite packet explicitly
permits delivering instructions/text handoff with this exact residual.

## Outcome and review handoff

Implementation is ready locally under lesson-experience r9 and selection r8;
distribution r8 is unchanged. The current ZIP contains 11 canonical files.
The new reference carries the optional flow; ordinary response routing remains
compact. This unversioned working ZIP supersedes the local build path only;
the historical v0.7.0 candidate hash and published v0.6.0 record stay unchanged. Source-specific example maintenance separates Vocabulary/UI material
from the existing Common Phrases gold fixture; no gold data was invented.

Local verification: make check passed all 16 tests, package validation and
build. Skill-creator quick_validate passed in a temporary venv (system Python
lacked PyYAML); the venv was removed. Seventeen packaged Markdown references
resolve; five exact-text search queries round-trip correctly. Diff whitespace
check passed. There are 42 scenario definitions, including 11 new ones. These
checks validate packaging, definitions and link construction, not model behavior.

Self-review of requested paths (reasoning against instructions, not independent
or installed-client acceptance): ordinary selection keeps short answers; supplied
barely/B2 and two Vocabulary collocations keep their distinct sources; unrelated
or B1 Suggestions cannot satisfy a strict B2 phrase request; missing fields stay
unknown; empty/unavailable API uses model language without catalog claims;
listen-only ends at links; explicit speaking reuses selected expressions;
Voice gets the copyable context; clicking never establishes mastery.

Example response for the supplied Vocabulary choices:

- [barely enough — слушать на PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=barely+enough) — едва хватает.
- [barely noticeable](https://www.playphrase.me/#/search?language=en&q=barely+noticeable) — едва заметный.

Можно просто слушать поток. Возвращаться к примерам — по желанию.

Portable context on an explicit Voice request:

> Мой уровень английского — B2. Я выбрал barely enough — «едва хватает» и
> barely noticeable — «едва заметный». Поговори со мной по-английски, используя
> эти выражения естественно. Давай конкретные поправки к формулировкам и
> грамматике, показывай естественный вариант и продолжай разговор.
> Без теста и числовых оценок.

After the main chat released Safari, a task-owned new tab opened chatgpt.com.
The authenticated account's Chat composer was observed with Dictate and Send
controls and an existing draft character. No message was sent, draft changed,
installation modified or audio exchange started. The task-owned tab was closed
and the original PlayPhrase.me tab restored; Safari is released. This confirms
account/UI access only. It does not establish Voice availability or unavailability
in other states, installed-skill interoperability or spoken feedback.

Residual: fresh candidate ZIP invocation and all changed conversational outcomes
remain unverified in ChatGPT. The precise Voice step is a real spoken exchange
using the retained expressions (or pasted handoff), followed by actual feedback.
No such audio/runtime evidence exists here. No install, public release, automatic
skill transfer, durable memory or pronunciation-accuracy claim is made.

The main chat reported that both already-authorized critics separately reviewed
the complete diff/contracts/eval definitions and found no material skill defects.
Its coordinator accepted this local result and explicitly requested the scoped
checkpoint/push. Review scope: method fidelity, source/Voice honesty and ordinary
answer preservation. No new reviewers or model sessions were launched here.

Local instruction/package delivery is accepted within the finite packet;
installed-client behavior and Voice remain unverified as detailed above.
Checkpoint/push identity is returned in the final chat receipt; no release is
published. Next runtime action, under separate installation authority: in Safari
through Computer Use, install this exact candidate ZIP and invoke the changed
ordinary/listening/context/speaking cases; then perform an actual Voice exchange
with user audio and concrete feedback. Keep actual model/Voice observations
separate from the 42 definitions. No additional agents are needed.


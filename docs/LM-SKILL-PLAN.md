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

## LM-SKILL-02 — assistant-led learning and spoken repetition

Authority: new explicit author instruction relayed by the main chat on
2026-09-28: «Учебным сценарием управляет ChatGPT». Execute in the same scope;
no installation, release, new agents, branches or storage architecture.
Prior completed checkpoint: 003b46584afa945098b9dde1fe412b385aaac260.
Execution remains single-agent; master started clean and synchronized.

Traversal: current AGENTS → docs/specs/README.md → lesson-experience r9 →
learning-material-selection r8; distribution r8 / SD.COMPATIBILITY and the
previously read governance and released/candidate contracts remain applicable.
Excluded: landing, Learn, API/backend, installation and publication. The complete
selected response/selection contracts and existing implementation were reread.

Final Spec Basis: Evolve LE.ROUTING/LE.SPEAKING plus new LE.STUDY-LIST and
LMS.LEVEL/LMS.CURATION. The prior unknown-level wait and learner-supplied
conversation prompt are observed implementation, not authority against the new
instruction. Guided learning now starts selection immediately; the assistant
provides useful diverse phrase cores, explanations and the practice sequence.
Ordinary individual questions stay short; catalog-only unknown-level discovery
keeps its existing clarification path. Explicit level/count and exact API text
remain protected. Campaign A2 usefulness does not assign global A2, phrase CEFR
or scene level. Earlier barely/B2 examples are historical regression inputs,
not the only campaign example or a required default.

Task-owned write set: this plan; docs/specs/lesson-experience.md (r10) and
learning-material-selection.md (r9); skills/playphraseme/SKILL.md and its
references/listening-and-speaking.md, learning-query-planning.md,
response-patterns.md; evals/cases.json and evals/README.md. Update contracts
first, then instructions and narrow scenario definitions; run make check,
reference/link checks and diff check. No product/API execution code changes.

Study list semantics: offered, explained, known-by-user-report, listened-by-user-
report, spoken attempt with its actual evidence source, and return-to items are
independent facts, not a mastery ladder. No link-to-listening inference, invented
hearing, persistence promise, profile store or score. Keep the report compact in
the current chat; do not append one to every short answer or demand clip reports.
Speaking is opt-in: choose an item from this list, give a phrase/example, wait
for speech, correct a concrete observed issue and invite a retry of that same
item before advancing. No invented situations/questions demanded of the learner.
Honor stop/easier. Text-only checks cannot establish spoken behavior.

Before checkpoint, send the exact current diff scope, contract pins, changed
examples, checks and residuals to the main chat for both existing critics.
Pending: implementation, local checks, two-critic review, scoped checkpoint/push.

### LM-SKILL-02 local outcome ready for review

Pinned result: lesson-experience r10, learning-material-selection r9,
skill-distribution r8 unchanged. Contract first, nine task-owned paths modified.
The conditional reference now owns assistant initiative, independent in-chat
study facts and the spoken correction/repetition loop. The router and query
planner explicitly distinguish guided learning from generic catalog discovery.
Free-conversation preferences remain protected; no forced drill against a
specific request. No API/request/URL behavior or installation changed.

Illustrative model-selected response (not API/CEFR/clip evidence):

- [make a decision — слушать на PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=make+a+decision) — принять решение.
- [change your mind](https://www.playphrase.me/#/search?language=en&q=change+your+mind) — передумать.
- [take your time](https://www.playphrase.me/#/search?language=en&q=take+your+time) — не торопись.

«Начнём с повседневных выражений; сложность можно подстроить.
В нашем списке эти три выражения предложены и объяснены. О прослушивании
и практике пока нет сведений» — no situation/question homework or B2 default.
For the A2 scenario, these are useful teaching choices, not verified A2 records.

Illustrative requested-practice turn: «Произнеси: I made a decision. Я подожду».
For supplied text “I made decision.”: «Нужен артикль a: I made a decision.
Попробуй повторить целиком». This is a grammatical correction to supplied text,
not observed audio or a pronunciation diagnosis. The report can say “supplied
text attempt; return to the article a”; it cannot claim speech or mastery.

Checks: make check passed 16 tests, skill validation and build; 11 packaged
canonical files. Definitions increased from 42 to 51, with earlier Voice/context
expectations adjusted. These are not executed model conversations. Additional
checks passed: 18 packaged references resolve, three new phrase links decode to
exact cores, specification leaves stay within 100 lines, and diff whitespace is
clean. Skill-creator quick_validate passed in a temporary venv, then the venv
was removed.
Actual fresh installed-ZIP, spoken attempt/correction/repeated attempt and Voice
reporting remain unverified. Safari was not acquired or operated for LM-SKILL-02.
Before checkpoint: send this result to both existing critics through the main
chat, apply bounded actionable findings, then checkpoint/push current master.

### LM-SKILL-02 critic repairs (before checkpoint)

The main chat accepted both critics' P2 findings and one P3 synchronization:
(1) a word-learning request must show words/meanings and several distinct
expressions with EACH word, not the earlier flat three-phrase example;
(2) active Voice with available context starts the first phrase immediately,
without an unnecessary transfer or open-Voice prompt;
(3) generic catalog clarification is only for an unknown level.
Final pins advance to lesson-experience r11 and selection r10; distribution r8
is unchanged. These corrections supersede the flat guided-word example above;
it remains a valid direct-expression response only.

Corrected model-selected word-learning example (no API/CEFR/clip claims):

**decision — решение**
- [make a decision — слушать на PlayPhrase.me](https://www.playphrase.me/#/search?language=en&q=make+a+decision) — принять решение.
- [a difficult decision](https://www.playphrase.me/#/search?language=en&q=a+difficult+decision) — трудное решение.

**mind — ум, мысли; смысл зависит от сочетания**
- [change your mind](https://www.playphrase.me/#/search?language=en&q=change+your+mind) — передумать.
- [keep in mind](https://www.playphrase.me/#/search?language=en&q=keep+in+mind) — помнить, иметь в виду.

**time — время**
- [take your time](https://www.playphrase.me/#/search?language=en&q=take+your+time) — не торопись.
- [on time](https://www.playphrase.me/#/search?language=en&q=on+time) — вовремя.

Study summary: these words/expressions were offered and explained here; listening
and attempts remain unknown. Already-active Voice example with this context:
«Произнеси: I made a decision. Я подожду». No handoff or request to reopen Voice.
The same instruction must still wait for an actual attempt, never fabricate one.
The existing three-expression test context now explicitly requests expressions;
new exact regression cases cover word grouping, active Voice and known-level reuse.

Repair owner checks: make check passed 16 tests, package validation/build; six
grouped example links preserve exact cores; 54 scenario definitions are unique;
packaged references resolve; diff check passed. These checks do not establish
actual model/audio behavior. The repair was submitted to both existing critics
for recheck before checkpoint. No UI, installation, release or new agents.

### LM-SKILL-02 accepted local delivery

The main chat reports both critics accepted all three repairs in the actual
LE r11 / LMS r10 diff without new findings, and its coordinator accepted the
instruction/local-check result and authorized scoped checkpoint/push.
This supersedes the pending-review status above. Nine task-owned files only;
current master, no installation/public release or new agents. The final chat
receipt supplies the checkpoint identity and push/clean-tree result.

Runtime acceptance packet: use the generated dist/skill.zip (11 canonical
files) after separate installation authorization, in Safari through Computer Use.
Verify guided word grouping/links/explanations and the independent study-report
facts against actual generated responses. In an already active Voice session
with the list available, verify immediate first phrase, then actual spoken
attempt → concrete correction → retry of the same phrase → attributed report;
verify easier/stop and no fake errors/scores. Separately verify handoff only for
missing context, a different chat or a direct request. No new agents are needed.

Exact residual: fresh installed ZIP and actual spoken attempt → correction →
retry → report have not been tested. The 54 scenario definitions are not
executed model runs; local checks do not establish host/Voice compatibility.

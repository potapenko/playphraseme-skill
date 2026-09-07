# Playphrase.me AI landing
- Status: Active brief; Russian copy pending editorial acceptance
- Stability: Evolving
- Revision: 2
- Domain: `skill-landing`
- Authority: Eugene approved the landing proposal and clarified its standalone
  scope in this conversation on 2026-09-07.
- Requires: `skill-distribution` rev. 8 (`SD.CHANNELS`, `SD.COMPATIBILITY`),
  `lesson-experience` rev. 8 (`LE.ROUTING`, `LE.ACTIVE-LINKS`,
  `LE.CONTINUATION`, `LE.MODES`, `LE.DEGRADATION`),
  `learning-material-selection` rev. 7 (`LMS.CURATION`, `LMS.DEGRADATION`).

## LP.AUDIENCE — Explain the complete experience

The proposed domain is `playphraseme.ai`; registration and deployment are not
part of this editorial step. Address a newcomer who has never used
Playphrase.me. Explain the website, the skill, the handoff between ChatGPT and
the website, installation, and the first useful action on this page.
Learning English is the primary use case. Phrase and clip discovery for
personal interests is a substantive secondary use case.
Reusing Learn's explanations is allowed. Never require a visit to Learn to
understand or start the experience.

## LP.CONTENT — One continuous page

Use five major parts: introduction and first conversation; contextual
follow-ups and two further conversations; phrase/clip discovery and additional
use cases; an optional short practice session; installation and compact FAQ.
Depth comes from distinct examples and useful explanations, not repeated
claims. The three authored conversations are labelled examples, not transcripts
of verified ChatGPT runs. Real screenshots keep their actual provenance.

For authored listening examples, select confirmed Common Phrases through the
public Learning API using the installed Codex skill. Preserve returned text
exactly, including punctuation, in display and query. A composed multi-sentence
answer must not masquerade as one catalog entry. Syntax patterns and fragments
being explained are distinct from catalog entries. An absent Suggestions match
means unconfirmed in that bounded response, not absent from the whole corpus.
Keep the editorial phrase decisions in `website/phrase-review.md`.
Ready-to-copy prompts are the main entry into each scenario. Use fenced text
blocks for fresh requests and clearly labelled contextual follow-ups. Fresh
ChatGPT prompts use the real `@PlayPhrase.me` invocation; preserve that literal
identifier despite the editorial brand spelling. The eventual website adds a
copy control to each prompt. Do not ask newcomers to compose search syntax or
operate filters themselves; the skill supplies destinations. Audio/video
playback still takes place on the website, not silently inside the chat.

Explain meaning, context, tone, level adjustments, listening and opt-in
practice. English phrases remain English; explanations and learner prompts
follow the page locale. Do not claim automatic proficiency assessment, retained
cross-chat learner profiles, pronunciation scoring, guaranteed clip matches,
automatic playlists, media downloads by the skill, or learning outcomes.

## LP.VISUALS — Illustrate the actual handoff

Use Safari for web examples and ChatGPT installation/acceptance. A screenshot
must explain a specific action or result. Native PNG capture and density rules
in the operator's computer-use governance apply; CUA frames are observation
only. Existing repository images may inform the editorial draft but are not
fresh release evidence. Do not expose unrelated tabs or account information.
The landing must retain readable text, working phrase links and meaningful alt
text independently of screenshots. Do not present a mock conversation as an
interactive or live chatbot.

## LP.LOCALES — Shared meaning, ten adaptations

Russian is the semantic source. After text acceptance, adapt into English,
Spanish, German, French, Brazilian Portuguese, Japanese, Simplified Chinese,
Korean and Arabic. One shared composition, one canonical text per locale;
English at `/`, other locales at Learn-compatible prefixes. Arabic uses RTL
with English study material isolated LTR. Ten page locales do not imply ten
languages taught by the English-oriented skill.

## LP.DELIVERY — Current boundary

This step delivers `website/content/ru.md` and `website/visual-brief.md` for
editorial review. Register this contract in `docs/specs/README.md`.
Check copy against the dependency contracts, link encoding, standalone
completeness, example attribution and the de-ai-writing editorial pass.
Save only task changes in a checkpoint on the current `master` branch.
Translations, visual design/build, DNS, hosting and skill release publication
follow their own accepted stages. Preserve the skill source, ZIP, existing
README, release records and Learn repository.

## LP.DELTA-1

Evolve: add a self-contained ChatGPT-first acquisition page with broad
Playphrase.me introduction and personal clip discovery, replacing the earlier
proposal's reliance on Learn for deeper explanations. No existing released
runtime or route changes. Visual layout is not selected in this editorial step.

## LP.DELTA-2
Evolve: Eugene requested installation in Codex and API verification of the
landing examples in this conversation. Replace unconfirmed authored listening
examples with exact returned Common Phrases; keep educational interpretation
separate from membership evidence. Russian semantic revision advances to 2.
Eugene further requested more copyable prompts and a prompt-first flow instead
of instructions to search manually. No skill runtime, release, website
deployment or Learn change is authorized.

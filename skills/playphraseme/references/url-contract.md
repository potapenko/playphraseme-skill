# Public URL contract

Use `scripts/playphrase_url.py` whenever possible. It produces deterministic
UTF-8 URLs with query state after the hash:

```text
https://www.playphrase.me/#/<route>?<query>
```

Quoted text, `&`, `#`, `%`, Unicode, and compact JSON filters are percent
encoded. Empty and default values are omitted. Build commands print the URL to
stdout; `--format json` returns `url`, `mode`, normalized `state`, and
`warnings`. `decode` returns JSON and removes unknown or internal parameters.

## Classic Search

```bash
python3 scripts/playphrase_url.py search --query "thank you"
python3 scripts/playphrase_url.py search --query "i love you" --exact
python3 scripts/playphrase_url.py search --query "hello * world"
python3 scripts/playphrase_url.py search --query "go home" --grammar
```

Grammar is English-only and is normalized to one `gr:` prefix. `pos` is
non-negative and omitted at zero.

## Common Phrases and Vocabulary

```bash
python3 scripts/playphrase_url.py catalog \
  --source common-phrases \
  --filter idiom=true \
  --filter language-level-from=B1 \
  --filter language-level-to=C1

python3 scripts/playphrase_url.py catalog \
  --source common-words \
  --filter domain=American-English \
  --filter part-of-speech=verb
```

Common Phrase fields: `idiom`, `is-question`, `language-level-from`,
`language-level-to`, `emotion`, `polarity`, and `topic`.

Vocabulary fields: CEFR range, `domain`, `part-of-speech`, `is-slang`,
`offensive-filter`, and `sort-by`. Parts of speech are `verb`, `noun`,
`adjective`, and `adverb`. Offensive modes are `exclude`, `include`, and
`only`; Learning API v1 itself always excludes offensive words.

Emotion values:

```text
angry, anxious, assertive, concerned, confident, confused, determined,
embarrassed, empathetic, excited, fearful, friendly, frustrated, happy,
hopeful, nervous, neutral, nostalgic, other, romantic, sad, sarcastic, scared,
serious, skeptical, supportive, surprised, urgent, worried
```

Topic values:

```text
art, business, daily-life, decision-making, education, emergency,
entertainment, family, government, health, healthcare, history, language, law,
legal, life, literature, medical, personal development, personal-development,
personal-reflection, philosophy, politics, problem-solving, relationship,
relationships, religion, sports, transportation, travel, work, other
```

## Clip Search

```bash
python3 scripts/playphrase_url.py clip-search \
  --query "break a leg" \
  --filter year=1990..1999 \
  --filter genre=Comedy \
  --filter director="quentin tarantino"
```

Fields are `year`, `source-kind`, `genre`, `cast-actor`, `voice-detection`,
`director`, `movie-id`, `imdb`, and `serie-imdb`. Arrays can be supplied by
repeating `--filter`. Accepted input aliases are `actor` → `cast-actor` and
`year-range` → `year`; output always uses canonical keys.

`voice-detection` accepts at most one value and is removed with a warning for a
non-English corpus. `movie-id` or `imdb` can coexist in the route with generic
metadata, but the builder warns that the generic filters are ineffective for
an exact source.

## Reels and actor scope

```bash
python3 scripts/playphrase_url.py reels \
  --source custom-search --query "break a leg" --language en

python3 scripts/playphrase_url.py actor --actor-id ACTOR_ID
```

Reels always uses an explicit language route such as `/#/reels/en`. Supported
sources are `common-phrases`, `common-words`, `favorites`, and `custom-search`.
Catalog filters use their catalog-specific schema. Same-language
`translate-direction` is omitted.

Never guess an actor id from a name. Without a public actor id, use Clip Search
cast or voice filters and preserve their distinct meaning.

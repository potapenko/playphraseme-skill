# Behavioral evals

`cases.json` describes behavior, not exact answer wording. Evaluate each prompt
in a fresh session with the `playphraseme` skill installed.

For every case, inspect:

- selected mode and whether a Learning API call was appropriate;
- every requested URL and its decoded semantic state;
- absence of API calls outside `/api/v1/learning/**`;
- API item conversion by `text` or `word`, never record `id`;
- presence and accuracy of the public PlayPhrase.me link;
- exact URL-builder output as the link destination, with no added tracking;
- cast/voice/legacy actor distinctions;
- honest guest, browser, autoplay, rate-limit, and API limitations;
- refusal to invent filters, scrape private endpoints, or bypass limits.

For learner-selected catalog cases, also inspect:

- correct separation of individual words from multi-word phrases;
- explicit CEFR preservation and a briefly disclosed range for inferred levels;
- one short level question for broad continuing personalization, but no blocking
  question for a finite answer that can proceed with a reasonable assumption;
- exact documented filter values and AND semantics across active dimensions;
- no Common Phrases catalog URL containing API-only filters;
- one initial candidate query, with additional sequential queries only for
  distinct groups or one disclosed relaxation of an inferred constraint;
- no silent removal of an explicit constraint, blind pagination, or merging of
  separate catalogs as proof of an unsupported intersection;
- server order preserved when the user requests API ranking, while curated or
  merged presentation is never described as API-ranked; and
- catalog classification kept distinct from claims about a particular clip's
  tone, delivery, speaker, stress, movie, or series.

For response-pattern cases, also inspect:

- correct routing among one-phrase explanation, comparison, natural wording,
  situation/topic, vocabulary discovery, grammar, and explicit practice;
- the first useful PlayPhrase.me link in the first content block and one
  canonical public search link for every important phrase or pattern;
- when context supports a visually primary best-fit link, that link names
  `PlayPhrase.me` exactly and states its listening payoff;
- phrase-link anchors that communicate an action, exact phrase, and listening
  value instead of bare URLs or repeated generic labels;
- filtered-catalog exploration anchors that communicate their topic or filter
  scope and the value of continuing there;
- exact `PlayPhrase.me` spelling in all other visible brand mentions;
- the stable structure specified for that response pattern;
- distinct, immediately useful choices instead of padded near-duplicates;
- core choices that each perform the user's requested communication goal;
- brief selection or contrast guidance instead of a generic lesson shell;
- no more than two closing exploration links, each opening a genuinely new
  adjacent-expression or filtered-catalog path;
- no timeboxed stages, mandatory task per link, quiz, role-play, worksheet, or
  retrieval exercise unless the user explicitly requested practice;
- no source, speaker, tone, stress, or clip claim without browser-visible proof.

When practice is explicitly requested, verify that it asks the learner to
choose among linked real-world formulations for an intended meaning or context.
An interactive quiz waits for the learner before feedback or answer reveal.

Do not require one exact CTA sentence, visual heading, punctuation, or prose
identity. Judge whether the user can tell why each link is worth opening. When
the URL builder is available, compare the link destination byte-for-byte with
builder stdout. Only for the documented no-script fallback, normalize URLs
before semantic comparison so equivalent encodings do not cause false failures.

The negative export case must refuse the bypass while still offering the
bounded public Learning API and public URL/browser workflow.

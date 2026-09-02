# Browser extraction

Open a public URL only when the user wants live scenes, pronunciation, source
metadata, or browser-visible verification. If the user asks only for a link,
return the validated URL without unnecessary extraction.

## Ready signals

These selectors are current hints, not a permanent public API:

| Mode | Ready signal | Visible result hints |
| --- | --- | --- |
| Classic Search | `#search-input` and `.search-result-count` | active subtitle or phrase context |
| Curated/Vocabulary | `.one-common-phrase-container` | catalog rows |
| Clip Search | `[data-testid="clip-search-results-summary"]` or `.clip-search-search-result-count` | `.clip-search-card`, `.clip-search-card-text`, `.clip-search-card-source` |
| Reels | `.reel[data-active="true"]` | `.reel-title` and visible metadata |

Wait for a meaningful loaded state. If a selector is absent, inspect the
accessibility tree or visible text, make one reasonable retry, and then stop.
Do not invent results when dynamic content cannot be read.

After route normalization or redirect, read the browser's actual URL and
return that canonical URL.

Collect at most 10 currently visible results by default:

- phrase or word text;
- source title when visible;
- visible count or total when present;
- mode and applied filters;
- final URL.

Do not infinitely scroll. Do not start video merely to enumerate text. When
pronunciation or audio matters, open one selected result; browser autoplay may
still require a user gesture.

Guest limits, locked previews, sensitive-content placeholders, login, and
paywalls are expected product states. Report them without attempting to bypass
them. A visible guest set is a sample, not a corpus export or exact total.

# Maintenance

Last contract review: 2026-09-04.

Review the skill when the Learning API, public URL state, browser DOM, Agent
Skills specification, or host installation guidance changes.

## Compatibility review

1. Re-read the current public Learning API contract and confirm the exact three
   endpoint paths, parameters, limits, response envelopes, and deployment
   status.
2. Re-check Classic Search, catalog, Clip Search, Reels, actor, and share-link
   contracts. Never infer a new URL field from an internal service parameter.
3. Run all offline tests and Agent Skills validation.
4. Run bounded localhost API smoke tests for development changes and one small
   production smoke when deployment status or production compatibility is under
   review.
5. Fresh-install on each client before changing its matrix status.
6. Update the compatibility date and record any limitation without fixing
   result counts, since corpus contents change.

If production behavior differs from this contract, record the URL, date,
visible state, and browser evidence. Treat that as a reconciliation task; do
not silently teach the skill a private, debug, or one-off runtime behavior.

When updating canonical filters, keep script validation, URL documentation,
unit tests, and behavioral evals aligned. Preserve the boundaries against full
phrase APIs, internal streams, credentials, bulk export, and product-limit
bypass.

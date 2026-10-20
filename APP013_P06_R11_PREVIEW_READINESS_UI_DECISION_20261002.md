# APP-013 / 2B / P06-R11 preview-readiness UI decision

Owner decision: **Alternative 1 approved for local implementation and tests only.** No database read, build, deployment, provider request, message, ceiling increase, browser journey or job action is authorized.

Implementation result: **locally complete and validated.** The HTML-visible reason/deadline projection is implemented in the three approved files. The exact button gate is unchanged. Mock-only50-case mobile/desktop coverage, Safari-specific accepted-code/checked-review proof, full2,486 Jest, lint, build, architecture, syntax and formatting pass. Backend evidence: `evidence/APP-013/p06-r11-preview-readiness-ui-repair-20261002.md`. Release remains separate and unapproved.

## Demonstrated gap

Enabled34 reached the details screen with owner-reported **Code accepted** and checked **I reviewed these details**, but **Preview validated draft** appeared disabled near the 12:15 p.m. runtime deadline. The consumed browser state was cleared at expiry, so its internal `busy`/`pending` values cannot be reconstructed. Exact-source Chromium regression passes 46 cases, and a Safari-specific fictional-data reproduction enables preview after the same two visible prerequisites. No underlying gate defect or Safari incompatibility is reproduced.

The current page states the phone prerequisite but does not tell the customer which exact prerequisite is currently blocking preview, whether a request is still processing, or when the private session expires. This caused an attended run to end without an actionable UI explanation.

## Alternative 1 — recommended local UI repair

Approve a local-only change under APP-013/2B/P06-R11:

1. Add an HTML-visible preview-readiness status next to the button.
2. State exactly one current condition: phone check required, review acknowledgement required, request still processing, prior operation outcome pending, session expired, or ready to preview.
3. Display the private-session expiration time and a clear warning during the final 90 seconds.
4. Keep the button's existing fail-closed conditions unchanged.
5. Add mock-only 390px/1440px browser cases for every status, transition, final-90-second warning and expiry clearing; include a Safari-specific local check of accepted phone plus checked review.
6. Change only `scripts/fixtures/customer-intake-journey.html`, `scripts/fixtures/customer-intake-journey.js`, `scripts/verify-controlled-intake-ui.mjs`, corresponding page expectations if required, and evidence.

Acceptance: a customer can read why preview is disabled and the session deadline; accepted phone plus checked review plus no busy/pending state visibly reports ready and enables preview; all existing refusal, correction, uncertainty, duplicate-click, privacy clearing and no-live-call tests remain unchanged and pass.

Exclusions: no admission or job rule, verification/provider request, resend/retry, address policy, service-area rule, ceiling, allowance, database schema, retention, authentication, deployment, live query or browser journey. No new section or acceptance denominator.

Rollback/disabled state: revert the local UI/status projection. The existing server-owned gates remain authoritative throughout.

## Alternative 2 — retain current UI

Make no source change. Before any future journey, separately approve an exact read-only post-enabled34 balance check and then decide whether another bounded journey is justified. The page would still not explain a transient busy/pending or near-expiry disabled state.

## Decision requested

Approve Alternative 1 for local implementation and tests only, or select Alternative 2. Neither alternative authorizes a database read, build, deployment, provider request, message, ceiling increase, browser journey or job action.

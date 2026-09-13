# P05 — customer flow source card

Backend review reference: b10d922 on existing PR21 feature branch. Full governance consistency, frozen baseline and 21 governance tests passed at closeout. Items 2–4 remain; no release or whole-package completion.

Checkpoint: item 1 implemented and validated; items 2–4 remain. Backend evidence/APP-013/p05-browser-adapter.md. Seven new adapter tests, 2,282 full tests passed (3 skipped); build/lint/architecture/audits and existing database/browser regressions passed. No new controlled browser journey or activation is claimed. P05 active, not review-ready as a whole.

Entry 2026-09-13: owner reviewed P04 and, after documentation-only admin planning, said to proceed. Source backend f0201ac, governance 2ab7cb1; focused remotes fetched, worktrees clean. Existing P05/2B only. No admin implementation, new package, release or live approval.

## Fixed finish line

Existing UI shows correction, exception, restart and truthful created/not-booked states; desktop/mobile connected journey passes. Reuse P04 submitControlled and exact receipt replay, existing CustomerConsentBrowserTransport ingress/privacy/budget controls, structured customer-confirmed address contract, and existing organization/browser database harness. Legacy review-only and operator guards remain unchanged.

## Finite checklist and current bounded patch

1. Strict controlled browser adapter: version-2 submit input through the existing authenticated/bounded submit endpoint, separate optional server-injected controlled port, minimal validated ADMITTED/CORRECTION_REQUIRED/REFUSED/UNCERTAIN response union. Legacy port never receives controlled submissions; absence refuses. This is the current bounded patch, not a new package.
2. Disabled-by-default controlled composition using existing services and reviewed activation interfaces; no implicit live values or credentials.
3. Existing customer UI: explicit structured address confirmation/correction, preserve draft on exception, exact retry identity after uncertainty, truthful created/not-booked result and restart/recovery guidance. No alternate demo.
4. Actual connected desktop/mobile journey and regression evidence, including duplicate/restart/refusal, before P05 review readiness.

Patch 1 files: customer-consent-browser-transport.ts/.spec.ts, narrow controlled result projection helper/spec if needed, backend evidence and boards. Version discriminator is not authority: existing origin/context/session/tenant/size/rate guards run first; server port supplies P04 binding. No browser proof, policy, actor or tenant fields accepted. Validate sanitized correction display fields, never expose provider proof/diagnostics. Unknown/malformed positive response fails closed; response projection never grants payment/booking/dispatch/delivery authority. No persistence or automatic retry at this boundary. Application composition remains absent until item 2; absent port is rollback/disabled state.

Validation for patch 1: positive/refusal/correction/uncertain response cases; extra/invalid/version/address/authority input; missing port; no legacy fallback; malformed/over-authorized/wrong-request responses; privacy projection; existing ingress/session/tenant/raw-body regressions. Run full backend tests, build/lint/architecture, dependency audits, frozen/full governance and 21 regression checks plus whitespace. Browser/database gates remain mandatory for items 2–4, not claimed by an isolated adapter unit test.

Remaining composition/UI source inspection must complete before those edits, with concrete files and browser scenarios recorded here. If actual gaps exceed these four items, report impact before expanding. No P05 completion or timing forecast from this partial patch. P06 retains release, resources, real provider costs/caps/window and live owner acceptance; responsible approver is owner. No scope deviation.

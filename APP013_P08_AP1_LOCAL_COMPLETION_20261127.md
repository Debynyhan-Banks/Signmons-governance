# APP-013 / 3A / P08 — AP1 local completion

AP1 is implemented and locally verified at backend `fef39a05cd7e83b54e74a6774716c2b9ab5a4286`. Owner approval is recorded at governance `5e701c5`, against clarified review `4331307`. This completion record supplements the approved original card and clarification; their historical proposal text and R65 receipts remain unchanged. Verified 2026-11-27T10:49:39.186538+00:00.

## Requirement and implemented result

Section 3A's unchanged exit criterion is same-job owner Sandbox Checkout, an authentic matching signed event, and the application payment gate, including failure/replay protection (`APP013_REMAINING_EXECUTION_CONTRACT.md`, §3A). AP1 advances that same journey by separating its existing authentication and payment boundaries; it is not payment acceptance or a replacement workflow.

The demonstrated missing behavior was identical retained `TOKEN_INTENT / ADAPTER_REFUSED_OR_UNKNOWN` for invalid token claims and runtime refusal, reproduced through the actual child/journal/parent boundary in `APP013_P08_R65_LOCAL_AMBIGUITY_REVIEW_20261127.json`. The approved six files now preserve token issuance at `TOKEN_INTENT`, runtime verification at `RUNTIME_AUTH_INTENT`, and optional existing payment composition at `PAYMENT_HANDOFF_INTENT`. Exactly four existing fixed codes are retained: `TOKEN_CLAIMS_DRIFT`, `TOKEN_TIME`, `AUTH_RUNTIME_REFUSED`, `EXACT_JOB_READBACK`. Native version 2 injects the payment hook; other callers omit it. Only nine current manifest hash values were refreshed transitively. The JSON companion lists all 15 exact file hashes.

## Completed finite checklist and readiness record

| Item / inspected source | Verification and boundary | Owner / result |
| --- | --- | --- |
| Sequence and native child | Actual success plus claims/time/runtime/job failures; exact journal phases/versions; one issue/auth/hook; existing caller without hook preserved | Implementer — PASS, source `fef39a0` |
| Child-to-parent serialization | Two new finite phases accepted; fixed diagnostics survive actual subprocess/journal/parent; unknown/private canaries excluded; no schema expansion | Implementer — PASS |
| Payment handoff and proof | Precondition failure after runtime success records authentication separately; payment remains false. Lost output, timeout, exit, interruption and merge drift retain null proof and AUTH_OUTCOME_UNKNOWN | Implementer — PASS |
| Deadlines, concurrency, recovery | Existing gates, no retry, version drift refusal, independent account/session closeout and synthetic private purge tested; no call-cap changes | Implementer — PASS |
| Configuration/source pins | Existing current and committed validators and `renewal_tree_check` pass; six approved sources/nine derived manifests only; unrelated AGENTS.md preserved | Implementer — PASS |
| Historical evidence | All 12 R65 receipt hashes rechecked unchanged; cleanup does not rewrite historical authentication | Implementer — PASS at 2026-11-27T10:49:39.186538+00:00 |
| Provider/CLI/SQL contract and effective access | Local regression fixtures exercise existing boundaries only. No current live owner/billing/access/API/key/runtime/Stripe qualification made | Respective credential/cloud/database/Stripe custodians — UNKNOWN |
| Connected customer acceptance | Actual same-job Checkout, authentic event, payment gate and product-owner acceptance remain outstanding | Product owner/implementer — NOT DEMONSTRATED |

No credential, provider, sign-in, database fixture, real SQL, browser opening, payment, deployment or new attended operation occurred. Source and request boundaries, resource pins, success predicates, spending/call limits and cleanup reserves are unchanged. Fixed codes describe the local failing check; they do not identify the provider-side cause or reconstruct R65.

## Verification

- `node --test evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.mjs`: 15 passed.
- From that source directory, `python3 -B -m unittest test_bound`: 20 passed.
- From native-entry source, `python3 -B -m unittest test_entry`: all 131 passed (113.251 seconds), including the actual synthetic connected success paths. Localhost permission was used for inert native success fixtures only.
- Existing connected `test_packet`, `test_launcher`, `test_bootstrap_open`, `test_attended_approval`, `test_approval_wait`: all 58 applicable synthetic tests passed. The initial 60-test selection hit sandbox localhost refusal in two browser-opening fixtures before a browser could launch; the corrected selection explicitly excluded `test_production_jxa_dispatches_loopback_and_closes_only_owned_window` and `test_actual_loopback_bridge_and_headless_chrome_handoff`. No test source or acceptance assertion was weakened. Browser QA is outside AP1's local scope.
- Current/committed qualification source guards, locked sources, native source manifest and `renewal_tree_check(fef39a05cd7e83b54e74a6774716c2b9ab5a4286)`: passed.
- Frozen baseline, complete cross-repository consistency, backend governance wrapper, architecture, all 25 governance tests, and both whitespace checks: passed. Post-document frozen-baseline, complete consistency, 25 governance tests, backend wrapper, architecture and whitespace checks also passed.
- Product lint/build, Prisma/database fixtures and browser QA are inapplicable: no application runtime/schema/UI source changed. No old test result is reported as new.

## Handoff and rollback

All approved AP1 implementation, local test, manifest and evidence items are complete. This is local correction only; no live demonstration or owner acceptance is claimed. The next step is a source-bound prerequisite review using these distinctions before proposing any smallest necessary external qualification. No new session is scheduled, and expired/consumed R65 authority cannot be reused. The implementer owns that review; external custodians and the product owner retain their explicit approval boundaries.

Rollback restores the six sources and nine manifests together to backend `4e29a91`; no provider rollback is involved. Accepted 1A/1B/2A/2B remain 4/8, 3A remains OPEN, R1 newly closed remains 0/27. No scope deviation in implementation. Verification selection was corrected before any browser launch; no PostgreSQL fixture ran.

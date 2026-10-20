# APP-013 / 2B / P06-R11 — preview-readiness release proposal

## Decision status

Owner approved **Stage 1 only** for October 2, 2026, 1:15–1:40 p.m. Eastern (17:15–17:40 UTC). Fresh operation `2ef628be-e610-4615-9772-27dad97edcd6` is installed at `/Volumes/Signmons-P06/r11-preview-balance-review-20261002-1315`. Installed byte readback and `R11_BALANCE_HELPER_CHECK_PASSED_NO_ACTION` pass. Start must occur before 1:35 p.m. Eastern. Owner hidden password entry and the one SELECT-only transaction remain; no database connection has occurred.

All later stages remain proposal only. No cloud or provider query, source upload, build, IAM change, image publication, deployment, verification message, browser journey, allowance change or customer/job action is authorized.

Enabled34 and plan `9f849aa4-f4a4-4ebe-b71e-0ffde45d0968` remain consumed and `CLOSED`; they may never be rerun, rebound or used as authority. This proposal separates the next work into stop-gated decisions so an exhausted allowance does not trigger another build or live journey.

## Approved section and acceptance criterion

- Section: APP-013 / 2B / P06-R11, with R12 containment and reconciliation.
- Criterion: one correlated protected phone-verification, eligible-address and reviewed-submit journey creates exactly one job and returns an authoritative receipt; invalid, stale or ineligible input returns a truthful no-job result while preserving recoverable progress.
- Purpose: release the already approved refusal-category repair and preview-readiness/deadline projection as one exact candidate.
- This does not add a section, change the acceptance denominator, alter admission or service-area policy, or award R11 acceptance before a connected result and owner review.

## Exact source and artifact

- Last enabled34 host candidate: `4489a345782969120d9c66ee52b2851cddf94103`, tree `34619d137ef78fab64822294f6b1b0147e484042`.
- Isolated candidate: `/private/tmp/signmons-preview-readiness-release-candidate-20261002`.
- Candidate commit: `37f156f220507ac3bb97e73dc46c9d4dc33db727`.
- Candidate tree: `7c3428d8851dd313b9c28882bf7c33aa703e1e05`.
- Candidate archive: `/private/tmp/signmons-preview-readiness-release-37f156f220507ac3bb97e73dc46c9d4dc33db727.tar.gz`.
- Archive SHA-256: `a60a00e2380cd66c9f1b63e9222223ad7cf2512e687d465a2e1bbae8728e35ee`.
- Archive size: `1,001,073` bytes.
- Proposed image tag, if a later build is approved: `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-preview-a60a00e2380c`.

The new commit changes exactly three approved files from `4489a345` with 105 insertions and four deletions:

- `scripts/fixtures/customer-intake-journey.html`
- `scripts/fixtures/customer-intake-journey.js`
- `scripts/verify-controlled-intake-ui.mjs`

The three files byte-match the owner-approved local repair. Against deployed source `0a857edcc88a6da36dc6669382a74546173e480b`, the cumulative candidate changes nine files: the prior refusal-category runtime/tests, the two bounded coordinator-limit files used for enabled34, and these three preview-readiness files. No unrelated dirty-worktree file is included. The committed archive contains 561 tracked files and excludes repository metadata, dependencies, compiled output, evidence, temporary files, environment files and private input.

## Implemented behavior and boundaries

The page now gives an HTML-visible current preview state: session expired, request processing, prior outcome pending, phone check required, review acknowledgement required or ready. It displays the private-session deadline and warns during the final 90 seconds. The existing fail-closed condition remains exactly `busy || pending || !reviewed || !phoneReady`.

Existing components remain authoritative: controlled-intake runtime configuration, durable verification, address and service-area gates, request identity, reviewed draft, one-job submission, liability readers, bounded database controller, zero-traffic Cloud Run deployment, owner-private credential/code entry and mandatory closeout. The candidate adds no retry, resend, payment, booking, dispatch, appointment, retention, provider-setting or production-traffic authority.

## Current unknown state and hard stop

The exact pre-LOGIN enabled34 baseline was 14 phone holds / USD 7.00 and nine overlapping address operations / USD 0.90. During enabled34 the owner received and accepted one verification code but did not preview or submit. A phone total of 15 / USD 7.50 is therefore plausible, but it is not a confirmed readback. No new address operation or job should be inferred. Current liabilities and runtime state remain unknown.

The previously proposed prospective phone ceiling was 15 / USD 7.50. If a fresh read confirms that ceiling is already reached, stop. Do not build, upload, grant IAM, create a packet, deploy, request another code, reset or release holds, or begin another journey. A later journey would require a separately recorded owner decision for a concrete higher cumulative ceiling, operating allowance and fresh window.

## Stage 1 — smallest next action

The immediate proposed action is one new, exact, SELECT-only database qualification in a future 25-minute Eastern window:

1. Bind a fresh operation identity, fixed account/tenant and approved query projection to the candidate and governance state.
2. Owner enters the database password privately; it is neither displayed nor persisted.
3. Use a read-only transaction to return only current phone hold count/micros, overlapping account/tenant address count/micros, controlled-runtime approval state, database role login/connection limit and active runtime-session count.
4. Roll back and close before writing a result receipt.
5. Do not query customer payload, phone number, address, verification code, prior browser fields or unrelated jobs.
6. Treat early/late invocation, drift, ambiguity, connection failure or a missing receipt as consumed safe stop with no automatic retry.

Observable finish is one exact balance/runtime receipt or a truthful consumed stop. Stage 1 authorizes no write, provider call, build or release action. Its result determines whether release planning may continue or must stop for an explicit ceiling decision.

## Later stages — not yet requested for execution

Only after Stage 1 is reviewed and any required ceiling decision is recorded may a later proposal authorize:

1. Fresh read-only Cloud Run, Artifact Registry and owner-authenticated provider metadata qualification, including unused target suffix `enabled35`, absent test tag, normal traffic 100%, disabled runtime, exact secret versions, approved provider service/settings and approved test recipient.
2. One source-bound Cloud Build with the existing build files and only three temporary grants: source-bucket viewer, Artifact Registry writer and logging writer; remove and read back all three grants on success, failure or uncertainty.
3. Immutable build ID/status, digest and archive/source identity capture.
4. A newly bound checked packet for `enabled35`, zero normal traffic, one owner-attended journey and mandatory closeout.

Enabled34 cannot be reused. A target collision, state drift, ambiguous build submission, failed grant removal or failed qualification stops without silent renaming, rebuild or substitute journey. Exact limits, allowance, Eastern/UTC times and operation identities must be proposed from the Stage 1 receipt before these stages can be approved.

## Validation and evidence

The isolated candidate passed:

- 50 mock-only Chromium cases at 390 and 1440 pixels, with `realProviderCalls: 0` and `actualJobWrites: 0`;
- full Jest: 132 suites passed, one skipped; 2,473 tests passed, three skipped;
- lint, architecture check, JavaScript syntax, Prettier and production build;
- exact three-file byte comparison with the approved repair;
- clean candidate diff and whitespace check.

The first full-suite attempt used a temporary dependency symlink and only the path-isolation security test rejected it. Replacing the symlink with a candidate-local dependency copy made the unchanged suite pass. This was a test-environment correction, not a source change. Browser evidence: `/private/tmp/r11-preview-readiness-release-candidate-ui-20261002/summary.json`. Local repair evidence: backend `evidence/APP-013/p06-r11-preview-readiness-ui-repair-20261002.md`. Candidate preparation evidence: backend `evidence/APP-013/p06-r11-preview-readiness-release-preparation-20261002.md`.

## Owners, rollback and decision requested

- Owner: approve or reject Stage 1 and provide a future 25-minute Eastern window; enter the database password privately.
- Implementer: prepare and validate the exact one-use reader after approval, preserve secrets, interpret the receipt and stop at the recorded boundary.
- Rollback/disabled state: Stage 1 is read-only and ends with rollback/connection close. Existing runtime remains disabled and enabled34 remains closed.
- Excluded: build, IAM, upload, provider access, verification message, browser journey, deployment, production traffic, migration, payment, booking, appointment, customer contact, hold reset/release and a second read after uncertainty.

Stage 1 approval/window are recorded. The owner now runs the installed helper once during the window and reports its fixed terminal status. Later build and journey authority will be presented only after that receipt is reviewed.

P06 remains 12/14; R11 and full R12 remain open; accepted 1A/1B/2A remain 3/8. No scope deviation from the approved local UI repair. The prospective external stages are recorded before implementation and remain unapproved.

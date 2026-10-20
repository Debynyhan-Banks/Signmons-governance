# APP-013 / 2B / P06-R11 — preview-readiness Stage 2 decision

Owner decision: **Alternative 1 approved**, including the proposed ceilings, USD 3.70 operating allowance and approved test-phone availability. The stated start plus the proposal's fixed 75-minute duration is recorded as October 2, 2026, 1:30–2:45 p.m. Eastern (17:30–18:45 UTC). Build phase is 1:30–2:00; attended coordinator support is 2:00–2:45, prospective runtime 2:15–2:30 and mandatory shutdown by 2:45. Preparation does not move these deadlines.

Candidate/build binding is locally checked: commit `37f156f220507ac3bb97e73dc46c9d4dc33db727`, archive SHA-256 `a60a00e2380cd66c9f1b63e9222223ad7cf2512e687d465a2e1bbae8728e35ee`, proposed image `p06-r11-preview-a60a00e2380c`, target `enabled35`. Fresh cloud/provider qualification, one build, grant cleanup, image/packet qualification and owner-private execution remain. No external Stage 2 action has occurred yet.

## Verified Stage 1 result

Read-only operation `2ef628be-e610-4615-9772-27dad97edcd6` completed once at 1:15 p.m. Eastern and returned `PHONE_CEILING_REACHED`. The immutable receipt and all hashed bindings verify:

- phone: 15 retained holds / 7,500,000 micros (USD 7.50);
- overlapping address account and tenant: nine operations / 900,000 micros (USD 0.90) each;
- invalid address rows: zero;
- controlled approvals disabled, runtime role closed and zero runtime sessions;
- read-only transaction, rollback/close before receipt, execution unauthorized and automatic retry false.

This operation and enabled34 are consumed. Do not rerun either. Retained liability is not an invoice statement, refund decision or authorization to release holds.

## Demonstrated decision

The previously proposed phone ceiling of 15 / USD 7.50 is fully reached. A new verification flow cannot be authorized under it. No build should begin until the owner expressly chooses whether to preserve all 15 holds and raise the cumulative ceiling for one final flow.

## Alternative 1 — one source-bound release and attended journey

Recommended only if the owner wants to continue R11 now. Approve the exact candidate already prepared in `APP013_P06_R11_PREVIEW_READINESS_RELEASE_PROPOSAL_20261002.md` and these prospective bounds:

- phone: retain 15 / USD 7.50; permit one new no-resend flow; cumulative stop ceiling 16 / USD 8.00;
- overlapping address account and tenant: retain nine / USD 0.90; permit at most two new operations; cumulative stop ceiling 11 / USD 1.10;
- address session: unchanged two / USD 0.20;
- operating allowance: USD 3.70 total — one build USD 1.00, staging runtime USD 2.00, phone USD 0.50 and address USD 0.20.

The allowance is a stop bound, not an invoice guarantee. All historical holds remain. No resend, automatic retry, replacement request, ceiling reset or second journey.

The owner supplies one future 75-minute Eastern window and confirms access to the approved test phone. The finite sequence is:

1. Recheck candidate commit `37f156f220507ac3bb97e73dc46c9d4dc33db727`, tree `7c3428d8851dd313b9c28882bf7c33aa703e1e05`, archive SHA-256 `a60a00e2380cd66c9f1b63e9222223ad7cf2512e687d465a2e1bbae8728e35ee` and clean manifest.
2. Perform fresh read-only Cloud Run, Artifact Registry and owner-authenticated provider qualification. Require unused `enabled35`, absent test tag, normal traffic 100%, disabled runtime, exact secret versions, approved provider service/settings and approved test recipient. Drift stops.
3. Temporarily grant only source-bucket viewer, Artifact Registry writer and logging writer to the existing build service account. Submit exactly one source-bound build; ambiguous submission consumes the attempt.
4. Remove and read back all three grants on success, failure or uncertainty. Capture build ID/status, immutable image digest and source identity.
5. Bind and validate a fresh one-shot attended packet with exact 15/USD7.50 and nine/USD0.90 pre-LOGIN prerequisites, proposed ceilings, image, unused `enabled35`, fixed window and mandatory closeout.
6. Owner privately enters the database password and phone code, reviews the displayed address/request and submits once. No resend or substitute request.
7. Save one authoritative correlated job receipt or truthful fixed refusal/uncertainty result.
8. Revoke approvals/ceilings, remove the target tag, restore runtime `NOLOGIN`/limit zero/zero sessions, confirm normal traffic 100%, reconcile liabilities and save `CLOSED`.

Any preflight drift, target collision, build uncertainty, failed grant removal, missed cutoff, no-job response, timeout or ambiguous outcome stops without another journey. The normal revision keeps 100% traffic throughout.

## Alternative 2 — pause after the verified read

Keep the tested local candidate and verified Stage 1 receipt. Perform no build, ceiling increase, provider action, deployment or paid verification. Resume later with a newly reviewed window and current-state qualification.

## Decision requested

Alternative 1 is approved for the recorded window. Implementer proceeds only through the finite sequence and stops on any stated drift or uncertainty. Alternative 2 remains the safe fallback if a gate fails.

P06 remains 12/14; R11 and full R12 remain open; accepted 1A/1B/2A remain 3/8. No scope deviation from the approved repairs.

## Execution result — enabled35 consumed and safely closed

The approved release was built once as Cloud Build `5fed9c20-0d5f-46f6-853d-a6fe4aa850fa` (`SUCCESS`), producing image digest `sha256:0fd8185f496861902bef3bfad76e081aec21b0d573b25ab08de6a340d666b70a`; all three temporary build grants were removed and read back absent. Fresh Cloud/provider qualification passed without a provider change or message.

The first private `1950` package stopped before action because six authorization files had an extra schema key; it has no action markers and is consumed. Corrected root `/Volumes/Signmons-P06/r11-supervised-run-20261002-1955`, plan `8f86712b-c5b0-4758-bd63-f9350c8fdbc6`, passed exact-schema checks and executed once. Pre-LOGIN readback matched phone15/USD7.50 and address9/USD0.90. Enabled35 reached `READY_NO_TRAFFIC` with normal traffic100% and target traffic0%.

The owner reported the **Preview validated draft** button disabled and stopped without preview or submit. Exact readiness text was **Preview locked: complete the phone code check and wait for Code accepted. Private session expires at 8:22:22 PM.** The simultaneous phone status was **Code check pending. Enter the code; an incorrect code uses an attempt. No automatic resend.** Exact deployed source maps that status to verification outcome `PENDING`; only `APPROVED` records the verified phone and unlocks Preview. The gate therefore behaved as designed and the journey stopped before phone-code approval. No request reference, terminal admission result or job receipt was produced. Revocation is `REVOKED` at `2026-10-03T00:11:39.664Z` with one matching audit; closeout is `CLOSED` with no failures. Post-closeout readback found the enabled tag absent and normal traffic100%. The operation is consumed and cannot be retried.

The inherited `neondb_owner` administrator password was exposed during owner-private entry. It is omitted here. Fresh metadata confirms it is separate from limited child runtime secret `signmons-staging-p06-child-database-url:2`; do not replace that secret. The administrator exposure requires the coordinated branch/shared-parent-consumer decision in `APP013_P06_R11_EXPOSED_ADMIN_CREDENTIAL_ROTATION_DECISION_20261002.md` before any future live action. Current post-run liabilities remain unknown. This execution provides verified containment, not R11 acceptance. P06 remains 12/14; accepted milestones remain 3/8. No scope deviation implemented.

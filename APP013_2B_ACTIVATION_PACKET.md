# APP-013 / 2B controlled activation packet

## Current P06 entry reconciliation — 2026-09-14 UTC

Owner said "proceed" after the bounded correction repair and the proposed P06 preparation. This authorizes preparation, not deployment or paid execution. Entry sources: backend 3667cda, governance 7be5f00; focused worktrees clean/fetched, backend PR21 open. P01–P05 locally accepted (5/60), walkthrough still 3/8. The historical preparation status below is superseded by this reconciliation; P06 is not complete. No scope deviation.

Read-only Cloud Run readback confirms service signmons-calldesk-staging / us-east5, runtime signmons-calldesk-runtime@signmons.iam.gserviceaccount.com, candidate phone-preflight -> signmons-calldesk-staging-00065-guw, normal traffic 100% signmons-calldesk-staging-app013bounds. Existing candidate image digest sha256:25e194acfd96299bb670de84e63b932d9dc69528e6f421ae42699f80fc9b3d75 is historical, NOT the new source. Six inspected candidate flags are false: DEV_AUTH_ENABLED, SCHEDULING_ENABLED, STRIPE_WEBHOOK_LIVEMODE, SMS_DELIVERY_ENABLED, BACKGROUND_WORKERS_ENABLED, STAGING_PHONE_TEST_ENABLED. Other tags unchanged. No secrets read or resources modified.

### Finite P06 checklist, not additional packages

1. **Entry/packet reconciliation — complete locally:** record actual source, staging readback, completed local evidence and remaining wiring. Google support reply plus approved minimal-record/correction contract removes the stale blanket support-wait gate; no legal certification and no expansion of retained fields. Correction UUID stays in volatile server memory up to five minutes/session expiry, one-use; missing state refuses. P01 durable allowlist remains.
2. **Connected runtime wiring — remaining, implementer:** main.ts currently calls customerSessionHttp() without resources. ControlledIntakeComposition has no production loader. customer-session-http.ts accepts direct socket TLS only; Cloud Run ingress mapping must be qualified, never blindly trust forwarded headers. Browser transport phone/verify routes are fixture-loopback guarded; connected harness pre-provisions phone proof via synthetic SDK before interaction. Reuse DurableVerificationService and the bound Twilio adapter for an explicitly authorized customer phone path, not the old phone-only runner. Before code, complete exact loader/config/ingress/phone interface and negative-test map against these seams. Preserve raw webhook bytes, tenant/session/policy/budget checks, no alternate form, no fixture flag promotion. This is the demonstrated P06 connection gap, not another readiness demo.
3. **Immutable disabled release packet — remaining, implementer prepares / owner approves:** bind source/image, resource names and numeric secret versions, database schema readback, tenant/organization/payment/category approvals, exact config/IAM diff, attribution/notices, managed ingress restrictions and itemized release costs. Current readback does not establish those gates. Re-read tenant/operator state and provider restrictions/rates; no old authorization reuse. Do not deploy until explicit approval of this exact diff; then verify disabled candidate and unchanged traffic.
4. **Capped connected run and closeout — remaining, owner authorizes and accepts / implementer executes:** one new protected session, phone code, eligible owner-confirmed real address, explicit submit and one test job; optional one correction. Proposed 15-minute window and USD0.70 verification envelope below remain proposals, not current spending permission. Privately confirm participant data and exact UTC window at execution. Capture truthful outcome and held liabilities, disable and read back, obtain 2B acceptance before P07/payment work.

Next observable result: a source-complete, default-disabled runtime-wiring card for item 2; then its same-page local phone-to-job proof. No invented config values, secret creation, migration, paid request, image build or deployment in this preparation checkpoint. Current evidence: backend evidence/APP-013/p06-entry-packet.md. Documentation/architecture/frozen/full consistency/21 governance regressions and whitespace checks apply to this docs-only checkpoint; prior 2,301 runtime tests are historical, not rerun here.

Status: **prepared for design review; NOT executable or approved for activation**. Owner authorized preparation after reviewing the bootstrap qualification. Source: backend f59dd78, governance 1cb2adb. Supplements APP013_2B_IMPLEMENTATION_CARD.md and the unchanged frozen five-section walkthrough. No scope deviation; accepted 3/8 (37.5%) unchanged.

## One observable result

One owner-participant, one new protected session, current phone verification and eligible confirmed address, one customer-reviewed draft and exactly one test job automatically created by Signmons after explicit submission and current approved tenant-policy checks. Routine operator approval is not required; separately authenticated operators handle exceptions without bypassing proof. This adopts APP013_2B_AUTOMATIC_ADMISSION_CHANGE.md; it does not activate the path. No payment, appointment, dispatch, customer confirmation message or production customer record. Correction stays in that same journey. An uncertain or expired result stops admission and preserves permitted draft state.

## Exact proposed reuse bindings

| Binding | Proposed value / qualification |
| --- | --- |
| Cloud project / region / service | signmons / us-east5 / signmons-calldesk-staging |
| Runtime identity | signmons-calldesk-runtime@signmons.iam.gserviceaccount.com |
| Candidate origin | https://phone-preflight---signmons-calldesk-staging-p572d6wipq-ul.a.run.app |
| Existing candidate | signmons-calldesk-staging-00065-guw; not the future integrated image |
| Normal traffic baseline | 100% signmons-calldesk-staging-app013bounds; must remain unchanged |
| Tenant proposed for reuse | a1adcfd4-15be-404b-9ac3-5edb1fda20f0; historically SUSPENDED; re-read status/ownership before any activation |
| Separate operator proposed for reuse | staging-phone-owner-20260912; historical disabled/revoked Firebase identity; exact tenant claim, owner role and stagingOnly restriction must be reverified |
| Server customer integration label | Proposed `integration:app013-controlled-intake`; server configuration only, not a provisioned identity or browser claim |
| Twilio Verify service | VA9aee2b6f81cdf797d4af79e939ab04f0, recorded account ending c417; verify exact account ownership and current restrictions before use |
| Google API | Address Validation in project signmons; deployed runtime authorization is not established by the earlier owner's local OAuth tests |
| Participant | Previously willing owner; privately reconfirm destination/address and current notice, never commit either value or OTP |
| Session / conversation | Fresh server-generated identifiers after approved activation; never reuse the closed test session |

Tenant/operator reuse is a proposal for this isolated test, not a claim that old permission covers job admission. The operator identity is for exception/recovery access, not the automatic service actor. Bind that service's exact internal authority and tenant automation policy in the completed card; never reuse a staff token for automatic admission. Existing historical records and all cost holds remain intact. No changes to the Eternity website or production tenant are involved.

## Proposed purpose-bound key references (not created)

Reserve proposed Secret Manager names in project signmons: `signmons-staging-customer-session-key` for CustomerConsentCredentials and `signmons-staging-customer-digest-key` for controlled recipient/proof binding. They are distinct from the old phone-only keys. Existence and collision checks must precede any separately approved creation; never overwrite an existing secret or assume its purpose. Customer session signing uses the existing 32-byte key requirement, with an explicit active key ID and versioned reference; no key material in this packet.

Numeric secret versions, runtime environment field names and exact least-privilege access diff will be bound to the implemented loader before execution review. No `latest` version, project-wide secret access, browser key, service-account key download or shared-key fallback. Do not create these speculative references before the Google retention/design gate closes. Existing encryption storage uses its reviewed key path; these proposed keys do not grant storage permission.

## Proposed bounded execution envelope

- One fresh 15-minute UTC window; literal start/end are intentionally unset until the owner is ready and gates pass. Missing times make the packet invalid, not renewable by an agent.
- One phone START, at most five CHECKs, no automatic resend or alternate channel. Proposed phone liability ceiling USD 0.50, subject to refreshed rates and explicit spending approval; not renewed historical authorization.
- At most two explicit address requests in that session: initial validation and, only if required, one customer-requested correction revalidation. Proposed address liability ceiling USD 0.20 total, subject to rates, approved content handling and explicit spending approval. More corrections preserve the draft and stop; no cap increase or background retry.
- Proposed combined verification liability ceiling USD 0.70 for this packet. This is a proposed application bound, not an invoice/account hard cap; unrelated traffic, build/runtime/storage and taxes are not covered. Separately itemize and approve release costs before deployment.
- Every dispatch reserves durable liability first; timeout, crash or ambiguous result keeps it held. Prior phone and Google holds must neither be subtracted nor reset to make this packet fit.
- Participant proof, exact source account, policy digest, tenant/session/revisions, current time and expiry are checked again at admission. A raw provider success or browser confirmation alone cannot admit a job.

## Release and execution approval checklist

All are mandatory; none is completed by approving preparation.

- [ ] Google or authorized terms review resolves permitted candidate/derived coverage/admission retention with exact fields, lifetime and deletion treatment. No inferred permission from encryption or a boolean.
- [ ] Owner reviews the complete 2B implementation card and proposed tenant/operator/key/ingress design; implementer resolves Google runtime authorization and exact loader interfaces without changing IAM by inference.
- [ ] Implement the existing finite patch map; required backend/UI/integration/security/recovery gates pass with version-matched dependencies. This packet is not a substitute for implementation.
- [ ] Bind immutable source SHA, image digest, numeric secret references, runtime identity, candidate revision, exact config/IAM diff and separately capped release cost. Preserve all normal traffic and existing unrelated tags; no production migration.
- [ ] Owner explicitly approves those configuration/release changes. Read back the disabled deployment and all safety defaults before issuing a session. Do not use old phone-only scripts to activate this flow.
- [ ] Refresh exact provider accounts, US-only/Fraud Guard, rates/caps, participant notice, tenant/operator state and privately held destination. Fill absolute UTC window and bind a canonical packet digest to durable approval.
- [ ] Owner explicitly approves one connected run with that exact packet and allowance. Keep general SMS delivery, scheduling, background workers, dev auth and Stripe live-mode disabled; the old STAGING_PHONE_TEST_ENABLED route stays disabled. Only the separately implemented controlled path can receive temporary authority.
- [ ] Demonstrate the same-session result, obtain owner acceptance, stop and reconcile all observed/unknown liabilities. Record sanitized receipts and actual outcome, not raw provider responses or identity tokens.

## Stop, recovery and closeout

Implementer stops new reservations immediately on owner stop, expiry, policy mismatch, cap exhaustion or ambiguous provider outcome; no auto-retry. An in-flight request cannot be recalled. Disable the controlled approval, close the session, revoke temporary operator credentials, restore tenant/operator inactive state and remove only this packet's temporary grants/mappings after readback. Keep necessary accepted test-job/audit/evidence records under approved retention; do not delete them as routine cleanup. General traffic remains on the baseline revision. Rollback the candidate only under the exact release plan; never remove unrelated tags/resources.

Closeout evidence: packet digest/window, source/image/config references without secrets, allowed request counts, actual provider result categories, current-proof/admission correlation and job count, stop/refusal result, final inactive readback, retained unknown holds and billing-reconciliation owner. Product owner accepts the user-visible result; implementer owns technical evidence/closeout. No claim of zero risk or total provider bill from application ceilings.

## Current stop point

This document prepares the requested configuration proposal. Implementation, release and run checkboxes remain open. The next decision is review of this proposed reuse/key/budget design, with provider retention resolution still required before completing the implementation card. Do not create another demo or new acceptance section while blocked.

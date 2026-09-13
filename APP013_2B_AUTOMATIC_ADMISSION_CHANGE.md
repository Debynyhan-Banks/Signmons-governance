# 2B automatic job admission — explicit acceptance amendment

## Authority and disposition

2026-09-13: owner asked why an authorized operator creates the job, stating that Signmons should create jobs. The assistant proposed automatic job creation when current verification and organization rules pass, human review for exceptions only, and separate payment/booking/dispatch gates. Owner replied “i agree proceed.” This records that actual approval of direction, not approval of text that had not yet been written.

Status: exact old/new text prepared for review before frozen-baseline adoption. Current baseline anchor 57ca1cf0f12ed79075b6afd4781bf28be5e36abc is unchanged. Do not implement this proposal through an unprotected document override. Source inspected: governance 891e673, backend 8a3c737; both origins fetched. Backend PR #21 remains open; no feature merge. Saved dirty repositories are untouched.

## Demonstrated gap and selected alternative

APP013_REMAINING_EXECUTION_CONTRACT.md makes operator admission mandatory. customer-intake-continuation.service.ts exposes an operator-only review/admission path, a PENDING_REVIEW receipt with jobCreated false and requiresHumanReview true. A customer submission does not currently authorize automatic job creation. Simply dropping its role check or pretending a customer is an operator would be unsafe.

Selected: a trusted, tenant-policy-bound Signmons admission path after explicit customer submission of the reviewed draft; reuse the atomic job/link/audit and current-proof checks. Keep authorized owner/admin/dispatcher access for exceptions and recovery, not every successful intake. Rejected: mandatory routine operator approval (contradicts approved experience); removing role checks (creates an authorization gap); allowing AI/browser assertions to bypass verification (untrusted authority).

## Exact protected-text amendment for review

Only the following replacements are proposed. All other frozen criteria, headings, IDs, ordering and accepted evidence remain unchanged. “Reviewed” in the retained 2B heading means customer-reviewed draft, not mandatory employee review.

File: APP013_REMAINING_EXECUTION_CONTRACT.md, section 2B, Finish paragraph.

Old:
> **Finish:** in one protected journey, the owner verifies phone access, confirms an eligible Cuyahoga address, submits the reviewed draft, and the authorized operator admits exactly one job. Invalid/uncertain/stale input preserves progress but cannot create the job. No payment/booking/send authority follows.

New:
> **Finish:** in one protected journey, the customer verifies phone access, confirms an eligible Cuyahoga address and explicitly submits the customer-reviewed draft. Signmons automatically creates exactly one job when trusted current phone/address/coverage evidence, required intake fields and the approved tenant admission policy all pass; routine operator approval is not required. Invalid/uncertain/stale input preserves progress but cannot create the job. Recoverable input requests customer correction; unresolved exceptions are available to an authorized operator without bypassing mandatory verification or policy. Job creation grants no payment, booking, dispatch or send authority.

File: PAYMENT_BOOKING_TEXT_STEEL_THREAD.md, section acceptance cards, 2B Demonstration bullet.

Old:
> - Demonstration: approved phone receives a code, correct code proves access, approved address correction and qualified county evidence produce one eligible job via 2A. Wrong/expired code, edits, out-of-area, boundary ambiguity, source outage and cap exhaustion preserve draft and refuse admission. Bind evidence IDs privately; record actual provider observations without secrets/customer payloads in public evidence.

New:
> - Demonstration: approved phone receives a code, correct code proves access, and approved address correction, qualified county evidence, required intake fields and current approved tenant admission policy let Signmons automatically create exactly one eligible job after explicit customer submission, reusing 2A safeguards without routine operator approval. Wrong/expired code, edits, out-of-area, boundary ambiguity, source outage and cap exhaustion preserve draft and refuse admission; unresolved exceptions are available to an authorized operator, who cannot bypass mandatory verification or policy. Job creation alone authorizes no payment, booking, dispatch or send. Bind evidence IDs privately; record actual provider observations without secrets/customer payloads in public evidence.

No APP-013 notification acceptance criterion changes. No replacement or reset of accepted 2A evidence: automatic execution is new 2B evidence, not a retrospective claim about 2A.

## Implementation boundaries after adoption

1. Server authenticates the existing customer session and resolves tenant/current organization policy; the browser cannot choose the service actor, tenant, VERIFIED state or permission. Missing/revoked automation policy fails closed. Use a distinct trusted service authority; retain operator role checks on operator routes.
2. Explicit customer submit is the trigger, not merely receiving a provider callback or editing a draft. Bind request ID, session, transcript and phone/address revisions. Current evidence must match at the final transaction-time check; no network call inside that transaction.
3. Reuse existing one-job transaction, unique linkage, audit and exact-replay behavior. Audit distinguishes service decision from customer intent and operator exception handling; never impersonate a staff account. Exact replay after a lost response retrieves the committed result without creating a second job. Changed replay, revoked policy and concurrent stale submissions refuse safely.
4. Customer-correctable failures stay inline. Unresolved exceptions use the existing review path, not a new queue product. Operators can assist correction and authorized recovery, but cannot declare stale/missing proof valid. An unavailable provider or exhausted allowance grants no job and triggers no automatic charged retry.
5. Job-created display explicitly distinguishes unpaid/not-booked status. Do not imply urgency assessment, dispatch, delivery consent or a confirmed appointment. Existing downstream gates remain unchanged.

Expected seams: current-proof-admission.ts; customer-intake-continuation.service.ts; existing customer transport and controlled composition; existing review controller; associated specs and parent integrated journey harness. No new service platform, table, AI authority layer or exception-management subsystem is authorized by this record. Finish the exact implementation card before coding; do not merely register the current operator controller as the automated path.

## Recovery, retention and finite tests

Removing the routine operator wait reduces the need for delayed proof, but does not itself establish Google retention permission or solve the transaction boundary. The implementer must specify current transient evidence ownership, invalidation and minimum permitted admission audit fields before controlled-source coding. Preserve the Google-only allowlisted candidate/customer-confirmed draft design. Restart with missing proof preserves the draft, not authority; uncertain costs remain held. No support response is assumed, and no provider replacement is proposed.

Required local tests inside existing 2B: successful customer submission without operator login creates one logical job; missing automation policy or untrusted actor refuses; tenant/session/revision mismatch refuses; expired/revoked proof and changed organization policy refuse; concurrent submissions and lost-response replay create one job; audit failure rolls back; callback alone cannot create a job; correction retains draft; exception operator cannot bypass proof; payment/booking/dispatch/send remain unauthorized. Browser acceptance must demonstrate the same customer flow plus exception visibility, not a separate demo. Full existing card checks and separately approved controlled acceptance remain required.

## Impact and adoption boundary

Approved scope-change direction: routine operator admission becomes automatic policy-bound admission; human review is exception-only. Five remaining sections stay 2B → 3A → 3B → 3C → 3D. APP-017 policy-management work is not pulled forward: use existing approved organization policy and identify any missing minimum activation field in the 2B card. No new routine phases. Walkthrough remains 3/8 (37.5%), not whole-MVP completion. Effort remains unsized until the revised source/identity/retention mapping is complete; no ETA claimed.

Next adoption action after review of this exact text: apply these two replacements, reconcile implementation card/data contracts/activation packet and status documents, and update the pinned baseline through a dedicated auditable adoption commit. Preserve guard regression tests, adding proof that only this approved amendment is accepted and unrelated mutations still fail. Do not move the anchor merely to make a failing check green. This packet itself changes neither baseline nor runtime.

Configuration, deployment, live verification/spend, merge and production actions still require their separate approval. Review-ready documentation only; no live job or customer changes.

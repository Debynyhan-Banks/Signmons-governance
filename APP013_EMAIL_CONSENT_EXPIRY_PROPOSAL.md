# APP-013 Appointment Email Consent and Expiry — Approved Contract v1

Status: **APPROVED DESIGN — LOCAL SESSION/CONSENT MODEL IMPLEMENTED; NOT ACTIVE.** Owner approved D1–D4, the inactive evidence foundation, and then answered "yes" to local-only implementation/testing of short-lived customer-session credentials with mailbox/prompt binding. No live key/configuration, production customer route, collection, verification, queue or sending is enabled. See APP013_CUSTOMER_SESSION_SECURITY_PLAN.md and the latest checkpoint for remaining transport/key/legacy-intake gates.

Scope: the supervised CallDesk pilot and three customer appointment emails only. APP-013 remains Now; no ticket promotion, marketing work or release. These are approved product/security rules, not a statement of legal requirements or legal compliance. Jurisdiction/provider compliance and production retention remain release-review obligations.

## Approved decisions (D1–D4)

| Decision              | Approved pilot rule                                                                                                                                                                         | Consequence / tradeoff                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| D1 Permission scope   | Explicit customer opt-in for confirmation, reschedule and cancellation emails for one job at one confirmed mailbox; no marketing or other-job permission                                    | More narrowly scoped than a permanent customer-level flag; new jobs need their own permission                                                      |
| D2 Mailbox authority  | Require purpose-bound mailbox verification before any of these private appointment emails; verification is not itself consent                                                               | Adds a verification step and implementation work; fewer wrong-address disclosures, but unverified customers receive no appointment email           |
| D3 Event deadline     | All three events expire 24 hours after their original immutable recording time; confirmation/reschedule additionally expire at the current bound arrival-window start, whichever is earlier | Late notifications are suppressed and surfaced to operations rather than sent after the useful window                                              |
| D4 Evidence lifecycle | Consent ends on revocation/address replacement or 24 hours after job completion/cancellation, whichever comes first; evidence retention is 90 days after job closure                        | Bounded per-job authority and post-close evidence; retention policy/hold compatibility must be approved before any purge implementation or release |

D1–D4 are approved without amendment. These product rules are not customer consent, mailbox verification, provider authorization or release approval. The 24-hour and 90-day values are approved design choices, not configured settings or runtime guarantees; retention/hold compatibility remains required before purge implementation.

## 1. Facts at the starting checkpoint

- Backend aa4c5470a0bdea64524cf1d2c65c0f8ee15e8cae has encrypted ask-once address capture, fixed email composition, default-off tenant preferences, immutable finalized appointment events and an inactive read-only event/policy/recipient diagnostic.
- Existing intake wording asks to keep an address and says it does not send email. Historical captured addresses therefore are **not** evidence for the new opt-in. Marketing lead consent, SMS consent and a business owner's project approval are different scopes and cannot be imported.
- Current diagnostic always returns eligible:false and deliveryAuthorized:false. Even when event/policy/recipient checks pass, consent authority and expiry policy remain unavailable. This document does not change those constants.
- Existing events have no consent-grant reference. They remain ineligible under this proposal; no historical-event rewrite, automatic backfill or send-on-enable migration.

## 2. Customer permission and capture

Proposed customer wording, shown only in an authorized future collection flow:

> May we email this address confirmations, changes and cancellation notices for this appointment, including a private link to manage it? This is optional and does not include marketing. You can stop these emails at any time. Please verify the address before we send appointment details.

- Show the selected address only to the customer in a private surface; require address confirmation and a distinct affirmative choice associated with the exact prompt/version. No prechecked box, inferred silence, bare address, generic “yes” to unrelated dialogue, LLM summary, or operator-created grant.
- Decline/missing/ambiguous response means no grant; booking and approved non-email fallbacks continue. Do not repeatedly ask the completed permission question on retries or reconnection. A customer may deliberately reopen preferences later, but that does not revive older events.
- Initial implementation should use an explicit structured response in a tenant/session-bound customer flow. Voice/SMS grants require a separately reviewed response-correlation/evidence path before acceptance; transcribed speech or free-form model output alone is not a grant. This limitation does not remove those channels from the wider pilot requirements.
- If captured before a Job exists, scope the evidence to the exact tenant/conversation/intake session. A separate atomic, one-time binding may attach it to the unique CREATED_FROM job. Preserve the normal placeholder-customer-to-job-customer lineage; an ambiguous association must refuse rather than guess. Do not let an intake grant attach to multiple jobs.
- Scope is the three named customer appointment events for that job, not assignment, payments, marketing, another tenant, another address or future jobs. Independent tenant event controls can further restrict permission, never broaden it.

## 3. Evidence contract (inactive persistence foundation supplied)

Use immutable evidence records plus a versioned current-state projection. Suggested fields are semantic requirements, not finalized Prisma/table/API names:

- Evidence ID/version, tenant ID, conversation ID/intake session, eventual immutable job/customer binding, channel and purpose APPOINTMENT_UPDATES_V1 with the three allowed event kinds.
- Exact mailbox binding using the existing normalization rules; preserve local-part semantics and never strip dots/plus tags as an equivalence shortcut. Store the address encrypted or by reference to encrypted capture, plus a tenant-scoped keyed fingerprint and key version for equality checks. Do not reuse a secrets key or introduce new key material without the separately reviewed implementation/security plan.
- Prompt/text version, customer-response evidence reference, source interaction ID, server-recorded UTC grant time and idempotency key. Keep minimal structured evidence, not full transcripts, raw private URLs, authentication tokens or ordinary-log copies of the address.
- Append-only GRANTED, DECLINED and REVOKED records; monotonic revision on the current authority projection. Corrections add evidence rather than changing history. A repeated submission returns the same logical receipt, not a second grant.
- A protected server boundary establishes actor/session/tenant authority. An input boolean, caller timestamp, customer ID or matching mailbox fingerprint alone cannot establish consent. Owner/admin may record an authorized suppression with an audit reason, not impersonate the customer to grant permission.
- Before event recording, bind the grant ID and observed authority revision to the event atomically with finalization. Database serialization/version checks must establish ordering; timestamps alone are insufficient for same-millisecond races. Missing binding records a blocked event, not presumed permission.
- A future versioned migration must leave all old events blocked. This proposal does not relax AppointmentEmailIntent immutability or existing Calendar/job/tenant retention constraints.

## 4. Verification, revocation and recipient changes

- D2 requires verified mailbox control before sending private appointment content. A verification challenge is a separate purpose, narrowly scoped to the same tenant/intake-or-job/mailbox with a bounded lifetime, one-time consumption, anti-abuse limits and no appointment-management authority. Its precise challenge lifetime, secure token design and transport acceptance belong to its bounded implementation review; they are not silently chosen here.
- The customer must explicitly request that verification step. A verification email must contain no appointment details or management link. This document does not authorize even a verification send or provider setup. Alternative existing verified-mailbox evidence may be reused only after its exact authority, scope and freshness are reviewed; no such source is established at this checkpoint.
- Verification and consent are separate: neither implies the other. Verification may complete after event finalization, but only an already event-bound grant can be used, the mailbox must be unchanged, and the event must still be current and unexpired. A grant obtained after the event cannot backfill it.
- Revocation immediately makes future admission/pre-dispatch checks refuse for this job/mailbox/purpose. Suppress unsent queue items without changing the appointment. Revocation must work through a customer-authorized preference/suppression surface and an authenticated operator suppression fallback; neither may grant new permission.
- Address replacement invalidates old-mailbox permission for future sending. The new mailbox needs a new explicit grant and verification. Do not redirect an existing event or queued credential to the replacement address; do not mutate immutable event/recipient bindings.
- Regrant does not revive an old, revoked, expired or previously blocked event. Only future independently finalized eligible events can use the new grant. A reviewed current-status resend would be a separate feature/authority, not a backfill exception in this contract.
- At dispatch, serialize local claim/suppression decisions and revalidate current consent, verification, recipient, tenant, job and policy immediately before the provider boundary. A provider request already in flight cannot be recalled reliably: revocation stops subsequent attempts, but must not falsely promise cancellation of already submitted email. Unknown outcomes remain review-held, not automatically resent.

## 5. Event expiry and supersession

For approved design policy APPOINTMENT_EMAIL_EXPIRY_V1, define recordedAt as the original immutable AppointmentEmailIntent.createdAt, expressed in UTC. It is not enqueue time, reread time, grant time or retry time. Calendar finalization must already be valid; the clock does not repair unknown external outcomes.

| Kind                    | Approved design deadline                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| APPOINTMENT_CONFIRMED   | min(recordedAt + 24 hours, bound windowStart)                                              |
| APPOINTMENT_RESCHEDULED | min(recordedAt + 24 hours, bound new windowStart)                                          |
| APPOINTMENT_CANCELLED   | recordedAt + 24 hours; the snapshot is the prior window, never an active management action |

- Require now < deadline. At the exact deadline, refuse. Use server/database UTC, validate clocks and reject future/invalid evidence. A missing/unknown expiry-policy version refuses. An earlier expiry or consent revocation still wins.
- Freeze the policy version/deadline in future admission records. A later configuration change may restrict but must not extend or resurrect prior work. Retries, restarts, recovered leases, late verification, regrant and operator review never reset the deadline.
- Supersession is separate and immediate: an incompatible current job/version/window, completed/cancelled active appointment, unfinished Calendar operation, current policy withdrawal or recipient change makes the event unsendable even before its deadline. Do not weaken the existing exact-version diagnostic to make old events pass.
- A cancellation notice still requires its exact finalized cancellation event and prior-window snapshot. Reopening/rebooking the job invalidates that old notice; it must not cancel a new appointment in the customer's understanding.
- Expired/suppressed work creates a privacy-safe operational outcome in the future queue workflow. It must not undo booking, invent a new event, send stale information, or automatically contact the customer through another channel. An authorized person can review the current appointment and choose an already approved fallback.

Examples (approved design policy, UTC): confirmation recorded Monday 10:00 with a Tuesday 15:00 window expires Tuesday 10:00; reschedule recorded Monday 10:00 for Monday 11:00 expires Monday 11:00; cancellation recorded Monday 10:00 expires Tuesday 10:00. A newer job revision at Monday 10:05 can suppress any of them earlier. The 24-hour clock is not a promise of delivery within 24 hours.

## 6. Retention and privacy boundary

- D4 requires no ongoing grant after revocation/address replacement, or later than terminal job time + 24 hours. This preserves the approved cancellation-notice window without granting future-job permission. Reopened jobs need fresh permission; an old terminal grant is not revived.
- Approved design for grant/verification/revocation evidence retention is 90 days after job closure, subject to an approved security/legal-hold policy. This is a product/security choice, not an assertion that 90 days satisfies a legal obligation. Before purge implementation, reconcile it with existing conversation, job, audit, Calendar-journal and tenant retention contracts.
- Purging evidence never changes “missing” into “permitted.” Retained events/queue items referencing unavailable authority remain suppressed. Necessary non-sensitive suppression/idempotency tombstones must outlive all retry/retention references under the approved retention plan; do not delete them in a way that enables duplicate sends.
- No new purge, retention migration, hold override, secrets change or evidence export is authorized. Operators get fixed statuses/reasons and approved masked identifiers, not grant proof tokens, raw emails, transcripts or private management URLs. Public errors remain tenant-safe and input-free.

## 7. Required implementation evidence after approval

1. Explicit prompt/version/response binding; address-only, unrelated yes, forged actor/tenant, missing and ambiguous responses refuse. Decline and retries never repeat completed questions or create grants.
2. Pre-job lineage binds once to the correct tenant/session/CREATED_FROM job; placeholder lineage is tested; duplicate/cross-tenant associations refuse.
3. Separate consent/verification checks, late verification before deadline, expired/consumed/wrong-purpose challenges, no appointment data in verification and no external sends without approval.
4. Event-time grant capture, concurrent finalization/revocation, same-millisecond ordering, transaction rollback and no historical-event resurrection.
5. Replacement mailbox, regrant, reopened job and revoked permission invalidate unsent work; old credentials cannot be retargeted.
6. All three deadlines, exact-boundary refusal, earlier arrival-window cutoff, unknown policy version, UTC/DST behavior, server clock skew and future timestamps.
7. No deadline extension under retries, crashes, regrant, late verification, operator retry or policy change; superseded events refuse before their time deadline.
8. Atomic queue identity, local suppression races, post-commit recovery and unknown provider-outcome hold; no claim of external exactly-once delivery or recall.
9. Expired/suppressed/failure visibility and safe operator review without rolling back appointments; no automatic channel switch.
10. Role/privacy projection, no consent-derived credential leaks, retention/deletion/hold compatibility and missing-authority refusal after purge.

These remain full acceptance obligations. The latest inactive persistence checkpoint supplies partial unit/database evidence only; it does not satisfy customer authentication, verification, expiry, retention or delivery acceptance. Existing eligible:false behavior stays unchanged until reviewed implementation supplies actual authority.

## 8. Review and implementation boundaries

Owner decision recorded: D1–D4 approved without amendment on 2026-09-09. No further approval of these same rules is needed. Retention/hold compatibility and verification challenge/transport details remain separate implementation/release gates.

Credential-bound encrypted transcript continuation is locally review-ready with ownership/replay/refusal tests, atomic audit and scripted-only collaborators. Next proposed bounded work: connect continuation to the local authenticated browser boundary with same-interaction retry and stale/expired-session UX. No production AI/tool/booking adapter, route, key, collection, verification, queue or sending activation. Application transcript locking is not database immutability or retention integration. See DATA_CONTRACTS.md, APP013_CUSTOMER_SESSION_SECURITY_PLAN.md and APP013_CUSTOMER_BROWSER_TRANSPORT.md. APP-013 remains Now.

Current completion estimate remains 50% APP-013 scope coverage and 0/12 formal acceptance. Planning allowance remains 7–12 unequal APP-013 sections and 20–35 for the supervised pilot, low confidence, not an ETA. D2 and the unresolved evidence/retention integration can increase the allowance; reassess when those implementation boundaries are sized and at demonstrated durable admission rather than treating this proposal as completed functionality.

Sources of current implementation truth: [APP-013 ticket](TICKETS/APP-013.md), [data contracts](DATA_CONTRACTS.md), [MVP plan](CALLDESK_MVP_PLAN.md), [global pointer](GLOBAL_EXECUTION_POINTER.md); backend evidence/APP-013/readiness-report.md and src/communications/appointment-email-eligibility.service.ts at aa4c547. D1–D4 are approved design choices, not findings of existing runtime behavior.

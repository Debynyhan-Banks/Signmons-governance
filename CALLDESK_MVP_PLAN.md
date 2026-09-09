# CallDesk MVP - Approved Supervised Pilot

Approved by the owner on 2026-09-09 after the bounded completion audit and capability review: "i agree include in docs so we can proceed". This document defines the first pilot boundary, not general availability of the full Signmons platform.

## Product promise and operating boundary

**Capture the request, confirm the facts, enforce the rules, coordinate the appointment and keep everyone informed.**

Signmons MVP is an AI front desk and dispatch assistant for a trades business. Start with one separately approved business, English-language operation, online access and owner/dispatcher supervision. Tenant isolation remains mandatory even in a single-business pilot. The pilot tenant has not been selected or provisioned by this approval.

The customer journey is call/text/chat -> confirmed intake -> policy/payment checks -> confirmed booking -> customer notifications -> dispatcher assignment -> technician progress -> visible outcome or human-owned exception. Payment ordering follows the existing server-side tenant policy; this plan does not change APP-012 contracts. No assistant statement alone can establish payment, booking or dispatch authority.

The wider seven-module product and future roadmap remain intact. This pilot is not the full trades platform, a replacement for all office staff, or a Growth-tier launch with unbuilt promised capabilities. Existing pricing, billing-domain, security and product-policy rules remain unchanged.

## Required pilot capabilities

These are launch requirements, not claims that every capability is available now.

| Capability | Required outcome | Existing work and remaining gap |
| --- | --- | --- |
| AI phone answering | Tenant-correct greeting and approved business information; collect service details and reach a governed booking/payment/human handoff | BE-008 transport accepted; inspected Twilio voice endpoint returns a greeting only. APP-033 conversational orchestration and call acceptance remain |
| SMS and web-chat intake | Confirm critical facts, retain context and avoid repeated completed questions; recover missed calls through approved text-back behavior | Webchat/intake foundations exist. Current Twilio SMS webhook handles consent keywords, not the complete conversational intake journey; channel handoffs and missed-call acceptance must be mapped before later ticket promotion |
| Safety and urgency | Approved instructions and human escalation for dangerous, urgent, unsupported or ambiguous requests | APP-006/007 foundations accepted; voice/channel composition and failure cases still need proof |
| Booking and customer management | Eligible slots, confirmed appointments, private view/reschedule/cancel access and recoverable failures | APP-011/013 foundations overlap APP-016; reuse evidence, do not rebuild them. Inactive recovery work is not a usable recovery workflow |
| Payment controls | Required booking fee/deposit and fail-closed progression based on verified payment | APP-012 sandbox/staging acceptance exists; live use remains separately gated |
| Customer communications | Eligible branded SMS/email confirmations, changes and on-the-way notices; preferences, consent, status and safe failure recovery | APP-013 Now; four customer SMS templates/settings, history, intents and email capture exist; customer email delivery and broader event/role coverage remain |
| Dispatcher workspace | Intake, urgency, payment/booking readiness and controlled assignment using service-area/availability policy | APP-006 through APP-010 have documented staging acceptance; integrated pilot journey must be revalidated |
| Technician mobile workflow | Assigned jobs, notification inbox, accept/en-route/started/completed status | APP-009 accepted; APP-013 inbox locally demonstrated; field completion must reflect confirmed work, not synthetic test actions |
| Operational oversight | Job activity, basic indicators, visible failures with an owner and controlled recovery | Existing audits/reporting/recovery foundations; minimal metric definitions, incident handling and end-to-end acceptance remain |
| Business-specific controls | Approved hours, coverage, branding, booking/payment rules and role access | Reuse current governed controls. No unrestricted rule editor or automatic exception authority is promised |

## Deferred from this pilot, not cancelled

- Full professional estimates/invoicing and broader Money workflows beyond the existing approved payment workflow.
- Diagnostic reports, inventory/purchasing, payroll exports, memberships, accounting integrations and full customer/equipment-history expansion.
- Offline technician synchronization, advanced analytics, broad template customization, autonomous dispatch, advanced automation and multi-location operation.
- Marketing expansion and Eternity work. FE-014 remains paused.

These deferrals do not weaken safety, tenant isolation, payment integrity, communication consent, data ownership or basic operational recovery. They do not authorize advertising unavailable features or changing paid-plan promises.

## Current progress checkpoint (2026-09-09, local customer browser security)

Backend checkpoint: see GLOBAL_EXECUTION_POINTER.md for the exact current PR #21 commit. Scope and release boundaries below remain unchanged.

Latest section adds an inactive browser boundary over the protected session/capture/consent models: exact origin/server context and customer-tenant checks, bounded compact JSON, local rate/concurrency limits and private responses/diagnostics. Desktop/mobile proof exercises actual services/database and rejects forged requests from a second local origin. 1384 backend/170 UI tests, nine new boundary checks, existing 19-migration/crash/consent/eligibility/browser regressions and four clean audits pass. See [APP013_CUSTOMER_BROWSER_TRANSPORT.md](APP013_CUSTOMER_BROWSER_TRANSPORT.md). No production route/key/configuration, full protected AI intake, collection, verification, queue or sending. Local limiter is not distributed production protection.

All three immutable appointment event kinds now feed an inactive read-only diagnostic binding current job/policy and the retained recipient in one consistent database snapshot. Matching CREATE read-back is covered; cancellation retains its prior immutable window. Every result remains blocked because implemented trusted consent evidence and configured expiry policy are absent; no positive admission, credentials, queue or transport. Evidence: backend email-eligibility/ and readiness-report.md; 42 new tests, 1232 backend/170 UI tests, 23 invariant-checked reads and a real revocation race/write refusal. Existing 18 local migrations/19 crash cases, browser regressions and four clean audits pass. Prior migration-before-code and old/in-flight cancellation compatibility still require separate release review.

Against the unchanged rubric below, criteria 3, 6 and 7 gain bound policy/event/recipient refusal evidence but still lack the full role/consent/brand matrix and durable admission/delivery. No additional criterion crosses the demonstrated boundary. Current classification: **1 demonstrated, 10 partial, 1 missing; 6/12 = 50% APP-013 scope coverage**. Formal acceptance remains **0/12**. This is not overall MVP completion, engineering effort or production readiness. The original 42% table below remains the initial audit baseline, not current status.

The planned two-section reassessment remains the planning baseline. Retain a **20-35 section low-confidence remaining allowance**, not mechanical subtraction or a calendar ETA. Customer flags, all three event snapshots and inactive binding checks are implemented; consent/expiry authority, broader role/brand policy, durable admission and credentials, transport/status, safe retry, operator visibility, broader SMS and approved integration acceptance remain. The existing 7-12 APP-013 allowance is provisional pending the proposed verification/retention sizing; other milestones remain unvalidated. Neither the diagnostic nor the approved contract is durable admission: reassess at consent implementation sizing and demonstrated admission. D1-D4 owner approval is now recorded. The inactive schema/evidence-binding section is review-ready. The local session/response model is also review-ready. Protected-session isolation and explicit authenticated capture are now locally review-ready. Local browser protections are now review-ready. Credential-bound encrypted transcript continuation is now locally review-ready (1411 backend/170 UI tests, twelve new database checks). Next proposed step is local authenticated browser continuation with explicit same-interaction retry and stale/expired-session UX, still scripted-only; production AI/booking and transport remain gated. Still no active collection or sending. APP-013 stays Now.

## Initial audit baseline and scoring

Audit baseline: backend `00337a756a177d3752204acfb082c2bf774d431f`; governance `7b72049c006f096cf9d79af334c980efb1772e56`. Both remotes were fetched and aligned during the audit. Evidence and source references below refer to that snapshot; future changes require re-scoring.

APP-013 has 12 broad acceptance criteria. Local evidence classification uses equal weight per criterion: demonstrated = 1, partial = 0.5, missing end-to-end workflow = 0. This is a coarse **scope-coverage index**, not effort-weighted engineering completion, probability of success or production readiness. Partial does not assert that half the implementation effort is done.

| APP-013 criterion (ticket order) | Local classification | Score | Evidence / uncovered scope |
| --- | --- | --- | --- |
| 1 Role-appropriate notifications | Partial | 0.5 | Operator history and technician inbox; broader event coverage remains |
| 2 Tenant-managed templates | Partial | 0.5 | Four fixed SMS templates/settings, not complete email/role controls |
| 3 Independent SMS/email policies | Partial | 0.5 | Customer SMS controls; full channel/event/recipient matrix remains |
| 4 All required SMS lifecycle events | Partial | 0.5 | Appointment lifecycle and departure; assignment/payment/other alerts remain |
| 5 Delivery/failure visibility | Partial | 0.5 | SMS history/intents; no customer-email status workflow |
| 6 Customer confirmation email | Missing end-to-end | 0 | Capture is not composition or delivery |
| 7 Reschedule/cancellation emails | Missing end-to-end | 0 | No complete customer email lifecycle |
| 8 Ask once and retain email | Locally demonstrated | 1 | Encrypted capture/job association, concurrency/restart evidence; at-most-once reservation can lose visible prompt and live model/channel acceptance remains |
| 9 Recoverable email failure | Missing end-to-end | 0 | No customer-email delivery/failure/retry workflow |
| 10 Management-credential protection | Partial | 0.5 | Existing private-link protections; email transport/preview path still needs proof |
| 11 Role-based redaction | Partial | 0.5 | Existing bounded projections; full future channel/role scope incomplete |
| 12 Auditable notifications | Partial | 0.5 | Existing SMS/intake/job audits; all required future events not complete |

Total: 1 demonstrated + 8 partial + 3 missing; 5/12 = 41.67%, rounded **42% APP-013 scope coverage**. Formal ticket acceptance remains **0/12 signed off**; no box is changed by this audit. APP-006 through APP-012 have documented staging acceptance (seven tickets), not a whole-MVP percentage. Previous APP-013 ~85% and overall ~81% estimates remain retired. No overall pilot percentage or calendar ETA is established here.

Implementation evidence: backend `evidence/APP-013/readiness-report.md`, `email-capture/summary.json`, `customer-messaging-settings/summary.json`, `technician-inbox/summary.json`, and earlier lifecycle/recovery evidence in that report. Source anchors: `src/communications/transactional-message-template.service.ts`, `twilio-webhook.service.ts`, `src/jobs/job-notification.service.ts`, `src/scheduling/scheduling.module.ts` and `ui/src/app/app/notifications/page.tsx`. Legacy operational email sending is not the required durable customer email pipeline. Calendar journal/review/recovery services absent from application module registration receive no live-workflow credit.

The preceding audit freshly passed four backend/UI full/production-only dependency audits with zero findings, architecture, four governance placement tests and docs consistency. Its reviewed implementation record reports 1020 backend tests/159 UI tests plus database/browser proof; those full suites were not rerun during the read-only audit. Old dependency findings are not current blockers; override maintenance remains a risk. This documentation checkpoint runs docs/placement/architecture/diff checks only and changes no runtime behavior.

## Milestone plan and authorization

| Milestone | Exit condition | Low-confidence remaining review sections |
| --- | --- | --- |
| Finish APP-013 | Required event/channel policies, content, delivery status, safe retry, privacy and owner acceptance | 7-12 |
| Calendar lifecycle acceptance | Reused APP-011/013 evidence plus uncovered APP-016 requirements; truthful/recoverable create/reschedule/cancel | 4-7 |
| AI voice and channel handoffs | APP-033 plus explicitly mapped SMS/missed-call ownership; approved calls/intake or recoverable human fallback | 6-10 |
| Pilot operational acceptance | Minimal metrics, onboarding, access, monitoring, restore/rollback and full-journey owner acceptance | 3-6 |

Reassessed remaining planning allowance: **20-35 bounded sections**, not equal-sized effort units or a delivery-date promise. Two-section reassessment is recorded above; next reassessment at durable email admission, not after an arbitrary percentage increase. Voice/provider integration and release acceptance are major uncertainties; uncovered work may increase the allowance. Freeze this pilot denominator; add proposed scope only through explicit owner review.

APP-013 remains the sole Now ticket. Future milestones are planning order, not permission to start other tickets; Global Next remains unassigned. After APP-013 acceptance, update pointer/board/handoff before promoting a ticket and explicitly map remaining channel/metrics/operations ownership to existing tickets rather than silently expanding APP-033 or another ticket.

### Completed first bounded APP-013 continuation (review-ready, not released)

Fixed customer appointment-email composition with local previews and tests, building on the retained optional email. Cover confirmation, reschedule and cancellation content from explicit canonical inputs: tenant branding, confirmed date/Eastern arrival window, reference/service type, private management action and calendar action where eligible, plus fallback and private-link warning. Cancellation must not offer an active management action.

The first section used fictional fixtures to prove input/state consistency, escaping, timezone handling, cancellation omissions and credential-free operator previews. The second now resolves a private recipient from retained capture, but does not authorize delivery or establish finalized event truth. No provider calls, actual credential issuance, queue/worker activation, email delivery or production action. See the current checkpoint above; delivery criteria remain incomplete.

## Pilot acceptance checklist (all open)

- [ ] Identify the approved pilot tenant, owner, dispatcher, technician roles, service area, hours, emergency fallback and support responsibility without weakening tenant isolation.
- [ ] Call/text/chat ordinary and ambiguous requests produce tenant-correct confirmed records without duplicate jobs; missed-call handling and channel handoffs have evidence.
- [ ] Emergency/unsupported input, silence, interruptions, dropped calls and model/provider/transfer failures end in approved instructions or recoverable human-owned work; no fabricated availability, prices or successful actions.
- [ ] Required payment blocks progression until verified status; denied, failed, duplicate and out-of-order callbacks cannot bypass policy.
- [ ] Create, reschedule and cancel obey availability/payment policy; duplicate/restart/concurrent/failure tests show truthful database/Calendar state and controlled recovery. Inactive code or safe refusal alone is not completion.
- [ ] Eligible SMS/email lifecycle notifications have event identities, privacy-safe content/status and controlled retry; STOP/HELP, consent and quiet hours work. Unknown provider outcomes are not automatically resent or described as delivered; external exactly-once guarantees must not be inferred from queue acknowledgment.
- [ ] Dispatcher assignment and technician mobile progress work end-to-end for allowed roles; denied and cross-tenant cases fail closed.
- [ ] Private links, tokens, customer information, recordings and transcripts obey approved access/redaction/retention policy. Recording remains disabled unless requirements are explicitly met.
- [ ] Operators can identify and own failed/unconfirmed work, use the tested recovery procedure and distinguish queued, sent, delivered, confirmed and uncertain states.
- [ ] Define and evidence minimal booking/payment/missed-call/urgency/response-time indicators with source events and denominators; record measured latency/fallback behavior and approve performance limits before acceptance, without inventing numeric targets here.
- [ ] Onboarding, export/retention responsibilities, monitoring, incident escalation, backup restoration, migration ordering and rollback procedures have scoped test evidence.
- [ ] Complete current code/security/browser/device gates and separately approved integration/release acceptance, with owner sign-off and explicit remaining-risk disposition. No outstanding blocker for lost requests, false bookings, duplicate actions, payment bypass or data exposure.

For each blocker record the user-visible failure, pilot impact, accountable owner, smallest fix/procedure, proving test and stopping condition. Defer nonblocking refinements with explicit operating limits. Passing tests do not replace owner acceptance or authorize release.

## Release boundary

Scope approval is not authorization to merge, deploy, migrate production, activate delivery, configure Stripe/Twilio, change IAM/secrets/billing, incur charges, send externally or change real customer data/appointments. Provider acceptance, pilot provisioning and all production actions require separate explicit approval. Work only in the saved Signmons backend project and related governance repository; never mix Eternity work.

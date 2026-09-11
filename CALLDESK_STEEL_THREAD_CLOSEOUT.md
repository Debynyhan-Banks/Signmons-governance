# CallDesk steel-thread closeout audit — 2026-09-10

## Current execution breakdown

PAYMENT_BOOKING_TEXT_STEEL_THREAD.md baseline v1 now fixes eight acceptance sections for the owner-tested payment/booking/text walkthrough. VO-3 maps to 1A/1B, current-proof admission to 2A/2B, and the focused S2 walkthrough to 3A–3D. Current target 1A pending policy/implementation approval; accepted 0/8. This supersedes historical next-section forecasts below, not the full MVP or existing acceptance ledger. Full email, S3 and S4 remain open. Planning approval grants no provider, coding or release authority.

## Approved automated verification MVP decision (2026-09-10, current)

Owner approved an automated normal verification path: phone one-time code, address autocomplete/validation, automatic configured service-area checks and existing verified-payment/availability gates. Mandatory operator contact/address confirmation is superseded; human help is for exceptions. Phone access is not identity, payment is not verification, and neither grants messaging consent. Existing human-reviewed admission is not silently removed. Current requirements, acceptance cases and approval boundaries: CALLDESK_MVP_PLAN.md, section "Approved automated verification MVP decision".

Documentation only; implementation and provider acceptance remain open. Next is to inspect/reuse contracts and bound the automated connection, including expiry, retry, abuse controls and invalidation on changed details. No provider selection/configuration, live code sending, charges, production action or release authorized. APP-013 sole Now, Next empty, FE-014 paused. Percentages unchanged: APP-013 50% scope coverage / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA.

## Reviewed preferred service window (2026-09-10, latest review-ready)

Owner reviewed b61bb55 and approved continuing the preferred-window section. Added local operator save/reload for a customer-stated preference, never availability or a booking. Exact job version, acknowledgment, active tenant and non-impersonated owner/admin/dispatcher required. Shared tenant/job locks and CAS atomically write preferredTimeText plus private review/audit metadata; preserve pricing, payment/intake snapshots, status and appointment fields. Refuse jobs with payment or scheduling activity. Exact same-actor retry writes once; fresh-version correction is explicit and audited.

Evidence: backend evidence/APP-013/preferred-window-review/README.md, summary and focused desktop/mobile screenshots. 1598 backend tests (25 new), 170 UI tests, lint/build/architecture/Prisma, four clean audits and local browser/DB proof pass. Parent includes 12 organization/intake, eight admission and 12 browser groups, including five new preference checks: lost-ack exact retry, real audit rollback, selective blocker removal, stale/foreign/role refusal and concurrent correction once. Fictional records/database removed. Existing toolchain/pg deprecation notices remain documented.

New route is unregistered in production. Plain text is not parsed to a date, timezone or reserved slot; payment/contact/address blockers remain and both booking/delivery authority stay false. No provider/payment/booking/send action, schema/package/migration, merge/deploy, real data, IAM/secrets/billing or charges.

Stop for review. Next priority: inspect contact/address validation and coverage evidence and define what proof can clear those blockers, not a checkbox-only verification claim. Full S2 booking/confirmation and production rollout remain open. APP-013 sole Now, Next empty, FE-014 paused. Progress unchanged: APP-013 50% scope coverage / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA. Sales/advisor and website import remain outside MVP.

## Approved payment-policy prerequisite (2026-09-10, prior checkpoint)

User explicitly approved owner/admin organization payment-policy setup after the missing authoritative setup was identified. Completed one local prerequisite: fixed USD fee/deposit draft, separate versioned approval, and explicit approved-snapshot attachment to a human-reviewed CREATED job. Tenant settings preserve other configuration; CAS and audits protect save/approval. Shared tenant/job locks, exact versions, pristine-job checks and atomic job/audit binding protect attachment. No auto-waiver or implicit approval; exact retry only. Later drafts/approvals do not rewrite existing job snapshots.

Evidence: backend evidence/APP-013/organization-payment-policy/README.md, summary and desktop/mobile screenshots. 1573 backend tests (19 new), 170 UI tests, lint/build/architecture/Prisma and four zero-finding audits pass. Real local database rollback for settings and binding audit failures, concurrent approval once, stale/foreign/role/superseded refusal and exact replay tested. Parent retains 12 organization/intake, eight admission and seven browser groups. All fictional records/database removed. Fixture identity is not production authentication acceptance; existing toolchain/pg deprecation notices remain documented.

New controllers/services are unregistered in production. Fixed positive integer USD cents only; fail_closed and webhook validation mandatory; no exceptions, emergency surcharge, SDK/provider/payment/gate change, schema or migration. Missing preferred window and contact/address verification still block. No booking, charge, send, merge/deploy, real data, IAM/secrets/billing or charges. This is a local policy source/attachment workflow, not automatic adoption by every existing job-creation path.

Stop for review. Next proposed: return to explicit preferred-service-window review on the created job, with exact job version; a preference is not availability or booking. Existing-job repricing/current-policy rollout and production/integration acceptance remain gates. APP-013 sole Now, Next empty, FE-014 paused; sales/advisor/website import outside MVP. Progress unchanged: APP-013 50% scope coverage / 0 of 12 accepted, onboarding 50% local / 0 of 6 accepted, pilot 0 of 12 accepted. No overall engineering percentage or ETA.

## Local job booking-readiness preview (2026-09-10, prior checkpoint)

Owner reviewed the browser admission checkpoint and approved the proposed bounded S2 readiness section. Added inactive jobId-only POST /booking-readiness/preview and operator fixture control opening the newly created job. Verified non-impersonated owner/admin/dispatcher and active tenant; CREATED jobs only. PostgreSQL repeatable-read READ ONLY snapshot reuses intake assessment and payment gate without changing policy/integrations. Missing explicit payment flags are UNKNOWN, not no-payment-required; missing window, human/verification and unfinished Calendar blockers are visible. No blockers still requires booking validation, never grants authority.

Confirmation preview explicitly refuses APPOINTMENT_NOT_FINALIZED for this unbooked job; no date, link or message is fabricated. This is not finalized-event content rendering or positive recipient/consent eligibility. No production module registration, booking, payment, sending, provider actions, schema/package changes or release authority.

Evidence: backend evidence/APP-013/booking-readiness-preview/README.md, summary and desktop/mobile screenshots. 1554 backend tests including 12 new, 170 UI tests, lint/build/architecture/Prisma and four clean dependency audits pass. Local proof now covers 12 organization/intake, eight admission and six browser groups. Reads leave job/audit unchanged; fictional required-payment policy demonstrates refusal; all disposable records removed. Prior Calendar test instability remains historical; this run passed. Existing non-blocking toolchain warnings and one pg concurrency deprecation are recorded.

Stop for review. Next proposed outcome: authorized review of missing preferred window and applicable payment policy on the created job, followed by the local booking decision; inspect/reuse existing mutation contracts before implementation and do not treat diagnostic flags as policy authority. Full S2 booking/notification remains open. APP-013 sole Now, Next empty, FE-014 paused. Coverage unchanged: APP-013 50% / 0 of 12 accepted, onboarding 50% local / 0 of 6 accepted, pilot 0 of 12 accepted. No overall engineering ETA. No merge/deploy, production migration, real data, IAM/secrets/billing/charges; advisory sales/website import outside MVP.

## Browser customer submission and operator approval (2026-09-10, prior checkpoint)

Owner approved continuing the local admission connection. Customer fixture explicitly submits its reviewed draft; separate operator fixture loads an opaque reference, reviews facts/current organization version, selects urgency and acknowledges statements, then creates one CREATED job. Inactive customer transport adds submit; new guarded read/approve controller is deliberately absent from production modules. Customer credentials never enter operator requests. Exact retry after lost acknowledgment returns the original outcome; closed/expired/changed requests do not silently become replacements.

Evidence: backend evidence/APP-013/browser-review-admission/README.md, browser-review-summary.json and three screenshots. Five new real-browser/local-database groups plus 20 prior organization/admission groups pass. 1542 backend tests (four new), 170 UI tests, lint/build/architecture/Prisma and four zero-finding audits pass. One existing Calendar HTTP test failed during a concurrent run, then the isolated full suite passed; root cause is not established. Disposable fictional records/databases removed. No process-kill or production-auth acceptance claim.

The local approved-information → customer submission → operator review → one job connection is now demonstrated. CREATED is not booked, charged, dispatched or sent; contact/address remain unverified. Stop for owner review of this connected milestone, then select the next existing MVP outcome. Do not automatically extend hardening or promote a ticket. Post-expiry/status recovery, changed-approval recovery, production identity/shared budget/key/retention/access controls and old-reader rollout remain gates. No live AI/provider action, schema/package change, production registration, real data, merge/deploy, IAM/secrets/billing or charges.

Progress unchanged: onboarding 3/6 = 50% local evidence and 0/6 accepted; APP-013 50% recorded scope coverage and 0/12 accepted; pilot 0/12 accepted, not 0% built. No defensible overall engineering percentage or ETA. APP-013 stays sole Now, Next empty, FE-014 paused; sales/advisor and website import remain outside MVP.

## Token-free operator admission (2026-09-10, prior checkpoint)

Owner approved proceeding from organization-bound intake to one job. Added unregistered admitReview: exact requestId, expectedOrganizationApprovedAt and explicit human decision; verified non-impersonated owner/admin/dispatcher only. No customer credential is accepted, read or reconstructed. Locked durable draft/transcript/current organization checks precede shared atomic customer/address/job/link/consent/audit/session-close persistence. Job policy retains request and organization binding; request event remains unchanged. Exact same-actor/decision replay before original expiry and while job/approval remain valid returns the original receipt without writes. No booking or delivery authority.

Backend evidence: evidence/APP-013/operator-review-admission/README.md and operator-admission-summary.json. 1538 backend tests (18 new), 170 UI tests, lint/build/architecture/Prisma, four clean audits; eight new local database groups plus 12 prior organization/browser groups pass. Real rollback and concurrency tested; three fictional jobs and their fixture database removed. No new browser admission controls, production auth acceptance or process-kill test. Shared persistence refactor preserves legacy admitDraft behavior. No schema/package/migration/route/module/UI activation or provider action.

Next after review: connect customer submission and operator decision controls to this local protected admission flow, including honest pending/uncertain/stale states. Full browser organization-to-job walkthrough remains unfinished. Post-expiry/status recovery, approval-change UX, production identity/key/retention and old-reader rollout remain gates. Customer/address remain unverified; CREATED is not booked. APP-013 stays sole Now; Next empty; FE-014 paused. Sales/advisor and website import stay outside MVP. Progress unchanged: onboarding 50% local evidence/0% accepted; APP-013 50% scope coverage/0% accepted; pilot 0% accepted, not 0% built. No overall engineering ETA. No merge/deploy, production migration, real data, IAM/secrets/billing or charges.

## Approved organization to protected intake (2026-09-10, latest review-ready)

Owner said proceed after the documentation-only advisory vision clarification. Completed one local steel-thread connection: continueOrganization answers from this tenant's approved FAQ/fallback, persists encrypted version-2 turns bound to approval timestamp/digest, and existing customer submit/operator read preserves and checks that binding. Draft edits do not change answers; reapproval invalidates the old session/request. Scripted and organization histories cannot mix. Operator read uses no customer credential and identifies organizationApprovedAt. No customer production route, live AI, job admission or provider activation. Sales/advisor and website-import work remain outside MVP.

Evidence: backend evidence/APP-013/organization-intake/README.md, summary and desktop/mobile screenshots. 1520 backend tests (nine new), 170 UI tests, lint/build/architecture/Prisma, four clean audits; 12 local organization/database/browser groups including five new intake groups. Browser demonstrates approved reply through optional-email skip/read-only draft; durable submission and operator read are service-boundary proofs, not a finished browser-to-job workflow. Disposable database removed and cleanup query empty. No schema/package/migration change. Version-2 history needs separately reviewed old-reader rollout; changed-approval recovery remains a human-owned future UI task, not silently repaired here.

Percentages unchanged: onboarding 50% local outcome evidence (3/6), 0% accepted (0/6); APP-013 50% scope coverage, 0% accepted (0/12); pilot 0% accepted (0/12). No overall engineering percentage or ETA. Next after review: token-free operator admission from durable request with organization-version binding and atomic job/consent outcome, followed by browser decision integration. APP-013 sole Now, Next empty, FE-014 paused. No merge/deploy, production migration, live data/provider/IAM/secrets/billing or charges.

## Organization setup slice (2026-09-10, latest review-ready)

Completed the owner-approved S0 page/API slice within the explicitly amended APP-013 steel-thread dependency. Company facts, greeting/tone and sourced FAQs save to a tenant-scoped draft; exact saved-version approval preserves a separate approved snapshot; deterministic FAQ or human-contact fallback preview uses only that snapshot. Source routes are registered and the root sandbox links to /app/organization; nothing is deployed. No runtime AI, customer-journey/job connection, canonical policy changes or provider calls. Details and exact commands: backend evidence/APP-013/organization-setup/README.md; governance DATA_CONTRACTS.md.

Validation: 1511 backend tests (19 new), 170 UI tests, lint/build/architecture/Prisma and four clean dependency audits. Seven local database/browser proof groups cover concurrency, audit rollback, tenant/role refusal, draft/approval separation, desktop/mobile and stale-save recovery. Fixture identity is explicitly substituted, not production Firebase acceptance. Temporary databases removed; cleanup query empty. No migration/package changes. Profile facts do not configure scheduler timezone or replace payment/routing policies; manual consistency review is still required. Exact-match preview is not semantic AI or automatic human-task creation.

Progress: onboarding 3/6 = 50% locally demonstrated outcomes (O1/O3/O4), 0/6 = 0% formally accepted. APP-013 recorded scope coverage remains 50%, formal acceptance 0/12 = 0%; pilot acceptance 0/12 = 0%. These are distinct denominators, not an engineering ETA. Next after owner review: connect the approved organization snapshot to the protected customer intake/operator request-to-job path, preserving tenant/revision authority and no external actions. Full steel thread is not complete. APP-013 stays sole Now; Next empty; FE-014 paused. No merge/deploy, production migration, IAM/secrets/billing, real-data/provider or charge authority.

## Organization setup and progress baseline (2026-09-10, latest planning)

Owner approved organization-onboarding gap review and requested percentages. See governance `ORGANIZATION_ONBOARDING_MVP.md`: basic tenant name/instructions and separate settings exist, but no organization onboarding page or approved FAQ/voice workflow was found in the inspected feature tree. Proposed next milestone S0 is owner-approved organization facts/rules/FAQ/brand voice with local answer preview, before S1 intake-to-job. Map implementation ownership and align governance before coding; APP-013 remains sole Now, Next unassigned, FE-014 paused. This is not automatic APP-033 promotion or an APP-013 scope expansion.

Progress baseline: APP-013 **50% recorded scope coverage** (1 demonstrated + 10 partial at half weight + 1 missing, divided by 12), **0/12 = 0% formal acceptance**; organization onboarding **0/6 = 0% acceptance**; full pilot **0/12 = 0% acceptance** against the existing pilot checklist. These are separate denominators, not effort, release readiness or an overall build percentage. Onboarding refines the existing business-controls requirement; do not add its six checks to the pilot denominator. No new engineering completion percentage or ETA is inferred. This documentation-only update does not rerun earlier runtime/security gates or claim new acceptance.

## Decision and evidence boundary

Owner requested a fixed MVP audit before more coding: “proceed. i thought we were doing a steal thread to avoid this. lets see what need to be done for mvp”. This checkpoint documents the audit, not approval to reduce the pilot, promote tickets or release. APP-013 remains sole Now; Next remains empty; FE-014 stays paused.

Fetched both origins and verified focused HEADs equal upstream: backend `670e973b8e18df7d3d849a61260b3bb0b95c4f07`, governance `0bc8b57ec6951d39d663245977c8a0fc7a72829e`. Reviewed pointer, boards, handoffs, APP-013 criteria, MVP plan, contracts and latest intake evidence/source. This is a checkpoint-based coverage audit, not a fresh runtime or production certification. Latest recorded gates are 1492 backend/170 UI tests and four clean dependency audits; they were not rerun for this documentation-only change.

The original steel-thread intent is recorded in TICKETS/GOV-004.md. Execution accumulated individually tested, inactive foundations instead of finishing a usable vertical workflow. Security work is valuable, but safe refusal and test totals are not user-outcome completion. Repeated unchanged section allowances are withdrawn as current forecasts: neither 7–12 APP-013 nor 20–35 pilot sections is a defensible remaining-effort estimate. The historical 50% rubric is only coarse scope coverage; formal APP-013 acceptance remains 0/12. No replacement percentage or date is asserted.

## Fixed product boundary

Keep the approved CALLDESK_MVP_PLAN.md: one approved business, English, online and human supervised; phone, SMS and web chat; governed payment/booking; customer communication; dispatch and technician progress; human-owned exceptions. The pilot business is not yet selected. Do not quietly turn the AI front desk into only a web form.

Proposed first proving path: fictional web-chat request → confirmed facts and optional email choice → authenticated operator review → one job → existing payment/availability checks → confirmed appointment → eligible SMS/email and visible status → dispatcher assignment → technician progress → visible outcome. Then exercise reschedule/cancel and failure recovery on that same journey. Use existing modules and fixed templates; do not rebuild accepted routing/payment/technician foundations.

Web chat first is proposed sequencing, not removal of voice/SMS. A local provider stub proves application behavior only. Actual provider delivery, voice intelligence and the pilot require separately authorized integration evidence.

## Finish milestones (outcomes, not equal-sized coding sections)

| Milestone | Reuse and remaining work | Demonstration required | Accountable workstream |
| --- | --- | --- | --- |
| S1 One usable intake-to-job handoff | Reuse transcript, draft, consent evidence and local admission. Connect request-ID-only operator decision to atomic job/consent outcome; connect protected customer/operator UI and identity boundary. Resolve expired/stale review with visible human ownership, not a silent dead end. | Customer submits; operator sees and approves; one job appears. Retry/restart does not duplicate; foreign role/tenant refuses; decline/skip still creates an eligible reviewed job without sending permission. | APP-013 dependency; no new ticket assignment without approval |
| S2 One governed booking and notification journey | Reuse APP-010/011/012, immutable appointment events and email composition. Finish current consent plus separate mailbox verification/expiry, durable email admission, private actions, transport/status/retry and operator visibility. Demonstrate Calendar recovery ownership and uncertain outcomes. | From S1 job, payment-required path refuses until verified; booking is truthful; eligible confirmation reaches controlled test recipient only after explicit integration approval. Reschedule/cancel update content; failed email preserves appointment; uncertain send is not blindly resent. | APP-013 messaging; Calendar gaps map to APP-016 before ticket promotion |
| S3 Operational completion | Reuse dispatcher/technician surfaces and SMS history. Finish required event/recipient controls, role visibility, assignment/payment/status alerts and auditable recovery. | Dispatcher assigns eligible technician; technician progresses job; intended roles see events, other roles cannot see private fields; operator owns failed work. Completion reflects confirmed field action. | APP-013 plus reused APP-006–012 foundations |
| S4 Full pilot channels and readiness | Add real conversational phone/SMS and missed-call/handoff behavior; reuse S1–S3 backend. Complete safety/fallback, access, retention, monitoring, restore/rollback and owner acceptance. | Ordinary and interrupted/ambiguous/emergency calls/texts converge on same governed job or human-owned exception; approved pilot checklist passes across channels. | APP-033 voice; map SMS/handoff and operations ownership before promotion |

All four milestones are open end-to-end. Their component maturity differs; this is not “0% built”. S1–S3 organize reuse and gaps, not permission to cross the sole-Now ticket boundary. S4 is required for the currently approved MVP, not a hidden follow-on after launch.

## APP-013 unchanged acceptance ledger

Status below follows recorded evidence, not new acceptance. Every row stays open until its proving workflow and owner sign-off exist.

| # | Requirement | Recorded state | Smallest observable closure |
| --- | --- | --- | --- |
| 1 | Role-appropriate notification center | Partial: history and technician inbox | S3 required events visible to correct roles, denied elsewhere |
| 2 | Tenant-managed templates | Partial: fixed SMS templates/settings | S2/S3 permitted fixed-template settings and brand controls work; unrestricted editor stays deferred |
| 3 | Independent SMS/email policy | Partial: settings and inactive eligibility/consent foundations | S2/S3 event × recipient × channel × consent × brand allow/refuse matrix through real application boundary |
| 4 | All listed SMS lifecycle events | Partial: appointment and departure foundations | S3 assignment, payment, technician and dispatcher events plus existing lifecycle prove deduplication and retained provider outcomes |
| 5 | Delivery/failure visibility | Partial: SMS history/intents | S2/S3 email and SMS status/failed/uncertain states visible to authorized operator |
| 6 | Eligible confirmation email | Partial: content, event, recipient and refusal evidence | S2 committed event, current verified eligibility, durable logical send, private/calendar action and controlled delivery evidence |
| 7 | Reschedule/cancel emails | Partial: composition and immutable changes | S2 one logical updated/cancel notice per event; cancellation contains no active management action |
| 8 | Ask once/retain email | Locally demonstrated, not formally accepted | S1–S2 integrated capture/skip/retry/job association, no repeated completed question |
| 9 | Email failure/retry | Missing end-to-end | S2 failure leaves booking intact; operator sees failure; tested recovery avoids unsafe duplicate send |
| 10 | Management credential protection | Partial | S2 tokens absent from ordinary logs/analytics/operator previews through complete transport |
| 11 | Role redaction | Partial | S1–S3 full relevant response/UI matrix including foreign tenant and unauthorized roles |
| 12 | Auditable events | Partial | S1–S3 each required lifecycle and recovery has correlated privacy-safe audit evidence |

“Exactly one” means one logical event/intent with proven duplicate handling; do not claim an external exactly-once delivery guarantee. Ambiguous provider outcomes require reconciliation or human review before retry.

## Work required versus work that can wait

Must resolve before affected path is accepted: wrong-tenant access, exposed private credentials, missing consent authority, payment bypass, lost requests, duplicate jobs/actions, false booking/delivery claims, and unowned uncertain outcomes. Expired or changed review requests need a tested operator-visible fallback. Retention/access responsibilities must be implemented or explicitly bounded before real customer data is used. No security waiver is implied.

Already deferred by the approved MVP: unrestricted customization, autonomous dispatch, advanced analytics, offline sync, multi-location, inventory/payroll/accounting/memberships and marketing. Do not add generic framework polish or unrelated hardening unless a reachable MVP blocker is demonstrated. Current checkpoint audits are clean; future findings are triaged by affected path and severity, not an endless automatic expansion.

Candidate simplifications requiring explicit approval if used: manual operator reconciliation instead of general automatic repair; restart plus human callback for expired review rather than seamless replacement; fixed templates rather than broader template authoring. These cannot silently weaken existing ticket criteria, privacy or delivery integrity. No tickets are moved or accepted by this audit.

## Control against another expanding chain

1. Before coding, agree the next milestone demonstration and list only its concrete missing connections. Recommended first target is S1 as a usable customer/operator journey, not token-free admission presented as a finished feature by itself.
2. Every bounded implementation must name its milestone, user-visible blocker, proving test and stop condition. Tests/framework work alone cannot be called completion of that milestone.
3. Any newly discovered prerequisite must show why it blocks that demonstration; otherwise propose it for later owner review. Never silently add scope or promote a ticket.
4. At each review show the same ledger: demonstrated workflow, remaining specific blockers, and acceptance evidence. Estimate effort only after routes/identity/provider dependencies are sized; distinguish engineering work from approval/provider waiting time.
5. APP-013 closes only when its unchanged twelve criteria pass or the owner explicitly approves a documented split/re-scope. No merely local mock proves provider delivery; no code approval authorizes release.

## Review and next decision

Review this plan alongside CALLDESK_MVP_PLAN.md and TICKETS/APP-013.md. Recommended decision: approve web chat as the first proving channel while retaining phone/SMS in MVP, and make S1 the next demonstration target. Before its next implementation, bound the missing admission/UI integration work against current contracts; do not start S2/S4 automatically.

Release gates remain explicit: no merge, deployment, production migration, provider/Stripe/Twilio configuration, IAM/secrets/billing changes, charges, external sends or real customer/appointment mutations. No Eternity work. This checkpoint changes documentation only.

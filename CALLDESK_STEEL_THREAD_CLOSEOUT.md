# CallDesk steel-thread closeout audit — 2026-09-10

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

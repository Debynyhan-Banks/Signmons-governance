# Core MVP source/evidence inventory — October 20, 2026

## Boundary and method

The owner approved the exact core-release amendment preserved at governance `7ed300a1d4f50a9a53500db405c3290130bd43cf`; see `MVP_CORE_RELEASE_SCOPE_CHANGE_20261020.md`. This is a bounded read-only inventory against backend `c426c319c240879dfb7c7ebf2f5aabfa5161c9d7`, using current source and saved acceptance evidence. No application implementation, new runtime tests, provider calls or release/customer acceptance occurred in this audit. Source presence, local tests, historical staging acceptance and current integrated owner acceptance are distinct.

## Approved first commercial feature set

- Basic AI phone answering, bounded web/SMS intake and missed-call recovery; approved facts, short qualification, safety/human fallback and critical-field confirmation.
- Finite approved hours, coverage, services, fees and booking/payment policy; server verification of required booking fee/deposit before eligibility.
- One supported calendar path, conflict-safe booking and private view/reschedule/cancel with essential eligible notices and visible failures.
- Manual dispatch, technician statuses, notes/relevant photos/equipment facts and a simple completion summary.
- Basic approved quote, final invoice, allocation of the initial payment against the final balance, payment link, receipt and truthful partial/failed/refund state.
- Minimum authorized customer/job history and an outcome/exception report showing what booked, completed and was actually collected.
- Guided setup, one location/up to two technicians, English, online field use, tenant/role security, consent/privacy/audit, fixed subscription activation, support and tested recovery.

QuickBooks/existing FSM, full pricebook, advanced diagnostics, sales/persona configuration, rich history/retrieval, memberships, costing, inventory, time/payroll, offline, financing and acquisition-to-profit are not first-release prerequisites. Retained safety and truthful financial/booking outcomes remain mandatory.

## Implementation versus acceptance

| Capability | Reusable implementation / saved evidence | Remaining R1 gap or acceptance |
| --- | --- | --- |
| Guided business setup and access | Tenant/organization/payment-policy services and UI; auth, tenant and role guards | Complete guided launch, safe paid-offer activation and administration acceptance not established |
| Verified web intake | Current-proof/customer-session and verification components; owner-accepted 1A/1B/2A/2B, including October 19 job creation/cleanup | Does not establish phone/SMS conversational intake or the full paid/completed journey |
| Phone/SMS intake and missed calls | BE-008 signed Twilio/consent/delivery foundation | `src/communications/twilio-webhook.service.ts` voice returns a greeting; ordinary SMS path handles consent keywords and otherwise returns an empty response. Basic conversational intake and missed-call recovery remain APP-033 work |
| Policy and initial payment | Versioned tenant policy, payment requests/signed webhooks, historically accepted APP-012; P07 locally tested/built | Current same-job 3A/P08 acceptance and readiness/deployment/destination/read-path prerequisites remain open. Existing request service covers required initial deposit/service fee, not final invoicing |
| Booking and essential communications | APP-011 and substantial journal/private-link/recovery/intent implementation | Current same-job 3B calendar, 3C received text and 3D recovery remain unaccepted; amended APP-013 and unchanged APP-016 criteria still require evidence |
| Manual dispatch | Historically accepted APP-008/010; `dispatch-board.service.ts` enforces eligibility, payment/concurrency checks and audit | Reuse in connected R1 journey; do not rebuild or infer new integrated acceptance |
| Technician status and completion evidence | APP-009 owner real-phone acceptance recorded September 2; technician status/completion transitions exist | Full notes/photos/equipment/completion-summary flow is partial: inspected note is audit metadata; no technician completion-photo/structured-summary workflow was established by this inspection |
| Basic customer Money | Payment/refund/ledger foundations; `DATA_CONTRACTS.md` already reserves estimate, invoice, allocation and receipt contracts | Major unsized APP-020 gap: no complete estimate/invoice/allocation/receipt models/controller/UI found; current one-payment-per-job model/request does not establish approved final balance and deposit allocation |
| Outcomes and collections | BE-007 tenant-safe job lifecycle/website_chat attribution report; existing operational exceptions | No collected-revenue/partial/refund invoice report or all-channel lead denominator established. Created jobs are not all leads; payments are not estimate revenue |
| Fixed subscription/admin | TenantSubscription schema and limited entitlement checks | Complete commercial subscription checkout/webhook/activation/dunning/admin and offer activation workflow not established by inspected source |
| Support, security and restore | Existing guards/audit/health/monitoring, runbooks and isolated synthetic backup/restore evidence | Map actual commercial operating owner, incident/rollback, retention/export/closure and environment restore evidence; fixture restore is not production readiness |

Older component acceptance is recorded in `EXECUTION_BOARD.md` Done entries; stale readiness-report prose does not reverse newer owner acceptance. Reuse accepted code/evidence without treating historical components as today's complete commercial journey.

Inspected seams include `src/communications/twilio-webhook.service.ts`, `src/tenants/tenants.service.ts`, `src/jobs/dispatch-board.service.ts`, `src/jobs/technician-workflow.service.ts`, `src/jobs/intake-readiness.service.ts`, `src/payments/payment-requests.service.ts`, `src/reporting/reporting.service.ts` and `prisma/schema.prisma`. Exact field/source cards are required before any implementation; this inventory is not permission to invent a replacement financial model or new subsystem.

## What can be measured honestly

| Measure | Current result | Meaning |
| --- | --- | --- |
| Fixed connected walkthrough | 4/8 accepted = 50% | Accepted verification/job-admission milestones; payment/calendar/text/recovery remain |
| Original remaining-work package plan | 6/60 accepted = 10% | Historical unequal integrated-pilot packages, not percentage of all code built or new commercial R1 |
| Original full-intelligence matrix | 0/13 fully accepted | Preserved broader/later-scope ledger, not new R1 launch completion |
| New commercial R1 overall | Not yet baselined | Requires finite source-sized implementation/evidence packages and reviewed acceptance mapping; no honest whole-MVP percentage or ETA follows from this table |

Do not average those measures, count these rows as equal effort, or raise completion because scope moved later. Much foundation exists; a commercial release still lacks complete integrated evidence. A percentage based on tests, commits, ticket labels or arbitrary half-credit would misrepresent progress.

## Immediate path and finite sizing work

APP-013/3A remains active. Existing P07 readiness prerequisites must be resolved under a fresh qualified operation where needed; the scope amendment renews no consumed window, package or external authority. The next observable current-section result remains authentic Sandbox payment clearing the same admitted job's gate, with verified failure/replay handling and closeout.

For the R1 work ledger, map each retained requirement to current source and reusable evidence; size the uncovered phone/SMS/missed-call behavior, completion documentation, basic Money/collections and commercial activation/operations gaps; assign existing ticket ownership and exact finish criteria; then review the finite denominator and execution placement. Basic Money/reporting/admin are commercial-tail obligations outside the old 60-package plan. No tail ticket is promoted by this inventory.

## Commercial price boundary

The approved catalog remains unchanged: Founding Partner $199/month for the first ten approved external businesses with its existing twelve-month price lock and activation terms; Starter $299/month for the one-location/up-to-two-technician core offer once its promises are released and accepted. Approximate 100 AI-handled calls/month is a suitability guide, not unlimited usage or a metered fee. Guided setup is included; contractor payment processing remains separate. Growth/Pro remain later gated offers. This inventory activates no subscription and provides no assurance of demand or gross margin.

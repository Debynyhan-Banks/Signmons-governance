# Screen Route API Matrix

Purpose: canonical alignment between screen IDs, frontend routes, and backend APIs.

## Public Marketing (Current Phase)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Contract Dependency | Delivery Ticket | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-PUB-001` | `/` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE baseline shipped | implemented |
| `SCR-PUB-006` | `/pricing` | `signmons-marketing-web-feat-marketing-site` | none required (static MVP), optional pricing-catalog API (post-MVP) | `PricingPlan`, `SubscriptionEntitlement`, `SubscriptionInvoiceRule`, `PaymentPolicy` | FE baseline shipped + FE-016 (subscription-only reconciliation) | correction required |
| `SCR-PUB-007` | `/demo` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/try-demo`, `GET /api/marketing/try-demo/:leadId`, `POST /api/marketing/try-demo/status` | marketingLead/try-demo contract | FE-008 | implemented |
| `SCR-PUB-009` | `/contact` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/lead-capture` | FE-007 lead-capture contract | FE-007 + BE-002 | implemented |
| `SCR-PUB-010` | `/privacy`, `/terms`, `/sms-terms` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE-006 | implemented |
| `SCR-PUB-011` | `/done-for-you-setup` | `signmons-marketing-web-feat-marketing-site` | none required | `BusinessRuleSet`, `TenantBrandProfile` (messaging dependency) | FE-009 | implemented |
| `SCR-PUB-012` | `/business-rules` | `signmons-marketing-web-feat-marketing-site` | none required | `BusinessRuleSet`, `DispatchPolicy`, `PaymentPolicy` | FE-010 | implemented |
| `SCR-PUB-013` | `/brand-voice` | `signmons-marketing-web-feat-marketing-site` | none required | `TenantBrandProfile` | FE-011 | implemented |
| `SCR-PUB-014` | `/dispatch-scheduling` | `signmons-marketing-web-feat-marketing-site` | none required | `SchedulingWindow`, `Appointment`, `DispatchPolicy` | FE-012 | implemented |
| `SCR-PUB-015` | `/revenue-dashboard` | `signmons-marketing-web-feat-marketing-site` | none required (static MVP), optional revenue-summary API (post-MVP) | `RevenueEvent`, `UsageMetricEvent` | FE-013 | pricing correction required |
| `SCR-PUB-016` | `/roi-calculator` | `signmons-marketing-web-feat-marketing-site` | none required (calculator model in FE), optional ROI estimate API (post-MVP) | `PricingPlan`, `SubscriptionEntitlement`, `UsageMetricEvent`, `RevenueEvent` | FE-013 + FE-016 | pricing correction required |
| `SCR-PUB-017` | `/compare/answering-services` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE-014 | placeholder |
| `SCR-PUB-018` | `/compare/field-service-software` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE-014 | placeholder |
| `SCR-PUB-019` | `/customer-technician-experience` | `signmons-marketing-web-feat-marketing-site` | none required | `NotificationPolicy`, `CustomerProfile`, `Appointment` | FE-015 | placeholder |

## APP Sequence (Owner-Approved CallDesk-First)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Contract Dependency | Delivery Ticket | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-APP-012` | `/app/intake-review` | backend app surface | `GET /jobs/intake-review`, `GET /jobs/intake-review/:jobId`, `POST /jobs/:jobId/readiness/review` | intake/job readiness contract | APP-006 | implementation verified; release pending |
| `SCR-APP-013` | `/app/urgency-review` | backend app surface | `GET /jobs/urgency-review`, `GET /jobs/urgency-review/:jobId`, `POST /jobs/:jobId/urgency/override`, `POST /jobs/:jobId/escalations` | urgency classification and escalation review contract | APP-007 | released |
| `SCR-APP-014`, `SCR-APP-017` | `/app/dispatch` | backend app surface | `GET /jobs/dispatch-board`, `GET /jobs/dispatch-board/:jobId`, `POST /jobs/:jobId/assignments`, `POST /jobs/:jobId/assignments/cancel`, `POST /jobs/:jobId/escalations` | dispatch board and technician assignment contract | APP-008 | released |
| `SCR-TECH-001`, `SCR-TECH-002`, `SCR-TECH-003` | `/app/technician` | backend app surface | `POST /jobs/technician-links/:technicianId`, `GET /technician/jobs`, `GET /technician/jobs/:jobId`, `POST /technician/jobs/:jobId/status` | technician mobile job workflow contract | APP-009 | released; authenticated real-phone acceptance passed 2026-09-02 |
| `SCR-APP-015`, `SCR-APP-016`, `SCR-APP-024`, `SCR-TECH-004` | `/app/routing`, `/app/dispatch` | backend app surface | `GET /jobs/routing`, routing rule/service-area/technician write APIs, `POST /jobs/:jobId/routing/evaluate`, APP-008 dispatch APIs | routing rules, service areas and availability contract | APP-010 | implementation in review |
| `SCR-APP-005` | `/app/jobs` (planned) | backend app surface | `POST /jobs/:jobId/complete` pilot deployed; broader queue/lifecycle APIs remain ticket-defined | audited job completion contract | APP-003 | pilot backend deployed; UI planned |
| `SCR-APP-018`, `SCR-APP-019` | `/app/revenue`, `/app/conversion` (planned) | backend app surface | `GET /reports/lead-sources` pilot; broader revenue/funnel APIs remain APP-014 | tenant lead-source report contract | BE-007 pilot + APP-014 | pilot backend implemented; UI planned |
| `SCR-APP-025` | `/app/schedule` (planned) | backend app surface | scheduling/availability API set (ticket-defined) | `SchedulingWindow`, `Appointment` | APP-016 | planned |
| `SCR-APP-026` | `/app/business-rules` (planned) | backend app surface | tenant rules policy API set (ticket-defined) | `BusinessRuleSet`, `DispatchPolicy`, `PaymentPolicy` | APP-017 | planned |
| `SCR-APP-027` | `/app/brand-voice` (planned) | backend app surface | tenant brand voice profile API set (ticket-defined) | `TenantBrandProfile` | APP-018 | planned |
| `SCR-APP-028` | `/app/customers` (planned) | backend app surface | customer profile/history API set (ticket-defined) | `CustomerProfile`, `NotificationPolicy` | APP-019 | planned |
| `SCR-APP-029` | `/app/invoices` (planned) | backend app surface | estimate/invoice/receipt API set (ticket-defined) | `ServiceEstimate`, `JobInvoice`, `CustomerPaymentAllocation`, `CustomerReceipt` | APP-020 | planned |
| `SCR-APP-030` | `/app/pricebook` (planned) | backend app surface | pricebook API set (ticket-defined) | service/pricebook contract (ticket-defined) | APP-021 | planned |
| `SCR-APP-031` | `/app/growth` (planned) | backend app surface | review/maintenance automation API set (ticket-defined) | review/maintenance policy contract (ticket-defined) | APP-022 | planned |
| `SCR-APP-032` | `/app/integrations/accounting` (planned) | backend app surface | accounting adapter/reconciliation API set (ticket-defined) | accounting adapter contract (ticket-defined) | APP-023 | planned |

## Customer Integration Pilot

| Screen ID | Route / surface | UI owner | Backend endpoint | Contract dependency | Delivery ticket | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-CUST-006` | Embedded tenant website assistant; Eternity pilot uses a server-side website proxy | tenant website | `POST /api/integrations/webchat/triage` | BE-003 webchat request, response, credential and safety contract | BE-003 | in progress |
| `SCR-CUST-007` | Customer estimate/invoice link (planned) | customer web surface | estimate approval, payment, and receipt API set (ticket-defined) | `ServiceEstimate`, `JobInvoice`, `CustomerPaymentAllocation`, `CustomerReceipt` | APP-020 | planned |

## Contract Rules

- Every route in `LINK_CTA_MAP.md` must appear in this matrix.
- Every backend endpoint here must be defined in `DATA_CONTRACTS.md`.
- Delivery ticket ownership must be explicit for each API-dependent screen.
- Any page that presents total monthly cost must use the fixed `PricingPlan` subscription and must not add setup, usage, booking, emergency, revenue-share, or basic per-invoice Signmons fees.

# What Signmons Is + Anti-Drift DoD

Purpose: provide one unambiguous product definition and release bar so contributors and AI agents do not drift into a generic chatbot, generic FSM clone, or scope-sprawl SaaS.

## Product Definition (Canonical)

Signmons is an **AI front-office operating system for trades businesses**.

It is built to:
- capture inbound demand across call/text/chat,
- classify urgency,
- enforce payment and policy gates,
- produce booking-ready and dispatch-ready jobs,
- route work with controlled rules,
- notify owner/dispatcher/technician/customer,
- report revenue outcomes with auditability,
- monetize through a governed commercial model (base subscription, setup fee, usage/overage, performance fees, and add-ons).

Primary ICP:
- HVAC, plumbing, electrical, and adjacent home-service operators.

## Product Family (Canonical)

Signmons is one platform with the following governed product modules:

1. **Signmons CallDesk**
   - AI-assisted phone, SMS, and web-chat intake
   - qualification, safety screening, booking, summaries, and human handoff
2. **Signmons Dispatch**
   - calendar availability, booking readiness, dispatch board, technician assignment, service-area rules, and rescheduling
3. **Signmons Money**
   - professional estimates, customer approval, deposits, invoices, payment links, receipts, reminders, refunds, and payment audit history
4. **Signmons Field**
   - technician job workflow, customer/equipment context, notes, photos, signatures, and status updates
5. **Signmons Customers**
   - tenant-isolated customer, property, equipment, service, payment, and communication history
6. **Signmons Growth**
   - missed-call recovery, review requests, maintenance-plan renewal workflows, and lead-source attribution
7. **Signmons Intelligence**
   - booking, response-time, payment, revenue, dispatch, and AI-quality reporting

These are modules of one product, not seven disconnected applications. Shared tenant identity, customer/job records, business rules, audit events, and permissions are mandatory.

## Canonical Customer Workflow

`call/text/chat -> identify -> qualify -> safety/policy check -> schedule -> collect required booking fee/deposit -> dispatch -> estimate/approve -> perform work -> final invoice -> collect balance -> receipt -> review/retain -> report`

Signmons may integrate with an existing CRM/FSM/accounting system at any stage, but the workflow must remain explainable and recoverable inside Signmons.

## What Signmons Is Not

- Not a generic website chatbot.
- Not just an AI answering service.
- Not a full fleet optimization suite in MVP.
- Not a replacement for all CRM/FSM systems in MVP.
- Not general-ledger accounting, payroll, bank reconciliation, tax filing, or an ERP.
- Not a promise that every governed module is available before its delivery ticket is complete.

## Product North Star

"Get paid before dispatch while maintaining high booking quality and dispatch confidence."

Supporting outcome: "Move a qualified customer from first contact to documented payment without duplicate data entry or unanswered ownership."

## Financial Workflow Boundary

- Professional estimates and invoices are a core Signmons product capability, not a separate accounting product.
- Basic branded estimates, invoices, payment links, and receipts belong in every paid plan once `Signmons Money` is released.
- Advanced deposits, progress/recurring invoicing, automated reminders, approval workflows, and accounting synchronization are tiered capabilities.
- Signmons must not store raw card data; payment collection uses an approved PCI-compliant processor.
- Accounting remains the system of record for general ledger, payroll, tax filing, and bank reconciliation; Signmons integrates through approved adapters.
- There are two distinct billing domains: contractor-to-customer job invoices and Signmons-to-tenant SaaS invoices. Data, numbering, policies, and permissions must not be conflated.

## Delivery Sequence (Anti-Drift)

Execute the product in this order unless the governance pointer explicitly approves an exception:

1. CallDesk reliability, safety, intake integrity, booking, and notifications
2. Tenant dashboard, customer/job history, and booking-readiness review
3. Calendar, dispatch, technician assignment, and durable customer confirmations with secure appointment-management access
4. Professional estimates, invoices, deposits, payments, and receipts
5. Technician mobile workflow and pricebook
6. Voice/SMS depth, accounting/CRM/FSM integrations, reviews, and maintenance plans
7. Advanced automation, auto-dispatch, multi-location controls, and intelligence

Marketing work may explain a planned module only when it is labeled as planned/early access. It must not present an unshipped module as generally available.

## Non-Negotiable Product Rules

1. **Policy before persuasion**
- AI can guide intake, but policy gates decide booking/dispatch eligibility.

2. **Canonical confirmation for critical fields**
- Required customer/job fields must be verifiable and fail-closed when ambiguous.

3. **Payment integrity**
- Payment status checks and webhook handling are server-side and fail-closed.

4. **Tenant isolation**
- No cross-tenant reads/writes/inference.

5. **Explainable operations**
- Every key system decision (urgency, routing, escalation, payment gate) must be auditable.

## High-Ticket Differentiator Definition

Signmons differentiates on **Revenue Integrity Dispatch**:
- deterministic rules,
- payment gate enforcement,
- urgency-aware routing,
- explainable handoff and audit trail,
- measurable revenue recovery.

## Anti-Drift DoD

A feature or phase is not complete unless all are true:

1. **Outcome alignment**
- Clearly advances revenue capture, booking quality, dispatch quality, or retention.

2. **Contract alignment**
- Screen, route, CTA, and API mappings are updated in governance docs.

3. **Policy alignment**
- Business rules, escalation, and payment behavior are explicit and testable.

4. **Evidence alignment**
- Required gates pass and objective evidence exists.

5. **Claim alignment**
- Marketing claims do not exceed implemented behavior.

6. **Workflow ownership**
- Every created lead, booking, job, estimate, invoice, payment, dispatch action, and notification has a tenant-scoped owner/status and an auditable failure path.

7. **Focus protection**
- Work outside the delivery sequence requires an explicit governance decision and cannot displace the active `Now` ticket silently.

## Required MVP Metric Set (Top 5)

1. Lead-to-booking conversion rate
2. Payment link completion rate
3. Missed-call recovery rate
4. Emergency job capture rate
5. First-response latency (p95)

## Phase Gate Rule

- Marketing-first phase remains active until `MARKETING_RELEASE_DOD.md` is satisfied.
- APP execution unlock occurs only after board + pointer explicitly move `Now` to APP scope.

## Required Use

- This doc must be read at session start for any repo execution.
- If a proposal conflicts with this doc, it is blocked until governance is updated.
- Commercial claims and pricing mechanics must align with:
  - `PRICING_AND_FEES_POLICY.md`
  - `OFFER_CATALOG.md`
  - `BILLABLE_EVENTS_SPEC.md`

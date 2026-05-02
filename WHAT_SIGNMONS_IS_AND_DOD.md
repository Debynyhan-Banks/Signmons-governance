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
- report revenue outcomes with auditability.
- monetize through a governed commercial model (base subscription, setup fee, usage/overage, performance fees, and add-ons).

Primary ICP:
- HVAC, plumbing, electrical, and adjacent home-service operators.

## What Signmons Is Not

- Not a generic website chatbot.
- Not just an AI answering service.
- Not a full fleet optimization suite in MVP.
- Not a replacement for all CRM/FSM systems in MVP.

## Product North Star

"Get paid before dispatch while maintaining high booking quality and dispatch confidence."

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

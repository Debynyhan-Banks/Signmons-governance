# Signmons Scope + Definition of Done

## 1) Mission

Signmons is a multi-tenant AI front-office and dispatch SaaS for home-service businesses (HVAC, plumbing, electrical). It captures inbound demand, confirms critical customer/job data, schedules and dispatches work, supports the job-to-payment workflow, and delivers auditable operating records.

## 2) In Scope

- Multi-tenant backend with strict tenant isolation
- Twilio-backed voice intake and call routing with deterministic policy-driven flow
- Twilio-backed inbound/outbound SMS as the canonical confirmation channel for key fields
- Missed-call text-back, transactional customer/technician/dispatcher notifications, delivery status, and communication history
- Payment-first booking gate
- Calendar scheduling, booking readiness, dispatch, and technician assignment
- Customer, property, equipment, communication, and service history
- Professional estimates, approvals, deposits, invoices, payment links, receipts, and reminders
- Technician mobile job workflow
- Approved accounting/CRM/FSM integration adapters
- Review-request, missed-call recovery, and maintenance-plan renewal workflows
- Tenant dashboards for operations and visibility
- Marketing site and conversion funnel
- Admin/ops controls with auditability

## 3) Out of Scope (MVP)

- Advanced route optimization and full fleet management
- Advanced voice AI, transcription analytics, sentiment analysis, and automated outbound campaigns
- Broad ERP/CRM two-way sync beyond approved adapters
- General-ledger accounting, payroll, bank reconciliation, tax filing, or an ERP replacement
- Raw payment-card storage or custom payment processing outside an approved PCI-compliant provider
- Unvalidated multilingual claims
- Features without acceptance criteria and evidence

## 4) Non-Negotiable Product Rules

- Voice is persuasive intake, not canonical authority
- SMS confirmation is canonical for required fields
- Twilio is an MVP infrastructure dependency, but telephony and messaging must sit behind a provider abstraction so Signmons is not permanently vendor-locked
- Communication delivery must be idempotent and auditable, with consent, opt-out/STOP and HELP handling, quiet-hour policy, delivery/failure status, safe retry, and duplicate-message protection
- Payment webhook validation is server-side and fail-closed
- No cross-tenant data access
- No silent assumptions for critical customer fields
- Tenant brand voice policy must control greeting, tone, prohibited phrases, escalation language, fee language, and closeout messaging
- Business rules must be tenant-scoped, auditable, versioned, and enforced server-side
- Scheduling and calendar decisions must respect technician availability, service windows, urgency, and payment-gate status
- Customer profile/history access must remain tenant-isolated with no cross-tenant exposure
- Estimate, invoice, payment, refund, and credit transitions must be tenant-scoped, idempotent where required, and auditable
- Contractor-to-customer job invoices and Signmons-to-tenant SaaS invoices must remain separate billing domains
- Basic invoicing must not be marketed as bookkeeping or accounting
- Human fallback/escalation must exist for urgent, unclear, failed, or policy-sensitive flows
- Signmons-to-tenant pricing is a fixed monthly or annual subscription; Signmons does not charge setup, per-call overage, per-booked-job, emergency-capture, revenue-share, or basic per-invoice fees
- Plan capacity is a suitability and fair-use boundary. Approaching or sustained excess usage triggers notification and a fixed-price plan-upgrade conversation, not an automatic metered charge
- Normal Twilio, messaging, and AI usage is included within the subscribed plan; exceptional Enterprise volume is reflected in a negotiated fixed subscription
- Contractor-to-customer Stripe processing costs remain separate from the Signmons subscription and must never be presented as a Signmons performance fee

## 5) Definition of Done

### Ticket DoD

- Ticket is in `Now` on `EXECUTION_BOARD.md`
- Acceptance criteria complete
- Required gates pass:
  - Backend: `npm run -s build`, `npm test -- --runInBand`, `npm run -s arch:check`
  - Frontend: `npm run -s build`, `npm run -s lint`, `npm test -- --runInBand` (or approved equivalent)
- `QUALITY_GATES.md` checklist satisfied (architecture/security/contracts)
- Evidence attached (logs/tests/screenshots/API proof)
- `SESSION_HANDOFF.md` updated
- One focused commit

### Feature/Phase DoD

- All child tickets complete
- No critical regression in quality, security, conversion paths
- Observability exists for key flows
- Rollback strategy documented for risky changes

### Release DoD

- Security baseline checks pass
- Core revenue flows validated end-to-end
- KPI instrumentation active
- On-call and incident paths documented

## 6) Success Metrics (MVP)

- Visitor to demo conversion
- Demo to activated tenant conversion
- Call to booked-job conversion
- Payment link completion rate
- Repeat-question rate and first-response latency
- Missed-call recovery rate and transactional message delivery/failure rate
- Tenant retention/churn trends
- Estimate approval rate and invoice payment completion rate after Signmons Money is released
- Time from completed work to paid invoice after Signmons Money is released

## 7) High-Ticket Copy Guardrails

- Do not claim "zero staff required"; use "human handoff for urgent or unclear cases."
- Do not claim "2-minute setup" for full workflow setup; use "call forwarding in minutes, full workflow setup guided."
- Do not publish performance claims (for example, "3x bookings", "98% answer rate", "$0 no-shows") without linked evidence.
- Pricing claims must map to implemented or explicitly scoped capabilities.
- No high-ticket marketing claim may ship unless it maps to:
  - one metric in Section 6 (or an approved extension), and
  - one evidence source (dashboard panel, report extract, or ticket evidence artifact).

## 8) Commercial Model Guardrails (High-Ticket)

- Public plan ladder target:
  - Starter: `$299/mo`
  - Growth: `$799/mo`
  - Pro: `$1,499/mo`
  - Enterprise: fixed custom monthly/annual subscription
- Founding Partner bridge: `$199/mo` for the first `10` approved external businesses; it is limited early access, not a replacement public tier, and has no setup fee
- The MVP has no required setup fee, metered call overage, booked-job fee, emergency-capture fee, revenue share, or separately priced feature add-on
- Included plan capacity is disclosed as a suitability/fair-use guide; Signmons recommends a fixed-price upgrade when a tenant consistently exceeds it
- Normal Twilio/AI/provider operating costs are included in plan economics. Exceptional Enterprise needs are priced into the fixed custom subscription
- Basic professional estimates/invoices/payment links/receipts are included after the Signmons Money release gate without a basic per-invoice Signmons fee.
- Basic Stripe payment-before-booking enforcement is included in Starter and every higher paid plan after the Signmons Money release gate. Growth and higher tiers differentiate through advanced deposit, preauthorization, exception, partial-payment, and recovery controls rather than access to the core gate.
- Stripe and other customer-payment processor fees belong to the contractor-to-customer transaction and are separate from Signmons subscription billing.
- Annual pricing discount policy must be explicit and versioned (default target: `15%-20%`).

# Signmons Scope + Definition of Done

## 1) Mission

Signmons is a multi-tenant call-intake and booking SaaS for home-service businesses (HVAC, plumbing, electrical). It captures inbound demand, confirms critical customer/job data, enforces payment and policy gates, and delivers dispatch-ready records.

## 2) In Scope

- Multi-tenant backend with strict tenant isolation
- Voice intake with deterministic policy-driven flow
- SMS as canonical confirmation channel for key fields
- Payment-first booking gate
- Tenant dashboards for operations and visibility
- Marketing site and conversion funnel
- Admin/ops controls with auditability

## 3) Out of Scope (MVP)

- Advanced route optimization and full fleet management
- Broad ERP/CRM two-way sync beyond approved adapters
- Unvalidated multilingual claims
- Features without acceptance criteria and evidence

## 4) Non-Negotiable Product Rules

- Voice is persuasive intake, not canonical authority
- SMS confirmation is canonical for required fields
- Payment webhook validation is server-side and fail-closed
- No cross-tenant data access
- No silent assumptions for critical customer fields
- Tenant brand voice policy must control greeting, tone, prohibited phrases, escalation language, fee language, and closeout messaging
- Business rules must be tenant-scoped, auditable, versioned, and enforced server-side
- Scheduling and calendar decisions must respect technician availability, service windows, urgency, and payment-gate status
- Customer profile/history access must remain tenant-isolated with no cross-tenant exposure
- Human fallback/escalation must exist for urgent, unclear, failed, or policy-sensitive flows

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
- Tenant retention/churn trends

## 7) High-Ticket Copy Guardrails

- Do not claim "zero staff required"; use "human handoff for urgent or unclear cases."
- Do not claim "2-minute setup" for full workflow setup; use "call forwarding in minutes, full workflow setup guided."
- Do not publish performance claims (for example, "3x bookings", "98% answer rate", "$0 no-shows") without linked evidence.
- Pricing claims must map to implemented or explicitly scoped capabilities.
- No high-ticket marketing claim may ship unless it maps to:
  - one metric in Section 6 (or an approved extension), and
  - one evidence source (dashboard panel, report extract, or ticket evidence artifact).

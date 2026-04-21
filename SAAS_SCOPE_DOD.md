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

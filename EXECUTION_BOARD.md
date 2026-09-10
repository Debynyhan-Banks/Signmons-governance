# Signmons Execution Board

## Organization setup slice (2026-09-10, latest review-ready)

Completed the owner-approved S0 page/API slice within the explicitly amended APP-013 steel-thread dependency. Company facts, greeting/tone and sourced FAQs save to a tenant-scoped draft; exact saved-version approval preserves a separate approved snapshot; deterministic FAQ or human-contact fallback preview uses only that snapshot. Source routes are registered and the root sandbox links to /app/organization; nothing is deployed. No runtime AI, customer-journey/job connection, canonical policy changes or provider calls. Details and exact commands: backend evidence/APP-013/organization-setup/README.md; governance DATA_CONTRACTS.md.

Validation: 1511 backend tests (19 new), 170 UI tests, lint/build/architecture/Prisma and four clean dependency audits. Seven local database/browser proof groups cover concurrency, audit rollback, tenant/role refusal, draft/approval separation, desktop/mobile and stale-save recovery. Fixture identity is explicitly substituted, not production Firebase acceptance. Temporary databases removed; cleanup query empty. No migration/package changes. Profile facts do not configure scheduler timezone or replace payment/routing policies; manual consistency review is still required. Exact-match preview is not semantic AI or automatic human-task creation.

Progress: onboarding 3/6 = 50% locally demonstrated outcomes (O1/O3/O4), 0/6 = 0% formally accepted. APP-013 recorded scope coverage remains 50%, formal acceptance 0/12 = 0%; pilot acceptance 0/12 = 0%. These are distinct denominators, not an engineering ETA. Next after owner review: connect the approved organization snapshot to the protected customer intake/operator request-to-job path, preserving tenant/revision authority and no external actions. Full steel thread is not complete. APP-013 stays sole Now; Next empty; FE-014 paused. No merge/deploy, production migration, IAM/secrets/billing, real-data/provider or charge authority.

## Approved steel-thread implementation (2026-09-10, current)

Owner said “great proceed” after selecting the organization-to-job walkthrough. APP-013 explicitly owns the bounded S0 setup dependency for this walkthrough: owner/admin organization draft, version approval and deterministic FAQ/fallback preview with a usable page. This is an explicit scoped amendment, not APP-033 promotion. Reuse tenant settings and auth; no change to canonical booking/payment/routing policies. APP-013 stays sole Now; Next empty; FE-014 paused. Full customer-to-job integration follows review, not automatic completion. Live AI/provider calls and all release actions remain disabled. Acceptance percentages remain unchanged until evidence and owner acceptance.

## Organization setup and progress baseline (2026-09-10, latest planning)

Owner approved organization-onboarding gap review and requested percentages. See governance `ORGANIZATION_ONBOARDING_MVP.md`: basic tenant name/instructions and separate settings exist, but no organization onboarding page or approved FAQ/voice workflow was found in the inspected feature tree. Proposed next milestone S0 is owner-approved organization facts/rules/FAQ/brand voice with local answer preview, before S1 intake-to-job. Map implementation ownership and align governance before coding; APP-013 remains sole Now, Next unassigned, FE-014 paused. This is not automatic APP-033 promotion or an APP-013 scope expansion.

Progress baseline: APP-013 **50% recorded scope coverage** (1 demonstrated + 10 partial at half weight + 1 missing, divided by 12), **0/12 = 0% formal acceptance**; organization onboarding **0/6 = 0% acceptance**; full pilot **0/12 = 0% acceptance** against the existing pilot checklist. These are separate denominators, not effort, release readiness or an overall build percentage. Onboarding refines the existing business-controls requirement; do not add its six checks to the pilot denominator. No new engineering completion percentage or ETA is inferred. This documentation-only update does not rerun earlier runtime/security gates or claim new acceptance.

## MVP steel-thread audit (2026-09-10, current planning checkpoint)

Owner requested a fixed MVP/steel-thread audit before more coding. See governance `CALLDESK_STEEL_THREAD_CLOSEOUT.md` for the twelve-criterion ledger and four outcome milestones. This supersedes earlier next-section suggestions and rolling 7–12 APP-013 / 20–35 pilot forecasts; historical percentages are not completion estimates. APP-013 remains sole Now, acceptance 0/12; Next unassigned, FE-014 paused. No scope reduction, ticket promotion or release authority. Recommended next decision: approve web chat as the first proving channel and target a usable customer/operator intake-to-job journey, retaining phone/SMS in the full MVP. No implementation is authorized by this planning checkpoint. Backend implementation remains 670e973; this change is documentation only.

Purpose: single active queue for execution.

## Operating Rules

1. WIP limit is 1 (`Now` only).
2. No coding without a ticket in `Now`.
3. Do not pull from `Later` directly to `Now`.
4. Every completed ticket includes objective evidence.
5. Update this board before changing scope.
6. Ticket completion must satisfy `QUALITY_GATES.md`.
7. Owner-approved CallDesk-first execution supersedes the marketing-first pointer while the active APP ticket is in `Now`; paused marketing work remains governed by `MARKETING_RELEASE_DOD.md` when resumed.

## Required Completion Gates

- Backend tickets: `npm run -s build` + `npm test -- --runInBand` + `npm run -s arch:check`
- Frontend tickets: `npm run -s build` + `npm run -s lint` + `npm test -- --runInBand`
- Governance tickets: `node scripts/docs-consistency-check.mjs`

---

## Now

- [ ] APP-013 Twilio-backed notification center and transactional customer messaging (`SCR-APP-021`, `SCR-APP-022`, `SCR-TECH-005`)
  - Split customer/operator review-request foundation is review-ready: encrypted one-time customer submission and authorized request-ID-only operator read, no stored or reconstructed customer bearer. 1492 backend/170 UI tests, ten new PostgreSQL groups and prior browser/crash regressions pass; four audits clean. Original session deadline, stale/closed refusal and exact replay remain. No request-to-job admission or UI/route activation. Next proposed: token-free operator admission from the durable request with atomic job/consent outcome, no external actions. Coverage 50%, acceptance 0/12; 7-12 APP-013 / 20-35 pilot unequal sections, low confidence. APP-013 stays Now.

## Next

## Later

- [ ] FE-014 Competitive comparison pages (`SCR-PUB-017`, `SCR-PUB-018`) - paused by owner-approved CallDesk-first focus
- Remaining MVP epics in `MVP_BACKLOG.md`

## Blockers

- The APP-003 completion API has no public or operator UI; real job completion remains a protected operator action and requires confirmed field status.

## Done

- [x] BE-008 Twilio communications foundation
  - Backend PRs `#15`, `#16`, and `#18`; staging acceptance verified signed voice/SMS, tenant isolation, STOP/START, exactly-once consented delivery, terminal status callback, simulated rejection, dead-letter visibility, acknowledgment-gated replay, restored quiet-hour policy, and disabled-by-default outbound delivery. Evidence: `signmons-calldesk-backend/evidence/BE-008/readiness-report.md`.
- [x] APP-012 Payment gate and webhook status workflow (`SCR-APP-006A`, `SCR-APP-006B`, `SCR-APP-006C`, `SCR-APP-023`, `SCR-CUST-002`)
  - Backend PR `#14` merged at `068f4c2`; Cloud Build `dd7ca7ec-1777-45b6-8659-fba8998a9b63`; migration `signmons-calldesk-migrate-pgr84`; Cloud Run revision `signmons-calldesk-staging-app012release`; Firebase payment/dispatch routes published; automatic Stripe sandbox delivery and duplicate retry passed. Live mode remains separately approval-gated.
- [x] APP-011 Customer booking status and confirmation flow (`SCR-CUST-001`, `SCR-CUST-003`)
  - Backend PR `#13` merged at `28d394f`; migration `signmons-calldesk-migrate-xztrh`; Cloud Run revision `signmons-calldesk-staging-00024-wwn`; customer page `https://signmons-calldesk.web.app/appointment/manage`; release evidence in `signmons-calldesk-backend/evidence/APP-011/readiness-report.md`.
- [x] APP-010 Routing rules, service areas, and availability (`SCR-APP-015`, `SCR-APP-016`, `SCR-APP-024`, `SCR-TECH-004`)
  - Backend PR `#11` merged at `b809b9d`; Cloud Run revision `signmons-calldesk-staging-00023-47g`; Firebase console `https://signmons-calldesk.web.app/app/routing`; isolated staging acceptance verified strict ZIP, available/on-call constraints, `routing-v1` evaluation and an eligible `dispatch-v2` recommendation on 2026-09-02.
- [x] APP-009 Technician mobile job workflow (`SCR-TECH-001`, `SCR-TECH-002`, `SCR-TECH-003`)
  - Backend commit `413b671`; Cloud Run revision `signmons-calldesk-staging-00021-boh`; technician UI `https://signmons-calldesk.web.app/app/technician`; owner confirmed authenticated real-phone list/detail/action and dispatcher status/audit acceptance on 2026-09-02.
- [x] APP-008 Dispatch board and technician assignment (`SCR-APP-014`, `SCR-APP-017`)
  - Backend merge `d8de259`; Cloud Build `5dca0dd5-3c59-4968-b19b-d6e1bdee23d6`; Cloud Run revision `signmons-calldesk-staging-00020-m2m`; console `https://signmons-calldesk.web.app/app/dispatch`; evidence in `signmons-calldesk-backend/evidence/APP-008/readiness-report.md`.
- [x] APP-007 Urgency classification and escalation review (`SCR-APP-013`)
  - Backend commit `afb3644`; migration execution `signmons-calldesk-migrate-fp7rp`; Cloud Run revision `signmons-calldesk-staging-00019-swf`; console `https://signmons-calldesk.web.app/app/urgency-review`; evidence in `signmons-calldesk-backend/evidence/APP-007/readiness-report.md`.
- [x] APP-006 Intake review and booking readiness (`SCR-APP-012`)
  - Backend merge `2b715e4`; release configuration merge `2c3e608`; Cloud Run revision `signmons-calldesk-staging-00018-mxr`; console `https://signmons-calldesk.web.app/app/intake-review`; evidence in `signmons-calldesk-backend/evidence/APP-006/readiness-report.md`.
- [x] APP-003 Job completion lifecycle foundation (`SCR-APP-005`)
  - Backend commit `55d59de`; Cloud Run revision `signmons-calldesk-staging-00016-jz9`; evidence in `signmons-calldesk-backend/evidence/APP-003/readiness-report.md`.
- [x] BE-007 Tenant lead-source reporting pilot (`SCR-APP-018`, `SCR-APP-019`)
  - Backend commit `8264c74`; Cloud Run revision `signmons-calldesk-staging-00015-7hq`; evidence in `signmons-calldesk-backend/evidence/BE-007/readiness-report.md`.
- [x] BE-003 Eternity webchat backend production readiness (`SCR-CUST-006`)
- [x] GOV-001 Bootstrap governance docs
- [x] GOV-002 Cross-repo docs pointers (`DOCS_INDEX.md`)
- [x] GOV-004 PWA dispatch governance re-baseline
  - Ticket specs: `TICKETS/GOV-004.md`, `TICKETS/APP-006.md` ... `TICKETS/APP-015.md`
- [x] FE-001 Marketing Home (`SCR-PUB-001`)
- [x] FE-002 Public trust/compliance pages (`SCR-PUB-005`, `SCR-PUB-010`)
- [x] FE-003 Reusable component refactor (`SCR-PUB-001`, `SCR-PUB-007`, `SCR-PUB-009`)
- [x] FE-004 Pricing reposition (`SCR-PUB-006`)
- [x] FE-005 Pricing consistency analyzer and CI enforcement (`SCR-PUB-006`)
- [x] FE-007 Contact capture email-minimum with backend persistence (`SCR-PUB-009`)
- [x] FE-008 Live demo flow + CTA route parity hardening (`SCR-PUB-001`, `SCR-PUB-006`, `SCR-PUB-007`, `SCR-PUB-009`)
- [x] FE-006 Privacy + Terms + SMS terms route/content parity (`SCR-PUB-010`)
- [x] FE-009 Done-for-you setup page (`SCR-PUB-011`)
- [x] FE-010 Business rules and custom logic page (`SCR-PUB-012`)
- [x] FE-011 Brand voice and AI personality page (`SCR-PUB-013`)
- [x] FE-012 Dispatch and scheduling page (`SCR-PUB-014`)
- [x] FE-013 Revenue dashboard and ROI calculator (`SCR-PUB-015`, `SCR-PUB-016`)
  - Frontend commit `f8a83ef`; evidence in `signmons-marketing-web-feat-marketing-site/evidence/FE-013/`.
- [x] GOV-008 High-ticket surface expansion
- [x] GOV-009 Contract/policy lock + route matrix traceability

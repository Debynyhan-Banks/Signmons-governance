# Signmons Execution Board

Purpose: single active queue for execution.

## Operating Rules

1. WIP limit is 1 (`Now` only).
2. No coding without a ticket in `Now`.
3. Do not pull from `Later` directly to `Now`.
4. Every completed ticket includes objective evidence.
5. Update this board before changing scope.
6. Ticket completion must satisfy `QUALITY_GATES.md`.
7. Owner-approved CallDesk-first execution supersedes the marketing-first pointer while APP-006 is active; paused marketing work remains governed by `MARKETING_RELEASE_DOD.md` when resumed.

## Required Completion Gates

- Backend tickets: `npm run -s build` + `npm test -- --runInBand` + `npm run -s arch:check`
- Frontend tickets: `npm run -s build` + `npm run -s lint` + `npm test -- --runInBand`
- Governance tickets: `node scripts/docs-consistency-check.mjs`

---

## Now

- [ ] APP-006 Intake review and booking readiness (`SCR-APP-012`)

## Next

- [ ] APP-007 Urgency classification and escalation review (`SCR-APP-013`)

## Later

- [ ] FE-014 Competitive comparison pages (`SCR-PUB-017`, `SCR-PUB-018`) - paused by owner-approved CallDesk-first focus
- Remaining MVP epics in `MVP_BACKLOG.md`

## Blockers

- The APP-003 completion API has no public or operator UI; real job completion remains a protected operator action and requires confirmed field status.

## Done

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

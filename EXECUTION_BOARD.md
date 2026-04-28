# Signmons Execution Board

Purpose: single active queue for execution.

## Operating Rules

1. WIP limit is 1 (`Now` only).
2. No coding without a ticket in `Now`.
3. Do not pull from `Later` directly to `Now`.
4. Every completed ticket includes objective evidence.
5. Update this board before changing scope.
6. Ticket completion must satisfy `QUALITY_GATES.md`.
7. Marketing-first phase remains active until `MARKETING_RELEASE_DOD.md` exit criteria are met.

## Required Completion Gates

- Backend tickets: `npm run -s build` + `npm test -- --runInBand` + `npm run -s arch:check`
- Frontend tickets: `npm run -s build` + `npm run -s lint` + `npm test -- --runInBand`
- Governance tickets: `node scripts/docs-consistency-check.mjs`

---

## Now

- [ ] FE-008 Live demo flow + CTA route parity hardening (`SCR-PUB-001`, `SCR-PUB-006`, `SCR-PUB-007`, `SCR-PUB-009`)

## Next

- [ ] FE-006 Privacy + Terms + SMS terms route/content parity (`SCR-PUB-010`)
- [ ] APP-006 Intake review and booking readiness (`SCR-APP-012`) - unlocks after marketing DoD exit criteria

## Later

- Remaining MVP epics in `MVP_BACKLOG.md`

## Blockers

- None recorded

## Done

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
  - Implementation commit: `83a1edb feat(fe-007): persist contact leads with email-min validation`
  - Evidence: pending backfill under `signmons-marketing-web-feat-marketing-site/evidence/FE-007/` (carry-forward task)

# Signmons Execution Board

Purpose: single active queue for execution.

## Operating Rules

1. WIP limit is 1 (`Now` only).
2. No coding without a ticket in `Now`.
3. Do not pull from `Later` directly to `Now`.
4. Every completed ticket includes objective evidence.
5. Update this board before changing scope.
6. Ticket completion must satisfy `QUALITY_GATES.md`.

## Required Completion Gates

- Backend tickets: `npm run -s build` + `npm test -- --runInBand` + `npm run -s arch:check`
- Frontend tickets: `npm run -s build` + `npm run -s lint` + test command for touched surface

---

## Now

- [ ] FE-001 Marketing Home (`SCR-PUB-001`)
  - Source: `MVP_BACKLOG.md`
  - Ticket spec: `TICKETS/FE-001.md`
  - Evidence required: acceptance checklist complete + frontend gate output + screenshot proof

## Next

- [ ] FE-002 Public trust/compliance pages (`SCR-PUB-005`, `SCR-PUB-010`)
- [ ] BE-001 Enforce keyword opt-in/out persistence and telemetry
- [ ] FE-003 AI CSR page (`SCR-PUB-003`)

## Later

- Remaining MVP epics in `MVP_BACKLOG.md`

## Blockers

- None recorded

## Done

- [x] GOV-001 Bootstrap governance docs
- [x] GOV-002 Cross-repo docs pointers (`DOCS_INDEX.md`)

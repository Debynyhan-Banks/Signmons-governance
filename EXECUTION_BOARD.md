# Signmons Execution Board

Purpose: single active queue for execution.

## Operating Rules

1. WIP limit is 1 (`Now` only).
2. No coding without a ticket in `Now`.
3. Do not pull from `Later` directly to `Now`.
4. Every completed ticket includes objective evidence.
5. Update this board before changing scope.

## Required Completion Gates

- Backend tickets: `npm run -s build` + `npm test -- --runInBand` + `npm run -s arch:check`
- Frontend tickets: `npm run -s build` + `npm run -s lint` + test command for touched surface

---

## Now

- [ ] GOV-001 Bootstrap governance docs and cross-repo pointers

## Next

- [ ] FE-001 Marketing Home (`SCR-PUB-001`)
- [ ] FE-002 Public trust/compliance pages (`SCR-PUB-005`, `SCR-PUB-010`)
- [ ] BE-001 Enforce keyword opt-in/out persistence and telemetry

## Later

- Remaining MVP epics in `MVP_BACKLOG.md`

## Blockers

- None recorded

## Done

- None yet

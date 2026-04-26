# Workflow Runbook

Purpose: repeatable execution flow usable by any coding bot or human contributor.

## Session Start (Mandatory)

1. Open governance source of truth docs:
   - `SYSTEM_OF_RECORD.md`
   - `SAAS_SCOPE_DOD.md`
   - `EXECUTION_BOARD.md`
   - `GLOBAL_EXECUTION_POINTER.md`
   - `SCREEN_INVENTORY.md`
   - `MVP_BACKLOG.md`
   - `QUALITY_GATES.md`
   - `AI_WORKFLOW_RULES.md`
   - `SESSION_HANDOFF.md`
2. Confirm exactly one `Now` ticket.
3. Confirm per-repo board alignment with `GLOBAL_EXECUTION_POINTER.md`.

## Execution Rules

- Strict sequencing only.
- Execute only the current `Now` ticket.
- One focused commit.
- No scope expansion.
- Archive superseded docs immediately in the same PR.

## Required Gates

- Governance docs check: `node scripts/docs-consistency-check.mjs`
- Frontend ticket gates: `npm run -s build`, `npm run -s lint`, `npm test -- --runInBand`
- Backend ticket gates: `npm run -s build`, `npm test -- --runInBand`, `npm run -s arch:check`

## End Of Session

- Update `SESSION_HANDOFF.md`.
- Update evidence paths.
- Move ticket state in board only after gates + evidence pass.

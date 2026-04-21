# AI Workflow Rules

## Session Start Contract

Before coding, the AI agent must read:

- `SAAS_SCOPE_DOD.md`
- `EXECUTION_BOARD.md`
- `MVP_BACKLOG.md`
- `SCREEN_INVENTORY.md`
- `SESSION_HANDOFF.md`

## Execution Rules

- Execute only the current `Now` ticket
- No scope expansion
- One focused commit per ticket
- Report file changes and rationale
- Run required gates for touched repo
- Update `SESSION_HANDOFF.md` before ending session

## Reporting Format

- Ticket ID
- Scope completed
- Files changed
- Tests/gates run with outcomes
- Risks and follow-up
- Exact commit message/hash

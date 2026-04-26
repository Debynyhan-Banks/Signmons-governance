# AI Workflow Rules

## Session Start Contract

Before coding, the AI agent must read:

- `SYSTEM_OF_RECORD.md`
- `SAAS_SCOPE_DOD.md`
- `EXECUTION_BOARD.md`
- `GLOBAL_EXECUTION_POINTER.md`
- `SCREEN_INVENTORY.md`
- `MVP_BACKLOG.md`
- `QUALITY_GATES.md`
- `SESSION_HANDOFF.md`

## Execution Rules

- Execute only the current `Now` ticket.
- No scope expansion.
- One focused commit per ticket.
- Enforce `QUALITY_GATES.md` before marking ticket complete.
- Run `node scripts/docs-consistency-check.mjs` for governance PRs.
- Archive superseded docs/tickets in the same PR.
- Update `SESSION_HANDOFF.md` before ending session.
- Report changed files, rationale, gates, and risks.

## Cross-Repo Alignment Rules

- Per-repo `EXECUTION_BOARD.md` files must align with `GLOBAL_EXECUTION_POINTER.md`.
- If any board diverges from the global pointer, fix board state before coding feature work.
- Demo and contact CTAs must be mapped in both `SCREEN_ROUTE_API_MATRIX.md` and `LINK_CTA_MAP.md`.

## Reporting Format

- Ticket ID
- Scope completed
- Files changed
- Tests/gates run with outcomes
- Risks and follow-up
- Exact commit message/hash

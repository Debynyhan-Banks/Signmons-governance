# AI Workflow Rules

## Session Start Contract

Before coding, the AI agent must read:

- `SYSTEM_OF_RECORD.md`
- `WHAT_SIGNMONS_IS_AND_DOD.md`
- `SAAS_SCOPE_DOD.md`
- `MARKETING_RELEASE_DOD.md`
- `EXECUTION_BOARD.md`
- `GLOBAL_EXECUTION_POINTER.md`
- `SCREEN_INVENTORY.md`
- `SCREEN_ROUTE_API_MATRIX.md`
- `LINK_CTA_MAP.md`
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

## Marketing-First Phase Rule

- While `MARKETING_RELEASE_DOD.md` is active, APP ticket implementation is blocked unless `EXECUTION_BOARD.md` and `GLOBAL_EXECUTION_POINTER.md` move `Now` to APP explicitly.
- FE-007 must complete before FE-008; FE-008 must complete before APP-006 unlock.

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

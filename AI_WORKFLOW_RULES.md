# AI Workflow Rules

## Owner-reviewed intelligence dependency alignment (2026-09-12)

Owner reviewed PRs #28/#22 and requested the six-ticket dependency correction. APP-013 remains sole Now (2B). Next: APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033. BE-001 residual acceptance belongs to APP-013; nothing is marked complete. Older dated Next-empty/proposal-only sections are historical, superseded for sequence and pilot scope only. See INTELLIGENCE_ALIGNMENT_ADOPTION.md. No merge, deployment, feature implementation or training is authorized by this documentation correction.

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

- Owner-reviewed queue progression: complete the entire Now acceptance and required human/provider evidence, synchronize both boards/global pointer, then promote the first approved Next. Do not ask for routine phase selection; do not skip blocked Now or treat a mock as live proof. This does not grant merge/deploy/IAM/secrets, customer-contact, billing or training permission. Save a resumable checkpoint when required authority is missing.

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

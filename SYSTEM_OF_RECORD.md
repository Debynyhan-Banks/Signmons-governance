# System Of Record

Purpose: establish one unambiguous source-of-truth hierarchy so any coding agent can execute without contradiction.

## Canonical Precedence

If docs conflict, resolve in this exact order:

1. `SYSTEM_OF_RECORD.md`
2. `SAAS_SCOPE_DOD.md`
3. `EXECUTION_BOARD.md`
4. `SCREEN_INVENTORY.md`
5. `MVP_BACKLOG.md`
6. `DATA_CONTRACTS.md`
7. `QUALITY_GATES.md`
8. `AI_WORKFLOW_RULES.md`
9. `SESSION_HANDOFF.md`

All other docs are reference-only unless explicitly listed above.

## Canonical Artifacts

- Program charter and DoD: `SAAS_SCOPE_DOD.md`
- Active execution queue: `EXECUTION_BOARD.md`
- Global cross-repo state: `GLOBAL_EXECUTION_POINTER.md`
- Screen IDs: `SCREEN_INVENTORY.md`
- Delivery roadmap: `MVP_BACKLOG.md`
- Screen/route/API mapping: `SCREEN_ROUTE_API_MATRIX.md`
- CTA/link behavior map: `LINK_CTA_MAP.md`
- API/event contract policy: `DATA_CONTRACTS.md`
- Required quality gates: `QUALITY_GATES.md`
- Agent workflow contract: `AI_WORKFLOW_RULES.md`
- Session continuity: `SESSION_HANDOFF.md`

## Non-Contradiction Rules

- Every ticket must reference screen IDs from `SCREEN_INVENTORY.md` only.
- Every public CTA route must exist in `SCREEN_ROUTE_API_MATRIX.md` and `LINK_CTA_MAP.md`.
- `Now` ticket in `EXECUTION_BOARD.md` must be unique (WIP=1).
- Superseded docs/tickets must be moved to `ARCHIVE/` in the same PR.

## Strict Sequencing Rule

- Execute exactly one `Now` ticket at a time.
- Do not start `Next` until `Now` is moved to `Done` with evidence.

## CI Enforcement

PRs must pass docs consistency checks:

- screen IDs exist and are unique,
- `Now` section contains exactly one unchecked ticket,
- ticket screen references resolve,
- CTA map routes resolve against route matrix,
- superseded tickets are not referenced in `Now`/`Next`.

# Global Execution Pointer

Purpose: single cross-repo index of active work while keeping per-repo boards.

## Canonical Repo Boards

- Governance board:
  - Repo: `signmons-governance`
  - Board: `EXECUTION_BOARD.md`
- Backend board:
  - Repo: `signmons-calldesk-backend`
  - Board: `EXECUTION_BOARD.md`
- Frontend marketing board:
  - Repo: `signmons-marketing-web-feat-marketing-site`
  - Board: `EXECUTION_BOARD.md`

## Current Pointer (as of 2026-04-28)

- Program `Now`: `FE-008` (`SCR-PUB-001`, `SCR-PUB-006`, `SCR-PUB-007`, `SCR-PUB-009`)
- Previous `Now`: `FE-007` (completed; implementation commit `83a1edb`)
- Program phase: marketing-first high-ticket completion
- Sequencing: strict (`Now` -> `Done` before starting `Next`)

### Repo Status

| Repo | Active Ticket | State |
| --- | --- | --- |
| Governance | `FE-008` pointer + standards alignment owner | active |
| Frontend marketing | `FE-008` implementation owner (branch `codex/fe-008-live-demo-parity`) | active |
| Backend | support `POST /api/marketing/try-demo` provider alignment for FE-008 | supporting |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

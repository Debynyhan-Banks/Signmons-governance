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

- Program `Now`: `FE-006` (`SCR-PUB-010`)
- Program phase: marketing-first high-ticket completion
- Sequencing: strict (`Now` -> `Done` before starting `Next`)

### Repo Status

| Repo | Active Ticket | State |
| --- | --- | --- |
| Governance | `FE-006` standards and alignment owner | active |
| Frontend marketing | `FE-006` implementation owner | active |
| Backend | support endpoint/provider alignment for FE-006 | supporting |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

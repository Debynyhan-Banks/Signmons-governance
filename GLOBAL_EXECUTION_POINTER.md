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

## Current Pointer (as of 2026-04-26)

- Program `Now`: `APP-006` (`SCR-APP-012`)
- Sequencing: strict (`Now` -> `Done` before starting `Next`)

### Repo Status

| Repo | Active Ticket | State |
| --- | --- | --- |
| Governance | `APP-006` pointer and standards enforcement | aligned |
| Backend | `APP-006` implementation owner | active next execution repo |
| Frontend marketing | no active implementation ticket (blocked by strict sequencing) | standby |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

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

## Current Pointer (as of 2026-08-30)

- Program `Now`: `BE-007` (tenant lead-source reporting pilot)
- Program phase: owner-approved Eternity pilot reporting exception; marketing-first work resumes at FE-013 after BE-007 completion
- Sequencing: strict (`Now` -> `Done` before starting `Next`)

### Repo Status

| Repo | Active Ticket | State |
| --- | --- | --- |
| Governance | BE-007 contract and evidence alignment | active |
| Frontend marketing | `FE-013` revenue dashboard and ROI calculator | queued |
| Backend | `BE-007` tenant lead-source reporting pilot | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

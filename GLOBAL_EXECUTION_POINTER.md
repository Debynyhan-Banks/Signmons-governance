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

## Current Pointer (as of 2026-09-09)

- Program `Now`: `APP-013` (Twilio-backed notification center and transactional customer messaging)
- Program phase: owner-approved CallDesk-first product execution; `FE-014` is paused, not cancelled
- Sequencing: strict (`Now` -> `Done` before starting `Next`)

### Repo Status

| Repo               | Active Ticket                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | State  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Governance         | APP-013 contract and communications-boundary alignment                                                                                                                                                                                                                                                                                                                                                                                                                                                              | active |
| Frontend marketing | `FE-014` competitive comparison pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | paused |
| Backend | `APP-013` inactive subscribed Calendar review panel/browser HTTP integration is review-ready at a42f0a42660cb148734e67e81985a4765cc5bfae on PR #21: 20 real GETs/20 CORS preflights, six cancelled delayed reads, 135 UI/962 backend tests and regressions/audits pass. UI unlinked/controller unregistered. Next agreed step is acceptance-gap review and user-facing workflow prioritization; production/provider/recovery/release risks remain gated; BE-008 accepted | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

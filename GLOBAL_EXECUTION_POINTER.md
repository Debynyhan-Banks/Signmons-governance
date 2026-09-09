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
| Backend | `APP-013` inactive Calendar review HTTP adapter/session binding is review-ready on PR #21 at 39a2c9b20a136c428979d027cc8bd45a70cc178f: bearer-only fixed GETs, explicit origin, non-secret generations, bounded cancellation/body parsing; 36 new UI cases/135 total plus 16-GET native HTTP proof and backend/DB/audit gates pass. Pointer/step placement fixed with regression checks. UI unlinked/controller unregistered; browser composition, live acceptance and timing/provider/release risks remain open; BE-008 accepted | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

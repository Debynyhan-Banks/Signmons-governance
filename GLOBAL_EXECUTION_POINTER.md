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

- Approved first-pilot scope and acceptance plan: [CALLDESK_MVP_PLAN.md](CALLDESK_MVP_PLAN.md). One approved business, English, online access and human supervision; full platform roadmap deferred, not cancelled. Future milestone order is planning, not automatic ticket promotion.

### Repo Status

| Repo               | Active Ticket                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | State  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Governance         | APP-013 contract and communications-boundary alignment                                                                                                                                                                                                                                                                                                                                                                                                                                                              | active |
| Frontend marketing | `FE-014` competitive comparison pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | paused |
| Backend | `APP-013` tenant-scoped email recipient snapshot review-ready/inactive at 540cbc7245cf169df88bfaa4ee8b45a8cd663c25 on PR #21: private captured recipient, stale/lifecycle/Calendar/ambiguity refusals; 1128 backend/159 UI tests, 6 successful/26 refused database reads and browser/audit gates pass. No delivery authorization, runtime registration, credential issuance or sending. Scope coverage stays 50%, acceptance 0/12; reassessed pilot allowance 20-35 unequal sections, low confidence, not ETA. Stop for review; next proposed independent default-off email event controls. BE-008 accepted | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

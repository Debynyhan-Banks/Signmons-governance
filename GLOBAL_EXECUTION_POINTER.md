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

## Current Pointer (as of 2026-09-10)

- Program `Now`: `APP-013` (Twilio-backed notification center and transactional customer messaging)
- Program phase: owner-approved CallDesk-first product execution; `FE-014` is paused, not cancelled
- Sequencing: strict (`Now` -> `Done` before starting `Next`)

- Approved first-pilot scope and acceptance plan: [CALLDESK_MVP_PLAN.md](CALLDESK_MVP_PLAN.md). One approved business, English, online access and human supervision; full platform roadmap deferred, not cancelled. Future milestone order is planning, not automatic ticket promotion.

### Repo Status

| Repo               | Active Ticket                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | State  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Governance         | APP-013 contract and communications-boundary alignment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | active |
| Frontend marketing | `FE-014` competitive comparison pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | paused |
| Backend            | `APP-013` Local human-reviewed intake admission is review-ready: exact protected session/transcript plus verified owner/admin/dispatcher authority atomically create a CREATED job/customer/address/link/audit, bind any existing immutable email-consent history, and close the session. 1471 backend/170 UI tests, nine new PostgreSQL groups and prior browser/crash regressions pass; four audits clean. The service is unregistered; no preferred window, booking, payment, Calendar, notification, provider or sending action. Next proposed: a durable split customer/operator review-request boundary before any UI/route integration, without exposing the customer bearer credential. Coverage 50%, acceptance 0/12; retain 7-12 APP-013 / 20-35 pilot unequal sections, low confidence. APP-013 stays Now. Exact backend commit in latest SESSION_HANDOFF.md. No release authority; BE-008 accepted | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

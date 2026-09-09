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
| Backend | `APP-013` inactive consent evidence/schema and one-time job binding review-ready; exact backend commit in latest SESSION_HANDOFF.md checkpoint. D1-D4 approved; no production customer authority or fingerprint adapter/key, collection, verification, positive eligibility, event grant binding, expiry enforcement, queue or sending. 1261 backend/170 UI tests; 19 local migrations, 24 consent checks, existing 19 crash cases/23 eligibility reads, local browser proof and four clean audits. Retention RESTRICT compatibility remains a release gate. Coverage 50%, acceptance 0/12; 7-12 APP-013 / 20-35 pilot unequal sections, low confidence. Next proposed: authenticated structured customer-response/mailbox binding plus fingerprint key-lifecycle review. No release authority; BE-008 accepted | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

# Global Execution Pointer

## Organization setup slice (2026-09-10, latest review-ready)

Backend checkpoint: `d7821e1`, pushed on `codex/app-013-transactional-messaging` (PR #21), incremental `df63faa..d7821e1`.

Completed the owner-approved S0 page/API slice within the explicitly amended APP-013 steel-thread dependency. Company facts, greeting/tone and sourced FAQs save to a tenant-scoped draft; exact saved-version approval preserves a separate approved snapshot; deterministic FAQ or human-contact fallback preview uses only that snapshot. Source routes are registered and the root sandbox links to /app/organization; nothing is deployed. No runtime AI, customer-journey/job connection, canonical policy changes or provider calls. Details and exact commands: backend evidence/APP-013/organization-setup/README.md; governance DATA_CONTRACTS.md.

Validation: 1511 backend tests (19 new), 170 UI tests, lint/build/architecture/Prisma and four clean dependency audits. Seven local database/browser proof groups cover concurrency, audit rollback, tenant/role refusal, draft/approval separation, desktop/mobile and stale-save recovery. Fixture identity is explicitly substituted, not production Firebase acceptance. Temporary databases removed; cleanup query empty. No migration/package changes. Profile facts do not configure scheduler timezone or replace payment/routing policies; manual consistency review is still required. Exact-match preview is not semantic AI or automatic human-task creation.

Progress: onboarding 3/6 = 50% locally demonstrated outcomes (O1/O3/O4), 0/6 = 0% formally accepted. APP-013 recorded scope coverage remains 50%, formal acceptance 0/12 = 0%; pilot acceptance 0/12 = 0%. These are distinct denominators, not an engineering ETA. Next after owner review: connect the approved organization snapshot to the protected customer intake/operator request-to-job path, preserving tenant/revision authority and no external actions. Full steel thread is not complete. APP-013 stays sole Now; Next empty; FE-014 paused. No merge/deploy, production migration, IAM/secrets/billing, real-data/provider or charge authority.

## Approved steel-thread implementation (2026-09-10, current)

Owner said “great proceed” after selecting the organization-to-job walkthrough. APP-013 explicitly owns the bounded S0 setup dependency for this walkthrough: owner/admin organization draft, version approval and deterministic FAQ/fallback preview with a usable page. This is an explicit scoped amendment, not APP-033 promotion. Reuse tenant settings and auth; no change to canonical booking/payment/routing policies. APP-013 stays sole Now; Next empty; FE-014 paused. Full customer-to-job integration follows review, not automatic completion. Live AI/provider calls and all release actions remain disabled. Acceptance percentages remain unchanged until evidence and owner acceptance.

## Organization setup and progress baseline (2026-09-10, latest planning)

Owner approved organization-onboarding gap review and requested percentages. See governance `ORGANIZATION_ONBOARDING_MVP.md`: basic tenant name/instructions and separate settings exist, but no organization onboarding page or approved FAQ/voice workflow was found in the inspected feature tree. Proposed next milestone S0 is owner-approved organization facts/rules/FAQ/brand voice with local answer preview, before S1 intake-to-job. Map implementation ownership and align governance before coding; APP-013 remains sole Now, Next unassigned, FE-014 paused. This is not automatic APP-033 promotion or an APP-013 scope expansion.

Progress baseline: APP-013 **50% recorded scope coverage** (1 demonstrated + 10 partial at half weight + 1 missing, divided by 12), **0/12 = 0% formal acceptance**; organization onboarding **0/6 = 0% acceptance**; full pilot **0/12 = 0% acceptance** against the existing pilot checklist. These are separate denominators, not effort, release readiness or an overall build percentage. Onboarding refines the existing business-controls requirement; do not add its six checks to the pilot denominator. No new engineering completion percentage or ETA is inferred. This documentation-only update does not rerun earlier runtime/security gates or claim new acceptance.

## MVP steel-thread audit (2026-09-10, current planning checkpoint)

Owner requested a fixed MVP/steel-thread audit before more coding. See governance `CALLDESK_STEEL_THREAD_CLOSEOUT.md` for the twelve-criterion ledger and four outcome milestones. This supersedes earlier next-section suggestions and rolling 7–12 APP-013 / 20–35 pilot forecasts; historical percentages are not completion estimates. APP-013 remains sole Now, acceptance 0/12; Next unassigned, FE-014 paused. No scope reduction, ticket promotion or release authority. Recommended next decision: approve web chat as the first proving channel and target a usable customer/operator intake-to-job journey, retaining phone/SMS in the full MVP. No implementation is authorized by this planning checkpoint. Backend implementation remains 670e973; this change is documentation only.

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
| Backend | `APP-013` Split customer/operator review-request foundation is review-ready: encrypted one-time customer submission and authorized request-ID-only operator read, no stored or reconstructed customer bearer. 1492 backend/170 UI tests, ten new PostgreSQL groups and prior browser/crash regressions pass; four audits clean. Original session deadline, stale/closed refusal and exact replay remain. No request-to-job admission or UI/route activation. Next proposed: token-free operator admission from the durable request with atomic job/consent outcome, no external actions. Coverage 50%, acceptance 0/12; 7-12 APP-013 / 20-35 pilot unequal sections, low confidence. APP-013 stays Now. Exact backend commit in latest SESSION_HANDOFF.md. No release authority; BE-008 accepted | active |

## Synchronization Rules

- Update this file whenever `Now` changes.
- Per-repo `EXECUTION_BOARD.md` files must agree with this pointer.
- If any repo board diverges, treat as blocker and fix before coding.

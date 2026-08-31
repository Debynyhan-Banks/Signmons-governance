# Session Handoff

Last Updated: 2026-08-30

## Owner-Approved Product Direction (2026-08-30)

- Owner approved Signmons as one AI front-office and dispatch platform with governed CallDesk, Dispatch, Money, Field, Customers, Growth, and Intelligence modules.
- Professional estimates/invoices/payment links/receipts are a core paid-plan capability after the Signmons Money release gate; Signmons does not become general-ledger accounting.
- Approved delivery sequence is recorded in `WHAT_SIGNMONS_IS_AND_DOD.md`; new work cannot bypass the active governance pointer.
- Approved limited Founding Partner bridge: `$199/mo` + `$299` setup for the first `10` approved external businesses, with a `12`-month price lock while active.
- Public target ladder remains `$299/$799/$1,499/from $3,500`, subject to implementation and claim-evidence gates.
- Per-tier call overages replace the unsupported `$99/250 calls` target; performance fees remain disabled by default until attribution and dispute safeguards ship.
- FE-016 pricing reconciliation is complete on marketing branch `codex/fe-016-pricing-reconcile` at commit `83462ec`: the public ladder, setup fees, annual discounts, per-tier overages, Founding Partner disclosure, planned invoicing boundary, provider-fee disclosure, add-ons, tests, and `pricing:check` now match governance. Publishing/merging remains a separate operation.

## Current Program Pointer

- Global `Now`: `FE-013` (revenue dashboard and ROI calculator).
- Completed exception: `BE-003` (Eternity webchat backend production readiness).
- Completed exceptions: `BE-007` lead-source reporting and `APP-003` audited job completion.
- Program phase: marketing-first work resumed after APP-003 completion.
- Sequencing: strict (`Now` -> `Done` before `Next`).

## FE-012 Completion Context

- Repo: `signmons-marketing-web-feat-marketing-site`.
- Branch: `codex/fe-012-dispatch-scheduling` (cut from clean `main`; HEAD on `53c4eef`).
- Screen: `SCR-PUB-014` -> route `/dispatch-scheduling` (matrix now `implemented`).
- Acceptance criteria (`TICKETS/FE-012.md`) all satisfied; see `evidence/FE-012/parity-checklist.md`:
  - AC-1 Route registered (`/dispatch-scheduling` + `.html` + `/site/...html`).
  - AC-2 Page sections aligned to `MARKETING_SITEMAP.md` Sprint 2 contract: Dispatch Board (4 lanes), Routing Logic (3 rules), Scheduling Lifecycle (4 steps), Policy Integrity governance.
  - AC-3 CTAs map to `LINK_CTA_MAP.md` pattern (Book Revenue Demo -> `/contact`, See Live Demo -> `/demo`); reuses Business Rules / Brand Voice page CTA contract.
  - AC-4 Frontend gates green: `npm run -s build` (343 modules, 1.41s), `npm run -s lint` (clean), `npm test -- --runInBand` (10 files / 22 tests).
- Files touched (per `evidence/FE-012/parity-checklist.md`):
  - `src/types/site.ts`, `src/data/siteContent.ts`
  - `src/pages/site/SiteDispatchScheduling.tsx`, `src/pages/site/SiteDispatchScheduling.test.tsx`
  - `src/styles/site/dispatch-scheduling.css`
  - `src/App.tsx`, `src/main.tsx`
  - `evidence/FE-012/{build,lint,test,parity-checklist,mapping}`
- One focused commit on the FE-012 branch:
  - `235b0aa feat(fe-012): add dispatch and scheduling public page`.
- Non-goals respected: no backend dispatch implementation changes; no APP screen implementation. `SchedulingWindow` / `Appointment` / `DispatchPolicy` remain display dependencies (APP-016 / APP-017 own runtime contracts).

## Completed In This Session

- Completed APP-003 on backend branch `codex/residential-calendar-booking` at implementation commit `55d59de`; deployment evidence is recorded at docs commit `35a49b5`.
- Deployed Cloud Run revision `signmons-calldesk-staging-00016-jz9` with image `55d59de` at 100 percent traffic.
- Verified readiness and a sanitized unauthenticated HTTP 401 using a non-existent job UUID; no real customer job was changed.
- Full backend gates passed: build, 98 tests and architecture check; focused APP-003 lint passed.
- Completed BE-007 on backend branch `codex/residential-calendar-booking` at commit `8264c74`.
- Deployed Cloud Run revision `signmons-calldesk-staging-00015-7hq` at 100 percent traffic; health passed and the live reporting route rejected unauthenticated access with HTTP 401.
- Verified the August Eternity aggregate without selecting customer PII: 8 created, 5 booked, 0 completed, 1 cancelled, 1 attributed and 7 legacy unattributed jobs.

- Completed BE-003 on backend branch `codex/be-003-eternity-webchat-readiness` at commit `9586d9c`.
- Verified clean install, PostgreSQL 16 migrations with legacy preservation, 38 tests, lint, build, architecture, compiled runtime health/auth/safety smoke checks, and zero critical production advisories.
- Added tenant-bound hashed webchat credentials and deterministic life-safety interception without connecting the live Eternity website.
- Returned the global execution pointer to FE-013 after the owner-approved backend exception.
- Verified existing FE-012 implementation on `codex/fe-012-dispatch-scheduling`.
- Authored `evidence/FE-012/parity-checklist.md` and `evidence/FE-012/mapping.md`.
- Refreshed `evidence/FE-012/{build,lint,test}.txt` from current branch state.
- Amended the FE-012 commit to fold the evidence package into one focused commit.
- Recorded FE-012 implementation context here.

## Next Actions (Strict Order)

1. Execute FE-013 under the marketing board and ticket contract.
2. Keep APP-003 completion behind authenticated owner/admin access; do not add a public Eternity control.
3. Do not change a real job without confirmed field completion.

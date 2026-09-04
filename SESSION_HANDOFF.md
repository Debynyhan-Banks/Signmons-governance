# Session Handoff

Last Updated: 2026-09-04

## Owner-Approved Product Direction (2026-09-01)

- Owner approved Signmons as one AI front-office and dispatch platform with governed CallDesk, Dispatch, Money, Field, Customers, Growth, and Intelligence modules.
- Professional estimates/invoices/payment links/receipts are a core paid-plan capability after the Signmons Money release gate; Signmons does not become general-ledger accounting.
- Approved delivery sequence is recorded in `WHAT_SIGNMONS_IS_AND_DOD.md`; new work cannot bypass the active governance pointer.
- Owner approved subscription-only Signmons-to-tenant pricing. Signmons does not charge setup, per-call overage, booked-job, emergency-capture, revenue-share, required MVP add-on, or basic per-invoice fees.
- Approved limited Founding Partner bridge: `$199/mo` for the first `10` approved external businesses, with guided setup included and a `12`-month price lock while active.
- Public target ladder remains Starter `$299/mo`, Growth `$799/mo`, Pro `$1,499/mo`, and Enterprise fixed custom monthly/annual subscription.
- Plan capacity is nonfinancial suitability guidance. Approaching or sustained excess usage triggers notification and an agreed fixed-price upgrade, not automatic metered billing.
- Normal Twilio and AI usage is included within plan economics. Contractor-to-customer Stripe payments and processor costs remain separate from Signmons subscription billing.
- Owner approved basic Stripe payment-before-booking enforcement as a core Starter-and-higher entitlement after the Signmons Money release gate. Growth and higher differentiate through advanced deposit, preauthorization, exception, partial-payment, and recovery controls—not exclusive access to the basic gate.
- The earlier setup/overage/performance/add-on policy is superseded. The fixed-subscription marketing and ROI correction was merged in marketing PR `#23` and deployed to Firebase Hosting site `signmons`; repository hosting configuration was corrected in PRs `#24` and `#25`.

## Current Program Pointer

- Global `Now`: `APP-012` (payment gate and webhook status workflow).
- Completed exception: `BE-003` (Eternity webchat backend production readiness).
- Completed exceptions: `BE-007` lead-source reporting and `APP-003` audited job completion.
- Program phase: owner-approved CallDesk-first product execution; `FE-014` is paused, not cancelled.
- Sequencing: strict (`Now` -> `Done` before `Next`).

## APP-012 Review Checkpoint (2026-09-03)

- Backend branch `codex/app-012-payment-gate` implements one bounded payment-before-dispatch gate slice from backend `origin/main` at `8247a0a`.
- A shared reducer derives required payment from the tenant/job policy snapshot and fails closed unless canonical payment status is `SUCCEEDED`.
- Locked jobs remain in `NEW_REQUEST`, produce no eligible recommendation and reject new assignment before mutation or audit creation.
- The dispatcher UI visibly explains the lock and disables assignment; desktop and 390px browser evidence is in `signmons-calldesk-backend/evidence/APP-012/`.
- Backend build/lint, 24 suites and 175 tests, architecture and Prisma validation pass. UI build/lint and 4 suites/17 tests pass.
- Isolated local HTTP proof covered pending lock/HTTP 409/no mutation/no audit and simulated successful canonical state/unlocked recommendation; the fixture was removed.
- No Stripe call or secret configuration, production migration, deployment, IAM, billing or real-data action occurred.
- APP-012 remains active and unreleased. Payment requests, signed/idempotent webhook processing, customer recovery/status and payment-transition auditing remain open.
- Estimated completion: APP-012 approximately 20%; governed APP-006 through APP-016 sequence approximately 56%.

## APP-012 Payment Request Checkpoint (2026-09-04)

- Continued backend branch `codex/app-012-payment-gate` with one bounded server-side payment/deposit request section.
- Backend implementation commit `88d4b3ef001ceb04dc973ddd0263c105f9a6a701` is pushed and remote-verified.
- Authenticated owner/admin/dispatcher endpoints create and track tenant-scoped payment requests. Amount and currency are derived only from the job's policy/pricing snapshots; stale, closed, cross-tenant, incomplete-pricing and unready-account cases fail before provider access.
- Stripe Checkout uses a direct charge on the contractor's enabled connected account and records a zero Signmons application fee. Checkout creation requires a version-4 idempotency key, stores only its SHA-256 hash and does not expose provider identifiers in API/audit projections.
- Request success and bounded provider failure are audited. A replay with the same key does not duplicate the success audit.
- Backend build/lint, 26 suites and 189 tests, architecture and Prisma validation pass. The new migration and authenticated POST/replay/GET path passed in a disposable local PostgreSQL schema, which was removed after proof.
- No real Stripe request, secret/configuration change, staging or production migration, deployment, IAM, billing or real-data action occurred. This backend-only slice changed no rendered UI, so prior responsive gate evidence remains current and no new visual browser artifact was warranted.
- APP-012 remains active and unreleased. Signed/idempotent webhook ingestion, secure customer status/recovery, operator request UI and verified payment/gate transition auditing remain open.
- Estimated completion: APP-012 approximately 40%; governed APP-006 through APP-016 sequence approximately 58%.

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

- Merged APP-011 backend PR `#13` at `28d394f`, applied migration `20260902130000_add_customer_audit_actor` through execution `signmons-calldesk-migrate-xztrh`, deployed Cloud Run revision `signmons-calldesk-staging-00024-wwn`, and published `/appointment/manage` to Firebase Hosting.
- APP-011 live liveness, readiness, CORS and fail-closed secure-link checks passed; owner accepted the customer and dispatcher experiences before release.
- Revoked all temporary build grants and disabled `signmons-build`; APP-011 is `Done` and APP-012 is promoted to `Now`.

- Merged APP-010 backend PR `#11` at `b809b9d`, ran migration job `signmons-calldesk-migrate-gsf6l`, deployed Cloud Run revision `signmons-calldesk-staging-00023-47g`, and published `/app/routing` to Firebase Hosting.
- Completed isolated staging tenant acceptance: ZIP `44119`, strict available/on-call rule, deployed technician configuration, covered `routing-v1` evaluation, and eligible `dispatch-v2` recommendation.
- Removed the temporary anonymous acceptance identity and token files; the owner account remains enabled with approved owner/tenant claims and password sign-in remains disabled.
- APP-010 is `Done`; APP-011 is promoted to `Now`. Real tenant and technician provisioning remains a separate operational onboarding/cutover item.

- APP-010 remains review-ready on backend branch `codex/app-010-routing`; a bounded continuation pass hardened missing/cross-tenant routing-rule and service-area update handling and rejected whitespace-only required names.
- APP-010 backend, UI, Prisma, architecture, governance and responsive browser gates passed after the hardening section; no merge, migration, deployment or production action was performed.
- Evidence: `signmons-calldesk-backend/evidence/APP-010/readiness-report.md`.

- Merged APP-009 PR `#9` at backend commit `413b671`, applied migration `20260831180000_add_technician_job_workflow`, and deployed image `413b671` to Cloud Run revision `signmons-calldesk-staging-00021-boh` at 100 percent traffic.
- Published `/app/technician` to `https://signmons-calldesk.web.app/app/technician`; release UI gates passed with 11 tests, clean lint/type checks, and successful static generation.
- Live readiness passed; the unsigned technician endpoint returned a sanitized `401`, and the hosted missing-link route failed closed without horizontal overflow or application-origin console errors.
- Created `technician-link-secret` without exposing its value and scoped access only to `signmons-calldesk-runtime@signmons.iam.gserviceaccount.com`.
- Revoked all temporary build grants immediately after release and confirmed `signmons-build@signmons.iam.gserviceaccount.com` is disabled with zero residual project, build-bucket, or Artifact Registry bindings.
- Evidence: `signmons-calldesk-backend/evidence/APP-009/readiness-report.md`.
- Owner completed and accepted the authenticated real-phone technician list/detail/action workflow and confirmed dispatcher status/audit propagation on 2026-09-02. APP-009 is `Done` and APP-010 is promoted to `Now`.

- Completed and released APP-007 from backend commit `afb3644` on branch `codex/app-007-urgency-escalation-review`.
- Added a canonical three-level `JobUrgency` model so `HIGH` is no longer collapsed into `STANDARD`, with a forward database migration.
- Added tenant-scoped urgency list/detail, mandatory-reason override and internal escalation endpoints protected for owner/admin/dispatcher roles.
- Added bounded rationale, escalation-path previews, privacy-safe override/escalation history and truthful notification delivery outcomes.
- Added the responsive `/app/urgency-review` operator route; backend and UI gates passed and Chrome desktop/mobile QA recorded no console errors or horizontal document overflow.
- Evidence: `signmons-calldesk-backend/evidence/APP-007/readiness-report.md`.
- Applied the `HIGH` urgency migration with reusable Cloud Run job execution `signmons-calldesk-migrate-fp7rp`.
- Deployed backend revision `signmons-calldesk-staging-00019-swf` at 100 percent traffic and published `/app/urgency-review` to the dedicated CallDesk hosting site.
- Live readiness, sanitized unauthenticated access, console-origin CORS and Chrome route verification passed; the disabled build service account remained disabled.
- Rebased the global program to owner-approved CallDesk-first execution with APP-006 active and FE-014 paused, not cancelled.
- Implemented APP-006 locally on backend branch `codex/app-006-intake-review` at commit `14be641`.
- Added tenant-scoped intake list/detail APIs, explicit missing-field readiness, owner/admin/dispatcher enforcement, priority visibility, redacted conversation trace and PII-free readiness-review auditing.
- Added the private `/app/intake-review` operator route with responsive Chrome evidence; backend and UI gates passed before release.
- Merged APP-006 to backend `main`, built image `2b715e4`, and deployed Cloud Run revision `signmons-calldesk-staging-00018-mxr` at 100 percent traffic.
- Deployed the operator shell to the dedicated `signmons-calldesk` Firebase Hosting site without changing the public Signmons marketing site; live readiness, sanitized unauthenticated access, and console-origin CORS checks passed.
- Revoked the temporary Cloud Build bucket and Artifact Registry grants and disabled the build service account after the successful image build.

- Completed FE-013 on marketing branch `codex/fe-013-revenue-roi-reconciled` at commit `f8a83ef`, based on the approved FE-016 pricing foundation.
- Implemented `/revenue-dashboard` and `/roi-calculator` with governed CTA parity, sample-data labeling, plain-language assumptions, estimate-versus-realized disclosures, and legacy billable-event summaries.
- Replaced unsupported emergency-uplift and deposit-as-extra-revenue math with a traceable recovered-lead -> booked-job -> completed-job model.
- The ROI plan-cost model was corrected to the fixed subscription with nonfinancial capacity guidance, merged in marketing PR `#23`, and deployed to Firebase Hosting site `signmons`.
- FE-013 gates passed: build, lint, 12 test files / 24 tests, `pricing:check` (98 checks), and `ui:check` (17 checks).
- Chrome desktop and 390px mobile QA evidence is stored in `signmons-marketing-web-feat-marketing-site/evidence/FE-013/`.
- Merged marketing PR `#20` to `main` at `8d4b3c6` and governance PR `#17` to `main` at `fb88891`; both post-merge checks passed.
- Deployed the merged marketing build to Firebase Hosting project/site `signmons` and verified `https://signmons.com/revenue-dashboard` plus `https://signmons.com/roi-calculator` against production asset hashes `index-Cv5nKHuZ.js` and `index-D6QEgPyA.css`.

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

1. Review the APP-012 payment-gate and payment-request checkpoints and keep APP-012 in `Now`.
2. Continue APP-012 with signature-verified idempotent webhook processing, customer recovery/status and transition audits.
3. Keep APP-013 in `Next`; do not start Twilio implementation until APP-012 is accepted and marked `Done`.
4. Keep FE-014 paused until the owner returns the pointer to marketing work.

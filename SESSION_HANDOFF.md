# Session Handoff

Last Updated: 2026-09-08

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
- Owner approved structured system diagnostic reporting as a governed Signmons Field capability. Starter receives basic notes/photos/equipment details and a completion summary; the complete branded report workflow is required for Growth launch readiness; Pro adds configurable templates, quality review, equipment trends, and approved integrations. This future scope does not displace APP-012 or APP-013.
- Owner approved the trades-platform completeness standard and future APP-025 through APP-032 roadmap covering memberships, job costing, inventory/purchasing, employee time export, offline field synchronization, customer financing, migration/data ownership, and operational recovery. `TRADES_PLATFORM_COMPLETENESS.md` defines the boundaries; none of these items displaces the active APP-012 pointer.
- Owner clarified that MVP scope includes Twilio-delivered calls answered through an OpenAI-powered conversational intake workflow plus governed inbound/outbound and transactional SMS. BE-008 now owns communications transport/compliance/recovery, APP-033 owns AI voice orchestration, and APP-013 explicitly owns transactional SMS/email templates and status. These future specifications do not displace APP-012.
- The earlier setup/overage/performance/add-on policy is superseded. The fixed-subscription marketing and ROI correction was merged in marketing PR `#23` and deployed to Firebase Hosting site `signmons`; repository hosting configuration was corrected in PRs `#24` and `#25`.

## Current Program Pointer

- Global `Now`: `APP-013` (Twilio-backed notification center and transactional customer messaging). BE-008 completed staging acceptance on 2026-09-07 and remains the accepted transport prerequisite for APP-013 and APP-033.
- Global `Next`: unassigned; finish APP-013 before selecting another ticket.
- Completed exception: `BE-003` (Eternity webchat backend production readiness).
- Completed exceptions: `BE-007` lead-source reporting and `APP-003` audited job completion.
- Program phase: owner-approved CallDesk-first product execution; `FE-014` is paused, not cancelled.
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

- APP-012 sandbox acceptance passed with an automatic post-destination `$100.00 USD` Stripe Checkout, HTTP 200 webhook delivery, canonical paid transition, zero Signmons application fee, contractor-account binding, dispatch unlock and Stripe-originated duplicate idempotency.
- Owner authorized merge and staging release. Backend PR `#14` merged at `068f4c2`; Cloud Build `dd7ca7ec-1777-45b6-8659-fba8998a9b63` produced digest `sha256:838121ce33dc17343ec2182bee83d39118626a68aa702802b13205635d501a33`; migration `signmons-calldesk-migrate-pgr84` succeeded; Cloud Run revision `signmons-calldesk-staging-app012release` serves 100 percent of staging traffic; Firebase payment/dispatch routes are published.
- Release verification passed liveness, readiness, approved-origin CORS, unsigned-webhook fail-closed behavior and three public route checks. Temporary build grants were removed and the build identity was disabled. Stripe live mode and real transactions remain separately approval-gated.
- APP-012 is Done and APP-013 is promoted to Now without starting implementation.

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

1. Review APP-013 inactive one-shot CREATE execution on backend `codex/app-013-transactional-messaging` (PR #21), including two new process exits and competing-entry-point audit. Owner reviewed preceding consumer guards; APP-012 and BE-008 remain accepted.
2. After review, one bounded lifecycle/technician mutation-guard section preserving payment semantics, then authorized scheduling orchestration and bounded reader/worker ownership/retry/review controls. Do not activate executor/journal/reconciler alone. Reschedule/cancel reconciliation and dependency remediation remain open. Prior journal migration, retention/provider configuration, live use/acceptance and release stay separately approval-gated. High/moderate findings are not accepted.
3. Keep provider delivery disabled until an explicitly approved acceptance run; no external messages or release are authorized by this documentation checkpoint.
4. Keep FE-014 paused until the owner returns the pointer to marketing work.

## APP-013 Queue State Review Checkpoint (2026-09-08)

Historical checkpoint; the latest continuation is recorded below.

- Backend checkpoint: `a04f1d7129495ed687a5ac896c5f29dd022a036c` on `codex/app-013-transactional-messaging` (PR #21).
- New checks reject cancellation copy for active jobs and on-the-way copy without an assigned EN_ROUTE technician. Deleted jobs return not found; confirmation/reschedule require a stored calendar reference and ordered window; closed-job contradictions return 409 before delivery queue access.
- Tests use local doubles only: 16 focused tests and 302 full backend tests pass (3 existing skipped); build/lint/architecture/Prisma and critical audit pass. Existing high/moderate dependency findings remain recorded in backend evidence.
- Unchanged UI regression gates also pass: lint, 17 tests and production build. No rendered UI changed; APP-013 screen/browser acceptance remains open.
- Scope is queue-admission snapshot validation only; no claim of atomicity with concurrent calendar/job changes or send-time lifecycle revalidation. No migration, provider message, merge or deployment occurred.
- APP-013 remains active at roughly 20%; APP-006 through APP-016 roughly 70%, planning estimates only. Evidence: backend `evidence/APP-013/readiness-report.md`.

## APP-013 Appointment Lifecycle Review Checkpoint (2026-09-08)

- Backend PR #21 now queues fixed confirmation, reschedule and cancellation SMS after the corresponding job/calendar operation commits. Queue failure cannot roll back the appointment.
- Automatic events derive a deterministic identity from the template and a digest of current canonical state. The same digest is recorded for manual queueing and checked again against current tenant/job data immediately before provider access.
- Stale, contradictory, deleted or unverifiable transactional work is dead-lettered before send. Revalidation includes recipient and rendered brand/schedule/technician inputs, while raw values remain absent from history output.
- Focused lifecycle/delivery validation passed 44 tests; full backend build/lint, 308 tests with 3 existing skips, architecture, Prisma and critical audit passed. Unchanged UI lint, 17 tests and build passed; no rendered UI changed.
- Outbound delivery remained disabled. No provider message, credential/configuration change, migration, merge, deployment or real customer/job mutation occurred. A narrow post-check/pre-provider race remains non-atomic and documented.
- APP-013 remains active at roughly 35%; APP-006 through APP-016 roughly 72%, planning estimates only. Remaining scope includes other event triggers, email, preferences, UI and acceptance. Evidence: backend `evidence/APP-013/readiness-report.md`.

## APP-013 Technician On-The-Way Checkpoint (2026-09-08)

- Backend checkpoint: `477048abfa22a15ec63642f83519c180354341ea` on `codex/app-013-transactional-messaging` (PR #21).
- Changed on-my-way actions now queue customer SMS only after the status/audit transaction commits; no-op retries and failed writes never queue. Queue/logging failures preserve committed status and expose no raw payload in logs.
- The digest includes the technician status timestamp: same-episode retries retain one identity while later departures differ. Obsolete departure/assignment state fails before provider access; earlier on-the-way hashes fail closed.
- Passed backend build/lint, 323 tests (3 existing skips), architecture/Prisma and critical audit; UI lint, 17 tests and build. No rendered UI changed, no external message or configuration/release action occurred.
- Remaining durability limit: no transactional outbox; a crash or enqueue failure can lose the notification and requires operator-reviewed recovery. Other event triggers, email, preferences, UI and acceptance remain open. APP-013 roughly 40%; APP-006 through APP-016 roughly 73%, planning estimates only. See backend APP-013 evidence for exact review commands.

## APP-013 Read-Only Notification Center (2026-09-08)

- Backend checkpoint: `3330c7bfa011120fa26f10b6582ab471f2ad3728`, `feat(app): add APP-013 read-only notification center`, on `codex/app-013-transactional-messaging` (PR #21).
- `/app/notifications` (`SCR-APP-021`) adds bounded SMS history, status/job filters, explicit UTC and sent-versus-delivered status semantics. Dispatch navigation links to it. No send, replay, template or email control exists.
- Token remains in memory; token/job edits and session clearing remove results and invalidate pending reads. UI omits raw message/customer/provider payload and raw server error text; server tenant/role guards remain authoritative.
- Passed backend build/lint, 323 tests (3 existing skips), architecture/Prisma; UI lint, 23 tests and build (14 static pages). Local synthetic Chrome desktop/390px QA passed filters, invalid UUID, empty/403/500/loading states, late-response clearing, no credential storage, private-field omission and keyboard order. No page runtime errors. Live backend/provider acceptance is not claimed.
- Evidence and reproducible QA command: backend `evidence/APP-013/readiness-report.md`; screenshots `notifications-desktop.png` and `notifications-mobile.png` alongside it. Existing 4 high/9 moderate dependency findings and stale Browserslist data remain documented; 0 critical.
- No external message, configuration, migration, merge, deployment or customer mutation. Durable enqueue recovery and remaining events/template controls/technician UI/email/acceptance stay open. Planning estimate: APP-013 roughly 50%; APP-006 through APP-016 roughly 74%.

## Latest APP-013 Inactive One-Shot CREATE Execution (2026-09-08)

- Backend checkpoint: `df9143a39aa580552ba134cabcd98bd2c953e2bf`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21). Owner reviewed consumer guards and said proceed; fetched/reconciled backend `3c159b9` / governance `abac6af`. APP-013 remains sole Now, original saved-checkout changes preserved.
- One bounded internal seam: narrow CalendarEventCreator/Google adapter and CalendarCreateExecutionService for already-authorized persisted CREATE reservations. Atomically latch PENDING -> UNCERTAIN and advance matching tenant/unassigned-job/claim version before one saved-ID/private-operation-marker POST. Unknown commit acknowledgment never dispatches; concurrent/restarted calls never reinsert. Fresh journal/job checks reject observed newer review/edits.
- Insert response is never success proof. Existing read-back alone may atomically finalize journal/job/intent/audit. Missing evidence stays held, no automatic recreate/compensation or immediate enqueue/send. Creator uses fixed reference-only summary, no customer content/attendees, encoded target, HTTP timeout and no redirect/retry/raw logging. Google documents provider caveats for notification suppression and distributed ID collision detection; no absolute exactly-once provider guarantee.
- Passed backend lint/build, 49 suites/570 tests (3 existing skips), architecture/Prisma; 15-migration disposable local suite including concurrent one-shot execution, lost insert/commit acknowledgments, newer edits, and two new actual process exits before/after synthetic insert (11 total crash cases). UI unchanged: lint/29 tests/static build and 14-request/92-request desktop/390px browser regressions passed. Zero provider calls; fixture dropped and absence verified.
- Initial formatter and pre-build fixture invocation failures corrected before clean sequence. Audit unchanged: backend 5 high/10 moderate, UI 10 high/1 moderate, 0 critical; critical-only commands pass, full audits are not clean or accepted. Existing pg warning persists.
- Executor/creator/journal/reconciler remain unregistered; no public scheduling-flow change or recovery worker. Source audit records technician mutation without journal guard, completion without version/journal guard, urgency direct policy update and payment-policy coordination. Post-preflight/provider races, legacy unjournaled scheduling and SENDING crash risks remain.
- No schema/new migration, provider/IAM/secrets/billing configuration, real data, external sends, staging/production, merge or deploy. Prior journal migration, retention and complete activation protocol require separate review. Next after review: one bounded lifecycle/technician mutation-guard section preserving payment semantics; then authorized scheduling orchestration and bounded reader/worker ownership/retry/review controls. Reschedule/cancel recovery, dependencies and remaining messaging/acceptance stay open.
- Stop review-ready. Planning estimates APP-013 ~81%; governed APP-006 through APP-016 ~80%, not release readiness. Exact file audit, provider reference and validation/review commands: backend `evidence/APP-013/readiness-report.md`.

## Earlier APP-013 Unfinished Calendar Consumer Guards (2026-09-08)

- Backend checkpoint: `3c159b993174971ff71dfb9025a9117e4f06acf8`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21). Owner reviewed CREATE read-back and said proceed; fetched/reconciled backend `f30760a` / governance `b2dcec5`. APP-013 sole Now, existing focused branches only; saved-checkout changes preserved.
- One bounded consumer section: unfinished-journal existence guards hold initial confirmation and signed customer views/actions with HTTP 409, dispatch recommendations/assignment changes and transactional notification admission/delivery. Customer conflicts discard stale appointment cards; dispatch keeps locally cancelled pending jobs visible as ESCALATED/provisional with no override. Tenant/version/no-unfinished conditional writes protect changed customer audits, legacy scheduling and dispatch claims.
- Lifecycle enqueue holds preserve PENDING/failure count and defer 60 seconds; pre-provider delivery holds conditionally return SENDING to QUEUED, refund only the unsent attempt and defer 60 seconds. Hold detection precedes stale hash comparison and provider/decrypt access; direct claims honor due time. Owner retry cannot bypass a hold. Existing hashes, consent, canonical deduplication and unknown-send safeguards remain.
- Passed backend lint/build, 47 suites/535 tests (3 existing skips), architecture/Prisma; 15-migration disposable local suite including 12 real action/status guard combinations, retry-budget/delay/tenant/mutation proofs and prior nine process-crash cases. UI lint/29 tests/static build, 14-request desktop/390px guard QA and 92-request notification regression passed; four new screenshots inspected. Provider calls zero, fixture dropped and absence verified.
- Initial test-double/type/claim-field/test-name/browser-locator failures and warning-panel layout were corrected before clean validation. Audits remain backend 5 high/10 moderate, UI 10 high/1 moderate, 0 critical; no dependency remediation or risk acceptance. Existing pg deprecation warning persists.
- Consumer queries require the prior journal migration at runtime, but no migration/schema/dependency/module registration or external action was made. Journal writers/reconciler/worker remain inactive. Unjournaled legacy crashes, post-check provider race, SENDING crash gap and other technician/job mutation entry points are not globally solved. No merge/deploy/staging/production/provider configuration, real data, secrets/IAM/billing or live sends.
- Stop review-ready. After review, separately scope guarded CREATE integration (saved ID/operation markers and competing-entry-point safety), then bounded recovery ownership/retry/review controls. Reschedule/cancel reconciliation, retention policy, dependency triage and remaining messaging/acceptance stay open. Planning estimates APP-013 ~79%; governed APP-006 through APP-016 ~80%, not release readiness. Exact files/commands/screenshots: backend `evidence/APP-013/readiness-report.md`.

## Earlier APP-013 CREATE Read-Back Reconciliation (2026-09-08)

- Implementation/evidence: backend `f30760a180ac48d56d7a5f60e0c7ced62ffb2d81`, `feat(app): reconcile journaled CREATE calendar evidence`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21).
- Owner reviewed the journal foundation and said proceed. Fetched/reconciled backend `cbdddc9` / governance `c0f47d8`; APP-013 sole Now, current focused branches only, original changes preserved.
- Completed one inactive reconciliation section: narrow read-only Calendar adapter plus CREATE reconciler validates saved identity, tenant/job/operation markers, confirmed single blocking event, exact future window and current job version. Provider ambiguity stays pending/review; no blind recreate, rollback, unjournaled adoption or external write.
- Matching evidence atomically finalizes journal/job/confirmation intent/system audit. ETag is hashed in audit metadata. Conditional versions protect newer review/finalized receipts and job edits; commit-acknowledgment loss recognizes completion without duplication. No queue processing or provider message.
- Passed backend lint/build, 46 suites/510 tests (3 existing skips), architecture/Prisma; UI lint/29 tests/build and 92-request synthetic desktop/390px QA, four screenshots inspected. Disposable local proof passed 15 existing migrations, three new process exits (nine including earlier journal cases), actual post-write rollback, concurrency, late reads, ack-loss, held conflicts and newer edits. Fixture removed and absence verified; provider calls zero.
- Initial test-double typing and stale-build fixture failures were corrected before the final clean sequence. Existing pg warning and dependency audit findings remain: backend 5 high/10 moderate, UI 10 high/1 moderate, 0 critical. No dependency/schema/migration change or risk acceptance.
- Reader/reconciler/journal have no SchedulingModule/route/worker registration. Existing live scheduling still lacks saved operation markers and cannot use this recovery automatically. Consumer pending guards are the next bounded checkpoint; guarded writer, worker policy, reschedule/cancel recovery, retention, provider configuration/live acceptance and release remain gated. Point-in-time Calendar reads are not distributed atomicity or ongoing drift detection.
- No staging/production, real customer/appointment, provider configuration, secrets/IAM/billing, live sends, merge or deployment action. Planning estimates APP-013 ~77%, governed APP-006 through APP-016 ~80%. Exact files/commands/limits: backend `evidence/APP-013/readiness-report.md`. Stop review-ready, no acceptance boxes checked.

## Earlier APP-013 Calendar Journal Foundation (2026-09-08)

- Implementation/evidence: backend `cbdddc9f3e0b661f72166b873c2f92b9d09af00d`, `feat(app): add APP-013 calendar journal foundation`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21).
- Owner approved the Calendar/crash-resilience recommendation and requested robust continuation. Fetched/reconciled backend `f7d5e1e` / governance `82fc1fb`; APP-013 remains sole Now. Continued existing focused branches and preserved original saved-checkout changes.
- Added only the inactive journal/reservation foundation: atomic conditional local CREATE/RESCHEDULE/CANCEL claim plus PENDING record, stable create ID, retained original event/window/label, monotonically advancing job version, tenant composite FK, partial unique unfinished-job index and SQL invariants. Same-window reschedule cannot start a fresh journal; eventual replay must use finalized proof.
- No production consumer, public API, worker, provider request, terminal transition, success audit or SMS intent is added. Hard-deletion of referenced jobs/tenants is restricted until an explicit archival policy is supplied. Existing scheduling still bypasses the journal; live Calendar ambiguity and pre-finalization risks remain open.
- Backend lint/build, 44 suites/464 tests (3 existing skips), architecture/Prisma passed. Disposable local PostgreSQL proof applied 15 migrations and passed six real child-process exits before/after commit, atomic rollback, restart persistence, concurrency, tenant/version/SQL/deletion protections and no premature messages. Fixture removed, absence verified; provider calls zero. UI lint/29 tests/build and synthetic desktop/390px browser QA passed 92 mocked requests; four screenshots inspected.
- One initial full-test process exited 139 during parallel validation; two subsequent full runs passed, root cause unestablished. Existing pg warning and audits remain: backend 5 high/10 moderate, UI 10 high/1 moderate, 0 critical. No dependency changes or risk acceptance.
- New migration `20260908180000_add_calendar_operation_journal` is local-tested only. No staging/production, real data, provider configuration, secrets/IAM/billing, merge or deployment action. Planning estimates: APP-013 approximately 75%; governed APP-006 through APP-016 approximately 80%. Exact files/review commands and next integration boundaries: backend `evidence/APP-013/readiness-report.md`. Stop review-ready, not accepted/released.

## Earlier APP-013 Post-Calendar Reschedule Intent Finalization (2026-09-08)

- Implementation/evidence: backend `f7d5e1ecde3900768058807e6da2dce80b40e6c8`, `feat(app): finalize APP-013 reschedule notification intents`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21).
- Owner reviewed backend `df97aa8` / governance `50c3db7` and said proceed. Fetched and reconciled both repositories; completed reschedule finalization only, on the current focused branches with APP-013 sole Now and original user changes preserved.
- New local rescheduling service version-binds reservation/compensation and captures the canonical reschedule intent plus existing customer activity audit atomically after Calendar acknowledges PATCH. Audit preserves previous/new labels and adds intent ID/finalized timestamp. Claim, finalization and compensation versions advance monotonically within one millisecond; current-version audit is required for same-window replay, not just local dates.
- Pending/legacy/changed replay snapshots require office review, including conservative invalidation after unrelated job edits. After acknowledged Calendar change, failed finalization never rolls Calendar/local window back; worker/operations/logging failures after finalization cannot undo success. SchedulingService no longer depends on the direct messaging queue/helper. All four current templates now use disabled-by-default intent processing and guarded owner/admin retry; no arbitrary send or backfill.
- Passed backend lint/build, 43 suites/443 tests (3 existing skips), architecture/Prisma; UI lint/29 tests/build; desktop/390px synthetic QA (92 mocked requests, 14 POSTs), four inspected reschedule screenshots. Disposable local PostgreSQL proof passed 14 existing migrations, actual intent/audit rollback, concurrency, replay, tenant/version, compensation, disabled processing/retry/stale-window checks. Zero provider calls; fixture removed and absence verified. Initial test/formatting failures fixed before clean run.
- Calendar/database atomicity, global external-operation serialization and pre-finalization/unknown-outcome reconciliation remain open; local customer view is not independent Calendar proof. No new schema/migration/dependencies/provider/configuration, live sends/real data, merge or deployment. Prior intent migration/live acceptance remain separately gated.
- Audit unchanged: 0 critical, backend 5 high/10 moderate, UI 10 high/1 moderate; release triage required. Planning estimates APP-013 74%; governed APP-006 through APP-016 80%. Remaining calendar reconciliation, other events/templates/preferences/technician notifications/email and owner/live acceptance. Exact commands/limitations: backend APP-013 evidence. Stop review-ready.

## Earlier APP-013 Post-Calendar Cancellation Intent Finalization (2026-09-08)

- Implementation/evidence: backend `df97aa83b6615b94e462f91deae3492a064aa63a`, `feat(app): finalize APP-013 cancellation notification intents`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21).
- Owner reviewed backend `9a3d86a` / governance `252f340` and said proceed. Fetched/reconciled both repositories; completed cancellation finalization only on the current feature branches, APP-013 sole Now. Original saved-checkout user edits preserved.
- New cancellation service version-binds the existing local claim/Calendar-error compensation and records intent plus `appointment.customer_cancelled` CUSTOMER audit atomically only after deletion acknowledgment. Intent/audit/commit failure after acknowledged deletion cannot restore the appointment; office review is required. Finalized replay uses local audit proof and creates nothing; legacy/in-flight/crash-stranded cancellation without proof fails closed.
- Post-finalization worker, operations-notification and logging failures cannot undo cancellation. Canonical cancellation intents use existing disabled-by-default processing, state/consent/quiet-hour/hash/deduplication checks and guarded owner/admin retry UI. Reschedule durability remains absent; no backfill.
- Passed backend lint/build, 42 suites/425 tests (3 existing skips), architecture/Prisma; UI lint/29 tests/build; desktop/390px synthetic Chrome QA, 92 mocked requests (78 GET/14 POST) and four inspected cancellation screenshots. Real disposable-local Prisma proof passed 14 existing migrations and cancellation ordering, rollback after actual intent/audit inserts, concurrency, tenant/version guards, replay, disabled processing, recovery, stale state and late compensation checks. Zero provider calls; fixture removed and absence verified.
- Calendar/database atomicity and crashes/unknown external outcomes before finalization remain manual reconciliation gaps. The prior pre-acknowledgment compensation is only version-hardened; customer view is still local status, not proof of Calendar deletion. No automatic repair of absent intents. See exact boundaries/review commands in backend APP-013 evidence.
- Audit remains 0 critical, backend 5 high/10 moderate, UI 10 high/1 moderate; release triage open. No new schema/migration/dependencies, provider/configuration, merge/deploy, live sends or real-data action. Prior intent migration and live acceptance remain separately approval-gated. Planning estimates APP-013 71%; governed APP-006 through APP-016 79%. Stop review-ready.

## Earlier APP-013 Guarded Exhausted-Intent Retry UI (2026-09-08)

- Backend implementation/evidence: `9a3d86a103df675fd0f329b15922dda2ffe8736b`, `feat(app): add guarded APP-013 intent retry review UI`, pushed and remote-verified on `codex/app-013-transactional-messaging` (PR #21).
- Owner reviewed backend `aab434b` / governance `5f3127a` and approved continuation. Completed one bounded notification-center recovery UI section on existing focused branches; APP-013 remains sole Now, no new ticket or marketing work.
- Authenticated tenant-bound private/no-store capability read shares the write role policy: owner/admin true, dispatcher false, other roles denied. UI fails closed on failed/non-true capability. Only supported exhausted/unlinked snapshots expose review; fixed reason and acknowledgment are mandatory, and exact listed `updatedAt` is submitted. Existing POST tenant/current-state/concurrency/atomic-audit safeguards remain authoritative.
- One in-flight request per page, 15-second timeout, no automatic resubmission; every outcome clears the snapshot and requires manual reload before another review. Pending is not delivery. Unknown/server/network/malformed/timeout outcomes warn the server may already have accepted. Session/token/job edits invalidate late GET/POST messages without undoing accepted work.
- Passed backend build/lint, 411 tests (3 existing skips), architecture/Prisma; UI lint/29 tests/build; synthetic desktop/390px Chrome QA with 92 mocked requests (78 GET, 14 POST), including duplicate clicks, rejection and uncertain outcomes. Four new screenshots inspected. Disposable local database proof passed all 14 existing migrations and recovery invariants with zero provider calls; fixture dropped and absence verified.
- Audit has 0 critical; backend 5 high/10 moderate (previous report 4/9), UI 10 high/1 moderate. No dependency/lockfile changes or risk acceptance; triage required before release. Existing Browserslist/pg warnings remain. No new migration/schema, provider/configuration, merge/deploy, staging/production or real-data action. Prior intent migration remains approval-gated.
- Evidence and exact review commands: backend `evidence/APP-013/readiness-report.md`. Remaining owner/live acceptance, reschedule/cancellation durability, calendar reconciliation, events/templates/preferences/technician notifications/email. Planning estimate APP-013 roughly 68%; governed APP-006 through APP-016 roughly 78%. Stop review-ready, not accepted or released.

## Earlier APP-013 Owner/Admin Exhausted-Intent Retry API (2026-09-08)

- Owner reviewed initial confirmation durability and approved continuation. Backend `aab434b3ddcd83f6ccbf91ee6c19fb8a3f1adb3b`, `feat(app): add reviewed APP-013 enqueue intent retry`, on `codex/app-013-transactional-messaging` (PR #21).
- API-only retry requires owner/admin, explicit acknowledgment, fixed review reason and exact listed `updatedAt`. Only current exhausted FAILED/unacknowledged intents with unchanged supported job state qualify. Conditional reset and user audit are atomic; stale/repeated/concurrent requests cannot add a second reset/audit. No arbitrary payload or stale-state override. UI remains read-only.
- The API re-arms PENDING only and never processes/sends. Normal worker delivery enablement, consent, quiet hours, state checks, queue identity and five-failure bound remain. Once deployed/enabled it may subsequently send through that normal policy path; no live retry is authorized by this checkpoint.
- Passed 403 backend tests (3 existing skips), build/lint/architecture/Prisma; UI lint/27 tests/build and unchanged desktop/390px browser regression (18 GETs). Real HTTP guard/validation/throttle/filter tests use synthetic Firebase verification; disposable local database proof verifies single concurrent reset/audit, no queue from retry alone, disabled processing, state rejection and audit rollback. All 14 existing migrations passed only in that fixture; database removed and absence verified. No provider calls.
- No new schema/migration/dependency, provider/configuration, merge/deploy, staging/production or real-data action. Existing advisories 0 critical, 4 high/9 moderate; Browserslist/pg warnings retained. Prior intent migration remains separately release-gated. Evidence and exact review commands are in backend APP-013 readiness report.
- Remaining recovery UI/acceptance, reschedule/cancellation durability, calendar reconciliation, other events/templates/preferences/technician notifications/email/live acceptance. Planning estimates APP-013 roughly 65%; APP-006 through APP-016 roughly 77%. Stop review-ready.

## Earlier APP-013 Initial Confirmation Intent Durability (2026-09-08)

- Owner reviewed intent visibility and approved continuation. Backend `1ea45446995bad740fbede9be51f49230f51fb6f`, `feat(app): persist APP-013 initial confirmation intents`, on `codex/app-013-transactional-messaging` (PR #21).
- Initial confirmation finalization atomically commits the acknowledged calendar reference, fixed SMS intent and customer audit. Post-commit enqueue/operations-notification/logging failures cannot undo booking. Recovery supports initial confirmations and technician departures only, with existing disabled-delivery, digest and queue-idempotency controls.
- Failed/ambiguous finalization after acknowledged Calendar insertion holds the reservation for office review. Unfinalized replay cannot report confirmation or insert again; finalized replay does not duplicate intent; closed/deleted requests cannot reopen. Calendar and the database remain non-atomic; pre-finalization crash reconciliation and unknown provider outcomes are not solved. Reschedule/cancellation triggers still have their post-commit gap.
- Final validation: 362 backend tests (3 existing skips), build/lint/architecture/Prisma; UI lint/27 tests/build and desktop/390px synthetic browser QA with 18 GETs. All 14 existing migrations and real transactional scheduling/intent integration passed in a new local-only database with provider doubles; fixture removed and absence verified. No external calendar/message, staging/production database, configuration, merge, deploy, billing or real-data action.
- Prior migration requires separate release approval. Existing audit findings remain 0 critical, 4 high/9 moderate; local pg deprecation and Browserslist warnings documented. Backend APP-013 evidence has exact review steps and new confirmation-intent screenshots.
- Remaining: reschedule/cancellation durability, calendar reconciliation, recovery actions/policy, other events/templates/preferences/technician notifications/email/live acceptance. Planning estimates: APP-013 roughly 62%; APP-006 through APP-016 roughly 76%. Stop review-ready.

## Earlier APP-013 Read-Only Enqueue Intent Visibility (2026-09-08)

- Owner reviewed technician durability and approved continuation. Backend checkpoint: `09bdbbd83547a3ef86136a6a498b090961b9ff60`, `feat(app): show APP-013 enqueue intent status`, on `codex/app-013-transactional-messaging` (PR #21).
- Notification center now independently reads history and enqueue intents. The new panel shows pending/stopped/queue-acknowledged states, safe failure labels, claim/backoff time, job/intent IDs and event references. Pending does not promise active retry, queue acknowledgment is not delivery, and job/status filters apply only to latest 100 tenant intents.
- Passed backend build/lint, 343 tests (3 existing skips), architecture/Prisma; UI lint, 27 tests/build; synthetic local Chrome desktop/390px QA with 18 GET-only requests. Tests cover independent partial failures, late responses after token/job edits or session clear, all intent filters, empty/error/loading states, private-field omission and keyboard order. New screenshots and exact review/rerun steps are in backend APP-013 evidence.
- No database, provider, configuration, merge, deployment, billing or real-data action. Prior migration still requires approved release sequencing; recovery actions/policy, appointment durability, other events/templates/preferences/technician notifications/email and live acceptance remain open. Critical audit remains 0 critical, 4 high/9 moderate; existing Browserslist warning. Acceptance boxes stay unchecked.
- Planning estimates: APP-013 roughly 58%; APP-006 through APP-016 roughly 75%. Stop review-ready.

## Earlier APP-013 Durable Technician Enqueue Recovery (2026-09-08)

- Backend checkpoint: `fab7fa6a3c590cab3adbd8293616f0cb8fccd23f`, `feat(app): persist APP-013 technician notification intents`, on `codex/app-013-transactional-messaging` (PR #21).
- Technician departure intent is now persisted in the same transaction as job status and audit. The existing delivery-enable gate controls immediate and periodic processing; conditional leases recover crashes, canonical queue identities prevent duplicate queue insertion, stale snapshots stop, and failures back off then stop after five.
- Read-only tenant-bound `GET /communications/sms/enqueue-intents` exposes operational status, never state hash/message/recipient data. No recovery UI or reset/replay command is included; the existing history screen remains unchanged.
- Passed backend build/lint, 343 tests (3 existing skips), architecture/Prisma; UI lint/23 tests/build and synthetic browser regression. All 14 migrations and real transactional rollback/concurrency/ack-loss/tenant-FK checks passed in a new isolated local database, which was removed. Provider calls: zero.
- Migration `20260908120000_add_sms_enqueue_intents` must precede any separately approved deployment. No staging/production database or provider/configuration action occurred. Existing dependency findings remain 4 high/9 moderate, 0 critical; the local PrismaPg concurrency test has a nonblocking pg deprecation warning.
- Appointment durability, exhausted-intent recovery policy/UI, other events, templates/preferences, technician notifications, email and live acceptance remain open. Planning estimates: APP-013 roughly 55%; APP-006 through APP-016 roughly 75%. Evidence: backend `evidence/APP-013/readiness-report.md`.

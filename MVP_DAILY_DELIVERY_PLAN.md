# Signmons Release A pilot — daily delivery plan v1

Prepared 2026-09-13 at owner request for a finite, trackable MVP plan before more coding. Planning baseline for review, not a promise of one-day completion or authority to activate later tickets. Source snapshots: backend 6b21839, governance 0977467; both fetched, focused worktrees clean at entry; backend PR21 remains open. No code or acceptance changed by this audit.

## Goal and boundary

Goal: owner-operated Eternity intelligence pilot meeting MVP_ACCEPTANCE_MATRIX.md and SIGNMONS_INTELLIGENCE_SPEC.md, including web, ordinary SMS, voice, approved knowledge/rules/behavior/memory, payment/booking/notifications, technician outcome, evaluation and safe operations. This is Release A, not public commercial availability. INTELLIGENCE_MVP_ROADMAP.md separately requires commercial onboarding/admin, subscriptions/entitlements, support/security/restore/offer gates and Money/Growth work for Release B; those are NOT silently declared done or covered by the dates below. No training, marketing, new provider or Eternity website work.

Frozen walkthrough stays 1A/1B/2A accepted, then 2B → 3A → 3B → 3C → 3D. After full APP-013 acceptance: APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033. Work packages below are internal scheduling units, not new acceptance sections or permission to skip Now. A later ticket remains queued until its predecessor is fully accepted.

## Evidence-based starting point

| Scope | What can be reused | What is not accepted yet |
| --- | --- | --- |
| 2B | Existing session/consent/draft/one-job transaction and fixture proof tests; automatic admission amendment; 81e0f8b nullable-location fix | Real automatic composition/identity/recovery and connected controlled acceptance. Nullable migration is local-only. |
| Payment/calendar/text | APP-011/012 component evidence; current payment services, Calendar journal/recovery and SMS stack | Same-job integrated acceptance. scheduling.module.ts registers AppointmentController, not every recovery controller; file existence is not activation. |
| Communications | communications.module.ts registered SMS/settings/phone-only services; email template/recipient/eligibility/intent source and historical local evidence | Full customer email delivery/retry, role/event matrix, BE001_DEPENDENCY_REVIEW.md residuals. |
| Organization | organization profile/payment policy API/UI and local organization-setup/address-thread evidence | Full rules/versioned automation, customer-facing behavior and all six onboarding outcomes. No duplicate onboarding rebuild. |
| Intelligence | Existing AI/life-safety, conversation encryption, customer/property/job models, technician workflow, reporting | Full APP-017/018/019/015/033 acceptance. Existing voice greeting and reporting are not conversational voice or an independent evaluation dashboard. |
| Gates | Latest stored nullable-location evidence: 2,151 passing backend tests, 3 skipped, build/lint/audits/local migration proof | Those results are historical evidence, not freshly rerun runtime tests for this planning audit or pilot sign-off. |

Read: all seven ticket acceptance sets including APP-015/016/033 integration additions; MVP_ACCEPTANCE_MATRIX; intelligence specification/roadmap; remaining execution contract; organization onboarding; BE001 dependency review. Inspected source/module registration and evidence inventories, not every future implementation line. Future-ticket sizing is therefore low confidence. Old 20–35-section allowance and nine-steps/nine-days inference are superseded for forecasting, not acceptance.

## Day-sized work rule

One package targets one focused engineering day (roughly 4–6 productive hours including affected tests and evidence), not one chat turn or one commit. Owner review, unattended builds and external waiting are tracked separately. The calendar assumes capacity to finish that work each day; a short daily approval session alone is not that capacity.

Every implementation package includes the affected unit/database/security tests, lint/build/architecture gates and browser QA when UI changes. Local fixtures are not provider acceptance. Every row has an observable output; documentation-only preparation is explicitly labeled and cannot earn a capability milestone. “Prove” means reproduce existing work and fix only demonstrated gaps, not rebuild it by default.

Before starting a row, refresh source, record exact files/interfaces, acceptance mapping, test commands, dependencies and exclusions in its existing ticket/card. If the row cannot fit a day, report a revised effort estimate before proceeding; do not call part of it Done. Splitting requires versioned child IDs and a reviewed forecast delta, with the parent's original finish line retained. Do not invent a new package to hide an unfinished one.

Status: P = planned, A = active, B = blocked, R = review-ready, D = accepted package. All 60 start P because this is a ledger of REMAINING work. Each status update records source/commit, proof, reviewer/date, actual focused days and blocked days. Reuse of existing code does not reset earlier acceptance. No package is D merely because a helper or test exists.

## Finite remaining ledger

Dependency: each row follows the preceding row by default; ticket acceptance gates override the schedule. External gates listed later apply in addition. IDs are permanent. Owner is implementer for code/proof, product owner for acceptance, account owner for external authorization.

| ID | Owner ticket / criterion | One-day target and observable exit | Status |
| --- | --- | --- | --- |
| P01 | APP-013 / 2B contract | Reconcile the completed terms review into the exact serializer and service/transaction card; no unnamed identity/storage decision; implementation-ready card, not a demo | D |
| P02 | APP-013 / 2B authority | Controlled server authority and tenant-policy binding reject forged/missing/revoked context while preserving operator exception guards | D |
| P03 | APP-013 / 2B proof | Current phone/address/county evaluation reaches the transaction with revision/expiry checks and no prohibited durable provider payload | R |
| P04 | APP-013 / 2B one job | Explicit customer submit atomically creates one eligible STANDARD job; audit rollback, duplicate and changed replay tests pass | D |
| P05 | APP-013 / 2B customer flow | Existing UI shows correction, exception, restart and truthful created/not-booked states; desktop/mobile journey passes | A |
| P06 | APP-013 / 2B live acceptance | Separately authorized release/run packet produces one real verified test job and closes identities/caps; owner accepts 2B | P |
| P07 | APP-013 / 3A payment wiring | Same admitted job opens Sandbox Checkout; missing policy/foreign payment/redirect-only success refuse | P |
| P08 | APP-013 / 3A acceptance | Authorized Sandbox webhook and duplicate/late-event tests establish correct same-job payment; owner accepts 3A | P |
| P09 | APP-013 / 3B integration | Paid job and current slot connect to existing Calendar journal/finalization; race and interrupted-write tests pass | P |
| P10 | APP-013 / 3B acceptance | Approved test calendar shows one appointment; uncertain recovery/readback demonstrated; owner accepts 3B | P |
| P11 | APP-013 / 3C + BE-001 | Stable consent-event identity prevents delayed START undoing STOP; raw/provider-normalized restoration and atomic rollback proven | P |
| P12 | APP-013 / 3C acceptance | Policy/consent-bound appointment text actually received under approved cap; truthful delivery state; owner accepts 3C | P |
| P13 | APP-013 / 3D lifecycle | Same-journey reschedule/cancel preserves appointment truth and only eligible notices; local failure matrix passes | P |
| P14 | APP-013 / 3D acceptance | Approved changed/cancelled journey and recovery replay demonstrated; owner accepts walkthrough, not all APP-013 | P |
| P15 | APP-013 / criteria 1–4 | Required assignment/status/payment/dispatcher SMS events and roles have complete policy/template mapping and tested intents | P |
| P16 | APP-013 / criteria 1–5,11–12 | Notification center exposes role-safe event/status/failure matrix and audit; unauthorized views/actions refuse | P |
| P17 | APP-013 / criteria 3,6,8,10 | Existing captured email/eligibility/private credentials bind one finalized confirmation intent; no repeat capture or credential leakage | P |
| P18 | APP-013 / criteria 6–7 | Confirmation/reschedule/cancel email lifecycle produces correct branded content and unique durable intent from actual events | P |
| P19 | APP-013 / criteria 5,9 | Existing intended email provider path sends only authorized intents; uncertain failure/retry ownership and status proven locally | P |
| P20 | APP-013 / criteria 2–3 | Owner-controlled SMS/email event/recipient/brand settings and previews work independently, with tenant isolation | P |
| P21 | APP-013 / channel acceptance | Separately authorized email lifecycle run verifies delivery, privacy and failure visibility; no unapproved resends | P |
| P22 | APP-013 / all 12 + BE-001 | Reconcile all criteria and consent/retention residuals with evidence; close only after full owner acceptance | P |
| P23 | APP-017 / rules versions | Reuse organization controls to draft/publish immutable operational rule versions with stale-update/access tests | P |
| P24 | APP-017 / runtime resolution | Preview and runtime resolve identical effective rules; missing/inactive/conflicting versions refuse | P |
| P25 | APP-017 / financial rules | Fee/currency/payment snapshots survive edits/replay; explicitly not-required payment differs from missing policy | P |
| P26 | APP-017 / triggers | Allowed automation actions enforce prerequisites/idempotency/failure owner; preview has zero side effects | P |
| P27 | APP-017 / full acceptance | Owner completes rules UI/runtime proof; map onboarding O2 and all rule criteria; accept ticket | P |
| P28 | APP-018 / behavior versions | Tenant brand behavior draft/preview/activation has versioned audit and access/revision tests | P |
| P29 | APP-018 / factual boundaries | Behavior cannot override APP-017 prices/availability/safety; approved-source/refusal tests pass | P |
| P30 | APP-018 / comfort scenarios | Respectful objections, old equipment and uneven-temperature scenarios pass independent no-pressure/no-fabrication checks | P |
| P31 | APP-018 / full acceptance | Owner reviews channel previews, unknown/fallback and safety interruptions; accept ticket | P |
| P32 | APP-019 / identity | Customer/property/equipment history reads enforce appropriate customer identity and tenant/role scope | P |
| P33 | APP-019 / provenance | Existing records expose source/time/confirmed/unknown status without promoting model suggestions | P |
| P34 | APP-019 / corrections | Audited corrections preserve lineage and reject stale/concurrent changes or unauthorized cross-channel joins | P |
| P35 | APP-019 / retention and brief access | Minimized export/deletion and authorized technician history distinguish findings from observations | P |
| P36 | APP-019 / full acceptance | Owner completes history/correction/access workflow; isolation matrix and ticket traceability accepted | P |
| P37 | APP-015 / metrics | Required repeat-question/latency/escalation/intake-failure/handoff metrics use documented events and denominators | P |
| P38 | APP-015 / failure review | Role-safe queue categorizes incidents, corrections, resolution owner and audit history | P |
| P39 | APP-015 / lineage and splits | Actual outcomes and model/prompt/policy/tool/source versions link to rights-controlled development/held-out sets | P |
| P40 | APP-015 / independent evaluation | Safety/tenant/payment/tool assertions block critical failures independently of sales scores; sample sizes/cost/uncertainty reported | P |
| P41 | APP-015 / full acceptance | Dashboard, human review and minimized export-readiness proof accepted; no export/training automatically launched | P |
| P42 | APP-016 / financial and slot integrity | Reuse 3A/3B proof; verify late-payment/expired-hold/concurrent-slot cases and immutable financial policy | P |
| P43 | APP-016 / private management | Customer management action refuses expired/foreign tokens and excludes credentials from analytics/referrers/logs | P |
| P44 | APP-016 / lifecycle truth | Reuse 3D; close uncovered reschedule/cancel/notification-failure recovery cases and ownership | P |
| P45 | APP-016 / full acceptance | All original and financial-integration criteria mapped and accepted with authorized environment evidence | P |
| P46 | APP-033 / knowledge | Approved versioned knowledge retrieval rejects stale/conflicting/unapproved/injected sources with provenance | P |
| P47 | APP-033 / shared orchestration | Existing web flow uses typed policy/payment/booking tools and authorized memory; model cannot assert action success | P |
| P48 | APP-033 / safety and discovery | Contextual hazards/negation/new warnings across discovery/payment interrupt safely; comfort discovery respects refusal | P |
| P49 | APP-033 / conversational SMS | Ordinary SMS shares protected context with explicit identity/confirmation/handoff; not just consent keywords | P |
| P50 | APP-033 / voice transport | Authorized sandbox voice reaches tenant-correct conversational workflow with measured first-answer latency | P |
| P51 | APP-033 / voice critical fields | Confirmation/mishearing and policy-required SMS confirmation prevent unconfirmed booking readiness | P |
| P52 | APP-033 / interruptions | Silence/disconnect/reconnect/delayed duplicate turns preserve state without duplicate jobs/tools | P |
| P53 | APP-033 / human fallback | Transfer/callback/voicemail/provider failure leaves visible owner and truthful outcome with recording disabled unless approved | P |
| P54 | APP-033 / technician outcome | Brief separates observed/unknown/verified facts; assignment/completion links real job/tool outcomes to review and versions | P |
| P55 | APP-033 / full channel acceptance | Approved web/SMS/voice scenario matrix, latency/cost and all ticket criteria accepted independently | P |
| P56 | Pilot matrix / onboarding | Reuse organization page; owner completes O1–O6 and canonical policy consistency on desktop/mobile | P |
| P57 | Pilot matrix / operations | Monitoring, incident owner and missed/uncertain-work recovery runbook demonstrated using existing systems | P |
| P58 | Pilot matrix / restore-release | Disposable restore/rollback and migration-order drill preserve data; approved release checklist and stop controls verified | P |
| P59 | Pilot matrix / integrated rehearsal | Authorized concern→discovery→knowledge→payment/booking→technician→outcome→review journey and mandatory failure scenarios pass | P |
| P60 | Pilot matrix / final acceptance | Owner signs row-by-row evidence, limits and risk disposition; no critical lost-request/false-booking/payment/privacy blocker | P |

## Coverage and no-double-counting

APP-013 criteria 1–12 map P15–P22 plus P01–P14; BE-001 stays P11/P22. Organization O1/O3/O4 reuse accepted local implementation, O2 P27, O5 P47/P48, O6 P56; P56 accepts rather than rebuilds them. APP-017/018/019 seven-criterion sets include access, browser gates and full traceability in P27/P31/P36. APP-015 original five plus five integration additions map P37–P41. APP-016 original eight plus three financial additions map P42–P45. APP-033 original nine plus five integration additions map P46–P55. All thirteen MVP matrix rows map across these groups; operations/onboarding/restore and final integrated proof are P56–P60. Existing technician workflow is reused, not scheduled as a replacement app.

Full equipment pricebooks, financing, diagnostics product, commercial subscription launch and training are not hidden in these rows. If the owner means Release B by “MVP done,” this schedule is insufficient; enumerate that release separately before promising a commercial date. This is a boundary disclosure, not deletion of approved later requirements.

## Forecast and uncertainty

Proposed baseline: 60 remaining packages, targeting 60 focused workdays. Reserve 24 additional focused days (40%) for integration/rework: planning range 60–84 productive days, NOT a statistical confidence interval or guaranteed ceiling. Reserve is time against existing rows, not 24 invented scope items. Confidence low overall, medium-low for near-term APP-013, low for voice/evaluation; no empirical one-day throughput is established yet. Update after the first five executed packages using actual effort; do not automatically reset the denominator.

At five workdays/week starting Monday 2026-09-14: 12–17 working weeks, approximately 2026-12-04 through 2027-01-07 before holidays, absences and blocked days. If genuinely completing one package every calendar day, 60 baseline days is about two months; that requires seven-day capacity and is not the recommended assumed schedule. The owner-tested payment/booking/text walkthrough is P01–P14: target 14 days, planning allowance 14–21 productive days (roughly Oct 1–12 on the same weekday calendar), plus external waits. Earlier nine-days claim is withdrawn.

Calendar delivery = productive days + unoverlapped blocked days + holidays/absence. External waits are unbounded here, not zero: provider account eligibility/reply if genuinely necessary, exact identity/IAM/key approvals, reviewed release/migration, test participant window and paid call/text/email/Calendar authorization. Do not count waiting as a completed work package or switch to a later ticket without governance approval.

Terms-review update: the owner's latest reviewed direction accepts the engineering interpretation that minimal job-action metadata need not await a blanket Google reply; do not retain raw/derived provider proof or call this legal certification. P01 must reconcile this conclusion against stale earlier unresolved wording and finish the exact engineering card, not repeat the same general terms review. A new specific contradictory clause/field must be evidenced before reopening it.

## Daily reporting and change control

P01 accepted 2026-09-13: owner reviewed the engineering contract (backend 8a4ef28/governance 506b9a2) and said “ok great i get to see how long each package take p1 was fast. Begin.” Design package D; elapsed/focused-day duration was not measured. This accepts the engineering card, not customer capability or live authority.

P02 accepted 2026-09-13: backend f1534fc/governance 60621f9, owner said “i reviewed, i agree with more data for timing, proceed.” Local unregistered authority; 47 new tests and 2,198 total passed (3 skipped) at that checkpoint. Measured execution 14:01:15–14:10:12 UTC, 8 minutes 57 seconds including Git closeout; not focused human effort. No external blocking. Review waiting duration was not independently measured. Evidence: backend evidence/APP-013/p02-controlled-authority.md.

P03 review-ready 2026-09-13: distinct encrypted controlled phone proof and transient Google-to-transaction connection, using existing durable address caps/claims and actual disposable PostgreSQL. Source/finite card APP013_P03_SOURCE_CARD.md; backend evidence/APP-013/p03-controlled-verification.md. Execution began 14:16:08 UTC; validation checkpoint 14:32:13 UTC (16 minutes 5 seconds), final evidence/Git closeout additional. Twenty-six new unit cases, 2,224 total passed (3 skipped), connected synthetic-provider database proof and required gates passed. No external blocked or owner-wait time during this run. Actual human focused days not measured; no one-day velocity inferred. P03 R awaiting owner review, P01/P02 D: 2/60 (3.3%) of remaining-plan packages accepted, not overall MVP progress. Next P04 actual job transaction/current-draft loader and recovery, then P05/P06 as planned. No forecast/denominator change; original 60–84 productive-day baseline remains low-confidence pending five measured packages.

P03 final pre-commit gate rerun: 14:35:56 UTC, 19 minutes 48 seconds from start, including final input-boundary review and repeated local checks. Git closeout additional. The earlier 16-minute timestamp is an intermediate validation checkpoint, not total package duration.

Report once per checkpoint: active package ID, planned versus actual focused days, exact working result, validations, R/D status, blocker/owner/wait days, next ID and revised forecast delta. Three separate metrics: walkthrough 3/8 (37.5%); remaining-plan D/60 (starts 0/60, NOT 0% of existing app); pilot requirements accepted/13 matrix rows (audit did not establish new row sign-offs). Do not manufacture overall engineering completion from any of these.

No additional package without demonstrated requirement, existing ticket owner, old/new scope, estimated days and explicit owner review for material scope change. A defect needed to meet a row stays charged to that row and consumes reserve; disclose forecast overrun. Deferred refinements do not block acceptance unless a named criterion requires them. No daily planning-document milestone and no repeated approval of settled product decisions.

Current checkpoint: P05 active: strict version-2 browser submit adapter implemented; separate server-injected controlled port, validated minimal admitted/correction/refused/uncertain responses, no legacy fallback or downstream authority. Seven new tests; 2,282 passed (3 skipped), build/lint/architecture, zero-vulnerability audits and existing disposable database/browser regression passed. This is adapter proof, not the new connected browser journey. APP013_P05_SOURCE_CARD.md fixes four existing items; item 1 complete, composition, customer UI and connected desktop/mobile proof remain. Backend evidence/APP-013/p05-browser-adapter.md. Owner reviewed P04 and subsequently requested proceeding after admin documentation; P04 local package accepted, not live 2B. Remaining-plan accepted 3/60 (5%); walkthrough stays 3/8 (37.5%). P03's existing R entry is not independently promoted here. No new package or measured velocity; 60–84 productive-day low-confidence baseline unchanged. P06/live activation and admin implementation remain gated. No scope deviation.

P04 local acceptance: owner said "i reviewed, what is next?" after f0201ac/40d8add evidence, then "great now that these requirements are documented, lets proceed" after the separate admin planning discussion. This accepts local P04 and authorizes P05 continuation, not live 2B or release. P04 focused/owner-wait timing remains unmeasured; no velocity sample awarded.

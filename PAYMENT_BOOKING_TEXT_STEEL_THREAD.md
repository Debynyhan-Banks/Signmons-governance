# Payment, booking and text steel thread — baseline v1

## Current: fixed execution contract; planning before coding

APP013_REMAINING_EXECUTION_CONTRACT.md is the current section-planning and status reconciliation. Preserve the five remaining IDs 2B → 3A → 3B → 3C → 3D; correction screens are internal 2B work, not new sections. Next is completing 2B's exact real-source/session/retention/patch/test contract before more implementation. County GIS is not a gate; prior phone/Google tests are closed and not current admission proof. Older blocked-entry, Next-empty and source/retention assumptions below are historical where superseded by the Google-only policy and approved intelligence queue. No standalone demo or automatic new live test. APP-013 sole Now; accepted 3/8 (37.5%) unchanged. This documentation correction grants no external/release authority.

## Owner-approved remaining five-section plan — 2026-09-12

Owner agreed to prioritize 2B blockers and stop presenting internal SMS implementation slices as new sections. This reaffirms the existing eight-section baseline; it does not add sections, authorize external actions or promise five turns. Accepted remains 1A, 1B, 2A: 3/8 (37.5% milestones). Current 2B is blocked at controlled-entry. No overall MVP completion percentage or ETA is inferred.

| Order | Existing section | Included work | Observable finish line |
| --- | --- | --- | --- |
| 1 | 2B verified intake to job | Qualified county/address source, existing phone/address adapters, protected journey, account/environment and capped-test prerequisites | Owner receives code, confirms eligible address and creates exactly one reviewed job; invalid/uncertain proof refuses admission |
| 2 | 3A Sandbox payment | Same job, existing Checkout and signed payment events, truthful pending/failed/paid state and retry | Owner completes Sandbox payment; matching verified event clears that job's gate without duplicate requests |
| 3 | 3B test-calendar scheduling | Paid job, availability, protected booking, calendar acknowledgment and initial-booking recovery | One appointment appears in app and isolated test calendar; unpaid/conflicting/uncertain work never falsely confirms |
| 4 | 3C received confirmation text | Remaining consent integration, provider replay protection, sender/recipient and send-release controls, actual capped test | Owner receives correct confirmation; app shows truthful delivery state and refuses stale/revoked/foreign authority |
| 5 | 3D changes and recovery | Same job's reschedule/cancel, existing recovery surfaces and integrated failure matrix | Owner repeats full workflow and failure cases without duplicate logical payments/bookings or unintended messaging |

3C's remaining engineering inventory is explicitly: (a) duplicate/delayed START versus later STOP protection; (b) approved policy-bound evidence to actual consent grant and protected intake UI/transport; (c) retention/key lifecycle and separate capture/send controls; (d) actual policy/provider/sender/recipient qualification and capped receipt demonstration. Existing registry, encrypted evidence, locks and fixture storage are reused, not rebuilt. These are material subtasks tracked within 3C, not additional acceptance milestones or automatic permission to continue SMS work while 2B is blocked.

Execution rule: work the current section's blocker or acceptance path. When an external prerequisite is unavailable, report its exact missing evidence/owner and stop; alternate offline work requires a separately agreed bounded purpose and must not be counted as acceptance. Any new section, material expansion or changed finish criterion requires owner-approved baseline change with reason and impact. Nonessential improvements go to backlog. Every future update identifies section ID, completed/remaining subtasks, blocker, next observable demonstration and accepted Y/8.

Approval gates are tracked separately from engineering: actual county qualification, existing account/environment readiness, notices/data handling, exact test destinations/resources, current account rates and enforceable caps, and explicit action/release approval. The old draft test budget is not approved by this plan. Account observations and prices are historical until refreshed.

This walkthrough is not the full MVP. Voice, email, organization onboarding, dispatcher/technician completion and operational acceptance remain visible in MVP_COMPLETION_AUDIT_2026-09-11.md and their existing ledgers; they are not hidden inside 3D or asserted complete. This turn is documentation/read-only reconciliation, not a fresh audit of those areas.

## SMS readiness dependency reconciliation — 2026-09-12

PILOT_SMS_ACTIVATION_READINESS.md maps completed local fixture capture/storage proof and the remaining tenant policy/real-consent integration plus external approvals into existing 3C. P1/P2 are internal work packages, not new acceptance sections or a promise of two remaining turns. No fixture-storage rewrite or additional planning loop is proposed. Current milestone remains 2B; acceptance remains 3/8. County/verification gates remain independent. No baseline change or controlled-action approval.

## Authority and target

Owner approved planning and sizing with “i agree with recommendation proceed” after the eight-section proposal. This checkpoint establishes a fixed delivery baseline, not blanket implementation, numerical-policy, provider or release approval. APP-013 remains sole Now; Next empty; FE-014 paused. No Eternity website work.

Target: the owner personally follows one controlled request through verified intake, one eligible job, Stripe Sandbox payment, an available test-calendar appointment and a received eligible confirmation text. Section 3C is the first connected happy-path demonstration; 3D completes change/cancel and recovery acceptance. Neither completes APP-013 or the whole MVP.

Use the same approved organization, customer journey and correlated request/job/appointment/message records across sections. Fictional personal/job data only until a named legitimate test participant and environment are explicitly authorized. Never hand-seed a paid/verified job to claim the connected walkthrough passed. Lower-level fixture tests remain useful but are labeled separately.

## Baseline and progress rules

- Fixed IDs: 1A, 1B, 2A, 2B, 3A, 3B, 3C, 3D. Eight acceptance sections, not eight equal effort units or eight turns.
- State progression: Planned → Approved → Implemented → Demonstrated → Accepted. Blockers are a separate field; implementation and provider approvals are recorded separately. Accepted requires the listed evidence and explicit owner sign-off for that section.
- Current section: 2B, section 4 of 8, entry review only; blocked before controlled actions. Owner accepted 2A with “i reviewed continue”. Accepted: 3/8. CONTROLLED_VERIFICATION_2B_CHECKLIST.md records unresolved county/source/account/participant/spend gates. No live action approval inferred. Existing VO-1/VO-2 evidence is reused, not reset or counted as a ninth section.
- Every subsequent update reports current section ordinal/ID, accepted Y/8, demonstrated workflow, concrete blockers, evidence/commit and next demonstration. Report local versus controlled-provider evidence separately.
- New section, split, removal or changed acceptance requires an owner-approved baseline change recording reason, demonstrated blocker, effect on count/dependencies and prior baseline. Log internal subtasks under the same section; do not quietly grow the denominator or hide material work as a subtask. Unrelated improvements go to the backlog.
- These eight sections cover this walkthrough only. APP-013 scope index remains 50%, accepted 0/12; onboarding local 3/6 (50%), accepted 0/6; pilot accepted 0/12. Do not convert accepted-section fraction into effort or whole-MVP completion. No calendar ETA is supported.

## Source-based sizing

Fetched both origins and inspected backend cbe605f and governance 6efb066, both aligned with their focused upstream branches. This is a read-only implementation inventory, not a fresh runtime/provider certification.

| Section | Relative integration size / confidence | Existing seams and concrete gap |
| --- | --- | --- |
| 1A | Medium / medium | durable-verification.service.ts, address-operation-ledger.ts/executor.ts, customer-session/revision contracts and local-verification-browser.service.ts. Mock-only flags remain false; no common current-proof eligibility consumption. Add bounded freshness/revocation without live authority. |
| 1B | High / medium | local-correction-port.mjs has process-local candidate/intent copies; VO-2 durable ledger retains liability. Need per-session server-owned purge/restart/restore behavior and explicit retained-reference mapping; no generic cleanup platform. |
| 2A | High / medium | customer-intake-continuation.service.ts admitReview already locks sessions, binds organization and deduplicates jobs; it explicitly refuses localAddress review records. Connect trusted proof consumption and existing customer/operator UI, not removal of that guard alone. |
| 2B | High / low until entry gates | Existing inactive phone/Google adapters and county contract; local browser service explicitly has no phone/booking/delivery authority. Qualify county, bind named test identity/accounts, compose the approved controlled path and prove it. Conditional source selection is not qualification. |
| 3A | Medium / medium | payments.module.ts registers request and signed-webhook services; payment-requests.service.ts, stripe-checkout.provider.ts, stripe-webhooks.service.ts and ui/src/app/app/dispatch/page.tsx exist. Connect the newly admitted job and current policy to Sandbox and demonstrate real test events; no replacement payment stack. |
| 3B | High / medium | scheduling.module.ts registers scheduling and confirm/reschedule/cancel; appointment-confirmation.service.ts records finalization and notification intent. Calendar recovery classes are not registered there. Connect current job/payment/availability and bounded recovery ownership without false confirmation. |
| 3C | Medium / medium | Registered SMS intent/delivery/worker/history and transactional policy/template services. Connect current finalized event/recipient/consent to controlled delivery and visible status; no generic messaging editor. |
| 3D | High / medium | Existing reschedule/cancel, calendar-applied/uncertain recovery, sms-enqueue-recovery and payment-event transitions. Integrate failure ownership and repeat the same journey; tests/classes alone are not operational recovery. |

Medium means primarily connecting existing seams plus regression proof. High means a missing lifecycle or application boundary plus integration proof. These labels are planning judgments, not hours. High/low-confidence 2B may require an explicit baseline revision after account/source gates resolve; eight is not a guarantee that unsized external work fits one run.

Evidence anchors: backend evidence/APP-013/address-execution/README.md, browser-review-admission/README.md, booking-readiness-preview/README.md, organization-payment-policy/README.md; evidence/APP-012/readiness-report.md; scripts/verify-initial-booking-payment.mjs. Prior 96 suites/1,835 tests are historical VO-2 results, not new plan validation. Existing toolchain warnings and the passed-on-rerun Node exit 139 are not declared resolved by planning.

## Section acceptance cards

### 1A — Freshness and invalidation (VO-3 first part)

- Entry: owner confirms numerical policies below and approves this section's mock-only implementation; current VO-2 checkpoint reviewed.
- Work: bind phone/address proof to tenant/session, exact respective revisions, checked/confirmed/expiry timestamps, notices and relevant current policy. Enforce expiry server-side; invalidate only affected proof on edits, all relevant proof on session closure/expiry. Recheck at consumption, not only browser display.
- Demonstration: complete the existing mocked verification flow; reuse valid proof without a new code/call, advance to exact expiry and refuse, edit one field and invalidate only its affected proof, race revocation against a read/consumption check and refuse stale eligibility. Keep the draft. Missing policy, foreign tenant/session and changed notices/policy refuse.
- Stop: responsive existing journey and database/unit proof pass; no live dispatch, county acceptance or job creation authority. Durable monetary holds unchanged.

### 1B — Cleanup and restart (VO-3 closeout)

- Entry: 1A accepted; owner approves reference/digest deletion mapping and 1B implementation. Submitted-business-record retention stays separate.
- Work: bounded per-session transient ownership, retryable server cleanup and startup/restore checks. Purge permitted correction data at session end or 24 hours, earlier wins; never revive expired proof. Preserve minimal unresolved liabilities independently. No raw provider data in durable stores/logs/backups.
- Demonstration: two sessions cannot access/clear each other; session end/expiry clears eligibility immediately even if cleanup fails; cleanup retry removes copies; restart and restore simulation do not resurrect proof or lose holds. Test abandoned-draft seven-day-or-earlier deletion only against matching fixture records. No OS-process-kill claim unless actually tested.
- Stop: same journey recovers truthfully; documented data inventory, purge deadlines and retry owner are evidenced. No deletion of production/customer/business records.

### 2A — Current-proof admission connection

- Entry: 1A/1B accepted and explicit section approval; inspect/reuse the admission transaction and permitted operator review. No new ticket promotion.
- Work: server-resolved proofs and current approved organization/coverage/payment policy consumed atomically with exactly one eligible job. Preserve required human job review as distinct from automated verification; do not add mandatory human phone/address checking. Map the actual customer/operator application identity and transport boundary, not another standalone form.
- Demonstration: existing customer submits, authorized operator reviews, one eligible fictional job appears through the controlled local boundary. Lost acknowledgment/concurrent submit replays the original job; changed address/phone/policy, stale/foreign/uncertain proof and audit failure cannot create it. Associate valid consent without treating verification as messaging consent.
- Stop: local injected-source result is explicitly fixture evidence only, not real proof acceptance. No booking, payment or sending. 2B must repeat this path using approved controlled sources before real admission acceptance.

### 2B — Controlled verification acceptance

- Entry: 2A accepted; qualified Cuyahoga source and approved source terms, legitimate test participant, U.S.-only destination/address rules, named tenant/environment/accounts, current rates, separate phone/address/shared caps, notices, retention and incident owner. Explicit narrowly capped calls/spend and any needed configuration approval required. +1 or ZIP alone never proves eligibility.
- Work: compose existing approved adapters into the same protected journey with trusted account/identity/evidence ownership. Resolve any reachable operational phone/address liability/reconciliation blocker; uncertain costs remain held, no unsupported refund/resend. No provider selection or account changes under this planning approval.
- Demonstration: approved phone receives a code, correct code proves access, approved address correction and qualified county evidence produce one eligible job via 2A. Wrong/expired code, edits, out-of-area, boundary ambiguity, source outage and cap exhaustion preserve draft and refuse admission. Bind evidence IDs privately; record actual provider observations without secrets/customer payloads in public evidence.
- Stop: owner accepts controlled verification-to-job evidence. If county/account prerequisites are unavailable, mark this section blocked; never replace county proof with a ZIP or quietly downgrade to a mock. Record an explicit change request if scope cannot fit the bounded path.

### 3A — Sandbox payment on that job

- Entry: 2B accepted for the connected demonstration; explicit Sandbox environment/account and test actions approved. Offline preparation can be separately approved while 2B is blocked, but does not pass the end-to-end dependency. Verify existing connected-account contract; do not change routing, fees or billing.
- Work: reuse trusted payment-policy/amount snapshots, request idempotency, Checkout and signed webhooks; connect existing customer/operator controls. No SDK/API upgrade, provider configuration or secret handling changes are implied.
- Demonstration: owner requests and completes a Sandbox payment for the admitted job. Verified matching-mode/account/amount/currency paid event clears its gate; redirect alone, pending/failed/unpaid events and forged/foreign events do not. Duplicate/out-of-order events and lost response cannot duplicate payment requests or regress settled state. Exercise asynchronous events where the configured method permits them.
- Stop: actual Sandbox event and application-state evidence, safe operator visibility and retry/recovery pass; no real money, booking or text send. This is the first connected payment test, after section 5 of 8.

### 3B — Test-calendar scheduling

- Entry: 3A accepted; named isolated calendar, scheduling timezone/availability and explicit test-calendar write permission. No live customer appointments; initial-booking recovery must be usable before claiming success, not deferred wholesale to 3D.
- Work: connect current paid job to availability, protected booking controls, Calendar acknowledgment and local finalization. Expose bounded uncertain-work ownership using existing recovery seams; no generic reconciliation engine.
- Demonstration: owner chooses an available test slot; exactly one logical appointment is finalized with acknowledged calendar evidence. Unpaid job, occupied slot, concurrent retry, provider failure and crash/lost acknowledgment before local finalization never falsely confirm or duplicate booking. Operator sees pending/uncertain state and permitted recovery.
- Stop: appointment visible in the test calendar and application; no automatic live confirmation message unless separately approved in 3C. First connected scheduling test: section 6 of 8.

### 3C — Controlled confirmation text

- Entry: 3B accepted; explicit named test recipient/sender/account, valid transactional policy/consent, current rates and capped external-send approval. Phone verification is not sending permission. Existing finalization enqueue must remain send-disabled until this gate.
- Work: reuse finalized appointment event, durable logical intent, fixed template, recipient eligibility, delivery/history and authenticated status callbacks in the same operator view.
- Demonstration: owner receives the appointment confirmation on the designated test phone; application records truthful accepted/sent/delivered/failed/uncertain distinctions. Duplicate event/callback does not create another logical send. Missing/revoked consent, wrong tenant/recipient and stale appointment cannot send. Initial delivery failure has visible ownership and never removes the booking.
- Stop: application evidence plus owner-confirmed receipt, not provider acceptance alone. No promise of external exactly-once delivery. First connected payment → booking → received-text walkthrough: section 7 of 8.

### 3D — Changes and recovery acceptance

- Entry: 3C accepted; explicit test change/cancel and bounded additional-send permission. Reuse that job and isolated resources.
- Work: connect existing reschedule/cancel and operator recovery surfaces; complete the integrated failure matrix, not new generic infrastructure. Refund behavior is observed using safe local/Sandbox evidence only if approved; no automatic refund policy added.
- Demonstration: reschedule updates the same appointment and eligible notice; cancel leaves no active booking/action claim and sends only eligible cancellation notice. Repeat exact retries, interrupted Calendar finalization, duplicate/out-of-order payment events, known send failure and ambiguous send outcome. Show private role-safe status, evidence-backed human recovery, no blind resend and unchanged accounting holds. Do not assert SMS already sent can be recalled.
- Stop: owner repeats full walkthrough and recovery cases with evidence/sign-off. Eight-section walkthrough accepted only when all eight cards pass; full APP-013 email/lifecycle and whole-pilot acceptance remain separate.

## Decisions and external gate register

| Gate | Proposed/current policy | Owner and required next evidence |
| --- | --- | --- |
| FRESHNESS | Owner approved 30 minutes from successful phone check/address validation, capped by session expiry and any shorter authoritative source expiry; exact revisions/current policy. Confirmation cannot refresh old validation. This is proof lifetime, not OTP expiry. Existing 15-minute session remains unchanged. | Explicit “yes i approve proceed” after the 1A approval request. Mock implementation demonstrated; no real-provider proof claim. |
| RETENTION | Approved for 1B: correction cache at session end/expiry or 24h, earlier; abandoned draft payloads at existing session expiry, earlier than seven days. Minimal resolved aliases: 90 days after authoritative cancellation with zero hold and no dispatch. Core accounting rows/counters/audits and unresolved liability retained, not erased/refunded. No new durable customer-input digest. | Owner “yes” approved 1B and ninety days. Only supported cancellation aliases qualify; provider/business-record terms and production rollout remain gated. Not legal/accounting advice or production deletion authorization. |
| COUNTY | All Cuyahoga County, Ohio; Google-only structured address/state/country/county evidence under GOOGLE_ONLY_SERVICE_AREA_POLICY.md. | County GIS reply is not required. Actual connected address/coverage evidence and permitted retention remain 2B obligations. |
| LIVE-VERIFICATION | U.S.-only legitimate participants, named environment/tenant/accounts, approved notices/rates/caps, test identity, privacy and recovery owner. Existing $50 phone policy is not permission to spend or an address allowance. | Product owner approves bounded integration actions; implementer records entry checklist and actual evidence in 2B. |
| SANDBOX/CALENDAR/SMS | Separate permission for Stripe Sandbox actions, named test-calendar writes and controlled SMS sends/spend. Existing credentials/configuration must be checked safely; public docs contain no keys or recipient personal data. | Product owner names resources and limits before affected 3A/3B/3C work; no account provisioning by inference. |
| SCOPE/OWNERSHIP | APP-013 sole Now; reuse APP-010/011/012. Calendar gaps retain APP-016 mapping; later-ticket implementation requires pointer/handoff approval. | Owner approves cross-ticket scope or baseline changes before implementation; no silent ticket promotion. |

## Acceptance tracker

| Ordinal / ID | Status | Blocker / dependency | Evidence and implementation commit | Owner acceptance |
| --- | --- | --- | --- | --- |
| 1 / 1A | Accepted | None for local section; live gates unchanged | Backend 4c5030a; evidence/APP-013/verification-freshness/README.md and committed database/browser summaries | Owner “proceed”, 2026-09-11 |
| 2 / 1B | Accepted | Production cleanup not activated | Backend 37bcb15; evidence/APP-013/verification-cleanup/README.md and committed database/browser summaries | Owner “i reviewed the evidence proceed”, 2026-09-11 |
| 3 / 2A | Accepted | Real source/identity activation remains 2B | Backend f8e35e8; evidence/APP-013/current-proof-admission/README.md and summary | Owner “i reviewed continue”, 2026-09-11 |
| 4 / 2B | In progress; connected acceptance pending | Real-source/session/retention contract and connected admission remain; new controlled actions need current approval. No current Chrome or county-GIS blocker inferred. | APP013_REMAINING_EXECUTION_CONTRACT.md; closed real-phone and Google subchecks; backend c52bd2b transient screen is synthetic-tested, not admission | Pending |
| 5 / 3A | Planned | 2B, Sandbox action approval | Pending | Pending |
| 6 / 3B | Planned | 3A, calendar and recovery scope approval | Pending | Pending |
| 7 / 3C | Planned | 3B, SMS recipient/consent/send approval | Pending | Pending |
| 8 / 3D | Planned | 3C, change/cancel/recovery test approval | Pending | Pending |

For each update append the actual commit, reproducible command, protected artifact reference, observed result and owner acceptance date/message. Gate resolution may be researched in parallel only with appropriate authority; it never justifies new provider actions or skipping acceptance dependencies.

## Validation, review and boundaries

Each implementation section requires focused/full backend tests, lint, build, architecture, relevant Prisma/schema validation, dependency checks with recorded risk disposition, real disposable database concurrency/rollback proofs where applicable, and mobile/desktop browser QA for affected customer/operator flow. UI changes also run UI tests/build/lint. Check authorization/redaction and evidence cleanup. Controlled external proofs require approved accounts/actions and actual results, not mocks. Do not rerun all runtime gates for docs-only changes or present historical results as current.

This documentation-only checkpoint runs governance consistency, four execution-placement tests and diff checks in both repositories. Review: confirm eight IDs and stop conditions; review FRESHNESS/RETENTION; verify section dependencies and named external gates; confirm 3C is happy-path demo and 3D recovery completion; check no production/send permission was inferred. Then approve 1A and its policy, not all eight implementations at once.

Remaining outside this walkthrough but still in approved MVP: eligible email delivery/failure/retry and private actions, all APP-013 role/event criteria, S3 dispatcher/technician completion, full conversational voice/SMS and missed-call handoffs, S4 safety/operations/restore/rollout and twelve-check pilot acceptance. Sales-advisor expansion, website import and marketing remain deferred. No merge, deployment, production migration, IAM/secrets, billing, real charges, real customer records or appointments authorized.

Plan validation results: governance consistency passed; four execution-placement tests passed; eight ordered acceptance cards and eight Planned tracker rows match; all eight governance cross-references resolve; documentation diff checks passed. An initial ad hoc progress-label assertion used the wrong capitalization and was corrected to match the existing label; no product failure was involved. Runtime tests/build/lint/browser QA were not rerun because only Markdown changed. Original saved backend checkout remains untouched, including unrelated user modifications/deletions.

Change log: v1 — owner-approved planning task established eight-section baseline. Subsequent 1A policy/implementation approval and local demonstration update the tracker only: 97 backend suites/1,855 tests, 170 UI tests, thirteen new database groups and parent browser evidence; owner acceptance pending, accepted 0/8. No baseline section/scope change. Supersedes rolling “next section” forecasts for this target, not the frozen MVP scope or historical evidence.

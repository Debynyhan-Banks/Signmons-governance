# APP-013 remaining execution contract

## Authority and fixed scope

Owner requested this planning correction after questioning repeated new sections, then agreed each section must be thoroughly planned before coding. This is a documentation-only reconciliation of PAYMENT_BOOKING_TEXT_STEEL_THREAD.md, not a new feature mandate. Its five remaining acceptance sections stay **2B → 3A → 3B → 3C → 3D**. The recent assistant list that counted the correction screen as its own section is superseded. Correction work belongs inside 2B.

Accepted remains **1A, 1B, 2A: 3/8 (37.5%)**. No acceptance is awarded here. This fraction is not overall MVP completion, effort or an ETA. Section counts are not turn counts. Internal commits do not create new sections.

Snapshot: backend c52bd2b; governance 3c62a0d before this correction; focused origins fetched. Current proof source/consumer and admission transaction inspected; latest correction evidence inspected. Existing downstream seam inventory comes from the steel-thread plan, not a fresh full code or provider audit. Do not call downstream cards implementation-ready until their entry inspection is completed.

## Reconciled inventory

| Classification | Evidence / disposition |
| --- | --- |
| Accepted, reuse | 1A freshness, 1B cleanup, 2A local current-proof admission; preserve their accepted status and existing tests. |
| Demonstrated subcheck, not reusable current proof | evidence/APP-013/real-phone-verification.md: real phone test passed and closed. Do not resend for another standalone proof; a connected journey may require fresh verification under a new approved window. |
| Demonstrated transport only | google-address-live-result.md and google-semantic-live-result.md: two closed requests; retained holds, no retained semantic outcome or real admission acceptance. Owner-reported correction is not a verified county result. |
| Implemented, synthetic proof only | Shared address/county parsers, one-shot control and transient-correction-connection.md. The latter discards selected input and is not a protected session integration. Reuse useful parser/presentation logic; no more independent demonstrations as a default next step. |
| Required, incomplete | Trusted real-source-to-current-session proof, correction/revalidation and approved retention/evidence mapping, actual protected intake/operator identity, atomic reviewed job admission and connected controlled evidence (2B). |
| External or owner gate | Google-derived retained-field permission remains unresolved where necessary for durable admission evidence. Current environment/rates/caps/notices/release authority must be qualified for the next actual run; past observations are not fresh approval. |
| Removed blocker | County GIS reply/CEGIS qualification: no longer required under GOOGLE_ONLY_SERVICE_AREA_POLICY.md. Do not request it as an entry gate. |
| Deferred | Further temporary-dialog/standalone-screen polish, new generic evaluators/recovery frameworks, provider replacement, billing redesign, marketing and Eternity website work. Security or correctness defects on the actual acceptance path are not deferred. |

## Mandatory section card before implementation

For the current section, fill these fields in this file or a directly linked evidence card **before coding**, not retrospectively:

1. Existing acceptance ID and user-observable finish line; exact criterion(s) served.
2. Current source SHA, existing components/tests to reuse, exact missing behavior and expected files/interfaces. Inspect registration and the actual route, not just class existence.
3. End-to-end sequence, identities, input/output contracts, state changes, retention and authority boundaries. State how edited/expired input reaches the next step without losing the draft.
4. Finite internal task checklist with an exit test for each; label investigation versus implementation versus controlled acceptance. No moving finish line.
5. Required positive/negative/concurrency/restart/browser tests and exact commands, including environment. Reuse accepted proof; rerun relevant regressions rather than rebuild it.
6. Entry dependencies and separate external approvals: status, named role responsible, exact missing evidence, and smallest decision required. Unknown is not absent or approved.
7. Explicit exclusions, rollback/disabled state, review artifacts and owner acceptance evidence.
8. Relative size/confidence based on inspected gaps. If still unsized or blocked, say so and do not invent an ETA or implement a substitute demo.

Routine fixes inside a complete approved card can proceed without asking the owner to select every function or commit. Missing material design/retention authority blocks that dependency. A new section, replacement provider, altered acceptance criterion, substantial new subsystem or prerequisite outside the finite checklist requires a change request **before implementation**, with cause, alternatives and impact. Do not turn that discovery into silent subtask growth. Documentation updates cannot retrospectively authorize scope.

## 2B — verified intake creates one reviewed job

**Finish:** in one protected journey, the owner verifies phone access, confirms an eligible Cuyahoga address, submits the reviewed draft, and the authorized operator admits exactly one job. Invalid/uncertain/stale input preserves progress but cannot create the job. No payment/booking/send authority follows.

**Reuse:** current-proof-admission.ts; customer-intake-continuation.service.ts/admitReview; existing protected customer/operator transport; Google shared parsers; verification freshness/cleanup/budget components. Current optional source is injected fixture evidence, not actual provider proof. The inspection CLI is not the final customer application boundary.

**Finite internal checklist (all within 2B):**

- [ ] Resolve the implementation contract: map actual source evidence to tenant/session/phone/address revisions, approved policy, freshness and the existing transaction. Specify permitted retained fields and unresolved Google permission dependencies. Inspect current-proof source/route/identity registration and produce the exact patch/file and test list. Exit: no unnamed source, storage, identity or expiry assumption. No new production resource by inference.
- [ ] Implement that same protected journey: correction selection updates its draft/revision; edits invalidate only affected proof; any required revalidation uses the approved budget path and explicit action, not automatic retry. Exit: current proof consumed at admission; no browser VERIFIED flag, fixture promotion or discarded selection masquerading as completion.
- [ ] Prove integration locally with the existing disposable database/customer/operator harness. Cover inside/outside/unknown, unit correction, wrong/expired code, changed policy/tenant/session/revision, duplicate/concurrent submit, audit rollback, restart/expiry, unavailable provider and held cost. Exit: one logical job or truthful refusal with retained progress, no provider calls inside the database transaction. Run relevant unit/full/backend/UI/browser/security gates.
- [ ] Qualify and execute one connected controlled acceptance packet only after explicit approval: exact environment/accounts/participant, phone/address ceilings and window, notices/retention, stop/reconciliation owner and required release actions. Reuse recorded participant willingness; do not reuse expired proof or reset prior holds. Exit: actual correlated phone/address/job evidence, private data handled as approved, owner sign-off.

**Entry status:** accepted 2A is satisfied; Google-only county policy is settled. Real proof binding and retained-field contract are incomplete; current live resources/permissions require refresh before use. Implementer owns source mapping; product owner approves material policy/resources/actions; Google/support or an authorized terms reviewer resolves provider permission where required. No promise that support must answer before all offline design can proceed, and no blanket assertion that retention is already permitted.

**Not included:** new standalone form, another connectivity-only test, manual verification as normal customer flow, county GIS, payment, booking, SMS confirmation, new infrastructure. Do not start additional offline work merely because a required gate is unavailable.

**Size:** high; low confidence until the first checklist item is resolved. Next action is this concrete implementation-contract inspection, not another new section or live call. Review artifacts: source/field map, local integrated results and approved controlled packet/results. Stop at review with pending acceptance explicitly identified.

## 3A — Sandbox payment on the admitted job

**Entry:** 2B accepted; approved Sandbox account/mode/actions and existing payment-routing contract verified. **Reuse:** payment-requests.service.ts, stripe-checkout.provider.ts, stripe-webhooks.service.ts and dispatch/customer controls; inspect current versions at entry.

**Finite work:** map admitted job/current policy to existing request → expose existing Checkout link → consume authentic matching Sandbox event → demonstrate payment gate and failure recovery. Patch only gaps found in this sequence; no replacement payment stack.

**Exit tests:** owner completes Sandbox payment for that same job; matching mode/account/amount/currency signed event clears its gate. Redirect alone, unpaid/failed/forged/foreign events cannot. Duplicate/out-of-order event and lost-response replay do not duplicate logical payment requests or regress settled state. Evidence includes provider test event and app state, not screenshot alone. Run existing payment unit/integration/browser gates and applicable full checks.

**Exclusions:** real charges, new fees/routing, refunds, Twilio Pay, SDK upgrade and booking. **Owner/gate:** product owner authorizes Sandbox actions; implementer verifies exact configuration and prepares card before coding. **Size/confidence:** medium/provisional pending entry source inspection. Stop at accepted same-job payment evidence; no external next-stage action inferred.

## 3B — one test-calendar appointment

**Entry:** 3A accepted; named isolated calendar, timezone/availability and writes explicitly approved. **Reuse:** scheduling.module.ts, confirmation service, current calendar journal/readback and recovery seams; inspect actual registration at entry.

**Finite work:** same paid job → available slot → protected confirmation → acknowledged calendar write → local finalization and visible uncertain-work recovery. Initial-finalization recovery belongs here, not deferred to 3D.

**Exit tests:** one appointment visible in app and test calendar. Unpaid/conflicting slot, concurrent retry, provider error, lost acknowledgment and pre-finalization interruption never falsely confirm or duplicate it. Operator can identify and resolve uncertain work with supported readback. Use disposable database crash/race tests, affected browser checks, full gates and approved calendar observations.

**Exclusions:** production appointments, generic reconciliation rewrite, automatic confirmation send. **Owner/gate:** product owner approves isolated writes; implementer qualifies recovery owner/path before execution. **Size/confidence:** high/provisional. Stop at accepted same-job appointment evidence.

## 3C — receive that appointment's confirmation text

**Entry:** 3B accepted; exact sender/recipient/account, current transactional consent/policy/rates/cap and send permission qualified. Phone verification is not SMS consent. **Reuse:** event/intent/template/delivery/history and authenticated webhook stack; use PILOT_SMS_ACTIVATION_READINESS.md and BE001_DEPENDENCY_REVIEW.md.

**Finite work:** reconcile existing delayed START/STOP replay safeguards → connect real policy-bound consent to protected intake and actual send eligibility → qualify retention/key/capture-versus-send controls → execute approved one-journey confirmation. Inspect for newer completed code before implementing any listed gap.

**Exit tests:** owner receives correct appointment text and app displays truthful provider status. Duplicate callback/event, delayed old START after STOP, revoked/missing consent, wrong recipient/tenant and stale event cannot authorize another logical send. Failed/uncertain send stays visible and does not undo booking; no blind resend. Unit/database/browser checks plus actual authorized receipt are required.

**Exclusions:** marketing, generic template editor, new consent-storage framework, external exactly-once promise. **Owner/gate:** product owner approves recipient/send; implementer records eligibility and recovery evidence. **Size/confidence:** medium/provisional. Stop at accepted connected payment → booking → received-text happy path.

## 3D — changes and recovery on the same journey

**Entry:** 3C accepted; test change/cancel and any extra messages explicitly capped/approved. **Reuse:** existing appointment lifecycle, payment event handling and calendar/SMS recovery controls.

**Finite work:** reschedule same appointment → cancel it → execute the existing integrated failure matrix → record operator recovery and owner replay/sign-off. Fix only demonstrated acceptance-path defects; no generic reliability platform.

**Exit tests:** app/calendar agree after reschedule/cancel; only eligible notices; no active booking claim after cancellation. Exercise duplicate/out-of-order payment callbacks, interrupted calendar finalization, known/unknown message failure and exact replay without duplicate logical effects or lost holds. Role-safe audit and recovery ownership shown. Full walkthrough repeated by owner and accepted with evidence.

**Exclusions:** unapproved refunds, real appointments, new observability platform and all remaining MVP scope hidden in this section. **Owner/gate:** product owner authorizes controlled changes; implementer records exact failure matrix before execution. **Size/confidence:** high/provisional. Stop: eight-milestone walkthrough accepted, not automatic APP-013 or pilot completion.

## Reporting and remaining MVP boundary

Every update uses: **section ID; completed checklist items; remaining items; blocker/owner; next observable result; evidence SHA; accepted Y/8**. New tests/commits do not increase acceptance. Update a single current status; historical entries do not override it. Do not present the next internal function as a new section.

After 3D, reconcile remaining APP-013's twelve criteria, including full role/event SMS coverage, independent SMS/email policy, branded email lifecycle, email failure/retry, private credentials/redaction and audit. The walkthrough does not accept those automatically. MVP_ACCEPTANCE_MATRIX.md remains the full pilot ledger. After full APP-013 acceptance follow the approved queue APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033. Onboarding, technician/dispatcher flow, intelligence/voice, evaluation and operational acceptance remain tracked there, not invented inside 3D. Do not apply stale pre-alignment sales/voice deferrals over the reviewed intelligence scope.

No merge, deployment, migration, IAM/secrets, charges, provider configuration, customer contact, production data changes or training is authorized by this planning correction.

# 2B implementation card — protected verification to one reviewed job

## Status and authority

Planning-only source inspection at backend 76d48e16e0154e3649364150f9e1e54f3f761690 and governance d1b1689. Both origins fetched; safeguards are now merged separately at backend 8f571c3 and governance 59b6b91. This card supplements, and does not modify, the frozen APP013_REMAINING_EXECUTION_CONTRACT.md. Product feature branches are preserved; this does not merge them or claim they already include main's newer controls.

Section: existing **2B**, internal checklist item “Resolve the implementation contract.” Finish criterion unchanged: one protected customer journey verifies current phone/address/coverage, retains the reviewed draft, then an authorized operator creates exactly one job. No payment, booking or notification authority. Accepted walkthrough remains 3/8 (37.5%). No scope deviation.

**Design proposed, not yet implementation-ready:** source and patch map below are concrete; provider-derived retention authorization and the exact protected customer bootstrap/release configuration remain gates. Do not mark the first checklist item complete or begin implementation until those decisions are resolved. No new standalone screen or transport rehearsal is the next step.

## Verified gaps, not inferred missing features

| Inspected source | Existing behavior | Required delta for 2B |
| --- | --- | --- |
| current-proof-admission.ts | CurrentProofSource and AdmissionSourceEvidence require FIXTURE_ONLY; consumer returns fixtureOnly true and realVerificationAccepted false; checks database time, tenant/session/revisions, approved organization/payment and county | Add an explicitly distinct controlled source/receipt contract; never rename fixture evidence to real or flip a return flag alone. Reuse the invariant checks. |
| customer-intake-continuation.service.ts | Optional admissionProof consumed inside admitReview transaction; exact replay and atomic job/link/consent/audit exist | Resolve real source at this existing write boundary; disabled/missing real evidence refuses controlled admission. Existing optional fixture path stays isolated. |
| durable-verification.service.ts / verification-freshness.ts | Encrypted conversation ledger supports optional proof; freshness policy currently fixture-only | Separate source provenance from shared time/revision arithmetic; trusted provider CHECK may create controlled phone evidence only in current approved session. |
| staging-phone.service.ts | Registered phone-only route constructs durable service without freshnessPolicy and returns jobAdmissionAuthorized false | Reuse provider/durable primitives in controlled intake composition; do not reuse a historical phone-only result or silently expand its old approval. |
| customer-consent-browser-transport.ts | Bounded headers/body/origin/session transport with correction/address/verification ports | Wire real ports behind a server-owned approved tenant/bootstrap binding, not browser-supplied tenant or VERIFIED fields. Keep credentials out of browser/operator payloads. |
| customer-intake-review.controller.ts / communications.module.ts | Operator controller has auth/tenant guards but is deliberately absent from application module; continuation also not registered there | Explicit disabled-by-default controlled registration with real operator identity; merely registering controller is insufficient without its providers and proof source. |
| address-operation-ledger.ts / address-operation-executor.ts / google-address-operation.ts | Session/revision operation and cost identity exist but execution/policy are fixture-only; Google operation discards semantic body | Reuse schema/locks/reservations while defining separate controlled provenance, trusted request loading and allowed semantic-result ownership. File-based one-shot holds are not a distributed ledger. |
| google-address.adapter.ts / google-service-area.ts | Shared transient parser and Google-only coverage checks exist; review output has no admission authority | Consume qualified result under exact session/address/policy binding; keep correction, UNKNOWN and out-of-area distinct. |
| scripts/run-google-semantic-inspection.mjs and transient screen | Closed inspection discards selected address; not a persistent protected journey | Reuse useful presentation logic only inside the existing journey. Do not call this CLI from the app or run another standalone test. |

## Proposed end-to-end sequence

1. Server starts the existing protected customer session from an approved server-side tenant/integration mapping; source identity is not a body field. Operator authenticates separately through existing RequestAuthGuard/TenantGuard. Exact deployment origin, bootstrap credential owner and tenant allowlist must be recorded before activation; none is invented here.
2. Customer draft remains in the existing encrypted continuation/session path. Browser submits intent, never authoritative proof. Normalize phone; request notice opt-in separately from messaging consent. Reserve approved liability, perform provider I/O outside job-admission transaction, then bind successful CHECK to the same phone revision/session/current policy.
3. Customer submits current address/unit. Claim a durable address operation keyed to session/intent/revision/policy and reserve allowance before I/O. Load request from trusted draft. Parse response transiently. Missing/conflicting county/unit evidence is UNKNOWN; no ZIP fallback or mandatory GIS lookup.
4. If correction is needed, show original and candidate in that journey. Confirm selects the exact server-owned candidate; edit changes customer-stated draft. Either affected change increments address revision and invalidates affected address/coverage proof. It does not refresh old validation or send another request automatically. Revalidation requires explicit action within the approved operation budget. Cancel retains original draft and grants no new proof.
5. Successful validation plus explicit confirmation and IN_AREA may create controlled current evidence only under the approved field-retention contract. Phone remains independently current. Session/tenant/notice/source/organization/coverage policy and respective revisions must match; unrelated edits do not force another code.
6. Customer submits reviewed draft through existing review-request path. Authorized operator reads by request ID and admits it. Under existing session locks, re-resolve all proofs using database time and current policies; atomically write one job, evidence reference, links/eligible consent and audit. No provider calls inside this transaction. Exact replay returns prior receipt; changed replay refuses.
7. Session close/expiry/revocation stops new authority immediately. Cleanup follows existing accepted policy and never releases unknown cost holds. Controlled proof never converts into payment, availability, booking or messaging permission.

## Proposed data contract and unresolved permission

| Data | Proposed owner/storage | Lifetime / gate |
| --- | --- | --- |
| Customer-stated phone, address/unit and draft revision | Existing encrypted session/conversation records; customer-confirmed edits remain separately attributable | Existing approved session cleanup and submitted-job record rules; not a new blanket retention period. |
| OTP, OAuth token, raw Google response | Process memory only; no logs/audit/browser diagnostics/database copy | Discard on completion/error; never restore or replay provider response from logs. |
| Suggested Google address/components | Transient server-owned candidate bound to session/revision; sanitized display | Earlier of session/candidate/source expiry under approved terms. No new 24-hour permission inferred. Exact allowed use/retention must be resolved before real connection. |
| Phone verification proof | Existing encrypted ledger with operation reference, source/account identity, checked/confirmed/expiry, revision and policy versions | Existing 30-minute proof ceiling, limited by 15-minute session or shorter source expiry; historical closed proof cannot be revived. |
| Address/coverage proof | Proposed encrypted conversation record: internal operation reference, checked/confirmed/expiry, session/address revision, source/coverage policy version and coverage result | **Unresolved Google-derived retention permission.** Encryption or hashing does not grant permission. No durable county/result/responseId field implemented until resolved. |
| Admission receipt | Existing policySnapshot.intakeAdmission path, containing minimal internal proof references/current policy/time and provenance | Existing business-record retention; derived meaning of retained admission evidence must be included in provider/terms review, not evaded by retaining only a boolean. |
| Costs | Existing durable operation/account liabilities; prior local holds untouched | Unknown outcomes remain held; no automatic retry/refund/reset. |

Recommendation: use explicit controlled provenance and existing encrypted storage/locks, not a new database platform or a memory-only proof that cannot survive required recovery. If permitted retention cannot support this design, stop and present the smallest design change for owner review; do not silently downgrade admission evidence. The historical Google case remains a permission source to review, not proof that all in-memory processing is forbidden. No legal compliance claim is made by this plan.

## Finite patch map after gates close

These are internal 2B tasks, not new sections. Each task must end in the same integrated acceptance path. Names of new files below are proposed, not existing-code claims.

1. **Controlled proof contract/source:** change current-proof-admission.ts, verification-freshness.ts and durable-verification.service.ts plus their specs; add controlled-admission-source.ts/.spec.ts for trusted transaction-time reads of approved records. Exit: fixture evidence cannot cross into controlled authority; provenance/current policy/time/revision tested. No schema expansion assumed—if existing encrypted records cannot support the contract, raise a change request first.
2. **Controlled provider composition:** reuse staging-phone-policy/admission primitives and address ledger/executor/OAuth/shared parsers; add controlled-intake-verification.service.ts/.spec.ts to own bound operations, proof writes and recovery. Changes expected to address-operation-ledger.ts, address-operation-executor.ts and google-address-operation.ts/.spec.ts must preserve existing fixture mode and holds. Exit: cap/refusal/unknown crash state truthful and no network inside admission transaction. Do not simply remove FIXTURE_ONLY checks.
3. **Protected application wiring:** add controlled-customer-intake.controller.ts/.spec.ts as an adapter over customer-consent-browser-transport.ts; update communications.module.ts and guarded operator controller/continuation composition. Exact raw-body middleware/filter/bootstrap binding to be specified against approved runtime before implementation. Serve/reuse the current customer/operator journey, update existing journey JS/HTML and operator controls where required; no third form or new frontend framework. Exit: real auth boundaries, preserved edited draft, no local fixture flag granting authority, disabled route cannot act.
4. **Integrated proof and controlled acceptance:** extend scripts/verify-current-proof-admission.mjs and existing customer/operator journey verifier through the current parent harness, not a new parallel harness. After local gates, prepare the single connected live-test packet with private identities and fresh rates/resources; owner approval required before any external action. Exit: actual current phone + eligible confirmed address → exactly one reviewed job, with owner evidence/sign-off.

No new payment/calendar/SMS-confirmation work, UI polish, generic cleanup/reconciliation framework, provider replacement, infrastructure purchase, production migration or automatic activation. Expected size remains high; no reliable calendar estimate while entry decisions remain unresolved.

## Required tests / evidence

- Positive connected journey: actual selected address/unit survives review submission; current phone/address/coverage consumed; one job; receipt distinguishes fixture/local from controlled evidence. Local synthetic proof is labeled as such.
- Refusal matrix: missing source/policy/notice; wrong tenant/session/account/revision; expired/revoked proof; wrong/expired code; missing/conflicting county/unit; adjacent county; non-US/non-OH; UNKNOWN provider/cap outcome. Draft retained, no job.
- Edit/cancel: affected proof invalidated, no auto-request, no old proof resurrection when changing back, unrelated fields do not invalidate phone.
- Concurrency/recovery: two submitters/exact replay, changed replay, audit failure rollback, source result arriving after edit/stop, expiry at consumption, interrupted dispatch versus held cost, restart/cleanup and historical receipt access. No network in job transaction; no falsely restored proof.
- Security: customer bootstrap versus operator auth, body/origin bounds, cross-tenant reads, redacted errors/logs/screenshots, no tokens/raw provider body in durable records, missing feature configuration refused.
- Browser: existing customer and operator flows at mobile/desktop, loading/error/correction/expired/retry states. No standalone screen screenshot counted as integrated acceptance.
- Controlled run: privately bind exact participant/environment/service accounts/notices, current rate ceilings, phone/address/shared caps, window, stop and reconciliation owner; no historical allowance reused. Preserve current live defaults until separate activation approval.

Commands after approved implementation: `npm run build`; `npm run lint`; `npm run arch:check`; `npm test -- --runInBand`; affected script tests; `npm --prefix ui test`; `npm --prefix ui run lint`; `npm --prefix ui run build` if UI changes; backend/UI full and production dependency audits with findings disposition. Existing parent integration command: `ORGANIZATION_EVIDENCE_DIR=<fresh disposable evidence path> PLAYWRIGHT_MODULE=<installed module> node scripts/verify-organization-profile.mjs`. Verify its disposable Unix-socket DB preconditions first; never point it at staging/production data. Run both baseline guards and cross-repository consistency checks. No live CLI is a regression command.

## Decision / approval register and stop condition

| Gate | Responsible role | Exact remaining evidence / decision |
| --- | --- | --- |
| Retained Google evidence | Owner with provider/authorized terms review; implementer supplies field list above | Is temporary candidate retention and the proposed minimal derived coverage/admission record permitted, and under what retention limit? No assumption that prior CEGIS exception applies. |
| Protected runtime identity | Implementer proposes; owner authorizes actual resource/configuration changes | Exact approved customer bootstrap origin/tenant mapping and operator binding; reuse existing resources where suitable, no invented identifiers or secret collection in docs. |
| Implementation design | Owner | Review controlled-source/record proposal and finite patch map once retention/bootstrap contract is complete. Current plan does not claim all assumptions resolved. |
| Connected live execution | Owner | Separate exact resources, fresh phone/address/shared allowances, participant/session/window, notices and stop/reconciliation responsibilities; prior willingness does not renew spent packets. |

Next permitted action is resolving the first two gates and completing their exact field/bootstrap configuration contract. If unavailable, report the missing evidence and stop; do not propose another helper. No scope deviation. This planning pass changes no runtime or acceptance result.

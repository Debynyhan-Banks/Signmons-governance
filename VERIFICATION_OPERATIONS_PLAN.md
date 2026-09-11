# S1 verification operations — bounded implementation plan

## Decision and scope

VO-1 update: owner subsequently said “approve proceed,” authorizing VO-1 only. The durable ledger/local migration proof is now review-ready; see the current pointer and backend evidence/APP-013/address-operations/README.md. VO-2/VO-3 and live activation are not approved by that decision. Historical sizing text below is preserved as the original plan, not the current execution pointer.

Sizing approved by “proceed” after the protected correction-browser checkpoint. Inspected backend `4ad7def` and governance `d71c6ab`; both focused remote branches fetched and aligned. This is a documentation-only plan, not approval to implement every section or activate providers. APP-013 stays sole Now; Next empty; FE-014 paused. No MVP expansion or Eternity website work.

Outcome: the existing customer review journey must preserve progress and potential costs through duplicate requests, process loss, timeout, edits and expired proof. No uncertain result may authorize admission. County qualification remains independently blocked; this package cannot replace it with ZIP or customer assertion.

## Existing code and exact gaps

| Boundary | Reuse | Gap to close |
| --- | --- | --- |
| Phone operations | `durable-verification.service.ts`: committed reservation before injected call, stable operation/attempt identity, replay without repeated call | One START/five CHECK local model; no orphan recovery, complete freshness/revocation or live activation |
| Phone costs | `verification-budget-admission.ts`: same-transaction HELD audit reservation, tenant lock, $50 ceiling and $25/$40 threshold recording | All months remain held; 10,001-row bounded scan refuses; no shared account budget, settlement, replenishment or delivered alerts |
| Address matching/confirmation | `google-address.adapter.ts`, `local-address-correction.ts`, protected correction browser | No durable operation/cost reservation or request deadline. Single-customer in-memory fixture is not reusable production concurrency infrastructure |
| Protected customer experience | Existing transport, draft-preserving refusal and exact-retry UI | Request limiter is process-local; browser clearing does not prove server cancellation or deletion |

The phone $50 limit is an approved policy, not live spend permission or an address allowance. This plan quotes no current vendor prices and performs no provider/source/account lookup. Actual rates, terms and legitimate test scope must be verified before activation.

## Three dependent reviewable sections

These are implementation boundaries, not equal effort units or a three-turn promise. Each requires its own passing evidence and review. Do not build a generic provider framework or add an unrelated dashboard.

### VO-1 — durable address operation and shared liability reservation (recommended next)

Deliver a disabled address-specific service and minimal durable ledger, exercised by real disposable PostgreSQL transactions. Reuse existing trusted session locks and request protections; retain the existing phone path unchanged. A migration may be authored and applied only to the disposable fixture after implementation approval, never production.

- Bind each operation to trusted tenant/session, address revision and policy/rate versions. Same logical ID and identical bound request replays; different input under the same ID refuses. Cross-tenant/session reuse refuses. Deduplicate identical concurrent submissions within the bound revision, not across customers.
- Reserve integer USD micro-unit worst-case liability plus request allowances atomically at shared account, tenant and session levels before a dispatch claim can exist. Use fixed lock order: account, tenant, session/conversation, operation. Commit before any provider call. Never hold a database transaction across provider I/O.
- Missing, stale, malformed or unapproved policy/rate/cap refuses. Tests inject clearly fictional caps and rates. No actual address cap, free-tier assumption or production key is introduced.
- Minimal durable records contain Signmons operation/attempt IDs, scope/version references, timestamps, state and accounting amounts. No Google content, coordinates, provider IDs, address/unit text, phone/code, bearer or raw error in audit/ledger. Any keyed customer-input digest needed for idempotency requires explicit purpose, key-version and deletion rules; it is sensitive derived data, not an exemption from retention.
- States: RESERVED (no dispatch claimed), DISPATCH_CLAIMED (call may have happened), OBSERVED (local observation recorded), UNCERTAIN (no reliable terminal observation). These describe execution, not charge settlement or verified eligibility. Dispatch claim commits exactly once; orphan claims never automatically call again. OBSERVED is not necessarily paid, free or successful.
- A safely cancelled RESERVED operation may release only through an atomic transition that prevents dispatch. After dispatch claim, timeout, process loss, expiration, editing, session restart or month rollover never release potential liability by themselves.

VO-1 exit evidence: concurrent same request reserves/claims once; conflicting reuse refuses; two tenants cannot overrun the shared ceiling; insufficient/missing policy causes zero dispatch; audit/transaction failure rolls back reservation; restart preserves held liability and prevents a second claim; exact month-boundary behavior keeps old unresolved holds; no sensitive provider fields persist. No browser rerun required unless rendered/request behavior changes. No live HTTP adapter, settlement, scheduler, job proof or module/controller registration in this section.

### VO-2 — bounded execution, uncertain outcomes and recovery

Compose VO-1 into the existing protected address review rather than create another standalone flow. Use explicit absolute deadlines, dispatch fencing and late-result refusal. Abort/timeout means outcome unknown, not proof that the provider did not execute. Exact retries read the existing operation and never silently create another paid attempt. User edits invalidate eligibility while retaining liability; a new operation requires current policy and remaining limits.

Define account/tenant/session attempt ceilings and cooldowns as versioned fail-closed policy. Do not use IP alone as customer identity or let a new session evade account/tenant limits. Preserve phone opt-in and existing attempt restrictions until separately reviewed. Give customers truthful pending/unavailable/correction states without exposing balances; retain the draft and offer assistance.

Recovery is an authorized, audited operation with actor, expected version, reason and attributable evidence; not a timer refund. Separate liability settlement from eligibility. No generic assumption that a provider offers per-operation lookup or idempotent POST. Where authoritative charge evidence cannot attribute an outcome, leave liability unresolved or conservatively charged; aggregate usage alone cannot refund an individual request. Approved accounted cost plus outstanding holds must not exceed caps; overage blocks new dispatch and raises an actionable incident. Cross-month holds remain distinct from current-period consumption. No billing changes or external alert delivery under mock approval.

Exit: crash before/after claim, provider acceptance with lost response, late result, failed result persistence, duplicate workers, exhausted cap and ambiguous reconciliation all preserve the one-operation boundary, draft and conservative liability. Real PostgreSQL plus existing mobile/desktop browser journey; zero live calls. Final provider-specific recovery mechanism and prices remain live entry gates.

### VO-3 — freshness, revocation and cleanup; close operational proof

Bind proof eligibility to current phone/address revision, tenant/session, notices and approved business/coverage policy, with explicit checked/confirmed/expires timestamps. Missing freshness configuration refuses; numerical proof lifetime is not inferred from the 24-hour cache ceiling. Correction confirmation alone never proves address, county, occupancy or messaging consent. Changes, closure and expiry invalidate proof without refunding liability.

Replace single-customer fixture assumptions with bounded per-session transient ownership and explicit purge behavior. Permitted correction cache expires at session end or 24 hours, whichever is earlier; disconnect cleanup needs retryable server ownership, not only browser keepalive. Raw/unpermitted provider data must never reach durable storage, logs, analytics or backups. Keep minimal accounting evidence separate from purged customer/cache data. Abandoned-draft seven-day-or-earlier policy and submitted-record schedule need explicit implementation/retention mapping; do not delete unrelated records. Restore-time handling must not revive expired proof/cache or lose liabilities.

Exit: session/tenant isolation, changed policies, exact expiry, revocation races, failed cleanup/retry, process restart and restore scenarios refuse stale proof and meet documented deletion rules while preserving accounting. Demonstrate the same customer journey, not a service-only claim. Full real-proof-to-job admission remains the subsequent S1 package and requires separately approved sources, accounts and current-proof consumption.

## Approval checklist

- [x] Size against existing code and fixed MVP audit; keep county UNKNOWN and live activation off.
- [x] Approve **VO-1 only**, including minimal ledger migration for disposable local testing, injected fictional policies and no provider activation. Implementation is review-ready; not live acceptance.
- [ ] Review VO-1 evidence before VO-2; approve VO-2 operational thresholds and recovery authorization model before implementation.
- [ ] Review VO-2 evidence before VO-3; approve proof freshness and retained accounting/digest duration before implementation needing those choices.
- [ ] Before any live test: qualified county evidence, named tenant/environment/accounts, verified rate ceilings, separate address/account caps, current notices/terms, legitimate test participants, cleanup/incident owner and explicit capped spend permission.
- [ ] Before real admission/release: current proof/policy atomic consumption evidence and explicit configuration/migration/merge/deploy approval. This document grants none.

## Validation and completion

This planning change runs governance consistency, four execution-placement tests and diff checks. No runtime/schema/UI change; build/tests/browser results from `4ad7def` are historical, not rerun. Implementation gates for each approved code section: focused/full backend tests, lint/build/architecture/Prisma checks, disposable database proofs where persistence changes, and responsive browser QA whenever the customer flow changes.

APP-013 scope index remains 50%, accepted 0/12; onboarding locally demonstrated 3/6 (50%), accepted 0/6; whole pilot accepted 0/12. No overall engineering percentage or calendar ETA. This sizing establishes dependencies and exit tests, not completion of verification operations. Next decision: approve VO-1; stop before coding.

# APP-013 / 3A / P08 — current-state qualification scope and binding proposal

**Decision-ready prerequisite alignment; NOT an implementation approval or live packet.** Owner requested this proposal after post-key reconciliation. Current backend/gov source hashes and review timestamp are in backend CURRENT_STATE_SCOPE_REVIEW_20261103.json. No code, credentials, database/provider calls, password request or live window.

## Demonstrated incompatibility requiring the smallest decision

Existing qualification_launch.py read_database returns dbRoleRetired only when roleCount==0. In contrast, restore.py NativeAdapter.role/readback/preflight requires count==1, NOLOGIN, connection limit0, expired validity, no unsafe privileges/memberships/owned objects/sessions and matching roleAclSha256. role_sql uses ALTER ROLE only; it has no CREATE ROLE branch. Therefore the old absent-role predicate cannot establish the existing restoration prerequisite. R10 stopped before its database domain, so no current role state is known and no live failed ALTER is asserted. This is a source-contract conflict, not permission to change the database.

**Recommended owner decision: use the existing safely retired role contract for future qualification.** The exact named role p07_payment_runtime must already exist, be disabled/expired, and satisfy the inspected restoration safeguards. An absent role or unsafe/unknown ACL must stop as NOT_READY/UNKNOWN. No create/drop/enable/password/grant/session termination is permitted by this decision. Do not simply rename roleCount==0 as a passing retired-state check.

This aligns qualification with the already implemented restoration lifecycle but changes a substantial qualification prerequisite, so owner approval is required before code. It does not change 3A acceptance, add a section, reset accepted milestones or rebaseline frozen governance. No blanket authorization for implementation is requested while the expected ACL baseline and complete execution card remain unresolved.

## Evidence mapping for the proposed read-only scope

| Native check | Reused actual source/output | Proposed pass/stop requirement |
| --- | --- | --- |
| owner | Existing cache config_snapshot/read_cached_token; exact project descriptor/fingerprint | Exact owner/project/config; valid through future purge. Missing/override/expired stops, no implicit renewal |
| billing | qualification_launch.read_cloud, billing project/account descriptors | Exact project/link fingerprint, billingEnabled=true and linked account open=true; current UNKNOWN until read |
| effectiveAccess | Exact role validator, permission-test descriptors, policy projections; existing effective diagnostic sequence where required | Distinguish owner permissions, exact definitions, retired binding absence and usable target access. Never equate testIamPermissions or direct membership to usable runtime access; unresolved diagnostic means UNKNOWN |
| services | Existing fixed six-service access descriptors | Exact required service states; no enablement on failure |
| database | Existing qualification SQL plus restore.NativeAdapter.role read-only query and strict retired readback | Retained-role decision above; exact operator/tenant/ownership and session facts. Zero/duplicate/foreign rows or unsafe/unknown ACL stops |
| firebase | Existing database-derived exact UID and accounts:lookup parser | One owned disabled test user, exact identity/claims/revocation lower bound; missing/null/foreign stops; no sign-in or mutation |
| job | Existing exact admitted job/tenant/policy/calendar queries | Same admitted job/current expected policy/payment gate/calendar absence; no substitute job or fixture |
| retiredRuntime | Existing Cloud Run service/revision, identity, six secret-version and seven policy checks; restore preflight/readback | Exact candidate image/identity/environment, normal100% traffic/tag absent, identity/secrets retired and bindings absent. Unsupported/missing fields UNKNOWN |
| privateInventory | Existing owned-root locks, session/process probes and independent closeout | Exact future operation inventory and current sessions; no historical cleanup substituted for new scope |

All are existing prerequisites, not nine new tasks of customer acceptance. Latest key absence at15:00 is historical point-in-time supporting evidence; no automatic reuse of it as a future permission/absence guarantee. Billing October29 pass is historical; no established current billing failure is asserted.

## Required output binding and trust boundary

Future qualified output must match authority.py exactly: status QUALIFIED_FOR_NATIVE_ENTRY, future authentication operationId, digest of exact plan/target/database/resources/limits, qualifiedUntil at least cleanupEnd, both hashes and exactly nine true checks. A caller-supplied all-true object, old domain verdict, synthetic test result or accumulated historical observations is insufficient. Capture provenance of producing source/decision/request reservations/time and bind each fact to this scope; no partial-success promotion. Missing/uncertain evidence produces unqualified output, not invented facts.

- runtimeEnvironmentSha256: canonical digest of exact observed environment only after matching the independently approved candidate/environment expectation. Do not bless drift by hashing whatever was returned.
- roleAclSha256: canonical ordered ACL projection from the existing role query only after comparison with an independently approved least-privilege baseline. Current code's equality to a supplied hash is not approval of arbitrary observed grants. Recover the exact expected ACL/ownership baseline before a complete implementation card; empty ACL or a test fixture must not be assumed.
- Qualification and restoration share future operation/target/DB/resource/window scope. Existing authority remains unchanged and fail-closed. Local proof never becomes external authorization. No object is emitted in this proposal.

## Reuse options and decision impact

1. **Recommended: approve retained-role prerequisite alignment, then finish the finite local implementation card.** Reuse strict existing parsers/read-only queries/cache/native authority/closeout; resolve expected ACL and effective-access semantics, actual transport/password delivery and source dependency impact before requesting code authority. Old launcher is26 CLI/10 HTTPS/2 SQL descriptors, primes all CLI calls and uses SDK credential resolution. Those numbers are not a no-retry request guarantee. Its hidden CHILD-password prompt cannot be bypassed with historical secrets. The narrow adapter lacks this combined scope; no command is currently execution-ready.
2. Administrator-supplied current authoritative observations can be considered only with exact identity/scope/time/source and the same checks/hashes; screenshots/assertions alone do not satisfy automated binding. No outreach or credential request is authorized. This option does not cure contradictory absent-versus-existing semantics by itself.
3. Defer. Retain disabled state and consumed receipts. Supporting an absent role through role creation would be a separate mutation-lifecycle change request; it is expressly not recommended or included.

Dependency/count/effort impact: no acceptance denominator change; current-state qualification continues to block restoration/authentication. Aligning predicates and proving transport/evidence binding is more than a JSON formatting fix. No duration/effort estimate is claimed before the missing ACL/access/credential boundary is resolved. No independent helper/service/demo is authorized.

## Finite readiness work and implementation boundary

Completed in this proposal: source SHA/evidence review; all nine mappings; contradictory role semantics demonstrated; output scope/hash/trust requirements; reuse alternatives; exact smallest owner decision.

After prerequisite alignment approval, implementer completes only the missing local design decisions and finite card: independently approved ACL/environment expectations and actual diagnostic dependencies; exact changed files/interfaces and transitive source pins; actual cached/SDK/SQL/HTTPS request contracts and limits; private credential ingress without reading old stores; source/decision/window binding and cleanup ownership. If another material scope change is needed, disclose it before implementation. The card must specify positive/negative/null/foreign/missing observations, absent and unsafe roles, ACL drift, inherited/effective-access uncertainty, stale/cross-scope evidence, one-use/concurrency/interruption/recovery, actual PostgreSQL TLS/session boundary and no-secret output tests. No browser test applies until customer UI work is actually in scope.

Before any live proposal, locally verifiable requirements must pass through the actual execution interfaces. SDK internal auth/API retries/cache maintenance need a fresh explicit exception if that path is chosen; renewal exception is consumed. Otherwise use proved cached-only/no-retry transport under a separately approved amendment. Credential delivery, timeout/process ownership and post-failure session readback must be reviewable before asking for a password or an attended window.

Later read-only operation must have a finite exact source/resource/command/time/credential/read-budget scope; no account/key/IAM/service/SQL business-state mutation, activation/signing/exchange/payment/customer/spending/merge/deploy. Private raw identity/runtime/ACL/password/token data stays memory-only or exact0600 owned inputs with explicit purge deadline; public evidence sanitized. Independent cleanup and authoritative session/process readbacks mandatory, no automatic cleanup promise. Proposed correction disabled state: no implementation/source change until separately approved finite card. Rollback for this document-only proposal is withdraw it; existing code and immutable receipts remain intact.

Responsible owners: product owner decides retained-role alignment; implementer produces complete card/source proof; DB owner supplies/approves expected retired-role/ACL baseline; provider/identity owners resolve effective access and exact test account evidence under later authority. Current role/ACL/access/current DB/Firebase/job/runtime/billing states UNKNOWN. Next observable result: owner selects retained-role alignment or deferral, then a complete bounded local card—not a database or native-entry launch.

Acceptance remains APP013_REMAINING_EXECUTION_CONTRACT3A and existing payment-admission DATA_CONTRACTS: same admitted job Sandbox Checkout, authentic matching settlement, gate/failure/replay and owner acceptance. Accepted1A/1B/2A/2B4/8, R1 newly closed0/27, 3A open. **Explicit prerequisite-alignment proposal before implementation; no scope deviation implemented.**

# APP-013 / 3A / P08 — retained-role and ACL qualification implementation card

## November 3 — approved local retained-role and complete ACL proof verified

R1-W01/APP-013/3A/P08. Owner approved implementation card at48bc2a9 before coding. Verified backend commit 2972104745134d42062afdf259d9c9f34bc7833f. Implemented the fixed read-only catalog query, independently pinned expected grants including CONNECT and column ACLs, strict retired-role comparator, and injected local-only evidence boundary. Existing101 tests preserved;110 unit tests and7 actual disposable PostgreSQL tests PASS. PostgreSQL proves baseline/legacy hash compatibility, missing/extra/grant-option ACL refusal, unsafe role/effective PUBLIC privileges/session refusal, statement timeout, lock contention, interruption and cleanup. An extra column grant leaves the historical hash unchanged but is rejected by the new comparator. Owned server reaped and scratch removed. Source/test manifests updated and validated; sanitized byte hashes are in RETIRED_ROLE_ACL_LOCAL_RESULT_20261103.json.

Checklist1–6 completed locally. Final source, architecture, frozen baseline, cross-repository/docs consistency,25 governance tests and whitespace checks PASS. Initial disposable bootstrap failed under sandbox; approved local execution succeeded. Initial test harness defects (fixture port-name collision and disabled connection limit preventing the session fixture) were fixed; final seven tests passed. The deadline test clock sequence was corrected to exercise post-cleanup expiry; final110 tests passed. No historical failures erased. No live database, credentials, provider action, deployment or native qualification occurred; liveObserved=false/executionReady=false. Historical locked sources and consumed receipts preserved; unrelated AGENTS.md excluded.

Remaining: current real role/ACL and other live prerequisites UNKNOWN. The existing lifecycle readback still omits column ACLs; the complete nine-check producer/current-operation binding is not implemented. Implementer owns a separate finite proposal for those gaps; DB/provider owners retain later current-evidence decisions. Next observable result is that bounded proposal, not a live launch. Accepted1A/1B/2A/2B remains4/8; R1 newly closed0/27;3A open. **No scope deviation beyond the explicitly approved local proof.**


## November 3 — owner approved bounded local retired-role/ACL proof before coding

Owner “i approve proceed” authorizes APP013_P08_RETIRED_ROLE_ACL_IMPLEMENTATION_CARD_20261103.md at48bc2a9. Entry backend9cad4b6. Exact card acceptance trace, five allowed source/test/manifest files, fixture/CONNECT baseline, column-ACL comparison, injected local-only query boundary, disposable PostgreSQL negative tests, exclusions/owners/rollback and observable finish incorporated here. Baseline passed before edits. No live DB/credential/provider/native-entry action authorized.


**LOCAL IMPLEMENTATION DECISION PENDING.** Owner approved retained-role prerequisite alignment at0434f36, authorizing this complete card. No source change or credential/provider/DB action occurred. This is the first bounded implementation portion of the current-state proposal; it does not implement the entire nine-check producer or authorize any live qualification. The bounded purpose is to close the demonstrated absent-role/retained-role and incomplete-ACL gaps through real disposable PostgreSQL, using the same fixed read-only SQL/classifier intended for later approved qualification.

## Approved criterion, inspected gap and baseline

APP-013/3A remains same admitted-job Sandbox Checkout → authentic matching signed settlement → gate/failure/replay → owner acceptance. No new acceptance section or denominator. Current-state qualification is an existing prerequisite. Latest runtime source5be6d5772394062395f735e23c7ae32423180d14, source-manifest3db5e61e6ec460a8425819c6ea0272dda8cf63606230ee9dd1fb63e1fa31528b; document-only backend4be4fbb entry. Reuse existing narrow access module, tests/manifests, restoration readback and disposable PostgreSQL fixtures. Preserve historical locked code and consumed operations.

- qualification_launch.py read_database requires roleCount==0. Owner now approves replacing that expectation in future qualification with the existing-role retired contract; historical file is not edited here.
- restore.py199–210/235–239 queries/counts role and ACL then requires count1/NOLOGIN/limit0/expired/no unsafe flags/memberships/owned objects/sessions, matching ACL hash. Its ACL query covers relation/schema/routine/database/default grants but omits pg_attribute.attacl (column privileges).
- Exact original scripts/fixtures/p07-payment-runtime-role-review.sql SHA25635785d3857f6fc9b01042d6dee3137eebb18950601fb1b8e7644e340be8fb83c explicitly grants column privileges. Original pinned legacy/controller.py428–431 applies that fixture plus GRANT CONNECT ON DATABASE to the named role. This recovers the intended baseline; empty ACL and the minimal restoration test fixture are not the baseline.
- Historical P07 role-closeout says roleAbsent=false/NOLOGIN/limit0/expired/zero sessions; October23 late-retirement report confirms retained disabled state. These support the chosen model but are not current role evidence.
- scripts/verify-p07-payment-runtime-role.mjs already creates an owned disposable cluster, exercises the grant fixture, reads column privileges, and checks effective public-schema CREATE/database TEMP denial. Reuse its fixture expectations; never execute that grant SQL against a live database in this work.

## Exact local change and files

Requested permission covers only the existing evidence adapter and tests: source/access_check.py, source/test_access_check.py, source/source-manifest.json, source/test-manifest.json, plus **one new source/test_retired_role_postgres.py** in the same directory and section/result/governance evidence. No application/native-authority/restoration/old qualifier/SDK/production migration edits. If additional runtime files or changing locked upstream source become necessary, stop and propose that expansion.

Add fixed read-only SQL descriptor and strict role classifier in access_check.py: retired_role_query(), classify_retired_role(observation, expected_acl), and a local-proof invocation function using injected read-only SQL/session ports. No CLI mode or native DB transport is added. Existing V2/V3/V4 capabilities and HTTPS/cache paths remain unchanged. Local proof cannot emit QUALIFIED_FOR_NATIVE_ENTRY or mark any nine-check object true. Its output is ROLE_CONTRACT_LOCAL_VERIFIED or fixed refusal plus sanitized hashes; live-observed=false and executionReady=false. The later real transport/authority must be separately specified and approved.

The SQL must use one read-only transaction and one catalog snapshot, fixed role p07_payment_runtime, statement/lock timeouts, bound current database, no business-row payload or password reads. Reuse restore.role catalog projections and add explicit column ACL rows (schema/table/column/privilege/grantability) plus effective-public-boundary checks. Exact allowed statement text is fixed; callers cannot supply arbitrary SQL, role/database/object names or grants. Capture current_user/current_database only to compare the synthetic fixture's expected identity in local proof; no ambient DATABASE_URL/PG* or external host.

## Data/state/identity rules and ACL expectation

Require exact one role; booleans strictly typed; login=false, limit integer0, validity finite and expired under database clock; no inherit/superuser/createDB/createRole/replication/bypassRLS, membership, owned objects or sessions. Null, missing, duplicate, malformed and wrong numeric types stop UNKNOWN; absent role is NOT_READY, not a create request. No termination/ALTER/GRANT/DROP in query or classifier.

Expected ACL derives from the reviewed fixture plus CONNECT, independent of the observed role. Construct a static canonical expectation from its explicit grants and validate it using the actual fixture in the owned disposable database. Table-level and column-level grants are distinct; duplicates, unknown schemas/objects/privileges, grant options, missing or extra grants, routine/default grants outside the baseline and unsafe public-derived CREATE/TEMP must refuse. Compare structured canonical rows before calculating hashes; never hash arbitrary observed ACL then accept that same hash. Normalize only the current database name in expected CONNECT comparison, not arbitrary role/resource identities.

Return both a full ACL evidence hash including columns and the exact legacy projection digest expected by restore.readback, only after complete comparison passes. This proves compatibility of hash encoding without claiming the old restoration readback detects column drift after qualification. That later lifecycle revalidation gap remains explicit and blocks claims of full end-to-end ACL enforcement until separately resolved. No old module is silently repaired.

Private data stays inside disposable owned fixtures/process memory. Retain only fixture/source hashes, fixed classifications/counts and cleanup evidence. No real credentials, account/job records, old private plans, provider API traffic or output. Every injected SQL operation is bounded; independent fixture cleanup confirms owned server/process/session/temp-root closure. Persistent failure yields cleanup-unconfirmed, not success; no guessed PID cleanup.

## Finite implementation/test checklist

1. Pin existing source and full fixture/provisioner/query hashes in local evidence; complete exact baseline expectation including CONNECT and columns. Preserve runtime/transitive SDK hashes and consumed receipt hashes.
2. Implement fixed read-only query and strict comparator/local evidence function in existing module; refuse native/external invocation and arbitrary query/target overrides. Keep the actual native-entry validator untouched.
3. Extend existing unit tests: exact retained role, absent/multiple role, null/missing/bool-as-int, active/unexpired/wrong-limit/elevated/membership/ownership/session cases; missing/extra column/table/schema/database/routine/default grants, GRANT OPTION and effective PUBLIC exposure; incorrect expected fixture/hash or serialization; secret-safe errors; source/test-manifest consistency. Preserve all101 existing cases.
4. New test file reuses the existing owned disposable PostgreSQL fixture class (restore/test_restore_postgres.py and bound TLS fixture patterns), applies repository migrations and pinned permission fixture **only** to the freshly owned database, then CONNECT, and executes the actual new read-only query. Verify canonical baseline and legacy-hash compatibility with restore.NativeAdapter.role. Add/revoke privileges and alter flags only in fixture to prove refusals; specifically add an excluded column grant that the legacy projection misses. Test read-only mutation refusal, timeout/lock contention, query interruption, connection/session cleanup and owned fixture teardown. No external PostgreSQL target or inherited credential accepted.
5. Update source/test manifests including new test file and corrected runtimeManifestSha256 reference; update manifest regression test's expected file set deliberately. Run full focused101+new cases, new actual PostgreSQL test, source validator, architecture, frozen/cross-repository/docs consistency,25 governance safeguards and whitespace. If the fixture environment fails, report environmental failure and stop; do not substitute mocked SQL proof or claim tested.
6. Record implemented/local-tested versus live-unverified, observed gaps and exact byte hashes; independently verify cleanup and preserve unrelated AGENTS.md changes. Complete only this card. No live qualification proposal claiming all nine checks ready.

Commands from backend (pinned Python3.14.2):

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/test_access_check.py -q
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/test_retired_role_postgres.py -v
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --check-source
node scripts/architecture-check.mjs
```

Plus AGENTS.md governance/baseline/25-test/whitespace commands. No UI/browser/application-build gate applies to isolated evidence Python; fixture uses repository migrations only in owned disposable database. Do not run the broad historical application harness unless required by a demonstrated dependency.

## Readiness, owners, exclusions and finish

| Prerequisite | Inspected evidence/status | Owner / next result |
| --- | --- | --- |
| Retained-role semantic decision | Owner approved0434f36 recommendation | Implementer preserves absence/unsafe stop |
| Original ACL intent | Pinned fixture + original provisioner's CONNECT recovered; hash verified | Implementer proves complete canonical expectation locally |
| Missing column-grant coverage | Actual restore query lacks column ACL while fixture grants columns | New local comparator proof; no old readback enforcement claim |
| SQL/TLS/session behavior | Existing actual disposable fixtures available; new query NOT IMPLEMENTED/NOT TESTED | Implementer only after local approval |
| Real role/ACL/current data | UNKNOWN, no reads authorized | DB owner and later exact read-only scope |
| Remaining eight checks/full producer | Current-state proposal remains incomplete externally; effective diagnostics, source/expiry/credential transport and lifecycle column-revalidation still gated | Implementer separate finite proposals, owner prior decisions |
| Approval | This card is PENDING local implementation/testing | Owner |

Rollback: restore four existing source/test/manifest files to5be6d57 and remove only new test file; retain immutable results/history. Observable finish: local real-database baseline/negative proof with manifest consistency and zero external actions, explicit unresolved full-entry gaps, not a completed customer capability. No role creation/enablement outside disposable fixture, provider/IAM/key/billing/credential/runtime/customer/payment action, deployment/merge/push, new allowance or source-anchor rebaseline. Accepted4/8, R1 newly closed0/27, 3A open. **No scope deviation in preparation; bounded local role/ACL proof proposed for explicit approval.**

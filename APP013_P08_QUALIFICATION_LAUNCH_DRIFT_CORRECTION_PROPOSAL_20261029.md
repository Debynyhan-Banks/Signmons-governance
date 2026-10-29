# APP-013 / 3A / P08 — qualification launch drift correction proposal

Status: PROPOSED; owner decision required before implementation. Backend source `aa257f7`; governance result `8463ee9`. No 8:15 a.m. operation plan, approval, command, attempt or credential prompt was created. The offered attendance window is not consumed.

## Demonstrated gap

Shift-left review of the native path before operation binding found four fail-open or unlaunchable assumptions:

1. The binding requires raw `firebaseUid`, `billingAccountResource`, project number and exact revocation timestamp. The October 26 disabled-account operation deliberately purged the raw target and retained only hashes/sanitized ownership evidence. Inventing or reconstructing those values is forbidden.
2. `NativeIO.sql()` runs the locked active-operator qualification, then returns every composed database fact as `true`. That read does not prove the exact retained DISABLED test ADMIN, its Firebase UID, ownership-receipt match, or each composed database predicate. A successful active-owner read could therefore be misreported as exact disabled-operator qualification.
3. Firebase lookup occurs before the launcher has established the retained disabled application row. It cannot safely bind the Firebase identity to the database identity without a new exact database projection.
4. The binding fixes the local preparation proposal SHA as though it were external execution approval, and native completion does not yet delete/read back the exact private operation files. A future attended operation must bind a separate immutable operation proposal and owner decision and prove purge.

No false result was produced because native remained unbound and no command was issued. Backend `aa257f7` remains disabled local evidence, not an executable qualification result.

## Alternatives

1. **Recommended — bounded local identity/binding correction with actual disposable SQL proof.** Preserve the five-domain classifier and 26-CLI/10-HTTPS/two-SQL ceilings. Correct only the launch binding and native reduction:
   - discover project number and linked billing resource inside the approved attempt, compare each in memory against already retained canonical fingerprints, use them only for the next fixed request, then discard them;
   - make the exact repeatable-read SQL return separate strict facts for the same job/tenant, retained DISABLED ADMIN selected by exact designated mailbox hash/private input, retired role/session state and ownership receipt; never derive disabled-operator facts from the active-owner normalizer;
   - use that exact database UID in memory for the one Firebase lookup, parse claims as JSON, require exact tenant/admin/testOnly claims, disabled state and revocation at or after the retained October 26 closeout bound;
   - bind the future external operation proposal SHA and exact owner decision separately from the local preparation proposal;
   - delete the exact private plan/binding/derived files with absence readback on success, stop, signal and closeout-only paths;
   - prove the SQL projection against disposable current-schema PostgreSQL plus fake Cloud/Firebase transports; retain native pre-credential refusal and all prior strict negative cases.
2. **Perform new read-only discovery operations for each missing raw identifier, then preserve the current launcher.** This adds more windows and private receipts while leaving the false database reduction unresolved; rejected.
3. **Proceed with hashes or guessed values.** Rejected: this could qualify the wrong identity or invent evidence.
4. Defer. No external read or mutation occurs.

Alternative 1 is a material correction to an already reported local prerequisite and requires owner approval before implementation.

## Exact local boundary and tests

Modify only `evidence/APP-013/p08-composed-qualification-local-20261029/` and its append-only result. Do not modify product source, schema/migrations, packages, historical receipts, section criteria/counts or the unrelated backend `AGENTS.md` change.

- [ ] Replace all constant-true native database reduction with one strict actual projection and exact parser; absence, null, duplicate, foreign tenant, wrong email/hash/role/status, changed job/policy, active session or ownership mismatch must stop.
- [ ] Derive Firebase UID only from that qualified database row in the same attempt; lookup one exact UID and compare parsed claims/status/revocation.
- [ ] Compare dynamic project/billing identifiers to retained fingerprints in memory and prevent their persistence.
- [ ] Separate local-source approval from future external-operation proposal/owner approval.
- [ ] Implement exact private-file purge/absence and closeout-only isolation.
- [ ] Prove positive/negative/concurrency/signal/deadline/output-limit/private-value cases with fake transports and disposable socket-only PostgreSQL; rerun applicable locked suites and all repository gates.

Observable finish: local tests prove no fact can become `true` without its exact source observation, native remains unbound before credentials, private raw identifiers remain absent from evidence, and a new operation can be prepared without inventing purged metadata. Then request fresh availability and separate exact external approval. The 8:15–9:15 a.m. attendance is not reused.

## Decision requested

Approve Alternative 1 for bounded local correction, disposable PostgreSQL proof and isolated fake-provider tests only, or defer. Approval includes no credential resolution, external read, database/Firebase/provider action, IAM/API/key/account/runtime/token/Stripe/payment/deployment/billing/spending action, attended operation, merge or push.

Accepted 1A/1B/2A/2B remain 4/8. Newly closed R1 remains 0/27, legacy 6/60, intelligence 0/13. P08 and 3A remain open. **Unintended launch drift disclosed before external execution; correction is proposed, not implemented.**

## Owner decision

Debynyhan Banks replied “yes i approve” after review of this proposal at governance commit `f2c722d`. Alternative 1 is approved for bounded local correction, disposable PostgreSQL proof and isolated fake-provider tests only. This decision authorizes no credential resolution, external read, database/Firebase/provider action, IAM/API/key/account/runtime/token/Stripe/payment/deployment/billing/spending action, attended operation, merge or push.

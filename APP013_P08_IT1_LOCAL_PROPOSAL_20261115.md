# APP-013 / 3A — IT1 in-house identity observation proposal

PROPOSED, NOT IMPLEMENTED. Owner explicitly declines support involvement and requests an in-house diagnostic plan. The support draft remains unsent and is not the next action. Baselines: backend80edf70e785aa200771fde1af1f54aab6b17a904, IQ1 runtime512c584; governanceef79226. No old live window/approval survives into this proposal. Approved provider owner remains debynyhan@signmons.com; no Gmail substitution.

## Traceability and demonstrated gap

Section3A acceptance remains authenticated same-admitted-job Sandbox Checkout, authentic event/application gate and failure recovery, independent cleanup and owner acceptance. IQ3 stopped at the prerequisite enabled-state readback. AL1 records enable followed by disable for the expected owner/identity; neither receipt retains the precise readback type or individual request timing. Boundary.send currently publishes only intent/step before dispatch; metadata returns UID/state but drops the observation after comparison. This gap prevents distinguishing a boolean state mismatch from accepted numeric encoding and comparing first readback to the already scheduled pre-disable cleanup metadata. No evidence establishes propagation delay, external interference or a required wait.

Proposed change: add bounded safe observation metadata to IQ1's existing final result. This is a prospective evidence-retention change requiring owner approval before implementation, not permission inferred from this newly written plan. No new subsystem, provider interface, acceptance section, additional read, delay, retry, polling, mutation or success waiver.

## Exact files and interfaces

Only backend evidence/APP-013/p08-connected-packet-20261110/iq1_identity_boundary.py, test_iq1_identity_boundary.py and iq1-source-manifest.json; local verification evidence and governance completion/readiness. Reuse Boundary.send, Cloud.cloud, RuntimeAdapter.readback, metadata, run_worker, Journal, NativeTransport, source/configuration guards and independent cleanup. Do not modify shared native adapter/qualification/SDK code or other manifests. No schema, endpoint, application UI, database, dependency, deployment or credential changes.

Add one bounded observations array to existing result.json (maximum11 entries, matching main5/cleanup6), without new journal files or altered custody rules. Each entry contains only:
- phase MAIN/CLEANUP; existing step label and zero-based ordinal;
- UTC request-start/return times and monotonic elapsed milliseconds (nonnegative); no fabricated timestamp on interrupted/incomplete transport;
- outcome RETURNED/TRANSPORT_FAILED/NOT_CLASSIFIED, fixed labels only;
- for existing identity/describe reads only: output shape OBJECT/OTHER/INVALID_JSON, email comparison MATCH/MISMATCH/ABSENT/INVALID, disabled class BOOL_TRUE/BOOL_FALSE/NUMBER_ONE/NUMBER_ZERO/NULL/MISSING/OTHER;
- for metadata reads already requesting uniqueId: UID comparison MATCH/MISMATCH/ABSENT/INVALID/BASELINE_VALIDATED, referencing the existing retained baseline UID hash. Readbacks not requesting UID say NOT_REQUESTED, never MATCH.

No raw output/value/error text, email, numeric UID, project number, token, password, principal, headers, body digest or SDK dump is added. Other unrecognized values collapse to fixed OTHER/INVALID labels. Audit timing is not a substitute for request timing. Mutation RETURNED means transport acknowledgement only, never state success. Record failed/unfinished observation truthfully, without filling in a provider response.

Classification is observational only: original raw bytes continue through the unchanged production serializer/predicate; do not canonicalize, default missing fields, reject previously accepted numeric values or introduce a new success path. Safe classifier failure must not replace the original error or prevent mandatory cleanup. Keep observations in bounded memory until existing final result publication; worker death can lose observations and remains UNKNOWN. No new durable publication before/inside a mutation or cleanup gate. If existing final-result persistence fails, preserve existing failure semantics; do not claim crash-proof telemetry.

Raw response remains transient under the existing lifetime; no retained private inputs or expanded purge window. Safe added metadata has the same evidence lifecycle as existing result.json. Same operation/source/UID/lease binds all observations. Concurrency and interruption protections remain unchanged.

## Finite checklist and verification

1. Implement small pure safe classifier and bounded observation collection at the actual existing send/metadata seams; preserve same bytes returned to Cloud and exact provider vectors/order/counts.
2. Test original successful sequence with exactly5main/6cleanup calls and no altered qualification result; exact boolean/type/absent/null/invalid-object/error fixtures through actual adapter boundary.
3. Reproduce IQ3 synthetically: first enabled readback BOOL_TRUE then pre-disable cleanup metadata BOOL_FALSE with same UID. Preserve STATE_MISMATCH and FAILED_AND_CLOSED; show later observed transition without claiming a proven cause. Also test both reads BOOL_TRUE, wrong UID/email, absent UID, numeric1/0 and malformed data. Do not introduce provider calls for tests.
4. Test thrown transport error, clock rollback/nonmonotonic wall time, timeout, interrupted read, diagnostic-classifier failure, oversized/sensitive strings, observation cap and result publication failure. Original no-retry/cleanup behavior must remain. Negative tests must assert no private sentinel is serialized.
5. Existing lease contention, source/configuration drift, budget/deadline, coordinator interruption, final-read recovery and process-closure tests stay in full connected/native regressions. Browser validation is limited to existing local loopback regression fixtures; no account browser is required. No new UI/browser test suite.
6. Regenerate only IQ1 manifest; run focused IQ1, full connected/native Python tests, committed source guard, governance frozen-baseline/cross-repo/25 tests, architecture and git diff --check in both repos. No TypeScript input change: no claim of newly rerun runtime build/lint unless actually warranted. Preserve original IQ1/IQ2/IQ3/AL1 receipts byte-for-byte.
7. Save completion/readiness with exact source SHA, command results, fixture-versus-live distinction and remaining UNKNOWNs. Stop at locally verified implementation; prepare any live qualification only after separate exact owner review.

Commands: pinned Python3.14 -I -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_iq1_identity_boundary.py', then same directory with 'test_*.py'; native suite discovery in evidence/APP-013/p08-native-entry-local-20261101/source with 'test_*.py'. Use repository-established import setup if isolated discovery requires it; no dependency installation or test weakening. Governance: node scripts/frozen-baseline-check.mjs; SIGNMONS_BACKEND_REPO=<B> node scripts/docs-consistency-check.mjs; node --test scripts/frozen-baseline-check.test.mjs scripts/execution-placement.test.mjs scripts/intelligence-alignment-check.test.mjs. Backend: SIGNMONS_GOVERNANCE_REPO=<G> node scripts/check-governance-baseline.mjs; npm run arch:check; git diff --check both.

## Readiness and observable finish

Inspected actual Boundary.send/metadata/cleanup/run_worker and journal final-result65536-byte cap. Existing cleanup metadata precedes disable, so it supplies a second already-budgeted observation without changing schedule. The same real SDK output/serializer boundary remains in use; safe diagnostic parsing does not change its meaning. Installed source and IQ3/AL1 evidence establish the gap, not its provider cause. Source80edf70 reviewed November15; implementer responsible. Existing command pins, baseline UID ownership, dynamic SDK configuration checks, eight-second process bound, independent closeout,11-command maximum and no-retry rules are reused and must pass affected tests. All current external facts/credential usability are UNKNOWN; no attendance/session is booked.

Finish: local tests prove safe timestamps/type/state/identity classifications survive into result.json without changing calls, success predicates or cleanup. This is diagnostic readiness, not payment acceptance or proof the live issue is fixed. A later live run could still be inconclusive; there is no guarantee that the already scheduled second read observes a transition.

Alternatives: repeat unchanged procedure (rejected: loses same evidence); arbitrary delay/polling or direct-REST comparison (not proposed: expands reads/semantics and needs separate evidence/approval); support escalation (owner declined). IT1 keeps the smallest existing-boundary evidence change. No section/dependency/count change; small bounded local test/evidence task, not a new acceptance milestone.

Rollback/disabled state: retain current committed runtime if local verification fails; no provider action follows rollback or this approval. Preserve unrelated AGENTS.md/renewal worktree changes. Implementer owns implementation/tests; owner approves the new safe result fields. Requested decision is local implementation/tests only, no credentials, sign-in, SDK operational call, remote SQL, identity change, support message or payment. No deadline or Terminal attendance needed.

Completed now: proposal and traceability only. Remaining: owner local decision, implementation/verification, separately reviewed live evidence if justified, current account containment/entry (R47 historical UNKNOWNs preserved), authenticated same-job payment/event/recovery, cleanup and owner acceptance. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27. Explicit prospective change: safe IQ1 final-result observations only; not implemented. No other scope deviation.

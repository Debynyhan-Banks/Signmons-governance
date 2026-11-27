# AQ1 — qualify authentication with the payment handoff disabled

PROPOSAL ONLY. APP-013 / 3A / P08. No implementation or live operation is authorized by this review. No attendance or deadline is needed for the proposed local work.

## Requirement, evidence and recommendation

The unchanged 3A exit criterion is: “owner completes Sandbox payment for that same job; matching mode/account/amount/currency signed event clears its gate.” Authentication is its existing prerequisite, not a new acceptance section. Preserve DATA_CONTRACTS.md's exact tenant, actor, admitted job and approved payment-policy snapshot; no booking or customer-message authority is inferred.

AP2 is completed at backend `4d428ca792ceb28aa8aba59dfc1660b4cdcce4e5`; governance baseline is `e7a03e643561a566c62bee0bee0e88ed1c1f61a7`. AP2 now retains bounded authentication failure details. R67's discarded runtime cause remains UNKNOWN. Its eleven retained receipt hashes were rechecked unchanged in the companion readiness record; no raw envelope or credential was read. R67 is consumed and cannot be replayed.

Inspected gap: packet.py accepts only normal version2 or NATIVE_PREFLIGHT_ONLY. Native version2 --run always installs the payment callback; preflight-only never authenticates. Version1 would discard current recovery/payment binding and BR2 identity-readback compatibility. Native child cleanup and independent account readback currently depend on the version2 payment preflight/disabled-endpoint receipt. Therefore the smallest compatible adaptation keeps that preflight and setup, and disables only the payment handoff with explicit guards.

This is NOT a Stripe-free or setup-free diagnostic. A future separately approved live operation would still need current qualification, temporary runtime/IAM/key/test-account setup, existing Stripe secret/endpoint reads, hidden SQL input and independent cleanup. It would skip webhook enabling, payment-policy/request changes, the operator bridge, Chrome/Checkout and payment attendance. No duration or live success is promised. Removing all Stripe prerequisites would be a larger redesign and is excluded.

Alternatives considered: unchanged full payment run retains avoidable payment authority; preflight-only cannot test the failing boundary; version1 downgrade is incompatible; a separate authentication runner duplicates ownership/cleanup. Recommend a distinct purpose on the existing version2 runner.

## Exact behavior and interfaces proposed

1. Add only `NATIVE_AUTH_QUALIFICATION_ONLY` as a version2 native purpose. Keep version2 recovery, all nine current qualification checks and resource/payment binding. Unknown purpose, version1 with this purpose, purpose/mode mismatch, stale source, altered scope or approval mismatch must fail before any native port. No purpose remains the existing connected payment path; NATIVE_PREFLIGHT_ONLY remains unchanged.
2. Bind the new purpose into the exact native envelope digest and a distinct decision: `APPROVE_EXACT_P08_AUTH_QUALIFICATION` externally and `APPROVE_LOCAL_AUTH_QUALIFICATION_PROOF` for synthetic proof. Existing payment approval cannot authorize the new purpose or vice versa. Qualification evidence still covers the same existing nativeScope; the separate native decision binds the restricted purpose.
3. packet.py and connected_launcher.py must propagate this purpose explicitly through construction, review, handoff and dispatch. Dispatch uses existing --run/--closeout, never the truthiness-based preflight dispatch. The published review must say authentication qualification, list retained temporary setup and read-only Stripe preflight, and exclude payment/Chrome. Reject Terminal-confirmation delegation for this new purpose in this first adaptation; keep existing normal delegated payment behavior unchanged. No change to existing stage_review/attended consent contracts is required.
4. native_child.mjs retains existing payment preflight, payment journal and cleanup/readback ports, but does not attach afterAuthentication for this purpose. It invokes the same CoordinatorAuthSequence, exact identity/token verification and protected same-job runtime GET. Normal and independent cleanup remain mandatory whether authentication succeeds, fails, times out or loses output.
5. Add independent defensive guards in connected_payment.mjs: runPayment and all application payment routes refuse the restricted purpose before I/O; endpoint enabling refuses before secret access/request. Existing GET and conditional disabling during cleanup remain permitted. A callback omission alone is insufficient. bootstrap_open.py already requires no purpose; preserve that rule and test that the new purpose cannot open Chrome.
6. entry.py keeps BR2 identity reconciliation, current setup, full authoritative closeout and private purge. For the restricted purpose, reject contradictory payment journal states (enable intent, open bridge or observed payment) conservatively; do not silently coerce them into a clean qualification result. Successful authentication may use the existing authenticationObserved/authProofReady fields only after the existing proof/cleanup checks. Payment remains unobserved and paymentReadyForAcceptance false. No synthetic success from a journal, cleanup or diagnostic label.
7. Keep all existing transport requests, authentication checks, retries, mutation counts, deadlines, key/account ownership and cleanup limits. Existing outer ceilings remain 196 CLI, 100 HTTPS, 60 SQL, 6 child processes and 200 child requests; no allowance increase. The reduced path must fit these bounds including independent cleanup. Retain the existing settling interval; changing it is excluded. A future live card must itemize the retained actions and bind new current evidence/time/authority, not reuse R67.

## Finite file scope

Exactly eleven existing source/test files, relative to backend evidence/APP-013:
- `p08-native-entry-local-20261101/source/authority.py`
- `p08-native-entry-local-20261101/source/entry.py`
- `p08-native-entry-local-20261101/source/native_child.mjs`
- `p08-native-entry-local-20261101/source/connected_payment.mjs`
- `p08-native-entry-local-20261101/source/test_entry.py`
- `p08-native-entry-local-20261101/source/test_connected_payment.mjs`
- `p08-connected-packet-20261110/packet.py`
- `p08-connected-packet-20261110/connected_launcher.py`
- `p08-connected-packet-20261110/test_packet.py`
- `p08-connected-packet-20261110/test_launcher.py`
- `p08-connected-packet-20261110/test_bootstrap_open.py`

Only hash values in these nine current derived manifests may change:
- `p08-native-entry-local-20261101/source/source-manifest.json`
- `p08-native-entry-local-20261101/source/test-manifest.json`
- `p08-key-correction-20261110/source-manifest.json`
- `p08-https-output-category-local-20261029/source/source-manifest.json`
- `p08-connected-packet-20261110/iq1-source-manifest.json`
- `p08-connected-packet-20261110/sq1-source-manifest.json`
- `p08-connected-packet-20261110/account-containment-source-manifest.json`
- `p08-connected-packet-20261110/account-containment-read-source-manifest.json`
- `p08-connected-packet-20261110/vm2-source-manifest.json`

The readiness JSON pins every current file hash. No new runner, credential store, product endpoint, schema, dependency, historical receipt or baseline-anchor change. Preserve unrelated AGENTS.md and renewal artifacts. Newly discovered material files/behavior require review before expansion; never weaken a check to fit the proposed inventory.

## State, identity, retention and rollback

Reuse the existing exact company owner, test administrator, tenant, admitted job, runtime origin/candidate, numeric secrets, key restrictions and recovered version2 payment binding. No pins are invented or replaced. Real credentials/tokens remain transient under existing bounded IO and purge; only AP2 fixed diagnostics and existing ownership/status receipts persist. Synthetic tests use fictional identities, injected network/database ports and, where required, local loopback servers. No PostgreSQL fixture, real database, cache read, browser or provider is authorized for local work.

The disabled state is the default until a fresh exact restricted-purpose approval exists. There is no fallback from qualification to payment. Failed authentication or incomplete authoritative cleanup remains unresolved. Rollback restores the eleven files and nine manifests together to the readiness hashes; historical evidence stays immutable. No deployed configuration changes occur in this local scope.

## Finite checklist and required tests

- Verify readiness hashes, canonical section and immutable receipt hashes before editing; record the owner decision.
- Implement purpose/decision binding, explicit dispatch and truthful review. Test normal/payment/preflight behavior unchanged; missing, foreign, downgraded, replayed and tampered authority fail before I/O.
- Test successful actual-child authentication through the Python parent and independent cleanup with zero callback, webhook-enable, payment application, bridge or browser calls. Verify the same account/token/job identity checks run. Use existing JournalContractIntegrationTests and injected transport fixtures, not a replacement classifier or runner.
- Test AP2 runtime failure matrix through that path: timeout, transport, HTTP, response/identity/token/job validation; preserve bounded diagnostics and no payment side effects. Test direct attempted payment-port/entry invocation rejects the restricted purpose before I/O.
- Test interrupted/expired work, lost output, child exit/timeout, invalid/foreign journal, concurrent lock/replay and partial setup failure. Existing cleanup must still run and unresolved outcomes must remain conservative. Test contradictory payment journal records refuse clean authentication-only acceptance.
- Verify independent cleanup and retention boundaries, BR2 exact identity readbacks, existing normal payment success/failure semantics and unchanged call ceilings. Reuse current synthetic fixtures; do not run PostgreSQL or browser fixtures. Browser safety is tested with a refusing/injected opener only.
- Refresh only the nine listed manifests, run actual current and committed source guards, record exact counts and per-case evidence, and preserve R67 receipt hashes. Do not edit source while a source-bound suite is running.

Commands after approval and implementation (backend cwd):

```sh
node --test evidence/APP-013/p08-native-entry-local-20261101/source/test_connected_payment.mjs evidence/APP-013/p08-native-entry-local-20261101/source/test_transports.mjs evidence/APP-013/p08-coordinator-auth-local-20261031/source/test_client.mjs evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.mjs
python3 -B -m unittest discover -s evidence/APP-013/p08-native-entry-local-20261101/source -p test_entry.py
python3 -B -m unittest discover -s evidence/APP-013/p08-real-client-binding-local-20261031/source -p test_bound.py
SIGNMONS_GOVERNANCE_REPO='/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery' node scripts/check-governance-baseline.mjs
npm run arch:check
git diff --check
```

Also run the exact connected selection command recorded in AP2's proposal: test_packet, test_launcher, test_approval_wait, test_attended_approval and test_bootstrap_open, excluding exactly test_production_jxa_dispatches_loopback_and_closes_only_owned_window and test_actual_loopback_bridge_and_headless_chrome_handoff. Record current counts; old test totals are not new evidence. Existing fixture failures, if any, must be disclosed and resolved only within the approved behavior; do not weaken payment checks or silently broaden scope. This review does not claim that the proposed mode or its tests already pass.

Run actual authority.verify_sources(), qualification model.verify_local_manifest(), exact client source guard and source-commit binding checks. From governance run node scripts/frozen-baseline-check.mjs; SIGNMONS_BACKEND_REPO='<backend>' node scripts/docs-consistency-check.mjs; node --test scripts/frozen-baseline-check.test.mjs scripts/execution-placement.test.mjs scripts/intelligence-alignment-check.test.mjs; git diff --check. No product/schema changes mean product build/database/browser gates are outside this local card.

## Readiness record and next observable result

Companion APP013_P08_AQ1_LOCAL_READINESS_20261127.json records source SHA, inspection timestamp, file hashes, responsible implementer, current source guards and unchanged historical receipts. Current authority, packet, actual child, payment ports, cleanup and bootstrap restrictions were inspected directly. Existing output contracts and AP2 bounded classifications are retained. No new provider parsing or SDK contract is introduced.

Current credential validity, effective provider access, API/key compatibility, dynamic environment, database role and runtime authentication remain UNKNOWN for a future operation. Existing historical/synthetic evidence is not current live qualification. The new purpose, its authority isolation, concurrency/deadline/partial-failure/cleanup matrix and retained call budget are NOT YET IMPLEMENTED OR TESTED. They block a live proposal until the local checklist passes. Fresh live readiness must inspect actual dynamic configuration/resource pins and current evidence using the existing validators; it must not be reconstructed from constants. No attendance window is scheduled.

Completed in this review: source/contract reconciliation, reuse/dependency analysis, scope alternatives and exact proposal. Remaining after owner approval: the seven local checklist items, verified completion evidence and then a separate live qualification decision. Implementer owns implementation/tests/readiness; Debynyhan Banks owns the scope decision and eventual acceptance. Local finish is a proven restricted path through the real child/parent/cleanup boundaries that cannot perform payment and returns useful authentication evidence. It does not itself fix an unknown provider/runtime cause or complete 3A.

Accepted milestones remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation in preparation; this is an explicit prospective purpose/authority adaptation beyond AP2, which explicitly excluded a new authentication-only mode. No criteria, section count or queue changes. Requested decision: AQ1 local adaptation and synthetic tests in these eleven files and nine manifests only. No credentials, sign-in, provider calls, SQL, payment, spending, support/customer contact or attendance included.

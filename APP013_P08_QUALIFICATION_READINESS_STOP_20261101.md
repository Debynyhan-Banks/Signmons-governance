# APP-013 / 3A / P08 — qualification readiness stopped on manifest drift

**Subsequent owner decision and result:** owner said “I approve lets proceed” to the exact repair. It is now implemented and verified: original six-file runtime manifest restored, separate two-file test provenance, actual validator and 11-case handoff suite PASS. Evidence: backend `evidence/APP-013/p08-real-client-binding-local-20261031/MANIFEST_REPAIR_RESULT_20261101.md`. The failed state and proposed remedy below remain historical. Resumed qualification proposal: `APP013_P08_NATIVE_ENTRY_QUALIFICATION_PROPOSAL_20261101.md`; no native implementation or external authority follows.

Status: **STOP; correction proposed, not implemented.** Owner approved proceeding with the qualification proposal after the November 1 local database result. Source review at backend `d5f1f876e8f17f8236d2262d1856a6fa323a86a4`, governance `996cc7fb5be906ddf64d1d337c7fa6dc24a3a001`, found a regression introduced by the preceding assistant turn. Both worktrees contain preserved, uncommitted evidence updates; backend `AGENTS.md` also has the prior owner edit. No external action or credential resolution occurred.

## Demonstrated failure and corrected status

At 2026-11-01T12:47:29Z, directly importing the existing `bound_handoff.py` and calling `verify_sources()` returned `SOURCE_GATE_STOP:MANIFEST_SHAPE` (exit 2). The current manifest has eight file entries; the unchanged validator requires exactly six. The previous turn added `bound-postgres-fixture.mjs` and `test_bound_postgres.py` after the 11 bound-handoff regression tests had passed. Its final check verified hashes but did not invoke the real manifest validator. The final assembled bundle therefore was not qualified, despite the reported successful tests. This is an assistant-introduced integration error, not a failed PostgreSQL assertion or new provider issue.

Source fingerprints:

| File under backend `evidence/APP-013/p08-real-client-binding-local-20261031/source/` | SHA256 / inspected result |
| --- | --- |
| `bound_handoff.py` | `d768ff2436a9e459c6f67a66d7ff9cf8d300fe6aac45ed380bb0cfe157152fb2`; `verify_sources()` requires six exact filenames |
| Current `source-manifest.json` | `7494d8071b824cba9a097accaa51aa4dad17fe35d67e04a7fa99b370f2ba3d64`; eight filenames, so refuses |
| `bound-postgres-fixture.mjs` | `89b8fef3ea555ed8d2e8c85e8644fbf27c430cb16f656391cc835f604e9393f9` |
| `test_bound_postgres.py` | `e4f32ddf4b65c9d0c1a156a5d5a9054af3c671844630deb54395437af20bbda5` |

Comparison with backend HEAD confirms all six original manifest entries and all `sourceLocks` are unchanged. The two added keys alone explain the shape refusal. The ten passing database tests remain valid historical observations of the tested files; they do not override the failing assembled-bundle gate. The current local readiness claim is withdrawn until repaired and checked through the real interface.

## Exact proposed correction

Recommended decision: approve this repair only, followed by resumption of the already requested qualification proposal. No new runtime feature or live authority is requested.

1. Remove only `files["bound-postgres-fixture.mjs"]` and `files["test_bound_postgres.py"]` from `source/source-manifest.json`, restoring its original six-file contract. Preserve every original hash, source lock and `DISABLED_LOCAL_ONLY` status. Do not alter `verify_sources()` or relax its exact set.
2. Record those two test hashes in a separate `postgres-test-manifest.json` beside the source manifest. Keep both test files unchanged. This artifact is test provenance, not an authorization or runtime manifest.
3. After all manifest changes, invoke the actual `bound_handoff.verify_sources()` and run `python3 -B evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.py` (11 cases). Validate both manifests against their actual files. If any failure appears, stop and report it; do not weaken assertions. The unchanged database suites need not be repeated solely to move provenance hashes, unless a new concern warrants it.
4. Run governance frozen baseline, backend cross-repository gate, full docs consistency, 25 governance safeguard tests, backend architecture and both whitespace checks. This is a manifest/documentation repair; prior lint/build/database evidence must remain explicitly historical.
5. Record the result and correct the top-level handoff. Resume source inspection for the qualification proposal only after the assembled-bundle gate passes.

Expected files are the existing runtime manifest, one separate test manifest, readiness/result notes and canonical handoff/pointers. No application code, native entry, test expectation, provider resource, scope ID, criterion, dependency or acceptance denominator changes. Rollback leaves the current bundle stopped; no live release exists to roll back. Observable finish is the unchanged exact validator and 11-case handoff suite passing against the final six-file manifest, plus independent provenance verification for both new tests.

The alternative is to leave the bundle stopped and defer the qualification proposal. Expanding the runtime validator to accept eight entries is unnecessary and is not recommended. Responsible implementer: the assistant repairs and verifies its manifest error after direction. Responsible owner: Debynyhan Banks decides this disclosed correction under the repository stop rule.

## Qualification findings preserved for the resumed review

The fixed 3A criterion remains same-admitted-job Sandbox Checkout, authentic matching signed settlement, failure/replay evidence and owner acceptance (`APP013_REMAINING_EXECUTION_CONTRACT.md`, 3A). No payment feature is added by this prerequisite.

- `p08-live-binder-local-20261029/source/coordinator.py` SHA256 `1eecc5241794cfed6d892db4385039274539e47b183f1d934899549eb5560f70` requires `LOCAL_INTEGRATED_PACKET_ONLY`, `externalActionAuthorized:false` and `APPROVE_LOCAL_SINGLE_COORDINATOR`; its native entry is disabled. This is not an external launch boundary.
- `p08-real-client-binding-local-20261031/source/bound-child.mjs` accepts only `--fixture-auth`/`--fixture-closeout`, with synthetic transports. `bound-clients.mjs` provides tested injected interfaces, not a native owner-OAuth/password/SQL/HTTPS factory.
- Historical `p08-authentication-local-20261026/source/auth-launch.mjs` SHA256 `180346d1874efa61986ea79575407af8669e940ec076639f828bbf2b65c0516a` has bounded owner CLI/OAuth and TLS/session primitives, but `runLaunch` uses its own authorization, attempt and journal. It must not be nested as a second lifecycle owner. Credential resolution cannot start from the local capability.
- `p08-native-closeout-local-20261031/source/adapter.py` SHA256 `c463671302f8d858d51063e94d7baaa6c0c72a395f505f5fa0a502674d8e532c` checks only `/private/tmp/p08-coordinator-private-<operationId>` and five allowed filenames. Historical auth plans/results, `/private/tmp/p08-auth-proof-<operationId>`, restoration plans/results and the coordinator journal/owned receipt have different owners/paths. Their absence has not been established by that synthetic root check. A future exact operation must name only the roots it actually uses and supply independent readback/purge ownership; no broad filesystem purge is authorized.
- `APP013_P08_ROLE_CONTRACT_LOCAL_RESULT_20261029.md` explicitly says not to repeat full qualification before resolving the service/key blocker. R10's consumed evidence observed disabled API Keys service, denied prospective-key read and role-shape mismatch; the local role parser correction does not establish current provider state. Do not replay R10 or use its stale window.

A resumed proposal must reconcile the existing primitives, one external approval/attempt/journal, exact credentials/transports, actual private-root inventory and independent closeout before scheduling a qualification. Any material native-boundary implementation needs an explicit proposal and decision before coding. This document authorizes neither such implementation nor a read-only provider operation. Current owner/database/Firebase/billing/effective permissions/API/key/runtime state remains UNKNOWN. `liveAuthorization:false`, `authProofReady:false`.

Completed: source/evidence reconciliation, actual manifest-gate failure diagnosis and this finite correction proposal. Remaining: owner direction, correction/verification, qualification proposal, separately approved external work, same-job Sandbox settlement/recovery and acceptance. Next observable result after correction approval: the final assembled local bundle passes its existing validator. Accepted milestones remain 1A/1B/2A/2B = 4/8; R1 newly closed 0/27; R10 consumed; 3A open. **Unintended manifest drift disclosed; repair proposed, not implemented.**

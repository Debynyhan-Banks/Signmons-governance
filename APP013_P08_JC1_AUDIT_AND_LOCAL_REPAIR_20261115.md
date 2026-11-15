# APP-013 / 3A — R51 audit and JC1 local repair proposal

Status: owner-approved JC1 IMPLEMENTED AND LOCALLY VERIFIED at backend72f0390. Exact decision: APP013_P08_JC1_APPROVAL_20261115.md; completed evidence: APP013_P08_JC1_LOCAL_COMPLETION_20261115.md. JC1 is an internal correction within 3A, not another acceptance section. User requested a thorough review to stop repeated inconclusive attempts. This document grants no live authority.

## Finding and correction to the earlier interpretation

Backend inspected: b61117720e980cc52dc909bf91f6f1c8afecdf5b; R51 runtime source d3d6e6bc150e8ff8c2bccf002d587c90c1f1758c. Governance starting HEAD: 4af4004bb6f5ba6f419e09c9f1689ce2392c2199. Both focused worktrees are on codex/p06-r08-recovery-20260918. Unrelated backend AGENTS.md edits and historical renewal artifacts are preserved.

A deterministic Python/Node contract mismatch is proven locally:

1. AD2 recovery-sequence.mjs:84–90 writes authStage, failureCategory and httpStatus.
2. real-client-binding/source/bound_handoff.py:30–33 omits all three from AUTH_FIELDS.
3. Its merge at119–140 rejects that journal with CHILD_JOURNAL_SHAPE before copying the child state into coordinator memory.
4. native-entry/source/handoff.py:53–54 merges before examining the child's exit/output.
5. live-binder/source/coordinator.py:193–195 saves stale parent memory, overwriting the child's diagnostic journal.

The audit exercised actual entry → Python handoff → Node runChild → parent save → independent cleanup using existing ConnectedEntryTests and synthetic owner/database/provider ports. Injected signing HTTP403 produced an exit0 child with SIGN / HTTP /403 and CLOSEOUT_FINISHED. The first parent merge rejected CHILD_JOURNAL_SHAPE; one stale save removed authClient; four subsequent cleanup/readback merges refused CHILD_JOURNAL_ABSENT. The final failure and four residual labels matched R51. There were six child calls and the same QUALIFIED/endpointDisabled:true/endpointCalls1/secretReads1 payment signature. Synthetic provider counts were not identical to live counts.

A second synthetic owner-authority refusal produced the same retained signature. Therefore the contract defect is proven, but its occurrence in R51 and R51's original provider failure remain UNKNOWN. Missing final authClient does not establish that the child never wrote one or that account/token actions never began. Earlier prose saying “stopped before auth journal” or “diagnostic code was not reached” is withdrawn. Immutable execution receipts are unchanged.

The earlier AD2 test at native test_transports.mjs:83–101 exercised runChild and its journal but not the rejecting Python merge. This was a verification gap in the implementation review, not a problem caused by the owner's Terminal entry.

## Cleanup reconciliation

R51 final ENTRY_CONTAINMENT_UNCONFIRMED retains ACCOUNT_SESSION, AUTH_OUTCOME_UNKNOWN, AUTH_REVOKE and PAYMENT_ENDPOINT_UNCONFIRMED. Preserve all four.

- entry.py:618–625 deliberately adds endpoint uncertainty when authentication was attempted and account/session closure remains unconfirmed.
- endpointDisabled:true came from the initial disabled-endpoint GET. Retained enableIntent:false means no endpoint-enable intent remains in the retained journal; stale parent overwrite prevents inferring that no endpoint action occurred. It is not a fresh final observation.
- connected_payment.mjs:133–146 requires successful main account/readback evidence and at least two endpoint calls before reusing the main observation. R51 has one call and ACCOUNT_SESSION.
- AUTH_REVOKE and ACCOUNT_SESSION report missing accepted cleanup proof; neither proves an active account or a failed provider mutation. AUTH_OUTCOME_UNKNOWN is historical and cannot be cleared by a later current-state read.
- Independent local inspection at 2026-11-15T22:02:02Z proved private purge, operation-process absence and restrictive receipt custody. It did not prove provider containment. No Checkout/browser opening/payment was observed.

Safe evidence remains backend evidence/APP-013/p08-connected-packet-20261110/r51-live-20261115 at b611177. Raw private identifiers were not copied or recovered.

## Requirement, reuse and proposed scope

Approved section: APP-013 / 3A. Exact existing criterion: APP013_REMAINING_EXECUTION_CONTRACT.md:66–70 requires the same admitted job's authenticated Sandbox Checkout, matching signed event and application gate, with safe failure/recovery evidence. Ticket credential/redaction criteria and DATA_CONTRACTS.md:528–538 preserve private credentials and exact job/payment identity. The defect prevents reliable authentication failure/cleanup evidence on that connected path. No payment policy or acceptance criterion changes.

Recommended single local bundle:

1. **Repair the demonstrated schema mismatch.** Accept the three AD2 fields only as an optional complete group on SIGN_EXCHANGE_REFUSED. Enforce exact enums, integer HTTP100–599 or null, HTTP/category consistency, and reject booleans, unknown fields and partial groups. Preserve all existing operation/version/phase/identity/ownership checks. Existing records without diagnostics remain valid.
2. **Cover the adjacent startup blind spot in the same review.** native_child currently discards every top-level failure into one status. Use one bounded serializer shared by the real entrypoint and the synthetic subprocess fixture. A refusal frame has exactly status, stage and code; stages are INPUT, AUTHORITY, RESERVATION, PAYMENT_PREFLIGHT, CLIENT_BINDING, AUTH_SEQUENCE, READBACK, CLOSEOUT, RESULT or UNKNOWN. Codes come from a finite literal source allowlist; unrecognized exceptions become UNCLASSIFIED. Never serialize error messages, stack, stderr, URLs, SQL, bodies, identifiers or credentials. A stage/code is diagnostic only and cannot prove absence of mutations.
3. **Validate and retain that frame through the parent.** Parse bounded child output safely even on a refused exit; record observations under nativeEntry bounded by the actual envelope.limits.child and the existing maximum of eight; R51 reserved six. Record only already-reserved calls; do not add a call allowance. Each observation contains only reserved call number, fixed mode, stage/code, process outcome and journal-merge outcome. Keep work and cleanup observations distinguishable. Preserve the original failure when cleanup also fails. Valid AD2 journals must reach parent memory before its next save. Malformed/foreign/version-regressed journals remain rejected and containment UNKNOWN; do not reconstruct trusted intent from an invalid journal or relax success checks.
4. **Prove the whole composition.** Use actual Python subprocess dispatch, actual Node runChild and shared failure serialization, parent merge, coordinator save, independent closeout, final retained journal/safe summary and private purge. The ENTRY result.json schema remains unchanged; no diagnostic output field is added there. Child-only assertions are insufficient.

No inherited coordinator.py change is proposed. No new runner, diagnostics service, live qualification mode, retry, wait, credential access or provider call is added.

### Exact prospective file list

Paths are relative to backend evidence/APP-013/.

Functional/tests/fixture changes, seven files:
- p08-real-client-binding-local-20261031/source/bound_handoff.py
- p08-real-client-binding-local-20261031/source/test_bound.py
- p08-native-entry-local-20261101/source/native_child.mjs
- p08-native-entry-local-20261101/source/handoff.py
- p08-native-entry-local-20261101/source/test_entry.py
- p08-native-entry-local-20261101/source/test_transports.mjs
- p08-native-entry-local-20261101/source/fixture_child.mjs

Hash-only dependency closure, seven manifests:
- p08-real-client-binding-local-20261031/source/source-manifest.json
- p08-native-entry-local-20261101/source/source-manifest.json
- p08-native-entry-local-20261101/source/test-manifest.json
- p08-key-correction-20261110/source-manifest.json
- p08-connected-packet-20261110/iq1-source-manifest.json
- p08-connected-packet-20261110/account-containment-source-manifest.json
- p08-connected-packet-20261110/account-containment-read-source-manifest.json

Independent dependency review found 14 files total and 32 affected hash references across the seven manifests. No new baseline anchor, changed manifest shape/status, historical receipt rewrite or additional hash-lock code file. Update only dependency hashes for approved changed files. Publish local completion and current pointers after verification. Any additional functional file or stronger recovery algorithm must be disclosed before implementation.

## Finite checklist and observable local finish

| Item | Required result | Status/owner |
| --- | --- | --- |
| Trace source and reproduce failure | Actual full-parent failure reproduced; distinguish historical UNKNOWN | Complete / implementer |
| Reconcile final cleanup labels | Conservative final labels explained without clearing them | Complete / implementer |
| Review complete local scope | Seven functional/test files, seven manifests, bounded interfaces above | Approved / owner decision recorded |
| Implement contract and safe failure path | No new actions; exact schemas; valid child evidence survives | Complete / implementer;72f0390 |
| Verify complete matrix below | Before/after regression and independent review pass | Complete / implementer; completion report |
| Publish local completion | Source/manifest hashes, commands/results, limitations, unchanged acceptance | Complete / implementer; completion report |

Local finish means diagnosis survives the actual parent and cleanup path; it does not mean provider authentication or payment works. Rollback is to retain the current disabled/no-launch state and revert only the approved repair. Consumed R51 remains consumed.

### Verification matrix and commands

- Positive: unchanged authenticated success and ordinary stopped/closed results; absent diagnostic group; SIGN, KEY_READ and EXCHANGE failures surviving the full parent and independent cleanup.
- Negative: exact enum/status/type checks; partial/unknown fields; missing/null/malformed/duplicate/oversize child output; refused exit; private sentinel in thrown errors/bodies never retained; foreign operation, source drift and version regression still refuse.
- Early boundaries: authority/reservation, owner refusal, database connect/TLS/preflight, sequence start and result serialization. Each must produce its correct safe boundary or UNKNOWN; no invented provider explanation.
- Recovery: main failure plus independent cleanup failure; valid child intent retained before parent save; invalid journal remains untrusted; endpoint/readback disagreement remains unconfirmed; database close/session probe failures remain visible.
- Timing/concurrency: cutoff expiry before/after child, timeout, lost output, process interruption, exclusive attempt/child reservation and no replay. Preserve existing call budgets and no retries.
- Browser: existing guarded-opening tests pass; no browser/bootstrap opening after any pre-authentication failure. No real browser or payment is needed for this local bundle.
- Privacy: all synthetic fixtures removed; no raw private input/error retention; unchanged private-file custody and purge checks.

From backend, use existing test entrypoints:
```sh
python3 -B evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.py
python3 -B evidence/APP-013/p08-native-entry-local-20261101/source/test_entry.py
python3 -B -m unittest discover -s evidence/APP-013/p08-native-entry-local-20261101/source -p 'test_*.py'
node --test evidence/APP-013/p08-native-entry-local-20261101/source/test_transports.mjs evidence/APP-013/p08-native-entry-local-20261101/source/test_connected_payment.mjs evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.mjs
python3 -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_*.py'
SIGNMONS_GOVERNANCE_REPO='/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery' node scripts/check-governance-baseline.mjs
npm run arch:check
git diff --check
```
Run focused regressions first, then each required suite once after the final changes; avoid redundant full-suite repeats. Use the pinned Node/Python installations already present. Validate every changed manifest through its existing verifier. Governance frozen baseline, docs consistency, three required governance test files and whitespace checks remain required. Build/lint/disposable DB gates apply if application TypeScript/database behavior changes; those changes are excluded here. Do not report old tests as newly run.

## Audit publication verification

November15 local publication checks passed: governance frozen baseline and cross-repository consistency; all25 required governance tests; backend governance check; architecture; whitespace in both repositories. Two independent reviews checked source diagnosis, containment interpretation, dynamic child limits and all manifest dependencies. The actual-parent signing403 and owner-refusal reproductions are audit evidence; no repaired runtime tests or live success are claimed. Backend runtime/source files remain unchanged.

## Gates that prevent another circular full run

These are review requirements, not a claim of new automated enforcement.

1. Complete the local checklist with actual parent/subprocess regressions and independent source review. A child-only pass cannot establish readiness.
2. Resolve current containment separately with the smallest approved observations; do not run payment to test cleanup.
3. Only then consider one connected attempt with a named remaining external question, exact current source/configuration/effective-access evidence, sufficient time for cleanup, and separate live approval. If it fails, preserve the safe boundary and stop there. No automatic replacement session.

Existing CT2 can freshly check exact app/Firebase disabled state and database sessions using transient SQL recovery plus fingerprint matching. It is hard-bound to R47's operation/hash/revocation cutoff; unchanged CT2 cannot certify R51-specific revocation. R51's erased intent cannot be invented. Any new revocation/cleanup requirement must be explicitly designed and approved after the local repair review, preserving historical UNKNOWN.

The smallest endpoint observation is one GET of the exact existing Sandbox endpoint with the existing endpoint() validator: ID fingerprint, URL, version, event set, test mode and disabled state. There is no inspected standalone endpoint-only executable, so it is a prospective reuse requirement, not a ready command or authorized call. Prepare complete actual interfaces before requesting live approval; do not reactivate retired secrets just for convenience.

Alternatives considered: repeat the current full run (rejected: proven evidence-loss defect remains); add only three field names (insufficient validation and leaves the nearby generic startup blind spot); build a new diagnostics/cleanup subsystem (excluded: use current seams). Recommended scope adds no acceptance section and leaves 3A's finish unchanged. Effort is local repair and integrated verification, followed by separately reviewed containment; no reliable end-to-end completion time is claimed.

Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. Implementer owns local repair/readiness; owner owns the proposed interface-scope decision and later external authority; cloud/DB custodians own credential/provider actions. No scope deviation in this audit. The JC1 interface extension was explicitly approved and is now locally verified; see the completion report. No live authority is inferred.


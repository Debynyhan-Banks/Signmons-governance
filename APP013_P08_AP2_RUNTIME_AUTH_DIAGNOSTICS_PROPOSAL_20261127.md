# AP2 — preserve runtime-authentication failure details

PROPOSED LOCAL REPAIR; NOT IMPLEMENTED. Owner's latest “proceed” authorizes preparation of this concrete proposal. Implementation approval is pending. No Terminal attendance or deadline is needed. Section APP-013 / 3A / P08 remains unchanged.

## Requirement and evidence

The existing 3A acceptance criterion in APP013_REMAINING_EXECUTION_CONTRACT.md is: “owner completes Sandbox payment for that same job; matching mode/account/amount/currency signed event clears its gate.” Authentication is an existing prerequisite to that connected journey, not an additional acceptance section. DATA_CONTRACTS.md's approved local payment policy/job binding retains exact tenant, actor, job, approval snapshot and no-booking authority. No payment, policy, routing or customer-facing behavior changes here.

Backend source is `fef39a05cd7e83b54e74a6774716c2b9ab5a4286`; governance preparation starts at `522833167a3cb389fc02ba57a76b83ca0c17891b`. APP013_P08_AP2_LOCAL_READINESS_20261127.json records the inspection timestamp, exact hashes of every proposed file, current passing source guards and unchanged R67 receipt hashes.

R67 passed current qualification and returned a nonempty token from issuance, then stopped at RUNTIME_AUTH_INTENT / ADAPTER_REFUSED_OR_UNKNOWN. Its child returned and its journal was accepted. The retained outcome is still ENTRY_CONTAINMENT_UNCONFIRMED with AUTH_OUTCOME_UNKNOWN, not proven successful authentication. Checkout never opened. Cleanup reports no resource residuals; private purge and owned-process/artifact removal are recorded. Do not rewrite these receipts or infer their discarded error from synthetic tests.

Inspected missing behavior:
- client.mjs authenticate performs entry guards, a Firebase lookup, exact test-identity checks, token decoding/claims/time checks and the exact protected job read. It does not preserve the substep that threw.
- recovery-sequence.mjs safeCode preserves AP1's four runtime codes but maps other failures to ADAPTER_REFUSED_OR_UNKNOWN. Detailed stage/category/status currently survives only SIGN_EXCHANGE_REFUSED.
- transports.mjs has a bounded five-second transport/read timeout, response byte bound and strict text decoding. Timeout and other transport/decoding errors are not fully represented in the authentication journal.
- bound_handoff.py accepts diagnostic fields only under the signing/exchange contract. It must validate any proposed authentication additions strictly.

This inspection identifies an observability defect. R67's actual cause (including whether it timed out) is UNKNOWN. No local reproduction or new runtime-test pass is claimed in this preparation.

## Proposed behavior and finite output contract

Reuse the existing client, transport, journal and child-to-parent merge. No new runner, endpoint, credential store or authentication-only execution mode.

1. Mark the active substep inside authenticate using a local fixed enum: AUTH_ENTRY, AUTH_IDENTITY_READ, AUTH_IDENTITY_CHECK, AUTH_TOKEN_DECODE, AUTH_TOKEN_CHECK, AUTH_RUNTIME_READ. Assign it in our code; never accept a provider-supplied stage. Only failure metadata is persisted; successful execution keeps the existing phase sequence and acceptance predicates.
2. Preserve AP1's existing fixed failure codes and all signing/exchange diagnostics. Other failures caught in this authentication boundary use one fixed AUTHENTICATION_REFUSED code with bounded diagnostics. Unexpected failures remain UNKNOWN within a known substep; do not manufacture a cause.
3. Reuse existing journal fields authStage, failureCategory, httpStatus and optional responseValidationCode. For the new authentication stages, categories are TIMEOUT, TRANSPORT, HTTP, RESPONSE_VALIDATION, GUARD or UNKNOWN. HTTP status is an integer 100–599 only for an observed HTTP failure; otherwise null. Never derive HTTP status from arbitrary exception text or an untrusted provider error property.
4. Response-validation labels, when applicable, are limited to BODY_BOUND, TEXT_DECODE, JSON_PARSE, RESPONSE_SHAPE, PROVIDER_ERROR, IDENTITY_MISMATCH, CLAIMS_MISMATCH, TOKEN_TIME and JOB_MISMATCH. Define and test the allowed stage/category/label combinations; reject mismatched or partial diagnostic records. Existing SIGN/KEY_READ/EXCHANGE combinations remain unchanged.
5. At the existing transport boundary, distinguish a bounded timeout, request failure, response read failure, byte-limit failure and decoding failure using fixed internal labels. Keep the original error outcome and all existing deadlines, redirect policy, response-size bound, TLS, requests and request counting. Do not introduce a retry, probe, longer timeout, extra fetch, response-body retention or general error logger. Safe metadata cannot grant successful authentication or alter cleanup.
6. Preserve precise known runtime HTTP refusal and wrong-job checks from the existing reader. Observe their existing response/status in the client wrapper without replacing the reader or changing its request. Identity lookup, malformed token and malformed runtime JSON must have distinct substep/validation combinations.
7. Read error metadata defensively: no arbitrary message, stack, cause, URL, token, credentials, response body or identifiers enter the journal/output. Throwing getters, malformed metadata and private canaries must not interrupt cleanup. Do not trust externally supplied stage/category/status to impersonate a successful or locally validated result.
8. Extend the existing parent validator only for this finite contract. Preserve source equality, operation/identity matching, journal concurrency/version rules, result digest requirements, failure conservatism, all independent readbacks and private purge.

## Exact file scope

All paths below are relative to backend evidence/APP-013. Exact before hashes are in the readiness JSON.

| Existing file | Permitted change |
| --- | --- |
| p08-coordinator-auth-local-20261031/source/client.mjs | Authentication-only substep/error projection; unchanged requests and success checks |
| p08-coordinator-auth-local-20261031/source/authority.mjs | Exact transformed-source comparison for this reviewed client delta; retain full equality guard |
| p08-coordinator-auth-local-20261031/source/test_client.mjs | Direct actual-client success/failure/privacy tests |
| p08-serialized-handoff-local-20261031/source/handoff.py | Derived source-lock hashes only |
| p08-real-client-binding-local-20261031/source/bound_handoff.py | Strict finite authentication-diagnostic validation plus affected source hashes |
| p08-real-client-binding-local-20261031/source/recovery-sequence.mjs | Persist bounded authentication diagnostics without changing authentication/payment/cleanup decisions |
| p08-real-client-binding-local-20261031/source/test_bound.mjs | Sequence, privacy, no-retry and cleanup regressions |
| p08-real-client-binding-local-20261031/source/test_bound.py | Strict merge, malformed/foreign diagnostics and concurrency regressions |
| p08-native-entry-local-20261101/source/transports.mjs | Fixed error metadata at existing request/read/decode boundaries only |
| p08-native-entry-local-20261101/source/test_transports.mjs | Injected transport timeout/read/decode/privacy tests, no real network or database |
| p08-native-entry-local-20261101/source/test_entry.py | Actual Node child/journal/Python parent/independent-closeout regression matrix |

Eleven existing derived manifests, hashes only:
- `p08-coordinator-auth-local-20261031/source/source-manifest.json`
- `p08-serialized-handoff-local-20261031/source/source-manifest.json`
- `p08-real-client-binding-local-20261031/source/source-manifest.json`
- `p08-native-entry-local-20261101/source/source-manifest.json`
- `p08-native-entry-local-20261101/source/test-manifest.json`
- `p08-key-correction-20261110/source-manifest.json`
- `p08-connected-packet-20261110/iq1-source-manifest.json`
- `p08-connected-packet-20261110/sq1-source-manifest.json`
- `p08-connected-packet-20261110/account-containment-source-manifest.json`
- `p08-connected-packet-20261110/account-containment-read-source-manifest.json`
- `p08-connected-packet-20261110/vm2-source-manifest.json`

Changing client.mjs also changes its exact extraction guard and the two current embedded hash chains; those dependencies are included now. Preserve historical source copies, previous approvals/results, frozen acceptance text, SDK pins, manifest keys/status/purpose and baseline anchors. No other source/test file is authorized. A newly discovered material dependency requires a scoped decision, not a silent expansion.

## Data, identity, state and retention

Sequence stays: exact existing capability -> memory-only approved credentials/token -> same Firebase identity checks -> same claims/time checks -> same protected exact-job GET -> existing payment handoff only after authentication -> normal and independent cleanup. No new I/O is added. Synthetic tests use fictional identities and injected network/database ports. They do not initialize PostgreSQL, access a real database, read credential/cache files, launch Chrome or contact any provider.

Only fixed labels, observed bounded HTTP status and existing journal ownership metadata persist. Tokens and raw responses remain transient under existing cleanup. Parent proof stays false/unknown when output or journal verification fails. R67 authentication remains UNKNOWN regardless of new local proof. Existing permitted private purge and source-hash evidence retention rules remain unchanged.

## Finite implementation checklist and exit tests

1. Preserve/hash-check R67 receipts and inspect approved file hashes before editing. Refuse source drift; preserve unrelated AGENTS.md and renewal artifacts.
2. Add the finite diagnostic projection in the existing boundaries. Trace every expected failure path to a safe label; do not expand provider access.
3. Synchronize strict journal validation and the exact extraction guard. Demonstrate malformed/forged/partial metadata cannot weaken acceptance or block cleanup.
4. Refresh only the eleven current derived manifests in dependency order and the named embedded source hashes. Current and committed guards must pass.
5. Run the following synthetic matrix through existing actual interfaces, not a duplicate classifier-only mock:
   - Happy authentication and existing payment handoff retain one issuance, one protected read and unchanged proof/cleanup behavior.
   - Firebase lookup transport/timeout/HTTP failure, invalid/null/missing response, malformed custom claims, identity mismatch and claims mismatch.
   - Missing/foreign/malformed token, JSON decode error, invalid claims, expired/future token.
   - Runtime connection/timeout/HTTP 401/403/500, body-limit/UTF-8/read failure, malformed/null JSON, missing/foreign job ID; no payment invocation on failure.
   - Arbitrary thrown values, private canaries, forged stage/status and throwing accessors remain bounded; unexpected errors have UNKNOWN, not a guessed cause.
   - Replay/concurrent journal drift, lost child output, child timeout/exit/interruption and rejected parent merge preserve conservative outcome and independent cleanup. No diagnostic becomes parent authentication proof.
   - Unchanged signing/exchange diagnostics and post-authentication payment-failure distinction.
6. Record per-case results, actual request counts, cleanup/purge and unchanged R67 receipt hashes. Every expected failing case must identify a useful substep/category without raw private content. Do not count tests as section acceptance.
7. Re-run only applicable source and governance gates after the change. Report any unresolved case before proposing external work.

Exact local verification commands after implementation (from the backend unless noted):

```sh
node --test evidence/APP-013/p08-coordinator-auth-local-20261031/source/test_client.mjs evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.mjs evidence/APP-013/p08-native-entry-local-20261101/source/test_transports.mjs
python3 -B -m unittest discover -s evidence/APP-013/p08-real-client-binding-local-20261031/source -p test_bound.py
python3 -B -m unittest discover -s evidence/APP-013/p08-native-entry-local-20261101/source -p test_entry.py
SIGNMONS_GOVERNANCE_REPO='/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery' node scripts/check-governance-baseline.mjs
npm run arch:check
git diff --check
```

Reuse the AP1 connected selection: test_packet, test_launcher, test_approval_wait, test_attended_approval and test_bootstrap_open; explicitly remove test_production_jxa_dispatches_loopback_and_closes_only_owned_window and test_actual_loopback_bridge_and_headless_chrome_handoff from the loaded unittest suite before running it. This is the previously reviewed 58-case selection, with current cases counted at execution; no browser fixture is authorized. Exact selection command from backend:

```sh
python3 -B - <<'CHECKS'
import sys, unittest
sys.path.insert(0, 'evidence/APP-013/p08-connected-packet-20261110')
names = ['test_packet', 'test_launcher', 'test_approval_wait', 'test_attended_approval', 'test_bootstrap_open']
excluded = {'test_production_jxa_dispatches_loopback_and_closes_only_owned_window', 'test_actual_loopback_bridge_and_headless_chrome_handoff'}
def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item
loaded = list(flatten(unittest.defaultTestLoader.loadTestsFromNames(names)))
assert {t._testMethodName for t in loaded} >= excluded
suite = unittest.TestSuite(t for t in loaded if t._testMethodName not in excluded)
result = unittest.TextTestRunner(verbosity=1).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
CHECKS
```
 Run the existing current/committed native, qualification and client extraction guards using their actual public functions. No broad test discovery into PostgreSQL fixtures.

From governance, run node scripts/frozen-baseline-check.mjs, SIGNMONS_BACKEND_REPO='<backend path above>' node scripts/docs-consistency-check.mjs, node --test scripts/frozen-baseline-check.test.mjs scripts/execution-placement.test.mjs scripts/intelligence-alignment-check.test.mjs, and git diff --check. Product build/lint/schema/database/browser gates are not applicable to this diagnostic-only scope; no product source, dependency, schema or browser flow changes. Any need for those surfaces stops this scope for review.

## Readiness, alternatives and next gate

Readiness owner is the implementer. Current source/extraction/manifest guards and frozen-baseline/cross-repository checks pass at the readiness timestamp. Actual client, transport, source-equality guard, journal allowlists and real child/parent test seams were inspected. R67 receipt hashes match. Preparation changes documentation only; the new behavior and test matrix are NOT YET IMPLEMENTED/TESTED.

Configuration/resource pins, effective provider access, current credentials, API compatibility and live authentication are not re-qualified here. They remain UNKNOWN for a future operation. Existing no-retry, one-attempt, concurrency, deadlines and cleanup interfaces are reused; their regression proof is a required implementation exit gate. No live execution-ready claim follows from this card.

Alternatives: another unchanged full run would still lose unrecognized errors; preserving just one timeout code would leave identity/parsing/transport ambiguity; logging raw errors risks private data; replacing the runner or adding a new auth-only subsystem expands scope. The proposed finite projection covers the existing boundary together, with one local owner decision and no attendance.

After local completion, inspect the smallest reusable externally approved qualification interface. Do not promise that an authentication-only live mode is already available: the prior source review found version1 incompatible with the current version2 recovery handoff and BR2 path. A future bounded live check needs its own inspected readiness and explicit authority; a new mode requires a separate proposal. No fresh full session is scheduled by this card. Remaining provider cause cannot be recovered retroactively from discarded R67 data.

Rollback: restore these eleven source/test files and eleven current manifests together to the recorded hashes; preserve R67 receipts and existing disabled/no-live-authority state. No deployment or service configuration rollback is needed because none is proposed.

Completed: canonical/current-source reconciliation, contract/failure-path/dependency inspection, immutable receipt verification and this proposal. Remaining after owner approval: the seven-step local implementation/checklist above. Implementer owns code/tests/evidence; Debynyhan Banks owns the scope decision and later acceptance; provider custodians retain future external authority. Observable local finish is a verified finite failure matrix through the real child/journal/parent flow, unchanged success/cleanup/request semantics and passing guards. This fixes diagnostic loss, not an as-yet-unknown provider/runtime cause.

Accepted milestones remain 4/8; 3A OPEN; R1 newly closed 0/27. No section count, criteria, queue or dependency order changes. No scope deviation in preparation; this is an explicit prospective diagnostic-scope amendment beyond AP1. Requested approval: AP2 local repair and synthetic tests in the listed eleven files and eleven derived manifests only. No credentials, sign-in, provider calls, PostgreSQL fixture, payment, spending, support/customer contact or attended operation is included.

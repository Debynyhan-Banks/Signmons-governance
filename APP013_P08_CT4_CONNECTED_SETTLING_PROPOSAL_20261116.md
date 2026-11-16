# APP-013 / 3A / P08 — CT4 connected settling correction proposal

Status: local review complete; owner implementation decision pending. No provider action or code change. Source baed83f8ebd22700c247ef59ad2b1c0c3d9a584c; SQ3 source48a0a7d and safe evidencebaed83f. Governance result913207e. No new acceptance section or denominator.

## Requirement and demonstrated gap

APP013_REMAINING_EXECUTION_CONTRACT.md section3A requires the admitted-job Checkout, authentic matching event and application payment gate. Authentication is a prerequisite to that same journey. SQ3 demonstrated one successful SIGN after a420-second wait, with independent restoration. It did not prove historical403 causation or guarantee future access.

Actual native import chain: native-entry/source/entry.py loads native-closeout/source/adapter.py, whose load_sources selects live-binder/source/coordinator.py. That Coordinator.run restores runtime first, adds and reads back lookup and signing bindings, immediately invokes stage_a, then creates/reads the key and invokes authentication. Native entry Coordinator.invoke preserves this ordering. Bridge.stage_a derives fresh receive_time when invoked. The bound-client issue path constructs the JWT immediately before SIGN. No fixed settling interval exists on this actual chain. An older composed_auth.py is not the selected coordinator and must not be patched as a substitute.

SQ3 instead checks owned policy, waits420seconds, then performs fresh prediction and SIGN. Its local policy acknowledgement to sign intent was437.112seconds. Metadata/readback/prediction alone are not proof of usable signing. Thus replaying the unchanged connected flow would omit the timing behavior just demonstrated.

## Proposed bounded behavior and files

Implement only in existing native-entry/source/entry.py Coordinator: enforce time admission before the first forward runtime change; after both exact IAM owned readbacks, before the existing stage_a invocation, wait420monotonic seconds with existing capability/interrupt/custody/deadline gates and sleeps at most1second. Require420+960seconds remaining work at first mutation and again before waiting, preserving a full16-minute post-wait work allowance; cleanup remains outside that work allowance under the separate approved cleanupEnd. Anchor the work horizon to both wall and monotonic time and reject nonprogressing/backward clocks or early completion. No wait during cleanup; no retry or new provider request. Reject missing ownership or repeated stage invocation before waiting. Keep existing conditional bindings, call counts, role definitions, identities, payment guards and independent closeout unchanged. Generate JWT only afterward through the existing child.

This proposes longer temporary-resource lifetime by seven minutes and a stricter admission requirement. Future exact windows must accommodate it and credential validity; this document grants no live authority. The16-minute allowance is a proposed conservative reservation based on the previous connected work window, not a guarantee of completion. If full interface tests expose another prerequisite, stop and report it before expanding scope.

Expected code/test files: evidence/APP-013/p08-native-entry-local-20261101/source/entry.py and test_entry.py. Update only derived hash references in these seven existing manifests under evidence/APP-013: native-entry/source/source-manifest.json and test-manifest.json (directory p08-native-entry-local-20261101); p08-key-correction-20261110/source-manifest.json; p08-connected-packet-20261110/account-containment-read-source-manifest.json, account-containment-source-manifest.json, iq1-source-manifest.json, sq1-source-manifest.json. Any further manifest dependency must be disclosed before edits outside this set. Never rewrite old approved packets or receipts. Local evidence and governance completion/readiness documents are included.

## Finite checklist and verification

1. Reproduce missing interval through actual native Coordinator.invoke/selected coordinator using inert ports.
2. Add admission and gated wait at the existing boundary, without changing external interfaces or cleanup.
3. Positive proof: owned bindings, full420seconds, fresh stage_a afterward, one auth/SIGN and unchanged cleanup.
4. Negative proof: missing/foreign ownership, insufficient horizon before mutation/wait, clock rollback/freeze, early wakeups, deadline expiry and second invocation refuse without downstream signing.
5. Recovery/concurrency proof: interruption and process termination during wait preserve existing independent cleanup; lock/replay refusal; cleanup is never delayed. Validate actual worker/supervisor paths with existing synthetic fixtures.
6. Run native Python tests via python3 -m unittest discover -s evidence/APP-013/p08-native-entry-local-20261101/source -p 'test_*.py'; connected packet tests similarly from p08-connected-packet-20261110; applicable existing Node child/transport/payment suites. Preserve and report existing failures without weakening tests. Browser invariant: no Checkout opening before authentication/payment-ready, no opening on wait refusal, existing guarded opening remains once-only; use existing synthetic browser/child tests, no live browser session.
7. Validate actual source guards and derived manifest closure; required baseline, consistency, architecture, governance tests and both whitespace checks. Record exact commands/results and new source SHA.
8. Publish local completion/readiness with live access/credential horizon/payment UNKNOWN. Only then prepare the next separately approved connected packet.

## Boundaries, alternatives and finish

No new credential retention, raw payload/signature logging, provider calls, IAM changes, deployment, password entry, spending, sign-in, payment or support contact. The wait runs before authentication and preserves existing private inventory/independent purge. Old consumed operation IDs remain consumed. Backend AGENTS.md and unrelated renewal artifacts remain untouched.

Alternatives: rerun unchanged (omits demonstrated timing; not recommended); permanent grants or retries (larger scope; excluded); narrowly adopt the bounded interval (recommended). Owner approves this local correction and longer future lifetime design; implementer owns tests and source readiness; cloud/credential/payment owners retain separate live decisions. Rollback is revert only this focused patch and derived pins; no live run is enabled by either version without exact authority.

Observable local finish: actual native-chain tests demonstrate wait/admission/cleanup, source guards pass, no provider actions. Observable customer finish remains same-job Sandbox payment/event/gate evidence and owner acceptance. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. Explicit prospective CT4 timing deviation proposed, not implemented.

Preparation checks: frozen baseline, cross-repository consistency, backend architecture, both whitespace checks and25governance tests PASS on November16. No new runtime tests run or claimed for this documentation-only proposal.

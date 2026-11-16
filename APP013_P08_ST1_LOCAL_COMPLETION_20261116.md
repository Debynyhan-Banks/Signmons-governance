# APP-013 / 3A / P08 — ST1 local correction complete

IMPLEMENTED AND LOCALLY TESTED; LIVE SIGNING UNKNOWN. Owner approval 208511f of proposal 6081161 authorized exactly the three existing SQ1 diagnostic files and local evidence. Backend source 48a0a7d01481bb054ba47b5b73a70f8b0df94058 implements that scope. No credentials, provider actions, live waiting, IAM changes, sign-in or payment occurred.

## Behavior and verification

The diagnostic now requires 720 seconds of remaining main time at entry and until its effective main deadline before enable. After proving its exact owned policy readback, it requires 480 seconds remaining and waits at least 420 monotonic seconds. Sleep chunks are at most one second, separated by existing deadline, interruption, source/configuration and custody checks. A non-progressing clock refuses promptly; early wakeups cannot shorten the interval. It then constructs a fresh prediction time, checks the same identity and makes at most the existing single SIGN request.

Cleanup logic, 660-second independent cleanup and 120-second closeout reserves, one-hour maximum window, conditional policy ownership/expiry, source-bound authority, result/scope schemas, SDK pins, permission checks and provider-call ceilings are unchanged. No deadline is extended. Only sq1_signing_boundary.py, test_sq1_signing_boundary.py and their two entries in sq1-source-manifest.json changed; unrelated AGENTS.md and historical renewal files remain untouched.

All 100 focused tests passed in 17.997 seconds; all 422 connected-packet tests, including those 100, passed in 42.114 seconds. New cases prove the complete interval, fresh prediction, 720/480-second equality and refusal boundaries, early wakeups, frozen/rollback/forward clocks, source/configuration/custody drift, post-wait UID refusal, and real subprocess SIGINT/TERM plus worker/supervisor death during waiting. Existing replay/overlap, denial/success, conditional policy edits, lost acknowledgements, independent restoration and privacy cases also pass. Process tests accelerate only injected phase sleeps with a shared synthetic offset across exec; signal delivery, ownership and process supervision remain real. No provider adapters are live.

The first restricted test run recorded sandbox failures for localhost sockets, process inspection and nested sandbox-exec. Four new test fixtures also advanced the clock inside a bounded HTTP request and correctly triggered the earlier HTTP timeout instead of the intended between-call admission check. The fixtures now inject the elapsed time after the actual HTTP method returns. The final permitted local synthetic runs pass; no runtime test or safety check was weakened. The connected suite's expected negative repository-error test emits “fatal: not a git repository” and exits successfully overall.

Actual committed source_guard passed at 2026-11-16T14:08:34Z over 51 repository files and 61 SDK files. Manifest digest d572ac13394a4db8b35fa91e2da3ff904fb9d713df4a74f7349bb87ad2cca0cc; old SQ1 source binding refused with SQ1_SOURCE. Only the two approved source hashes changed; all other manifest members/pins remained equal. Static inspection did not read credentials or create authority. Review was by the implementer; no independent-agent review is claimed.

Local evidence is retained under backend evidence/APP-013/p08-connected-packet-20261110/st1-local-verification: initial/final focused logs, connected-suite log, source-guard.json, review.json and final checks.json. This evidence is local validation, not current usable signing permission or owner acceptance of payment.

## Completed checklist and next boundary

All six approved local checklist items are complete: timing/admission implementation; positive interval/order tests; negative boundary/drift tests; interruption/recovery/concurrency regression coverage; focused/connected/source/governance verification; source-bound completion and unresolved-fact handoff. No extra file or shared runtime prerequisite was introduced.

The seven-minute value remains an experimental bound. Propagation as the cause of SQ1's denial remains unproven and seven minutes cannot guarantee convergence. SQ1's immutable HTTP403 result and verified cleanup remain; historical R52 cause and AUTH_OUTCOME_UNKNOWN remain unchanged. Section 3A still needs usable signing/application authentication, same-job Sandbox payment, authentic event/application-gate evidence and owner acceptance.

Implementer next prepares a fresh signing-only qualification against this source if the owner proceeds. Its actual dynamic configuration, credential horizon, current provider state, source/command/resource pins, call budgets, sufficient main time and unchanged cleanup reserves must be reviewed before requesting live approval. Owner/cloud/credential custodians retain that separate decision. No current live packet or attendance window is established, and old approval cannot authorize the amended operation. Observable next result is one separately authorized isolated SIGN outcome plus independent restoration, not acceptance of payment.

Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation beyond approved ST1.

# APP-013 / 3A / P08 — ST1 local signing-timing amendment

PREPARED FOR OWNER REVIEW; IMPLEMENTATION NOT AUTHORIZED. The owner's “proceed” after SQ1 closeout authorizes preparation of this bounded review. No code, credential read, provider action or live session is started by this document. SQ1 remains consumed and closed.

## Traceability and decision

Section 3A's acceptance criterion remains the admitted job's Sandbox payment plus authentic matching event and application payment gate, followed by owner acceptance (APP013_REMAINING_EXECUTION_CONTRACT.md, Section 3A; DATA_CONTRACTS.md PaymentPolicy). Signing is an existing prerequisite to that connected workflow, not a new acceptance section.

Backend HEAD 6187afcd0acc07d6b23da5aa71a6fd250e2e28c8 contains SQ1 live evidence; diagnostic source is bf2d2c1cc5e6c73dde5e6247d9ee610fd04f0eb4. Governance result 7ae4772 / APP013_P08_SQ1_RESULT_20261116.md records the current HTTP403 IAM_PERMISSION_DENIED and verified cleanup at 2026-11-16T13:42:48Z. Local receipt timestamps place policy-add acknowledgement 12.884 seconds before SIGN intent. These are not provider application timestamps. Inspected Driver.main performs policy readback, prediction and same-UID check with no settling interval; validate_scope currently permits only 300 seconds of remaining main time at entry.

Official guidance inspected for SQ1 says policy edits typically take about two minutes and may take seven minutes or longer: https://docs.cloud.google.com/iam/docs/access-change-propagation. Propagation remains a plausible, unproven cause. A seven-minute interval is a finite experimental choice, not a convergence guarantee or proof of the historical R52 cause.

Alternatives: leave the code unchanged and stop; repeat immediate signing without resolving the timing confound; broaden diagnostics with extra provider calls; or add one fixed interval using the existing clocks and gates. Recommend the last option. This explicitly changes SQ1's no-extra-propagation-wait exclusion and permits a longer temporary-grant duration only in a future separately approved run. No milestone, dependency order, provider-call ceiling, success predicate or cleanup reserve changes. No support contact.

Requested decision: approve ST1 local correction and tests in the exact scope below. Live qualification, IAM changes and spending require a later exact decision after local readiness is complete.

## Exact files, behavior and boundaries

Modify exactly three existing backend files under evidence/APP-013/p08-connected-packet-20261110:

1. sq1_signing_boundary.py: add the fixed 420-second settling interval and sufficient-time admission checks.
2. test_sq1_signing_boundary.py: exercise the changed behavior through the existing injected Clock, Provider, PhaseContract and process/supervisor tests.
3. sq1-source-manifest.json: update only the hashes changed by these two sources; preserve all other source/SDK pins.

Reuse Driver.gate, monotonic/wall-clock hooks, injected sleep, source/configuration guard, same-identity lease, journal reservations, existing safe error codes, and independent cleanup/supervisor. No new runner, transport, scope field, result schema, shared native change or production path. Local test evidence may be added under st1-local-verification; governance proposal/readiness/completion and synchronized pointers may be recorded. Any additional source file requires a new exact scope decision.

Required behavior:

- Raise minimum remaining main time at entry from 300 to 720 seconds (420-second wait plus the existing 300-second allowance). Before the first enable mutation, require at least 720 seconds until the driver's effective main deadline. Insufficient time stops before any mutation.
- After the exact owned policy readback passes, require at least 480 seconds until the effective main deadline: 420 seconds for the interval and 60 seconds reserved for existing prediction, UID and SIGN stages. These are conservative admission bounds, not runtime-duration guarantees; all actual per-call and phase deadlines still apply.
- Start the 420-second interval after that readback. Measure elapsed time with the monotonic clock. Sleep in chunks no greater than one second, using the existing gates between chunks and immediately after the interval. Early wakeups must not shorten the interval; deadline, clock rollback, interruption, source/configuration drift or custody failure stops subsequent main actions and enters independent cleanup. A non-progressing injected clock must not create an unbounded test loop; preserve actual clock/deadline safety and test this condition explicitly.
- After the complete interval, generate a fresh prediction receive_time and use the existing prediction, same-UID/state read and single SIGN in their current order. No provider polling, signing retry or mutation retry. No long uninterruptible sleep, retained secret or new raw output.
- Preserve current conditional binding expiry, unchanged cleanup/purge deadlines, minimum 660-second independent cleanup reserve and 120-second closeout reserve, and maximum 3600-second total window. Never extend an approved deadline to accommodate waiting. Fresh source-bound scopes must provide sufficient time and credential coverage through their final closeout horizon; old authority cannot be reused.

The owner/project/identity/role pins, 25 CLI / 14 direct HTTPS / 2 explicit cache-read ceilings, one enable/add/SIGN/remove/disable, safe response projection and SDK exception boundaries remain unchanged. During the wait, credentials and identifiers remain only in existing process memory; independent process/private-data closure remains mandatory. Policy removal failure must not suppress identity disable. Same-job payment, SQL, Firebase exchange, browser opening and customer data remain excluded. No additional spending is authorized.

## Readiness record — preparation only

Inspected November 16, 2026 against the source above:

| Prerequisite | Existing evidence / result | Responsible owner |
| --- | --- | --- |
| Actual provider serialization, parsing, missing/null fields and safe errors | Existing SQ1 projector and phase tests; live safe refusal retained. Unchanged by proposed wait. New regression execution PENDING. | Implementer |
| Dynamic commands/configuration, resource pins and source guards | Driver.gate and validate_scope inspected; reuse exact existing functions. Current live effective access and credential coverage UNKNOWN. | Implementer / cloud and credential custodians |
| Wait and time admission | Missing in Driver.main; 300-second entry minimum inspected. Proposed constants and actual-boundary tests above; NOT IMPLEMENTED. | Implementer after owner approval |
| One attempt, concurrency, interruption and recovery | Existing lease, consumed phase reservations, supervisor and independent cleanup inspected; new interruption-during-wait cases PENDING. | Implementer |
| Restoration and retention | SQ1 authoritative policy absence, same-UID disabled and process/private closure verified; future outcomes UNKNOWN. | Cloud custodian / implementer |
| Connected acceptance | Authentication/payment/event/gate and owner acceptance remain missing; this change proves none of them. | Owner / implementer |

This is local implementation readiness only, not execution readiness or automated proof of propagation. Existing 80 focused / 402 connected tests are historical same-source results. Do not substitute them for the amended tests or current provider access. No live window is scheduled.

## Finite checklist and verification

1. Implement only the specified timing/admission behavior and source pins.
2. Positive tests: actual Driver.main waits at least 420 monotonic seconds after owned readback; prediction time is fresh; exact call order and ceilings unchanged; success and structured403 each lead to independent restoration.
3. Negative tests: insufficient entry/pre-enable/pre-wait time; boundary equality; early wakeup; frozen/rollback/forward-jump clocks; source/configuration/custody drift; prediction or UID refusal after waiting. Assert no premature SIGN and no mutation when pre-enable admission fails.
4. Interruption/recovery/concurrency tests: SIGINT/TERM and supervisor recovery during the interval; cleanup after policy addition but before SIGN; consumed/overlapping attempts refuse; branch independence and lost-acknowledgement behavior unchanged. Confirm no additional provider calls, retries or raw private retention.
5. Run focused and connected-packet suites using injected/local transports only, inspect manifest/source guard, and complete all governance/baseline/architecture/whitespace checks. No browser/SQL/build behavior changes; assert those paths remain unreachable rather than claiming a new live browser/database gate.
6. Record exact changed source, tests/failures/results, unresolved facts and finite completion; prepare any future signing-only qualification only after this local work passes. Stop for new scope if the existing seams cannot satisfy these requirements.

Backend commands: `python3 -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_sq1_signing_boundary.py'`; then the same command with `-p 'test_*.py'`; `SIGNMONS_GOVERNANCE_REPO=<resolved governance> node scripts/check-governance-baseline.mjs`; `node scripts/architecture-check.mjs`; `git diff --check`. Use the existing required test environment and source guard, without native defaults. Governance commands: frozen-baseline-check; docs-consistency-check with exact backend; the three required governance test files; whitespace. Do not weaken tests to accommodate the new timing.

Rollback/disabled state: leave the unapproved implementation absent; after any approved implementation, lack of a new committed exact source-bound authority prevents live dispatch. Reverting the three changed files requires checking their pins and retaining all historical evidence. Never replay SQ1 or restore a historical whole provider policy.

Observable local finish: changed three-file implementation, passing actual-boundary timing/cleanup tests, pinned manifest and completed readiness record. Current blocker is owner approval of this explicit timing deviation; no Terminal attendance is needed. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. Explicit prospective ST1 deviation; none implemented.

Preparation verification on November 16: frozen baseline before/after, backend governance wrapper, cross-repository documentation consistency, architecture and whitespace checks PASS; all 25 governance tests PASS. These validate this documentation-only proposal, not the unimplemented timing behavior. Backend source and pre-existing user changes remain untouched.

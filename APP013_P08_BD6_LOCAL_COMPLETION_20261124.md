# BD6 local correction complete

APP-013 / 3A / P08. Owner approval `392c0c7` for the reviewed ten-file proposal is implemented in backend **`1e21bb87a3640ef5f5ceb3f76fe569ca6ea4a612`**. The local checklist is complete. This does not complete section 3A or authorize an external operation.

## Behavior and evidence

The original defect was reproduced with actual SIGINT and SIGTERM at the process-creation/registration boundary. In both cases the old runner reported cleanup while a harmless canary child remained alive; the test harness independently reaped it. The corrected billing path records interruption without abandoning child registration, stops subsequent dispatch, retains actual owned handles and separately verifies reaping and process-group absence.

A fresh reader now requires an exact completion receipt. Interruption during finalization must have its matching immutable veto; missing or failed completion cannot become a positive result. The single completion boundary occurs after deferred handlers are restored. Interruption after a completed, closed observation does not retrospectively negate that observation. Failed reaping, unknown group state and missing process history remain UNKNOWN. Separate closeout validates those receipts; it does not reconstruct OS ownership or adopt saved PIDs after a crash.

Shared `NativeIO`, owner/project and permission classes are unchanged. Billing command limits, resource pins, SDK exception, socket/outer deadlines, no-retry gates and output acceptance remain intact. The change is confined to the two approved Python files and eight derived manifests. There are 27 billing test methods, including 18 added regressions. All 260 current file references in those manifests verify; 45 historical R56/R57/VM2 evidence files are unchanged. The actual committed source guard passes with manifest `f97f04298c4c35a287bb213a5659745d7b62fd301c8cbb4a459f75ed74de81d4`.

## Validation and resolved failures

Final runtime results: **267 qualification tests, 100 SQ1 tests and 53 VM2 tests — 420 passed, zero failures/errors.** These use synthetic data, inert local processes and local loopback fixtures. No real credential, provider, SQL or payment operation was performed during this correction.

Commands use pinned Python `/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B`, loading `test_qualification_launch`, `test_sq1_signing_boundary` and `test_vm2_metadata_read` with `unittest.defaultTestLoader.loadTestsFromName`. Exact suite counts, log paths/hashes, source inventory and control results are retained in `APP013_P08_BD6_LOCAL_VALIDATION_20261124.json` and `APP013_P08_BD6_LOCAL_SOURCE_INVENTORY_20261124.json`.

The first focused run had two failures and four errors. Missing completion now returns the existing safe refusal code. Three new tests were corrected to construct synthetic approvals before intercepting Popen; another injects its signal inside the actual inherited guard. Runtime assertions were preserved. The next focused run passed all 59 tests.

The initial broader run reported 15 failures and 42 errors across 42 distinct methods. Baseline `2cde22c` reproduced the same expiry failures: a reused native execution fixture had cleanup at `now+2720s`, but its qualification fixture purged at `now+1000s`. The runtime guards correctly refused it. Independent review confirmed that this packet-construction fixture never executes native work and should use the existing `EntryTests.setUp(timing=False)` mode. That one-line fixture alignment, plus its explanatory comment, stays in the approved test file; no assertions, runtime guards or live windows changed. The subsequent full 267-test run passes. Initial logs and baseline/current comparison results remain recorded; they were not relabeled as passes.

Independent source/test review passed. Frozen-baseline, complete consistency, backend governance wrapper, architecture, whitespace and the 25 required governance tests passed; final post-document results are recorded in the validation JSON. Browser, database and application build tests are not applicable to this local CLI lifecycle correction. No existing live evidence was replaced by a fixture or test result.

## Handoff

Completed: approval traceability, exact local reproduction, billing-only correction, direct and broader regressions, independent review, current manifest verification and preservation of historical evidence. The implementer owns this completed local work and any future exact readiness/launch comparison.

Remaining: the current billing prerequisite is UNKNOWN. VM2 recorded HTTP 403/PERMISSION_DENIED, but the specific cause and secret-version state remain UNKNOWN. The cloud/billing custodians retain any external-state decision. BD6's prior live approval expired without execution; its operation root was never created. There is no new live window, provider authority or Terminal attendance request.

Next observable result: a fresh, exactly reviewed three-read billing qualification, or a precise readiness blocker. This is a prerequisite observation, not a unique diagnosis of the 403 or payment acceptance. The same-job Sandbox payment, matching signed event and cleared payment gate remain required for section 3A.

Accepted 1A/1B/2A/2B remain **4/8**; **3A OPEN**; R1 newly closed remains **0/27**. **No scope deviation beyond the explicitly approved local correction and tests.** Unrelated owner changes and prior renewal evidence are preserved. No push, deployment or external change occurred.

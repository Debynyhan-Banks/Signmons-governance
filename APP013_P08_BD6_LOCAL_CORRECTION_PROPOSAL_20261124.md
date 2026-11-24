# BD6 local runner correction — owner decision pending

APP-013 / 3A / P08. This proposes one local correction to the existing billing diagnostic and its tests. It is not another acceptance section, a replacement payment workflow or live authorization. No Terminal attendance or deadline is needed.

## Traceability and demonstrated gap

Section 3A's entry requires the approved Sandbox configuration to be verified; its exit remains the same admitted job's payment, matching signed event and cleared application gate. See `APP013_REMAINING_EXECUTION_CONTRACT.md`, section 3A. The billing diagnostic checks one current prerequisite without repeating the full payment workflow. It cannot uniquely explain VM2's HTTP 403.

Reviewed runtime source: backend `c1ee4b0ec834505936c1de66cb965b42f697f8e4`; current HEAD `2cde22c` adds only VM2 safe evidence. At that source, `NativeIO._owned_run` creates a process before registering its handle, while the billing runner's SIGINT/SIGTERM handler immediately raises. An interruption between those steps can leave an untracked child and a falsely positive cleanup Boolean. Independent review confirmed the path and the missing test. This is a source finding, not an observed BD6 orphan: BD6 never launched. Exact approval and stop evidence are in `APP013_P08_BD6_HELD_20261124.json` and `APP013_P08_BD6_READINESS_ADDENDUM_20261124.md`.

The nine existing billing tests passed before the finding but do not exercise this interval. The preparation record's readiness PASS is superseded. No unchanged approved execution path avoids the gap: SQ1/IQ1 exclude billing; VM2 is metadata-only; broader qualification changes the call allowance. Another timed run or signal wrapper would not be a justified substitute.

## Finite files and behavior

Reuse the existing billing capability, runner, IO, command descriptors, owned-process cleanup, immutable receipts and direct tests. Keep shared `NativeIO` and the behavior of non-billing modes unchanged. Direct edits are limited to:

- `evidence/APP-013/p08-https-output-category-local-20261029/source/qualification_launch.py`: billing-only signal handling, pending-interruption checks, owned-handle closure verification and result/closeout interpretation.
- `evidence/APP-013/p08-https-output-category-local-20261029/source/test_qualification_launch.py`: direct reproduction and regression tests.

Refresh only derived file hashes in these eight current manifests, in dependency order:

1. `evidence/APP-013/p08-https-output-category-local-20261029/source/source-manifest.json`
2. `evidence/APP-013/p08-native-entry-local-20261101/source/source-manifest.json`
3. `evidence/APP-013/p08-key-correction-20261110/source-manifest.json`
4. `evidence/APP-013/p08-connected-packet-20261110/iq1-source-manifest.json`
5. `evidence/APP-013/p08-connected-packet-20261110/account-containment-source-manifest.json`
6. `evidence/APP-013/p08-connected-packet-20261110/sq1-source-manifest.json`
7. `evidence/APP-013/p08-connected-packet-20261110/account-containment-read-source-manifest.json`
8. `evidence/APP-013/p08-connected-packet-20261110/vm2-source-manifest.json`

Independent review traced this ten-file set and found no embedded Python/MJS digest replacement needed. Preserve manifest keys, purposes, SDK pins and baseline anchors. Historical audits, R57/VM2 receipts and old approvals are immutable. Governance proposal, approval, completion/readiness evidence and canonical status may record this work; no other runtime file is included.

For billing only, make SIGINT/SIGTERM handlers record a pending interruption instead of raising during child creation/registration. Check the flag and deadline after guards/reservation, immediately before dispatch, and after each existing CLI returns. A pending interruption stops subsequent commands. Let the already bounded owned call complete its cleanup; do not add retries, delays or another command.

Retain the actual owned process handles through a second absence/reap verification. An empty active-child set alone is insufficient. Persist a billing-only immutable interruption veto when finalization is interrupted; billing result readback and closeout must honor it and require the main cleanup evidence. Reuse the existing immutable-write and safe-marker pattern without adding a supervisor or process registry. The separate closeout command is a validated receipt readback; it cannot reconstruct OS ownership after process death. Missing history, failed reap/absence verification and SIGKILL remain UNKNOWN. Never adopt a PID from disk or signal an unowned process.

Preserve exact owner/project/billing-account pins, output acceptance, Boolean/error sanitization, three CLI calls, zero separate cache/HTTPS/SQL calls, ten-second billing socket timeout, thirty-second outer bound, cleanup reserve, source/configuration checks, committed approval and one-attempt/deadline gates. The SDK exception is unchanged. Only bounded interruption/cleanup evidence may be added to billing receipts; no raw process command, output, credential, account number or provider body is retained.

## Checklist, tests and observable finish

1. Record the owner decision before coding; inventory the ten files and preserve unrelated AGENTS.md/renewal changes. Run frozen-baseline and complete consistency checks.
2. Reproduce the registration gap through the actual billing runner with an inert local subprocess and its actual SIGINT/SIGTERM handler. The test harness must own and close the canary child independently even while demonstrating the old failure.
3. Implement the billing-only correction above. Add tests for interruption before registration, during guards/reservation, before/after dispatch and during result publication; assert no later CLI is launched and no success readback survives the finalization veto.
4. Test successful output/cleanup, cleanup or group-absence failure, missing history, SIGKILL, concurrency/replay, deadline exhaustion and private-value exclusion. Preserve the existing exact command, output, no-retry and timeout tests. Verify non-billing modes are unchanged.
5. Refresh the eight current manifest hashes topologically. Verify every reference and confirm historical evidence remains byte-identical.
6. Run direct billing, owned-process, owner/project and project-permission tests from `test_qualification_launch.py`, followed by applicable full qualification regressions. Run existing SQ1 and VM2 tests because their source guards depend transitively on the changed manifest. Use pinned Python with `-I -B`, synthetic credentials/outputs and inert local processes only. Record actual commands, applicability and counts, including any failure; do not silently rebaseline old locked evidence.
7. Run backend architecture/governance checks, governance frozen-baseline/complete consistency and the three required governance test files, plus `git diff --check` in both repositories. Browser, database and payment tests are not applicable to this local CLI lifecycle change; no application behavior is changed.
8. Obtain independent source/test review before declaring local readiness or requesting a live window. Finish with exact source/test evidence, unresolved facts and one truthful next step. Do not automatically schedule or launch another qualification.

Observable local finish: the inert child-registration interruption no longer escapes tracking, cleanup uncertainty cannot become a positive result, existing behavior outside billing is unchanged, current source pins validate, and independent review passes. This removes a local execution blocker only. Current billing status, secret-version state and the reason for VM2's 403 remain UNKNOWN until separately authorized observations establish them.

## Readiness, ownership and boundaries

At proposal time, inspected source and test findings are recorded above; the existing nine billing tests and pre-change governance checks passed. The proposed correction and new tests have not been implemented. The complete live readiness gate therefore remains blocked. The implementer owns reproduction, correction, verification and accurate closeout reporting; the owner decides this local scope; cloud/billing custodians retain later external decisions.

No credentials, cache reads, provider calls, sign-in, SQL, IAM/API/secret/billing changes, payment, spending, deployment or support/customer contact are authorized by this proposal. No new helper subsystem, command allowlist, SDK version, acceptance criterion or dependency order is proposed. Rollback restores only the approved ten-file delta and derived pins; preserve all attempt evidence. The expired BD6 approval is not reused, and corrected source remains disabled for external use without fresh exact authority.

Explicit prospective scope change: the prior BD6 approval permitted reads and cleanup only; this decision would add the finite local correction and tests described here. None is implemented. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. The same connected customer journey remains the objective.

Requested owner decision: **Approve BD6 local runner correction and tests** within these ten files and stated exclusions. No timed attendance is required.

# R1-W01 / APP-013 / 3A / P07 closeout-only local card

Status: card completed before coding; local preparation/testing now complete. External use remains gated.

## Authority, source and workflow

Owner approved Alternative 1 in `APP013_P07_MANDATORY_CLOSEOUT_RECOVERY_PROPOSAL_20261022.md` and specifically requested the failure reason be logged. Backend source `057465be235ab6117ea22cae3e4c35f27e6f6aba`; governance source `d647bf95825fb99b50fada93b9f76caeb76ea511`.

3A's acceptance remains authentic same-job Sandbox settlement of the approved payment gate; this helper earns no acceptance. It resolves mandatory closeout for consumed operation `bfc0bb5b-1564-4991-a446-3960caa67d49` before the connected payment workflow can proceed.

Inspected evidence: immutable `stop.json` has `INTERRUPTED`, `possibleMutation:false`, `commitState:NOT_STARTED`, `closeoutVerified:false`; no mutation-intent or closeout receipt. Existing `closeout()` discards all database stderr and returns only false, so its actual failure cause is unknown. Reuse its exact read-only `pg_stat_activity` query and PostgreSQL 16 Unix-socket fixture pattern. Do not modify the consumed controller/receipts.

## Finite behavior and data boundary

Fresh private package `/private/tmp/p07-closeout-only-20261022-prep1`: `helper.py`, two test files, README, plan, manifest only. Plan `76a8f82d-1d34-44e9-8a5f-0234c48b8052`; packet `6504f835-2c15-4268-bc5b-16c9ee8f6bb6`; closeout operation `0d2f9eca-c8e8-49b6-b3c5-182416164a90`. No bound window or live approval at preparation finish.

Only database SQL: repeatable-read READ ONLY transaction, count sessions matching the consumed operation application-name prefix, exclude the reader PID, ROLLBACK. Require exit zero plus exact output `0`. Set verify-full/system roots, bounded connection/query/process times and session read-only options. The owner supplies the current CHILD password through hidden Terminal input; no computer-use handoff or Stripe ID.

Reserve one exclusive attempt only after window, integrity, explicit approval and TTY checks. Enforce a wall-clock deadline during hidden input and query; kill/reap the child on timeout or interruption. Classify in-memory stderr into fixed authentication/TLS/DNS/connectivity/query/unknown codes; persist only allowlisted stage/reason, child-exit state, timestamps, operation references and booleans. Unknown errors stay unknown; never infer a root cause. No raw stderr, passwords, account IDs, SQL output/counts, tenant rows or customer data in receipts. Private exclusive files in mode-0700 directory; keep sanitized evidence and receipts, clear volatile input/error values; no broad retention sweep.

## Checklist and verification

- [x] Prepare one disabled package, exact manifest and no-action check.
- [x] Implement exclusive one-use reservation, exact approval/window checks and read-only closeout.
- [x] Log fixed failure stage/reason and truthful unconfirmed result on failure.
- [x] Unit tests: success, nonzero/malformed output, password/TTY, classification including unknown/sensitive errors, deadlines/signals, private receipt/concurrent reservation, exact approval, no-window/no-approval refusals and failed readback.
- [x] Disposable PostgreSQL: exact query detects a named competing session, returns zero after closure; clean up fixture even on test failure.
- [x] Run `python3 -B -m unittest -v test_helper.py test_postgres.py` (21 helper cases and 2 PostgreSQL cases run separately), `python3 -B helper.py --check`, and assert `--run` refuses without a window. No browser test: no UI/application/browser changes or authorized browser action. No product build/lint: only private standard-library helper and repository evidence.
- [x] Run governance baseline/consistency, 25 safeguard regressions, backend architecture and both whitespace gates; publish local preparation evidence and progress handoff.

## Owners, dependencies and disabled state

Implementer owns preparation, tests and failure classification. Owner owns hidden input and later exact external approval/window. Live query depends on existing administrator credentials/network/TLS; no grants, settings or credentials change. Local proof depends only on installed PostgreSQL 16. No merge, push, deployment, provider change, payment, tenant mutation, session termination or main-operation retry.

Rollback: remove unused preparation only if separately requested; preserve consumed receipts. Failed external proof remains consumed/unconfirmed, with no retry. Finish: complete local evidence, fixed tested failure reporting, both no-window and no-approval refusals demonstrated using synthetic files, no real database access. Later closeout execution remains a separate gate. Measures remain 0/27 R1, 6/60 legacy, 4/8 walkthrough, 0/13 intelligence. **No scope deviation from the approved local recovery and failure reporting.**

# R1-W01 / APP-013 / 3A / P07 runtime guard completion proposal

Status: **Alternative 1 owner-approved and locally completed; 60/60 isolated tests pass; no external action authorized**.

## Traceability and inspected gap

This serves the existing 3A criterion: only an authentic matching same-job Sandbox settlement clears the payment gate. P07 must first start the existing repaired image in an isolated runtime with verified closeout. It adds no product feature, acceptance section or ledger row.

Source snapshots: backend `4558f8e3d478d5551c5c4930b19d84f8c36cd376`; governance `1ff9350bd820cb6a973424e723c96c19cdf17575`. Worktrees clean on entry. Existing approved card: `APP013_3A_PAYMENT_SECTION_CARD_20261020.md`; architecture/startup/envelope/account/TLS/predicate decisions remain unchanged. Reuse private `/private/tmp/p07-repaired-runtime-readiness-20261021-repair5`, manifest `17c5fad2837ec01bb590d1607f4dbdaf88ab48ee3f8856fadf27f61279ced6fe`; controller `e04fe931932ca3bf3568cef6bacb6a60ceb29dc3845186d0d428a2d4c8e622d1`.

The tenant binding succeeded and closed at approximately 5:06 p.m. Eastern. No application/runtime source, Prisma, Dockerfile or package manifest/lock changes exist between repaired application commit `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd` and the current backend head. The unused repaired image is retained. All 36 existing controller tests and no-action check pass now, but those tests omit three guards required by the approved operation:

1. **Deadline enforcement:** controller lines 517–530 permit provisioning after hidden-input/preflight delay crosses work end; the first explicit work-end check is line 531, after role/secrets/identity creation. `run_status` lines 111–116 applies a fixed per-command timeout without the remaining operation deadline. A synthetic clock probe returned from database preflight one second after work end: mocked database provisioning, startup secrets and identity creation were all still called. No external commands ran.
2. **SIGTERM cleanup:** SIGTERM remains the default handler after controller import; no handler is installed in the run/cleanup paths. Catching BaseException does not intercept default process termination. Existing interrupt coverage injects KeyboardInterrupt, so it does not prove actual SIGTERM containment.
3. **Cleanup readback:** `remove_tag` lines 456–459 does not verify the tag absent afterward, and service-identity disable lines 493–495 has no disabled-state readback. A mocked successful disable acknowledgment returned no containment failures without a service-identity describe/readback. Acknowledgment alone cannot prove the required final state.

These are local controller gaps, not a new live failure or a failure of the completed tenant binding. Existing files/packages/receipts remain unchanged. Backend evidence: `evidence/APP-013/p07-runtime-readiness-resume-review-20261022.md`.

## Alternatives and recommendation

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Complete only these three local guard gaps in a fresh disabled copy | Enforce existing deadlines, route catchable termination into bounded cleanup, and require authoritative cleanup readback; retain exact resources/actions | Recommended |
| 2. Run the current package because its 36 tests pass | Leaves demonstrated late-mutation and falsely verified-cleanup paths | Reject |
| 3. Redesign the payment runtime or rebuild the app | Unnecessary product/architecture work for controller-only gaps | Defer |

## Finite local section card for Alternative 1

**Behavior/files/interfaces:** create a fresh private copy with new plan/packet/operation IDs. Change only its `controller.py`, existing focused `test_controller.py`, manifest/plan/README and evidence/governance records. Reuse the unchanged role SQL and existing Firebase, IAM and database-closeout helpers. Preserve normal revision, repaired image, tenant/job, SQL/grant boundaries, six secret resources, seven secret references/bindings, disabled six-event destination, zero normal traffic, USD 1 allowance and fixed retirement within 24 hours. No other source or helper subsystem.

**Data/state/identity/retention:** hidden password and signing-secret input stays memory-only; raw IDs/values/errors stay excluded from files/arguments/chat/logs/receipts. Exact immutable approval and exclusive no-retry reservation precede access. Recheck live clock after waits/input/preflight and before any ordinary mutation; cap ordinary input/commands by work end. Cleanup has its separately bound containment budget, never treated as permission for more provisioning. No success after an expired phase. SIGINT/SIGTERM must enter cleanup with truthful residual reporting; repeated signals during cleanup must not create an unbounded loop or claim success. SIGKILL/power loss remains uncatchable and requires the existing journal-based cleanup-only recovery.

**Finite checklist:** (1) phase/deadline enforcement including delayed hidden input and command completion; (2) real catchable-signal cleanup with private input restoration; (3) authoritative tag-absence/service-identity-disabled readback and strict normal-traffic preservation; (4) retain/extend current tests, syntax/no-action/refusal/hash inventory; (5) evidence and required repository checks. Report persistence or unavailable readback as unconfirmed, never verified. No new allowance, grant or provider action.

**Verification:** all existing 36 tests retained. Add deterministic before/at/after deadline cases, preflight crossing deadline, hidden-input timeout, slow command, no mutation after expiry and cleanup budget exhaustion; actual isolated child-process SIGTERM plus SIGINT and repeated-signal cases with every provider/database action replaced by local fakes; tag still present, identity still enabled, malformed/failed readback, unchanged normal traffic and successful verified cleanup; exclusive concurrent reservation, journal/recovery and no-retry regressions retained. Commands: `python3 -B -m unittest -v test_controller.py`; AST/Python and existing Node helper syntax; `python3 -B controller.py --check`; no-window live modes refuse before input/access. Run frozen-baseline/consistency/25 governance regressions, backend governance/architecture and whitespace checks. No new live database/browser/provider test is authorized; actual browser/provider qualification belongs to the later exact operation.

**Dependencies/owners:** owner Debynyhan Banks approves/refuses this local correction; implementer prepares/tests only after approval. Owner supplied **today, October 22, 5:30–7:00 p.m. Eastern** as availability only. It is not bound or approved for execution. Do not rush past unresolved guards to use that block, silently extend it or revive a prior package. After local completion, bind/retest a fresh operation only if its exact approved cutoff remains attainable; otherwise obtain replacement availability.

**Rollback/disabled state:** new copy has no binding, approval, attempt or external authority; all live modes refuse. Abandoning it leaves live state unchanged. Original packages and receipts are preserved. No application/build/deployment, database/role/grant, IAM/secret, Stripe/destination, payment, booking, message, push or merge action is included.

**Observable finish:** a fresh disabled package passes the guard tests and no-action/refusal checks, with sanitized hashes/evidence and explicit remaining external gate. Only then present a fully bound exact external operation. The later runtime-ready result is not P08 payment or 3A acceptance.

## Owner decision required before implementation

Approve/refuse **Alternative 1 for local correction and testing only**. The current “proceed” instruction authorizes review/preparation, not this newly demonstrated controller repair. AGENTS.md requires explicit approval before substantial prerequisites or material task-list expansion, and prohibits treating a newly written plan as prior authority.

Progress remains **0/27 newly closed R1; 6/60 legacy; 4/8 walkthrough (1A/1B/2A/2B accepted); 0/13 intelligence**. **Proposed bounded prerequisite correction; not implemented or retrospectively approved.**

## Owner decision recorded before implementation

Debynyhan Banks answered **“Approve Alternative 1 for local correction and testing only”** to the exact question bound to proposal commit `08660742253351c2f2ebe15c5292e2c9ab1cf29d`. Implementation starts from backend `2c3ad5dbdbc599a8121539ed37e8d31e53542c5b` and governance `08660742253351c2f2ebe15c5292e2c9ab1cf29d`; pre-change frozen-baseline/consistency pass. This authorizes only the three local guards, fresh disabled copy and isolated tests described above. It grants no live action or allowance. The supplied 5:30–7:00 p.m. Eastern block is availability only.

## Approved local result

Fresh `/private/tmp/p07-repaired-runtime-readiness-20261022-guards1` implements only the approved deadline/signal/cleanup-readback corrections; unchanged original package and helpers retained. Plan `f3252875-1a8a-4c64-b642-254fdc30a620`; packet `6c91b550-78cf-4dd1-a93e-63d9a282e21e`; operation `abff0262-3504-4f92-b49d-5c5dea238cdb`. Sixty tests (36 existing plus 24 guard cases) pass before and after binding, including actual isolated PTY SIGINT/SIGTERM/repeated signals, terminal restoration, input/subprocess deadlines, concurrent reservation, false acknowledgments, recovery and truthful residuals. Syntax/private inventory/hashes/no-action pass; live modes refuse without exact approval. Backend evidence and reviewable source patches: `evidence/APP-013/p07-runtime-guards-20261022/README.md`.

Owner's 5:30–7:00 p.m. Eastern availability is locally bound with strict 5:45 cutoff, work through 6:30, containment through 6:50 and retirement by 5:30 p.m. October 23. Bound manifest `8320b0e5cc3f1600f763cbffe4621e6af95b277e88c9ba2461fd560436cf8860`; binding `8b1bd73d9f707c237f582735a0499183fc08073346f98d4d42abbe71242c7cd5`. No approval/attempt/mutation receipt or external action exists. Next decision: exact external operation `APP013_P07_RUNTIME_READINESS_GUARDS1_OPERATION_20261022.md`. No scope deviation from the approved local correction.

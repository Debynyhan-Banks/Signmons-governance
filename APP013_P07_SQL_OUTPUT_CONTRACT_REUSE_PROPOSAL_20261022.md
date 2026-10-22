# R1-W01 / APP-013 / 3A / P07 SQL output contract reuse proposal

Status: **demonstrated local SQL defects; correction not implemented; owner decision pending**.

## Traceability and exact demonstrated gaps

Approved section remains R1-W01 / APP-013/3A/P07. Existing acceptance is authentic matching same-job Sandbox settlement before the booking gate clears; repaired runtime readiness is its existing prerequisite, not another product feature/section. Source snapshots: backend `ff9b964c13383dbb107ca999f8ab7521ba86bc6c`, governance `0cd1d63454e0f010f3e15bb72cf76b1b8aea18db`. Tenant binding remains verified; this proposal does not repeat it.

Exact approved operation `abff0262-3504-4f92-b49d-5c5dea238cdb` reserved at 5:40:09 p.m. Eastern and stopped `P07_STOP_DATABASE_PREFLIGHT_OUTPUT_INVALID` before mutation. Role absent/zero sessions and all mutation flags false/empty; containment verified. Its source, manifest, approval and stop receipts remain immutable. Browser wizard was cancelled without submitting; no destination exists. Evidence: backend `evidence/APP-013/p07-guards1-database-output-stop-20261022.md`.

Two actual SQL-to-parser mismatches are demonstrated:

1. `db_preflight` concatenates PostgreSQL booleans into text, yielding `true`/`false`; its parser accepts `t`/`f`. Null concatenations can also omit entire rows. Existing mock tests supply the expected short strings instead of database-produced output.
2. `provision_database` role-attribute readback likewise concatenates booleans but compares with `t|f|f|f|f|f|f|6|t|0|0`. An exactly configured role therefore fails this next check after provisioning, even if the first parser is repaired alone.

Read-only source review enumerated all runtime `psql_admin` consumers: only these two parse boolean readbacks; fixture/ALTER output is ignored, and direct restricted-role identity/read uses strings/counts. Transient tests extracted both exact SQL expressions from the unchanged controller AST and executed them in the existing disposable local PostgreSQL fixture, Unix socket only, TCP disabled, synthetic data. Healthy preflight reproduced the same fixed invalid-output code; correctly configured synthetic role returned eleven fields but failed the expected short-form row. Both local clusters stopped and removed. No raw live query was retained or new live query performed, so additional live predicate drift remains unknown.

The already-tested total-output diagnostic in `/private/tmp/p07-read-only-diagnostic-total-output-20261021-prep1` emits tagged/null-safe `IDENTITY`, `JOB`, `TENANT` rows, explicit `0`/`1` flags, counts and an in-memory-only encoded account field. Its classifier succeeds on the same healthy synthetic state. That previously approved correction was not carried into the full runtime package; this omission and the mocked SQL rows are the demonstrated integration gap.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Reuse the proved preflight protocol and align role readback; test both actual SQL outputs | Completes the two existing interfaces without another helper/subsystem, app change or privilege expansion | Recommended |
| 2. Accept long boolean strings only in the first parser | Leaves null/missing-row ambiguity and the known later role readback failure | Reject |
| 3. Replay another diagnostic/full runtime operation unchanged or loosen preflight | Repeats known broken source or weakens existing gates | Reject |

## Finite section card for Alternative 1

**Source/reuse/files:** fresh private copy of consumed guards1 with new plan/packet/operation IDs. Reuse its completed deadline/SIGINT/SIGTERM/cleanup-readback guards and all existing runtime components. Reuse the corrected diagnostic SQL/classifier and existing disposable PostgreSQL test harness. Changes allowed only fresh `controller.py`, existing `test_controller.py`, one reused/adapted `test_postgres_contract.py`, plan/manifest/README and evidence/governance. Existing three Node helpers, role grant fixture, application source/image/schema/dependencies unchanged. No replacement runtime, UI or standalone diagnostic helper.

**Exact behavior/interfaces:** replace only preflight query/output parsing with the already-proved tagged/null-safe read-only protocol. Preserve exact database/admin/P07 absence/P06 closed-state/accepted tenant-job/deletion/payment/calendar/admission digest/unbound-policy/account format/hash/charges gates; explicit count failures cannot pass via nulls. Keep exact read-only transaction and ROLLBACK. Align only the existing role-attribute SQL/comparison to explicit stable flags, preserving no inheritance/elevation/memberships/ownership, limit6 and expiry no later than work end. Every false/missing/foreign/malformed value fails closed with fixed sanitized code. No grants or required predicates are relaxed.

**End-to-end boundaries:** exact tenant/job and Sandbox account hash remain the only targeted identities. Raw rows, decoded or encoded account identifiers, passwords/database URLs and exceptions remain process-memory only and cleared/discarded; receipts retain bounded status/count/equality only. Existing exclusive no-retry attempt, exact approval, ordinary/cleanup/retirement deadlines, hidden input and privacy remain. Query correction advances only qualification of the same job's isolated payment runtime, not payment acceptance.

**Finite checklist:** (1) integrate existing total-output preflight protocol and classifier; (2) stabilize role-attribute output/comparison; (3) execute actual unchanged/new SQL through real disposable PostgreSQL into the actual parsers, including healthy/negative/absent/null/malformed cases; (4) retain all 60 existing controller guard/permission/refusal/recovery acceptance cases, adjusting fixtures only to the proved output protocol; (5) source/patch/hash/private inventory/no-action/refusal and mandated repository checks. No unrelated prerequisite or feature expansion; stop and disclose anything outside these two interfaces.

**Tests/commands:** `python3 -B -m unittest -v test_controller.py test_postgres_contract.py`. Preflight: healthy, absent P06/job/tenant, null account/charges/policy fields, wrong job/state/deletion, payment/calendar activity, account mismatch and malformed/extra/missing rows. Role readback: correct attributes/limit/expiry; each elevation/inheritance/membership/ownership/limit/expiry failure and missing role. Positive tests must use actual PostgreSQL-produced output, never fabricated boolean rows; preserve regression showing consumed source fails healthy real output. Retain real signal/PTY restoration/deadline/concurrent reservation/recovery/no-retry tests. Syntax/no-action/private modes/manifests; run/recover/retire refuse without window/approval. Frozen-baseline, cross-repository consistency, 25 governance regressions, backend governance/architecture and both whitespace checks. Existing permissions proof remains separate; a synthetic role-readback test is not a claim of new live permissions or customer acceptance. No provider/browser/live database test is authorized by local approval.

**Dependencies/owners:** Debynyhan Banks approves/refuses this local-only correction; implementer prepares/tests after approval. Consumed source/receipts unchanged. The 5:30–7:00 p.m. operation has stopped and cannot be retried; its start cutoff has passed. A fresh attended block of at least 90 minutes and separately reviewed exact external-operation approval follow only after local completion. Do not silently extend or revive the old window, allowance or command.

**Rollback/disabled state/exclusions:** new copy has no binding, approval, attempt or external authority; discarding it leaves live state unchanged. No application build/deployment, database/role/grant, IAM/secret, Stripe destination/event, payment/refund, booking/message/customer, merge/push action or new allowance. No wider grants, accepted P06 credential change, new fee/routing or weakened gate.

**Observable finish:** fresh disabled package passes the retained controller cases and actual SQL/parser PostgreSQL regressions, with reviewable patches/hashes, verified fixture cleanup and no-window refusals. Only then prepare the next exact runtime-readiness operation. Final customer finish remains the unchanged 3A same-job Sandbox settlement and owner acceptance.

## Owner decision requested

Approve/refuse **Alternative 1 for local correction and testing of these two SQL/output interfaces only**. The previous approval covered three runtime guards and the one consumed external operation; it did not authorize this newly demonstrated SQL correction. AGENTS.md requires approval before changing substantial prerequisites or materially expanding the task list. No correction has been implemented.

Accepted 1A/1B/2A/2B and **0/27 newly closed R1; 6/60 legacy; 4/8 walkthrough; 0/13 intelligence** remain. **Proposed bounded prerequisite correction disclosed before implementation; no product-scope/acceptance change.**

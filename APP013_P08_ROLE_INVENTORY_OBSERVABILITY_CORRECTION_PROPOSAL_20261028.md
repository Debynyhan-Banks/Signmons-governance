# APP-013 / 3A / P08 — role-inventory observability correction proposal

Status: PROPOSAL ONLY. No implementation or external retry is authorized. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated gap and criterion

Consumed operation `83bdf433-98dd-45c9-8b42-fb90494219ce` returned `P08_ROLE_QUALIFIER_STOP_OUTPUT_UNKNOWN` with containment verified, but the tested controller persisted neither its safe reason code nor command progress on a stop. Exact custom-role facts remain unknown. This blocks the already-approved access-resolution decision without changing the 3A same-job Sandbox payment acceptance criterion.

## Alternatives

1. **Recommended — add sanitized stop evidence locally.** Reuse the existing qualifier and exact command inventory. Persist one atomic sanitized result on success or stop with status, allowlisted reason code, commands started/completed, last started/completed stage, private-input absence and providerMutationPossible=false. Preserve raw stderr/body suppression and all existing refusal/cleanup behavior.
2. Defer. Keep role facts unknown and 3A blocked.
3. Rerun unchanged or inspect raw provider logs. Reject: the attempt is consumed, and raw output/log recovery would exceed the approved retention contract.

## Bounded local card

Approved section would remain R1-W01 / APP-013 / 3A / P08. Source is backend `c51dd78`; immutable stop evidence is `eb8499c`; existing qualifier/restoration sources are reused.

Expected changes are limited to the fresh evidence-contained `role_qualifier.py`, `test_role_qualifier.py`, source manifest, logs/result/README. No repository application/runtime file or governance acceptance contract changes.

Finite checklist:

- tag only the three existing stages `OWNER_CHECK`, `PROJECT_CHECK`, `ROLE_LIST`;
- distinguish command started from completed so a timeout/unknown response is not reported as a completed read;
- allowlist saved stop reasons; unknown exception text becomes only its safe type, with no stderr/body/role-list payload;
- atomically save sanitized `result.json` on every controller return, including owner/project drift, command/JSON/classification failure, timeout, deadline and signal;
- complete private plan/approval purge first, then update result with verified absence; failure to prove absence cannot report clean closeout;
- retain one-attempt reservation, exact source/decision/approval bindings, three-command ceiling, native-unbound refusal, child cancellation and no retry;
- test success and every stage failure, raw-error suppression, interrupted/unknown commands, write failure, private purge, concurrent reservation and compatibility with unchanged restoration role checks;
- rerun source-manifest, architecture, governance baseline/consistency/safeguard and both whitespace checks. Browser/database tests remain inapplicable.

Rollback is deletion of only this fresh local correction/evidence. The consumed attempt/evidence remain immutable. No external command is included. After a passing result, a fresh exact read-only operation with a new operation ID/window requires separate approval.

## Decision requested

Approve Alternative 1 for this bounded local observability correction and isolated tests only, or defer. No Google Cloud read, IAM role/grant, Firebase action, signing/token, API-key action, database/runtime action, Stripe/payment, deployment, spending or external retry is authorized.

Accepted counts remain unchanged. **Explicit correction proposed after unintended observability drift; no correction implemented.**

## Owner decision

Debynyhan Banks replied “i approve” after reviewing governance commit `8e2c089`. Alternative 1 is approved for the bounded local observability correction and isolated tests only. No external retry, Google Cloud read, IAM role/grant, Firebase action, signing/token, API-key action, database/runtime action, Stripe/payment, deployment or spending is authorized.

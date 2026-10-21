# APP-013 / 3A / P07 diagnostic total-output correction proposal

Status: **owner decision pending; no implementation or external action authorized**.

## Demonstrated gap

The owner-approved read-only operation in `APP013_P07_READ_ONLY_DIAGNOSTIC_OPERATION_PROPOSAL_20261021.md` reserved before cutoff, passed sanitized Stripe Sandbox preflight and reached the database diagnostic. It stopped with `P07_DIAGNOSTIC_STOP_DATABASE_PREFLIGHT_OUTPUT_INVALID`; mandatory closeout returned `CONTAINMENT_VERIFIED`. Backend evidence: `evidence/APP-013/p07-read-only-diagnostic-stop-20261021.md`.

The controller expects exactly three already-normalized composite lines. Source inspection shows that the SQL is not total over the states the classifier is meant to diagnose:

- the P06-role scalar subquery can return SQL null when the role row is absent, nulling the composite identity line;
- job aggregates can produce null Boolean fields when the exact job relation is empty;
- the tenant query emits no row when the exact tenant row is absent;
- the parser treats these output shapes as malformed before reaching the intended fixed identity, role, job or tenant classifications.

The focused fixtures supplied normalized three-line strings directly to the parser. They did not execute the SQL against PostgreSQL with absent-row and null-producing states. The live stop demonstrates that this seam is material. Raw output remains deliberately unavailable, so this proposal does not claim which database-state predicate differs.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Make the diagnostic output total and execution-test it locally | In a fresh disabled package, emit exactly three tagged, null-safe rows for every allowed database state; map absence and nulls to fixed classifications; execute the SQL/parser contract against a disposable local PostgreSQL 16 database with synthetic data; retain no raw values. | **Recommended** |
| 2. Accept variable/malformed output in the existing parser | Risks mapping ambiguous row loss or null propagation to the wrong state and weakens the diagnostic. | Reject |
| 3. Persist or display raw live SQL output | Would expose private database/account state to diagnose a local output contract. | Reject |
| 4. Retry the consumed operation unchanged | Repeats a demonstrated parser failure and violates the no-retry boundary. | Reject |

## Exact proposed local change

Alternative 1 may change only a fresh private diagnostic controller, its tests/manifest/README and the normal evidence/governance records. It must preserve the consumed package and all receipts unchanged.

The corrected SQL/output contract must:

1. Return exactly three explicitly tagged rows in fixed order: identity/role, exact job/activity/policy and tenant/account.
2. Use aggregates and explicit `CASE`/`COALESCE` encodings so role, job or tenant absence cannot remove a row or create an ambiguous empty field.
3. Keep database/user names, counts, Booleans and the connected-account identifier in process memory only; persist and emit only the existing allowlisted classification.
4. Map exact absence separately from malformed output. Do not weaken database identity, closed P06-role, P07-role collision, exact-job, payment/calendar, admission-policy, account-format/hash or charges-enabled checks.
5. Retain `BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY`, `ROLLBACK`, `verify-full`, system roots, bounded timeouts, hidden input, one-attempt reservation, no retry and zero-session closeout.
6. Contain no role/grant, application/database mutation, secret/IAM, Stripe configuration, deployment, Checkout, payment, booking, message or customer-action path.
7. Separate preparation-state tests from consumed-receipt validation so immutable attempt/result/closeout receipts do not make the post-operation verification suite fail while absence remains required before reservation.

The local test must execute the real diagnostic SQL and parser against a disposable local PostgreSQL 16 database with synthetic schema/data for success, each absent-row/null boundary and malformed/tag/order cases. It must verify rollback, no retained private output, teardown and refusal of live use without a fresh window and exact approval. Mock-only parser tests remain useful but are insufficient for this seam.

## Requirement traceability

- Approved section: R1-W01 / APP-013/3A/P07.
- Acceptance criterion advanced: the same admitted job opens one authorized Sandbox Checkout and only an authentic signed event for its exact stored Stripe resource clears the payment gate.
- Demonstrated source/evidence: the consumed diagnostic stop and the private controller's composite SQL/parser contract.
- Customer-workflow connection: a trustworthy exact-job/tenant prerequisite is required before the disabled P07 runtime can be prepared for the payment step. This correction adds no product capability or acceptance credit.

## Dependencies, exclusions and finish

Owner approval of Alternative 1 is required before local implementation because the live result demonstrates a material prerequisite not covered by the previous correction. Approval would cover local disposable-database preparation/testing only. It would not authorize a live database connection, Stripe action, role/grant, secret/IAM action, deployment, Checkout, payment, booking, customer contact, merge or push.

Observable local finish: a fresh disabled package passes its execution-faithful PostgreSQL contract suite, focused parser/security/refusal tests, syntax/no-action verification and required governance/architecture/whitespace checks. Only after review would a fresh attended window and separate exact external-operation approval be considered.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Unintended controller-assumption drift disclosed; proposed correction only.**

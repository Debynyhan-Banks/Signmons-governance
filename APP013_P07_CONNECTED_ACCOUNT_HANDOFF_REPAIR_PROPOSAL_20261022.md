# APP-013 / 3A / P07 connected-account handoff repair proposal

Status: **Alternative 1 owner-approved for local preparation/testing; no external action authorized**.

## Demonstrated gap and unchanged criterion

- Section: R1-W01 / APP-013/3A/P07.
- Unchanged acceptance criterion: the accepted job opens one authorized Stripe Sandbox Checkout from its approved payment policy, and only an authentic signed event for its exact stored Stripe resource may clear the payment gate.
- Evidence: consumed operation `aff460dd-740b-40c4-8fcc-ea6dbc21057e` passed current Stripe Sandbox qualification, then stopped `P07_TENANT_BINDING_STOP_CONNECTED_ACCOUNT_HASH_MISMATCH` before database access.
- What the stop proves: both hidden entries matched and had valid `acct_...` format, but they were not the one enabled connected account qualified from the Stripe connected-accounts row.
- What remains unknown: raw hidden input was correctly not retained, so evidence cannot identify which other valid-format account ID was entered.
- Safety result: `possibleMutation:false`, `commitState:NOT_STARTED`, no mutation intent or transaction, zero operation sessions and verified containment.

The controller behaved correctly. The missing behavior is an unambiguous secret-safe transfer from the exact enabled connected-account row to the existing hidden controller prompts.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Fresh package plus attended in-memory handoff | Rebind the unchanged reviewed controller under fresh identifiers. During a later approved operation, read the ID only from the exact enabled connected-account row and type it twice directly into the waiting hidden Terminal prompts without chat, clipboard, file, command argument, log or receipt exposure. | **Recommended** |
| 2. Fresh package with clearer manual instructions | Tell the owner to distinguish the platform account from the connected account and manually re-enter it. This retains the same avoidable selection risk that consumed the first operation. | Reject |
| 3. Store the ID in a file/environment variable | Simplifies input but creates a persistent secret-handling surface and weakens the approved privacy boundary. | Reject |

## Exact proposed local preparation and tests

Alternative 1 authorizes local preparation/testing only:

1. create one fresh disabled private package with new plan, packet, operation and audit identifiers;
2. preserve the reviewed SQL, predicates, same-transaction audit, deadlines, recovery, no-retry behavior and private receipt formats unchanged;
3. preserve hidden owner entry of the current CHILD administrator password;
4. define a later attended handoff in which the automation reads the identifier only from the unique enabled connected-account row and types it directly into each existing hidden prompt;
5. retain the raw identifier only in volatile browser/controller process memory and SQL stdin, clearing the in-memory value immediately after the second entry;
6. forbid chat, clipboard, files, environment variables, command arguments, logs, exceptions, receipts, audit metadata and screenshots containing the raw identifier;
7. rerun the 14 focused controller cases and five disposable PostgreSQL cases, plus a static handoff-boundary check that requires the two existing hidden prompts and forbids any new persistence/input channel; and
8. require a fresh attended window and a separate exact external-operation proposal before browser or database access.

No application source, live database access, tenant mutation, role/grant, secret/IAM, Stripe configuration, destination, deployment, Checkout, payment, refund, booking, customer contact, message, merge or push is included.

## Impact and next gates

This does not add an MVP feature or change a criterion, dependency, section ID or denominator. It replaces an error-prone manual identifier selection inside the existing prerequisite operation. If approved and locally prepared, the next decision would still be one exact external operation with no retry. Successful tenant binding would still leave the disabled webhook destination, runtime readiness, P08 authentic Sandbox payment and 3A owner acceptance open.

## Decision requested

Debynyhan Banks approved **Alternative 1 for local preparation and testing only**. Approval authorizes only the fresh disabled package and finite checks above. It does not authorize browser access, the in-memory handoff, a database connection or mutation, any Stripe change, deployment or payment.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation; proposed procedural repair only.**

## Local implementation result

Fresh disabled package `/private/tmp/p07-tenant-stripe-binding-handoff-repair-20261022-prep1`, plan `0add40ae-f062-417f-8cab-aa7b7943f562`, packet `c1ba7f8c-8e93-4264-9551-02072df99f7e` and operation `bfc0bb5b-1564-4991-a446-3960caa67d49`, preserves the reviewed transaction and adds the exact attended in-memory handoff contract. Fourteen controller regressions, two handoff-boundary checks and five disposable PostgreSQL 16.11 cases pass. Syntax, exact inventory, private modes, manifest, no-action and both no-window refusals pass. Manifest SHA-256: `0f24d31b7dcb565fceb8396fe465ca297ae0685641725c403da006a6db36a55d`.

Backend evidence: `evidence/APP-013/p07-connected-account-handoff-repair-local-preparation-20261022.md`. No application or external state changed. The next input is an attended 45-minute Eastern block; exact binding/retest and a separate external-operation decision follow.

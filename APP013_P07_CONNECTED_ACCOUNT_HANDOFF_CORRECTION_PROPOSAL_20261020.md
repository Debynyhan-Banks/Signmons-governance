# APP-013 / 3A / P07 connected-account handoff correction proposal

Status: **owner decision pending; no implementation or external action authorized**.

## Demonstrated gap

Repair-2 operation `45ae622a-2cb7-4ab7-ae90-f94d30c9336a` passed corrected Cloud preflight and sanitized Stripe preflight, then stopped once at database preflight with `P07_STOP_CONNECTED_ACCOUNT_FORMAT`. The browser-scoped clipboard did not transfer a valid raw connected-account identifier into native Terminal. Receipts prove `possibleMutation:false`, empty mutation sets, proposed role absent/zero sessions and verified containment. The operation is consumed.

The controller currently asks the owner to paste a raw `acct_...` identifier and interpolates it into an administrator SQL predicate after only a format check. The identifier already exists in the tenant record, and Stripe preflight already retains its SHA-256. The cross-application paste is unnecessary, error-prone and creates an avoidable dynamic-SQL input surface.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Read, validate and hash the stored tenant identifier in memory | The bounded administrator preflight reads the exact tenant field, validates `acct_...`, hashes it against the sanitized Stripe receipt, verifies `chargesEnabled`, then discards it. No manual paste or SQL interpolation. | **Recommended** |
| 2. Ask the owner to copy the identifier manually from Stripe again | Keeps the clipboard/UI failure and user-error risk; still interpolates external input into SQL. | Reject |
| 3. Persist the raw identifier in a local receipt/file | Simplifies transfer but violates the approved secret/private-data minimization boundary. | Reject |

## Exact proposed local change

- Remove the connected-account hidden prompt and `account` argument from `db_preflight`.
- Use only fixed plan-bound job and tenant UUIDs in administrator SQL. Return the tenant's stored connected-account ID and `chargesEnabled` as a separate in-memory result line.
- Require exactly one tenant row, an `acct_[A-Za-z0-9]{8,}` value, `chargesEnabled=true`, and a SHA-256 match with `stripe-preflight.json`.
- Clear the raw value after comparison. Never display, log, persist or place it in an exception, command argument or receipt.
- Retain only the existing boolean `tenantAccountMatchesAndChargesEnabled:true` in `database-preflight.json`.
- Add tests for exact match, malformed/missing/extra tenant output, hash mismatch, charges disabled, absence of the prompt and absence of raw identifier persistence.
- Run all package, syntax, no-action/refusal, governance, architecture and whitespace checks.

No provider/database mutation, role/secret/IAM change, Stripe destination, deployment, payment, customer action, new section or denominator change is included. A fresh package with new IDs, window and exact external approval is required after local review. Neither consumed operation may be replayed.

## Decision requested

Approve or refuse Alternative 1 for local correction and testing only. Approval does not authorize another external attempt.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Proposed correction to unintended handoff drift; implementation pending owner approval.**

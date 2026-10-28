# APP-013 / 3A / P08 — CLI failure observability correction proposal

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated gap

Approved operation `ee86cf8f-078d-42da-a4bd-04b95909e32c` stopped on CLI call 4, the exact IAM service-state read, before any HTTPS or mutation request. The native adapter correctly discarded stderr and returned the sanitized reason `COMMAND_FAILED`, but it did not preserve a safe structured classification or the failed command stage. The stage can be reconstructed from the four-call count, yet the actual category—authorization, billing/service state, malformed invocation, transient transport or other—is unknown. Repeating the provider read without correcting this observability gap could consume another operation without explaining the blocker.

## Alternative 1 — recommended bounded local correction

Within the existing evidence helper only:

1. make the CLI adapter return a fixed command-stage identifier and one safe error category derived in memory from return code and tightly enumerated stderr indicators;
2. allow only `AUTH`, `PERMISSION_DENIED`, `BILLING_OR_SERVICE_DISABLED`, `NOT_FOUND`, `INVALID_ARGUMENT`, `TRANSPORT`, `TIMEOUT` or `UNKNOWN`; never retain raw stdout/stderr, account IDs, bearer values or provider bodies;
3. persist the failed stage and category in sanitized result evidence on every CLI stop;
4. preserve exact commands, six-CLI/seven-HTTPS ceilings, one attempt/no retry, private binding/purge, mutation gates and independent closeout unchanged;
5. prove the actual subprocess serialization and positive/error/unknown/privacy paths using fake subprocess/HTTP only, then run all repository gates.

No credential resolution, subprocess against gcloud, network/provider read, role create, IAM change, account/database/token/runtime/Stripe/payment action, spending or retry is included. A later external operation would require a fresh exact proposal and owner approval.

## Alternative 2 — stop

Keep the consumed result as `COMMAND_FAILED` and leave Stage A blocked.

Owner decision requested: approve Alternative 1 for bounded local correction and fake tests only, or choose Alternative 2. Accepted counts remain unchanged. **Demonstrated observability gap disclosed; no scope deviation implemented.**

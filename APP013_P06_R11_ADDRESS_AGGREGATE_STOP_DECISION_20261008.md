# APP-013 / 2B / P06-R11 — address-aggregate stop decision

## Decision status

Prepared for owner review; **no third live read is approved**. Both October 8 operations are consumed and must never be rerun.

## Exact result

Replacement plan `6c2d3098-0a93-46b2-b71e-d8f39b776167`, operation `11d2f708-7f7e-4b03-81b8-809e5ee4242c`, reserved at `2026-10-08T11:25:22.535Z` and stopped at `2026-10-08T11:25:38.289Z` at `ADDRESS_AGGREGATE`. Connection, database/role/PostgreSQL18 identity, repeatable-read read-only transaction, read-only-mode check and phone aggregate completed before that stage. The runner rolled back and closed. No result exists.

The saved stage combines address SQL execution and parsing. It does not prove whether SQL execution, returned shape or aggregate validation stopped. It establishes no current address totals and no current approval/role/session state. Phase B did not run, so no Cloud Run, registry or Twilio metadata was read.

## Local repair

The reader now splits address totals and invalid-row classification into separate parameterized queries and records four distinct stages: `ADDRESS_TOTALS_QUERY`, `ADDRESS_TOTALS_PARSE`, `ADDRESS_INVALID_QUERY`, and `ADDRESS_INVALID_PARSE`. State comparison is explicit text; signed held totals can be classified as invalid rather than becoming an unconfirmed parser stop. Full-reader tests cover every successful substage, negative invalid data and exact parse-stage failure. Fourteen focused tests pass.

## Alternatives

### Alternative 1 — one final replacement qualification

Approve one new 35-minute Eastern window. After approval, create one fresh identity/package using the split reader. It may complete Phase A and, only after a complete closed-runtime receipt, the original fixed provider/release Phase B. Any attempt or uncertainty consumes it. There is no automatic retry. A further unexpected stop ends this qualification path for owner review rather than generating another immediate attempt.

### Alternative 2 — pause

Preserve both consumed stops and verified credential recovery. Perform no new database, cloud or provider read.

## Exclusions and status

No new operation identity, package, window or read exists. No database write, hold/ceiling change, cleanup, provider transaction, message/code, build, IAM, secret, deployment, traffic/tag, migration, browser/customer or job action is authorized.

P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation.

# APP-013 / 3A / P07 mandatory closeout recovery proposal

Status: **owner decision pending; no helper or database action authorized**.

## Demonstrated gap

Consumed operation `bfc0bb5b-1564-4991-a446-3960caa67d49` stopped before database preflight or mutation because computer-use safety controls prohibit binding macOS Terminal for the approved direct in-memory account handoff. The raw account value was cleared and never entered Terminal.

The controller recorded `possibleMutation:false`, `commitState:NOT_STARTED` and `primaryStop:INTERRUPTED`. No mutation intent, commit, result or recovery receipt exists. Host inspection found no remaining controller or PostgreSQL client process. The controller's database-side zero-session query did not complete, so it truthfully returned `CONTAINMENT_UNCONFIRMED`.

The consumed operation cannot be retried. Mandatory closeout still requires an exact database-side zero-session readback.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Prepare a fresh closeout-only helper | Build and locally test a one-use helper that asks only for the current CHILD administrator password, executes only the existing read-only `pg_stat_activity` query for the consumed operation's application-name prefix, requires zero sessions, writes a private sanitized receipt and has no tenant-table, account-ID, mutation, provider or operation-retry path. Database use remains separately approval-gated. | **Recommended** |
| 2. Treat host process absence as full containment | Leaves the required database-side session state unknown and would weaken the mandatory closeout criterion. | Reject |
| 3. Rerun the consumed operation | Violates the no-retry boundary and reopens the failed handoff. | Reject |

## Exact proposed local preparation and tests

Alternative 1 may create one fresh mode-0700 package containing only a mode-0600 helper, tests, README, plan and manifest with new plan, packet and closeout-operation identifiers. The helper must:

1. refuse without a later exact window and owner approval;
2. require an interactive hidden current CHILD administrator password;
3. connect with TLS verification to the existing CHILD administrator database only;
4. execute only `BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY; SELECT count(*) FROM pg_stat_activity WHERE application_name LIKE 'signmons_p07_tenant_binding_bfc0bb5b%' AND pid<>pg_backend_pid(); ROLLBACK;`;
5. require exact output `0`, discard all raw database errors and write only a private fixed closeout receipt;
6. enforce a command deadline, signal handling, no retry and truthful `CONTAINMENT_UNCONFIRMED` on any failure; and
7. contain no tenant table, connected-account identifier, write SQL, Stripe/browser, provider, deployment or main-operation path.

Local tests must cover exact SQL and prefix, zero success, nonzero refusal, malformed output, password/TTY requirement, deadline/signal handling, sanitized errors, private exclusive receipt, exact approval and no-window/no-approval refusal. A disposable PostgreSQL case must prove the query detects a named competing session and returns zero after it closes.

No live database access, role/grant, tenant mutation, Stripe action, deployment, Checkout, payment, booking, messaging, merge or push is included in local preparation.

## Decision requested

Approve or refuse **Alternative 1 for local preparation and testing only**. A later exact read-only database closeout requires separate approval. This proposal does not authorize rerunning the consumed tenant-binding operation.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Unintended execution-channel drift disclosed; no scope or acceptance change.**

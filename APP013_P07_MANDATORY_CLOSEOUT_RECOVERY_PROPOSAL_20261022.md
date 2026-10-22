# APP-013 / 3A / P07 mandatory closeout recovery proposal

Status: **Alternative 1 approved for local preparation/testing; external database action remains unauthorized**.

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

Debynyhan Banks explicitly approved **Alternative 1 for local preparation and testing only**, adding: “lets ensure we log out the reason it fails.” Implement fixed, sanitized failure classifications and stage reporting without retaining raw database errors. A later exact read-only database closeout requires separate approval. This decision does not authorize rerunning the consumed tenant-binding operation.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Unintended execution-channel drift disclosed; no scope or acceptance change.**

## Local result

The approved local preparation is complete in `/private/tmp/p07-closeout-only-20261022-prep1`. Plan `76a8f82d-1d34-44e9-8a5f-0234c48b8052`, packet `6504f835-2c15-4268-bc5b-16c9ee8f6bb6`, closeout operation `0d2f9eca-c8e8-49b6-b3c5-182416164a90`. Manifest SHA-256: `bf50b94c8039827e530944c4fa7bad664c3d8279f6627a05687b833afcb7c117`.

Twenty-one helper tests and two disposable PostgreSQL 16.11 tests pass, including failure reason/stage privacy, hidden input and echo refusal, deadlines/signals, no retry, concurrent reservation and competing-session detection followed by zero-session readback. Syntax, inventory/private modes, manifest and no-action pass; run refuses without a window. Backend evidence: `evidence/APP-013/p07-closeout-only-local-preparation-20261022.md`.

No live database read or other external action occurred. The original failure reason remains unknown and original containment remains unconfirmed. Next input is a fresh attended Eastern block; exact binding/retest and separate read-only external approval follow. **No scope deviation from the approved local closeout recovery and failure reporting.**

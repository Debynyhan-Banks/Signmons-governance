# APP-013 / P06 R11 address capacity diagnostic

Status: exact operation and 5:30–6:00 PM Eastern window approved; private authorization installed; owner-operated execution pending.

The owner replied `yes o approve` to the exact diagnostic/window approval request. The helper returned `R11_ADDRESS_CAPACITY_CHECK_PASSED_NO_ACTION`; no attempt, connection or result exists. Preparation descriptions below are historical. No broader execution is authorized.

## Reviewable operation

Operation `98a32610-b621-4f1c-b92c-15e08b26b9ee` proposes one owner-operated hidden-input read-only PostgreSQL 18 connection during September 21, 2026, 5:30–6:00 PM Eastern (`21:30–22:00Z`). Reuse the fixed P06 database target and existing neondb_owner password. Verify exact database/user/major-version identity, begin repeatable-read READ ONLY, verify read-only mode, aggregate the fixed address account/tenant, roll back and close. Retain only counts, held-micro totals, invalid count, bounds, capacity booleans and sanitized classification. There is no provider call or authorization to raise a ceiling, release holds, reopen runtime LOGIN, create a job or retry.

Backend `6c7a762106ab1a099cdd0578ce3bce74bf1eeb00` binds the tested reader. Private directory `/Volumes/Signmons-P06/r11-address-capacity-diagnostic-20260921-1730` has exactly four mode-0600 preparation files (plan, hash binding, fixed caller and hidden-input wrapper) under a mode-0700 directory. No authorization, attempt or result exists. Consumed prior helpers were read only as templates and were not modified or invoked.

Validation: nine capacity tests and three existing hidden-input pseudo-terminal tests pass; syntax, exact window/authority fields, file inventory/modes, status allowlist and actual private no-action review pass. Result: `R11_ADDRESS_CAPACITY_PREPARED_NO_ACTION`. No database connection, SQL execution, provider or browser action occurred. A fake query client tests the aggregate reader; these checks are not a live SQL result.

After exact approval, install one authorization and run no-action check; owner runs the reviewed wrapper once in the approved window. Any stopped/unconfirmed operation is consumed. Database state must remain unchanged. Observable finish is `CAPACITY_AVAILABLE_OTHER_GATE`, `ACCOUNT_LIMIT_EXCEEDED`, or `ACCOUNT_AND_TENANT_LIMIT_EXCEEDED` (or explicit unconfirmed failure). The defensive projection also defines `TENANT_LIMIT_EXCEEDED`, although the fixed identical limits and subset relationship cannot ordinarily produce it.

## Section card

- Section/criterion: P06-R11 within APP-013/2B; one protected phone/address/reviewed-submit journey creates exactly one correlated job. Uncertain input does not create a job.
- Source: backend `a2c01b7b898c7e0f61ca8f7788f0020757025be8`, governance `ed36a97`; enabled19 private packet; `AddressOperationLedger.perform`; verified result in `evidence/APP-013/p06-r11-enabled19-address-stage-result.md`.
- Missing behavior: zero fixed-request aliases establish a pre-reservation stop; separate account and tenant address capacity has not been read. Phone capacity does not establish address capacity.
- Reuse: guarded fixed-target PostgreSQL 18 helper, private hidden-input wrapper, exclusive attempt marker, identity/read-only transaction and rollback. No production path change.
- Expected files/interfaces: inert `scripts/p06-r11-address-capacity-diagnostic.mjs` and focused test; private reviewed wrapper/plan/binding; local result evidence and governance status. Query client is supplied by the approved private caller only. Import and direct invocation cannot connect.
- Exact boundary: fixed address account `c8c98ce0-ea9c-4ab3-b8a3-1c2957061fd3`, fixed tenant `a1adcfd4-15be-404b-9ac3-5edb1fda20f0`. One read-only aggregate of AddressVerificationOperation produces only account/tenant counts, summed heldMicros, invalid-row count and capacity booleans/classification. No row identities, participants, provider content or proof are returned. All states count exactly as in the ledger; prior local Google holds are separate and not treated as database rows.
- Limits: consumed enabled19 policy cost 100000 micros per operation; account and tenant each two operations/200000 micros. This is comparison to the prior policy, not permission to spend or execute.
- Checklist: implement fixed SELECT and defensive projection; exercise zero/below/exact/over-limit, malformed/unsafe/negative data, identity/read-only refusal and query failures; prepare fresh one-use private caller with source/hash/window binding; review without authorization; request exact external approval; owner runs once; record result.
- Tests: `node --test scripts/p06-r11-address-capacity-diagnostic.test.mjs`; existing private-input pseudo-terminal tests; Node/Python syntax and private no-action review; architecture, frozen baseline, consistency, governance regression and whitespace checks. SQL classification tested through a fake query client: no live/disposable database or provider calls in preparation. Concurrency uses the existing exclusive attempt marker; failure consumes the operation, rollback/close is mandatory, and no retry is automatic. Browser testing is inapplicable to this diagnostic.
- Dependencies/owners: implementer prepares/tests; owner selects/approves the exact diagnostic window and enters the existing database-owner password locally. A result at read time is not a historical transaction trace. Available capacity leaves other reservation gates unresolved; exhausted capacity requires a separate policy decision, not automatic ceiling changes.
- Exclusions: no LOGIN change, activation, deployment, traffic/provider/browser action, code, database write, hold release, secret/IAM/billing change, new runtime packet or automatic retry.
- Finish/disabled state: one sanitized capacity classification after rollback, or explicit unconfirmed stop; no execution without authorization. P06 remains 12/14 with R11/full R12 open. No scope deviation.

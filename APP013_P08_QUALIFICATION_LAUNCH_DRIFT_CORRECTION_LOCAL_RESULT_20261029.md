# APP-013 / 3A / P08 — qualification launch drift correction local result

R1-W01 / APP-013 / 3A / P08. Owner approved Alternative 1 in `APP013_P08_QUALIFICATION_LAUNCH_DRIFT_CORRECTION_PROPOSAL_20261029.md` at proposal commit `f2c722d`; the decision is recorded at governance `9db37a4`. Backend evidence is committed at `d7c40c1` under `evidence/APP-013/p08-composed-qualification-local-20261029/`.

The approved correction is complete. The native launcher no longer converts a locked active-owner read into constant-true disabled-account facts. One repeatable-read statement now returns the exact job/tenant, human-review policy state, calendar absence, retired role/session state and exactly one disabled ADMIN selected by the designated tenant/mailbox. The ordered target record must match the retained October 26 ownership hash before its UUID can be held in memory for the one Firebase lookup. Missing, duplicate, foreign, active, wrong-role, changed-policy, calendar-present, role-present, session-present or ownership-mismatched facts cannot qualify.

Project number and linked billing account are discovered during the attempt and compared in memory to retained canonical fingerprints; neither is required in the private binding or written to evidence. Firebase custom claims are parsed as JSON and must equal tenant/admin/testOnly, while token revocation must be at or after the retained October 26 closeout bound. The local preparation hash and a future immutable operation-proposal hash are separate; the owner decision binds the latter. Exact `plan.json` and `binding.json` files must be private regular files in the operation directory and are deleted with per-file absence readback on every bound exit. Native remains unbound before credentials without those future exact inputs.

Verification passed:

- 30 focused fake-provider/model cases, including binding drift, missing/duplicate/foreign database rows, policy/calendar/role/session drift, Firebase claims and revocation, deadlines/signals, output limits, private-value absence, closeout isolation and bound-stop purge before any password prompt;
- three disposable socket-only PostgreSQL cases proving the actual repeatable-read projection, all listed negative row/state variants, read-only behavior and zero leftover sessions;
- unchanged role 26/26, restoration 37/37, access 40/40 and authentication 60/60 regressions;
- backend governance baseline, architecture and whitespace gates; governance frozen baseline, cross-repository consistency, all 25 safeguard tests and whitespace.

The disposable PostgreSQL tests required host shared memory. The unchanged authentication suite ran from a private no-space scratch copy because its URL pathname handling cannot resolve the checkout path containing spaces; all 60 cases passed and the scratch copy was deleted. These environment accommodations did not change locked sources or test expectations.

No credential was resolved. No Cloud, database, Firebase, Stripe or other provider read occurred. No database/provider/IAM/API/key/account/runtime/token/payment/deployment/billing/spending mutation occurred. No product source, schema, migration, section criterion, denominator, merge or push changed.

Next/owner: when ready, supply a fresh attended window for a newly prepared immutable read-only qualification operation. That future card must bind fresh operation IDs, exact source/plan hashes, the 26 CLI/10 HTTPS/two SQL ceilings, USD0, no retry, hidden CHILD database password, and mandatory closeout/purge. The prior 8:15 availability was never started and is not reused; this local approval grants no external authority.

Accepted 1A/1B/2A/2B remain 4/8. Newly closed R1 remains 0/27, legacy 6/60, intelligence 0/13. P08 and 3A remain open. **No scope deviation.**

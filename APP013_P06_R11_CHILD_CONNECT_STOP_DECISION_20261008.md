# APP-013 / 2B / P06-R11 — child connection stop decision

## Verified result

Owner-approved plan `5e961f29-504e-4809-bc4e-eb0e9cf65702`, operation `69001f5e-ac79-44e0-9fd8-fde92ab8a1ea`, reserved at `2026-10-08T11:50:46.743Z` and stopped at `DATABASE_CONNECT` at `2026-10-08T11:50:58.099Z`. The attempt and stop receipts exist; no result receipt exists. The operation is consumed and must never be rerun.

The fixed target was child branch `br-sparkling-sun-ay6gr5e8`, direct endpoint `ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech`, database/role `neondb` / `neondb_owner`. The runner rejected the production parent and pooled hosts before connection. No transaction or application query ran. Cloud Run, Artifact Registry, Twilio and browser work were not authorized or reached.

The sanitized stop stage does not distinguish password rejection, DNS, TLS, timeout, refused/reset connection or another connection error. It does not prove credential drift or endpoint failure.

## Proposed smallest diagnostic

Alternative 1 is one fresh child-only connection diagnostic in a future 15-minute Eastern window:

1. Bind a new plan/operation identity to the same child project, branch and direct endpoint; reject parent, pooled and override targets.
2. Accept the owner-saved child `neondb_owner` password only through hidden TTY-to-pipe input; never print, persist, log or place it in argv/environment.
3. Make exactly one TLS PostgreSQL connection attempt with five-second connection timeout and no automatic retry.
4. Execute no application SQL. On a successful authenticated connection, close immediately.
5. Persist only one sanitized category: `AUTH_ACCEPTED`, `PASSWORD_REJECTED`, `DNS`, `TLS`, `TIMEOUT`, `REFUSED_RESET` or `OTHER`, plus plan/operation/time. Never persist provider text, hostname supplied by an error, password, connection string or database rows.
6. Stop after the category. Even `AUTH_ACCEPTED` does not authorize a qualification rerun, Cloud/Twilio reads, release work or a journey.

Alternative 2 is pause. Any attempt or uncertain outcome consumes the diagnostic. A new qualification is a later separate decision.

## Gate and status

Owner approval of Alternative 1 plus a future 15-minute Eastern window is required before helper preparation or external connection. Excluded: password reset/trial against any other endpoint, secret access, SQL query, database write, migration, LOGIN change, cloud/provider read, build, IAM, deployment, traffic/tag, message, browser/customer/job/payment/appointment action.

Owner approved Alternative 1 for October 8, 8:10–8:25 a.m. Eastern. Fresh plan `a72ec2f2-3308-4a97-b532-3a3b4702d408`, operation `bc83b9bd-5dcd-4fe8-81f9-f836090a5390`, is prepared at `/private/tmp/r11-child-connect-diagnostic-20261008-0810`. Private modes, exact binding, six classification checks, formatting and no-action preflight pass; no marker or external connection exists. Invoke once during the fixed window and never rerun after any attempt or uncertainty.

The owner invoked it once. Attempt reserved at `2026-10-08T12:11:51.201Z`; result `AUTH_ACCEPTED` saved at `2026-10-08T12:12:05.075Z` with `sqlExecuted:false`. No stop exists. The diagnostic is consumed. Follow `APP013_P06_R11_CHILD_QUALIFICATION_AFTER_AUTH_DECISION_20261008.md`; no qualification package or read is authorized yet.

P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation.

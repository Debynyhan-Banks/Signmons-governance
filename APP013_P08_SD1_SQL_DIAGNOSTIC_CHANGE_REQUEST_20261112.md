# APP-013 / 3A / P08 — SD1 bounded SQL diagnosis proposal

PROPOSED ONLY. Owner requested investigation after R36 failure. Source backend63fea28; immutable r36-result.json establishes successful cloud owner/project checks, recovery SQL PROCESS_REFUSED and failed normal/independent session readbacks. Private purge/process closure verified; database sessions UNKNOWN. Owner reports same Neon password as R35; this is not proof of the bytes entered or an authentication failure. No raw stderr exists to recover the historical cause.

## Demonstrated gap and alternatives

Current qualification_launch.py NativeIO.sql uses exact pinned psql host/user/database/TLS options and NativeIO._owned_run. The latter sends stderr to DEVNULL except BD1's exact billing descriptor; any SQL nonzero exit becomes PROCESS_REFUSED. Existing RoleDiagnosticCapability/IO offers exclusive reservations, hidden password, three SQL slots and independent closeout, but the same opaque subprocess failure. Repeating recovery or role diagnosis cannot distinguish authentication, network/TLS, server refusal or query failure. Do not change credentials or relax TLS from this evidence.

Proposed small extension requires owner approval BEFORE implementation: add distinct SQL connection/session diagnostic within the existing role-diagnostic framework, with two read-only invocations of the existing CLOSEOUT_SQL (normal and independent). Inspected CLOSEOUT_SQL filters usename=p07_payment_runtime OR application_name LIKE signmons_p08_qualification_%, excluding only its own backend PID. Preserve that full existing filter for both probes. Add exact identity booleans; resulting descriptor is below. No tenant/customer/payment rows, private-ID recovery, cloud CLI/cache/SDK/provider API or writes. No terminate-backend, password reset, configuration change or automatic retry. A successful fresh diagnostic establishes current connection/session observation, never the cause of the historical R36 failure.

Alternative existing opaque diagnostic rejected as non-informative on failure. Alternative full recovery rejected as unrelated work and consumed attempt replay. Alternative raw stderr retained/copied into chat rejected. Alternative switch SQL client deferred; reuse installed pinned psql boundary.

## Section card and finite local scope

Approved section3A same-job Sandbox payment; exact criterion served is trustworthy prerequisite qualification and independent closure before connected execution. No new acceptance section or count. Source63fea28, current qualification_launch.py plus existing test_qualification_launch.py; reuse RoleDiagnosticCapability/IO lifecycle, existing exclusive marker/lock/deadline logic, hidden password, owned subprocess group, BD1 bounded simultaneous stdout/stderr draining and sanitized result conventions. Current manifests/dependent current native/correction source hashes only; immutable historical files unchanged.

Finite checklist after local approval: inspect pinned psql/libpq installed message contracts and existing CLOSEOUT_SQL/session filter; finalize exact two-read descriptor and identity/session output shape; implement distinct authority/mode and SQL-only transport allowlist; opt-in stderr classification solely for those descriptors; tests; refresh current dependency hashes; full affected qualification/native/connected/correction regressions and governance25/architecture/whitespace; record local readiness and prepare separate external diagnostic packet. If a trustworthy installed error contract cannot be established, retain SQL_ERROR_UNKNOWN; do not infer from arbitrary text. No local implementation or new external approval implied by this proposed card.

Classification must be conservative: exact supported authentication/connection/TLS/SQLSTATE evidence only, with a fixed safe enum; mixed, malformed, oversized, unsupported or ambiguous messages UNKNOWN. Never retain/hash/print raw stderr, host details from messages, password, SQL row bodies or arbitrary exception strings. Verify locale and verbose-output effects against actual installed source/interface; psql connection errors may lack SQLSTATE. Do not claim SQLSTATE is always available. Keep all existing SQL/BD1 behavior unchanged unless explicitly in the new mode. Error capture uses existing total byte/time bounds and pipe cleanup.

Tests through actual owned-child serialization boundary: successful exact identity/session booleans; false/missing/null/wrong-type fields; known and unknown/mixed error formats; secret sentinels absent; stdout/stderr saturation/output bound; timeout/interruption/parent death; two exclusive reservations and no replay; forbidden command/order/SQL/CLI/HTTPS/cache; independent process and session readback failure remain UNKNOWN; no credential retention. No browser requirement for local tests; later hidden input only in confirmed visible standalone Terminal. No real provider/database tests under local approval.

Readiness record before external approval must bind exact source SHA, installed psql/CA/runtime hashes, actual argv/env/SQL serialization/parser, identity/session filter, time windows, original R36 residual being reconciled, owner and cleanup deadlines. Local tests cannot establish credential correctness or current sessions. Primary and independent probes have separate reservations; failed primary must not suppress independent closure. Externally unavailable database means session closure remains UNKNOWN, never successful by zero process count.

Implementer owns local change/readiness/cleanup; owner approves this bounded extension then exact external diagnostic; database custodian owns external database/network/credential remedies. Disabled without fresh exact diagnostic authority. Rollback only local addition/current manifests, no external rollback. Excludes all Stripe/payment execution, new diagnostics subsystem and automatic further recovery. Observable local finish is accurate safe error category or explicit UNKNOWN and enforceable two-read/session closure interface; live diagnosis remains separate.

Impact: small extension of existing diagnostic task list; no dependency/order/section count/acceptance change. Additional focused implementation and regression work; no reliable live-resolution estimate because cause UNKNOWN. Earlier1A/1B/2A/2B remain accepted4/8;3A OPEN;R1newlyclosed0/27. Explicit deviation proposal; none implemented. Owner local decision pending.

## Exact proposed diagnostic query

Both reserved read-only probes use this same statement, pinned in the new mode; no user-provided query:

```sql
SELECT json_build_object(
 'databaseMatched',current_database()='neondb',
 'userMatched',current_user='neondb_owner',
 'sessionsAbsent',NOT EXISTS(SELECT 1 FROM pg_stat_activity
 WHERE (usename='p07_payment_runtime' OR application_name LIKE 'signmons_p08_qualification_%')
 AND pid<>pg_backend_pid()));
```

Output must have exactly these three Boolean keys; databaseMatched/userMatched must be true. sessionsAbsent=false means observed residual sessions, not permission to terminate them. The existing filter includes R36 qualification application names and runtime sessions. No session identifiers or rows retained.

## Owner decision

Owner explicitly approved: "I approve SD1 local implementation." Implementation and local tests authorized; no external database read or credential input authorized. Implementer will reuse versioned RoleDiagnosticCapability with a distinct SQL diagnostic kind and exactly two slots; existing versions remain unchanged.

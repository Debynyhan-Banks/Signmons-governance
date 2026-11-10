# APP-013 / 3A / P08 — TC1 exact selective TEMP correction

PENDING exact live owner/DB-owner/credential-custodian approval and attendance. Policy b04abb4 and concurrency guarantee0f5142f already approved;this packet binds their first live mutation. Local implementation d3d35f7 complete. Preparation only;no password prompt,SQL,permission change or root created.

## Exact timing,resource and authority

November10,2026 **8:00–8:20a.m.Eastern (EST)**. Start at8:00 or later and strictly before8:10;transaction/readEnd8:15;closeoutEnd8:20. UTC13:00/13:10/13:15/13:20. One attempt,no retry or extension. Owner stays at Terminal/chat throughout and maintains no concurrent user-controlled role/DDL/job maintenance on this CHILD during the window. This does not exclude provider/other administrator activity;approved residual concurrency limitation below applies.

Operation 4a768a38-27f1-469d-9132-8e71fff7eef8;scope 3330273473e3df3912fc37e2b179f5283912727c9fcb696c369124f7697d6b6f;backend d3d35f74526930e0e2ce9d5475d903444279afe1;manifest 2af12b08f0b2183d6a77246e2036c2a0644a1ffbfdc22ad72a8918f4542372d4. Exact packet APP013_P08_TEMP_CORRECTION_PACKET_TC1_20261110.json;canonical decision APP013_P08_DATABASE_ROLE_TEMP_CORRECTION_OPERATION_20261110.json currently PENDING_OWNER_APPROVAL/externalMutationAuthorized false. Version4 EXTERNAL_BOUNDED_MUTATION;old diagnostic/expired/consumed authorities cannot authorize TC1.

Fixed CHILD br-sparkling-sun-ay6gr5e8,endpoint ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech:5432/neondb;admin neondb_owner;target p07_payment_runtime. Exact psql/Python/CA bytes and snapshot/cleanup/protocol hashes in packet. Source pins live TI1 baseline (25roles,version180006,observed flags/effective TEMP/sources) and approved target administrative membership/full retired-role contract. Live drift rejects before writes.

## Only permitted privilege changes

One transaction,with before/after validation on the same connection:

```sql
GRANT TEMPORARY ON DATABASE neondb
  TO p06_intake_runtime,p06_migration_owner,p06_migration_runner,token_roles;
REVOKE TEMPORARY ON DATABASE neondb FROM PUBLIC RESTRICT;
```

Preserve existing provider/admin grants and all non-TEMP database ACLs. All eight approved retained/provider roles must keep TEMP;payment and16 pg_* roles must have TEMP false after correction. Four selective roles retain previously effective access;no claim of proven workload need. Future roles no longer receive PUBLIC TEMP automatically. No CASCADE,grant option,role/membership/LOGIN/password changes,other database,customer/job data,session termination,deployment,Google/Neon API,billing,real charges or payment test.

## Exact allowances and retention

Maximum3SQL connections,12SQL statements,2privilege statements;zeroCLI/HTTPS/cache provider operations. Fixed transaction10 statements:BEGIN,three SET LOCAL timeouts,DO cooperative advisory guard,prestate SELECT,GRANT,REVOKE,poststate SELECT,COMMIT. Normal cleanup SELECT1;fresh independent state/session SELECT1. Client echo framing is not SQL. Failures execute fewer statements. Uncommitted transaction is rolled back on disconnection;no automatic postcommit reversal statement exists. Exclusive operation root/lock and named reservations prevent replay.

Bounded retained checkpoint:normalized current-database pre/expected-post ACL entries (grantee/grantor/privilege/grantable,maximum256),plus sanitized status/identity/scope/cleanup receipts. Full SQL output and password transient. Existing snapshot validators bound roles256,TEMP grants64,sources64 per role and target role ACL512;actual baseline25 roles must match. No credential,session SQL text,PIDs,client addresses,private project identifiers or customer rows retained. Permission metadata retention is included in this exact approval.

## Readiness before live approval

At 2026-11-10T12:41:51.382597+00:00,actual RoleDiagnosticCapability validated committed source/dependencies/locked files,manifest,resource/protocol/runtime/CA pins and actual environment. Only proposed approval bytes and start clock injected in memory for readiness;no persisted authority or external call. Fresh root absent. Evidence APP013_P08_TEMP_CORRECTION_TC1_READINESS_20261110.json. Source local evidence at2026-11-10T12:38:37Z:249runtime+25governance PASS,owned servers reaped/scratch absent,providerCalls0. These are local facts,not current live state.

| Prerequisite | Inspected source/evidence and verification | Owner / unknown |
|---|---|---|
| Output/parsing/effective privileges | d3d35f7 correction snapshot,strict JSON,impact parser,shared full retired-role classifier;owned TLS positive/drift/rollback PASS | Implementer;current provider state UNKNOWN,checked inside transaction before mutation |
| Pins/config/identity/compatibility | Actual capability PASS at timestamp above;packet pins all three query/protocol hashes and psql/Python/CA bytes | Implementer repeats actual command/source/authority/runtime/time comparison before launch |
| Permissions | Non-superuser database-owner local proof PASS;fixed admin identity and full role precondition guards | DB owner/custodian;live password and usable privilege remain UNKNOWN until guarded entry |
| Deadline/concurrency | Start cutoff,absolute read/closeout deadlines,statement15s/lock5s/idle20s,cooperative advisory lock and root lock tested | Owner maintains quiet interval;other privileged writer exclusion is not guaranteed |
| Failure/recovery | Forced precommit rollback,lost acknowledgment,concurrent membership after final check,public crash/fresh read,no replay tests PASS | Implementer/custodian;uncertainty stops rather than triggering another write |
| Retention/cleanup | Validated bounded ACL checkpoint,transient raw/password,normal/fresh session read and owned-process cleanup | Owner approves metadata;interrupted cleanup can need hidden input again |
| Authority/attendance | Decision false;no launch or window authority yet | Exact owner/DB/custodian confirmation required |

## Execution and recovery checklist

1. Obtain exact TC1 approval/attendance/quiet-interval confirmation;commit decision and bind private envelope to that commit/hash.
2. Prepare existing source command: pinned Python -B qualification_launch.py --correct-temp <private-envelope.json>. Recheck actual source/resources/runtime/environment/authority/clock;do not launch outside window or on mismatch.
3. Owner enters SQL password at hidden prompt within120seconds/read deadline. Run once;never paste password into chat. Before mutation,guards must match baseline/full target role and observe no other database sessions.
4. Inspect result,normal cleanup and fresh independent PRESTATE/POSTSTATE/DRIFT/UNKNOWN. TEMP_CORRECTION_VERIFIED requires acknowledged COMMIT and exact independent post-state plus cleanup. It proves a bounded observation,not indefinite permission stability or payment acceptance.
5. Invoke pinned source --closeout-temp-correction /private/tmp/p08-temp-correction-4a768a38-27f1-469d-9132-8e71fff7eef8. Completed normal/fresh cleanup yields receipt-only public closeout,zero further SQL/password. Interrupted path may use only an unused independent slot before8:20 and may require hidden input again;process history remains UNKNOWN. No reserved-slot replay,no blind PID kill,no afterdeadline SQL.
6. Save sanitized result/closeout and reconcile status. A precommit detected failure aborts the uncommitted transaction. Lost COMMIT acknowledgment or failed/drifted/missing fresh readback means CORRECTION_UNCONFIRMED,no further writes/payment/full qualification. Postcommit correction may have applied;do not equate failure with rollback. Preserve evidence for DB-owner decision. No automatic reversal or reuse of TI1/TC1.

Approved concurrency limitation:provider/admin changes can commit after last transaction check;fresh read detects tested conflicts but cannot roll back a committed transaction or guarantee future state. Even a matching post-state after lost acknowledgment stays unconfirmed. Quiet interval is an operational condition,not automated global exclusion. Any subsequent rollback/mutation needs a separate exact state-bound decision.

Completed packet/readiness only. Remaining exact live approval,one correction/verification/closeout,then review whether existing qualification can proceed toward the same admitted-job Sandbox journey. No automatic downstream action. Browser N/A to catalog correction.3A OPEN;accepted1A/1B/2A/2B4/8;R1newlyclosed0/27. No scope deviation.

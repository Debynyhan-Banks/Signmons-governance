# APP-013 / 3A / P08 — PUBLIC TEMP impact qualification proposal

PROPOSAL ONLY. Owner approved proceeding with impact review after membership correction;new query scope and retention described here have not yet been approved. Base backendec7d913;governancee65f4a6. No runtime edits or external database access. Accepted milestone scope unchanged.

## Completed review and demonstrated gap

RP3 evidence7f57a41 confirms target p07_payment_runtime has effective TEMP solely through PUBLIC;explicit neondb_owner/neon_superuser TEMP entries exist. Prior source/execution records identify CHILD branch br-sparkling-sun-ay6gr5e8 and endpoint ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech/neondb. October3 governance APP013_P06_R11_UNMAPPED_SHARED_SECRET_REPLACEMENT_DECISION_20261003.md also records p06_migration_owner,p06_migration_runner,p06_intake_runtime on CHILD. October8 backend p06-r11-child-target-reconciliation-20261008.md confirms CHILD versus parent boundary. These are historical consumers,not current inventory or current execution authority.

Search of src,prisma,scripts for CREATE TEMP/TEMPORARY,pg_temp,temp_tablespaces found no application use;only scripts/verify-p07-payment-runtime-role.mjs explicitly tests denied CREATE TEMP TABLE. P06/P07 fixtures grant specific persistent-object privileges,not TEMP. Static absence is not proof about provider tooling,dynamic SQL,untracked consumers or future roles. Do not infer that CHILD is disposable or unused. The October28 P08 role inventory is Google IAM,not a PostgreSQL consumer inventory,and cannot answer this question.

[PostgreSQL18 REVOKE](https://www.postgresql.org/docs/18/sql-revoke.html) describes PUBLIC as all roles and additive privileges. [Privileges](https://www.postgresql.org/docs/18/ddl-priv.html) identifies database TEMP's default PUBLIC grant. Removing target direct grants cannot remove PUBLIC access. Existing explicit grants would remain if only PUBLIC TEMP were revoked,but other roles relying on PUBLIC could lose access. Actual affected set and intended preserved access remain UNKNOWN.

## Recommended bounded extension and alternatives

Use the existing SQL diagnostic lifecycle for one TEMP-impact mode,not a new subsystem or another full qualification run. Proposed commands --diagnose-temp-impact and --closeout-temp-impact in qualification_launch.py,with distinct authority/query/source/resource pins,operation root and fixed3SQL slots. Reuse NativeIO,RoleDiagnosticCapability/IO,strict JSON,hidden input,exclusive no-retry reservations and public closeout. Exact mode/decision naming must prevent old role/provenance approvals from authorizing this expanded inventory.

One READ ONLY REPEATABLE READ catalog query for fixed CHILD/neondb/admin:database owner/version/current TEMP ACL,then bounded role rows with role name,LOGIN/superuser flags,effective CONNECT,current effective TEMP,whether TEMP remains via non-PUBLIC direct/inherited grants,and aggregated session count on this database. Use server pg_has_role USAGE and ACL expansion with null/default handling;do not guess inheritance from direct membership. Include relevant non-PUBLIC grant-source names for each role to make projections reviewable. Cover NOLOGIN/group/provider roles too;do not equate LOGIN false with no impact. Administrative membership exception remains unchanged.

This is a counterfactual privilege projection,not proof of workload need or a grant recommendation. A role is affected when current TEMP true and projected non-PUBLIC TEMP false. Unexpected/missing identity,metadata/null/type/version/unexplained effective results,oversize or truncated lists remain UNKNOWN;no retry. Existing transport cap unchanged. Proposed cap256 role rows,64 TEMP ACL entries,and64 source names per role;query returns a sentinel row beyond each cap to detect overflow. Scope includes role metadata on this branch because roles are cluster-wide,while privileges/session counts are for this database only. No customer tables,session query text,PIDs,client addresses,passwords,secret values,Google or Neon API access.

Retain only validated bounded administrative role names/flags/grant-source names and aggregate session counts in governed receipts. Raw SQL output/password transient. This expands retained metadata beyond RP3 and needs explicit owner approval. No automatic preservation list,no blanket regrant to all login roles,no other database inventory.

Alternatives:owner supplies a complete authoritative current consumer/policy inventory;or defer correction. Immediate PUBLIC revoke,waiving noTEMP,granting TEMP to every other role,or creating a replacement database are not justified by current evidence.

## Complete local implementation card

Section APP-013/3A/P08;exact acceptance for this extension:accurate bounded affected-role projection with normal/fresh independent cleanup,or explicit UNKNOWN. It advances the existing same-job Sandbox prerequisite without changing its payment acceptance criteria. Sourceec7d913;reuse current provenance mode and owned PostgreSQL/TLS fixture. Expected files only existing qualification_launch.py,test_qualification_launch.py,test_qualification_launch_postgres.py,source-manifest.json and evidence/governance cards. No locked legacy source or approved membership/TEMP criterion changes.

Finite checklist:
1. Add distinct TEMP-impact capability/command/query pins in existing module,3SQL/0CLI/0HTTPS/0cache,unchanged hidden-input/deadline/cleanup controls.
2. Validate exact output schemas and complete limits;classify affected/protected/unknown without selecting grants or claiming workload need;always candidate null/executionReady false.
3. Actual PostgreSQL/TLS tests:PUBLIC-only,direct,inherited/multihop/INHERIT false,superuser,NOLOGIN group,explicit owner grant and owner ordinary TEMP revoked,null/default ACL,role absence/newrole,CONNECT false,aggregate session visibility,unsupported version and incomplete metadata. Strict native-byte JSON/type/null/duplicates/control-name/overflow/transport-cap cases.
4. Distinct-authority/old-command refusal,source/resource drift,concurrent one-attempt,cutoff,timeout/interruptions/hard crash,unused independent cleanup and no replay;preserve original mode/full qualifier behavior.
5. Run affected complete current suite plus25governance,architecture,baseline/consistency/whitespace;record source/query hashes and cleanup. Browser N/A:catalog diagnostic only.

Readiness before live scheduling:existing lifecycle/interfaces inspected,prior399tests historical PASS;new query/projection/retention/authority tests NOT IMPLEMENTED. Current live inventory,credential usability,TEMP consumers and concurrency state UNKNOWN. No live packet/window may be requested until local checklist passes. Separate exact live approval then authorizes at most one catalog read plus two cleanup reads;its result informs DB-owner policy review. Nothing here authorizes a permission mutation.

Rollback/disabled:without distinct committed approval mode refuses;consumed operation never replays. No database state change to roll back. Hard-crash history stays UNKNOWN even if independent sessions absent. DB owner owns intended consumer access;implementer owns source/readiness/metadata interpretation;credential custodian owns hidden input. Existing source manifests repinned only for approved implementation;frozen baseline remains untouched.

Observable finish:local tested inventory capability,then separately approved live projection and cleanup. After results,prepare exact grants-if-needed plus PUBLIC TEMP revoke in a separately approved transaction with preconditions,concurrency bounds,readbacks and rollback;do not preselect grants now. No parent/production connection,no migration,deployment,payment,credential reset or full qualification retry.

Completed this turn:retained-source/public-documentation impact review and concrete extension card. Remaining owner decision on this bounded local implementation and expanded administrative metadata;live read/correction separate.3A OPEN;accepted1A/1B/2A/2B4/8;R1newlyclosed0/27. Explicit deviation proposal before implementation:one TEMP-impact query/mode in existing diagnostic with bounded broader metadata. No deviation implemented.

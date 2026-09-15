# R02 external qualification packet — NOT executable

## Current: owner-authorized metadata inspection completed

Owner said continue following the metadata-only request. Backend evidence/APP-013/p06-r02-source-metadata.md records actual child SQL-console results, all13 matching migration checksums, exact23-table/34-enum inventory, managed ownership/default ACLs, zero observed other sessions and current tagged-consumer/quota readback. No schema, credentials or data changed. Do not ask to approve this completed metadata inspection again.

Source PostgreSQL18.6/UTF8/C.UTF-8,11,165,696bytes; public functions0, extension plpgsql1.0 owned by cloud_admin. Public schema pg_database_owner with PUBLIC USAGE; inherited neondb_owner has broad Neon membership. The two cloud_admin default ACL entries granting neon_superuser rights must be accounted for in restore qualification, not silently dropped. No managed role grants to the proposed runner.

Current quota display1.84/100CUh,0.04/0.5GB,0/5GBnetwork,2/10branches is delayed telemetry, not a billing guarantee. Known consumers remain shared-secret references; no payload read today. Exact secure delivery, restoration of managed ACL metadata, ownership-change order/rollback, measured run capacity, mount permissions and UTC execution/expiry are still final packet fields. These are existing requirements, not additional P06 tasks. Next finalize the consolidated execution proposal; do not execute while fields remain unresolved.

Local qualification passed per backend p06-r02-local-qualification.md. This packet is the consolidated output, not permission to perform external actions. The missing source facts below prevent a truthful final credential/export approval request. No migration authority.

## Fixed target and permitted direction

Project soft-smoke-54063480; child br-sparkling-sun-ay6gr5e8; direct ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech; neondb/public. Never parent, pooled/shared application connection or shared DATABASE_URL. Owner Debynyhan. Existing private logical-backup direction retained. No new root, paid snapshot or cloud resource.

## Next source inspection — metadata only, requires owner authorization

Use authenticated child SQL console without reading/resetting a password or creating a role. Verify selected child first. Read-only transaction; no customer rows or role password hashes:

```sql
BEGIN READ ONLY;
SET LOCAL statement_timeout = '10s';
SELECT current_database(), current_user, version(), pg_database_size(current_database());
SELECT datname, pg_encoding_to_char(encoding), datcollate, datctype
FROM pg_database WHERE datname=current_database();
SELECT migration_name, checksum, finished_at IS NOT NULL AS finished,
       rolled_back_at IS NOT NULL AS rolled_back
FROM public._prisma_migrations ORDER BY migration_name;
SELECT n.nspname, c.relname, c.relkind, pg_get_userbyid(c.relowner) AS owner,
       c.relacl, c.relrowsecurity, c.relforcerowsecurity
FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
WHERE n.nspname='public' ORDER BY c.relname;
SELECT t.typname, t.typtype, pg_get_userbyid(t.typowner) AS owner
FROM pg_type t JOIN pg_namespace n ON n.oid=t.typnamespace
WHERE n.nspname='public' AND t.typtype='e' ORDER BY t.typname;
SELECT p.oid::regprocedure, pg_get_userbyid(p.proowner) AS owner,
       p.prosecdef, p.proacl
FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace
WHERE n.nspname='public' ORDER BY p.oid::regprocedure::text;
SELECT extname, extversion, pg_get_userbyid(extowner) AS owner FROM pg_extension;
SELECT rolname, rolsuper, rolcreatedb, rolcreaterole, rolreplication, rolbypassrls
FROM pg_roles ORDER BY rolname;
SELECT pg_get_userbyid(roleid) AS granted_role,
       pg_get_userbyid(member) AS member, admin_option
FROM pg_auth_members;
SELECT usename, application_name, state, count(*)
FROM pg_stat_activity WHERE datname=current_database() AND pid<>pg_backend_pid()
GROUP BY usename, application_name, state;
ROLLBACK;
```

No query text, addresses, phone numbers or table rows collected. Session statistics alone cannot prove no future writers. Pair with current consumer/configuration references and no authorized child application attachment. Refresh Neon quota/compute and local free space without changing settings. Query failure is a stop, not authority to repair schema/permissions.

## Tested credential design to finalize against inventory

Propose SQL-created child-only p06_migration_owner NOLOGIN and p06_migration_runner LOGIN, both NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS. Never grant inherited neondb_owner/neon_superuser membership. Local fixture demonstrates explicit ownership of app tables/enums/functions plus schema USAGE/CREATE, runner owner-membership and migration-history access suffices. It does not establish provider permission to transfer actual objects.

Produce an exact allowlisted ALTER OWNER manifest from inspected source objects, preserving application access and recording old owner/ACL. Do not run broad REASSIGN OWNED or modify extension/system objects. New migration objects may be owned by runner; explicit post-migration ownership/revocation must account for this before approving changes. Owner-role access permits data writes; label it migration access, not least-privilege read access.

This is a proposal, not final executable SQL: actual object manifest, managed-role authority, existing reader grants, secure password-entry/delivery, role expiry and ownership rollback must be filled and reviewed. If ownership changes would break an existing consumer, stop and disclose rather than grant broader roles.

## One backup/restore envelope to finalize

Only after exact approval: one full child pg_dump custom archive, one private empty local restore with matched encoding/locale and explicit role/extension mapping. Keep archive, restore cluster, logs and temporary files inside existing encrypted image. No --no-owner/--no-acl shortcut represented as equivalent preservation. Compare actual full table contents privately (sanitized outcomes only), history, catalog, ownership/ACL and required behavior.

Before approval fill: source byte estimate, expanded restore/headroom, actual available capacity, current quota/cost cap, exact source credential, ownership-enabled mount/private access procedure, UTC start/end and seven-day absolute retention deadline. Existing volume is2GB decimal, not2GiB. No silent resize; stop if full restore cannot fit. Propose20minute overall deadline and one attempt, subject to measured sizing; no retry or deletion to hide failure.

Success produces usable checkpoint checksum, target identity, full restore comparison, owner and expiry. Failure preserves evidence inside locked image and reports smallest decision. Cleanup stops local database, revokes only approved temporary access, locks image; expired recovery cannot authorize migration.

## Next approval, not repeated micro-approvals

Smallest remaining authorization: the metadata-only child inspection above and current consumer/quota readback, with no credentials or data changes. Then present one completed credential/private-backup packet for review. Do not ask for blanket execution while SQL, size, security or cost fields remain unknown. R03 remains the subsequent migration gate. This is within the existing R02 source-qualification requirement, not a new task.

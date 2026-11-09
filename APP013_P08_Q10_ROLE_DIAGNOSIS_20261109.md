# APP-013 / 3A / P08 — Q10 database-role diagnosis from retained evidence

Review authorized by owner proceed after9612f7d hold. Runtime sourcef939224;Q10 receipt2698ce0. No code, credential, provider/database read or role change. No new attempt/window.

## What evidence establishes

Q10 reached database stage and returned ROLE_NOT_READY,27CLI/19HTTPS/4SQL/1cache reservations,empty cleanup residuals. Existing successful normal and independent cleanup consume two SQL reservations;the other two correspond to qualification projection and retired_role query in fixed source order. This supports having passed initial roleCount==1/target binding and reached retired-role classification. Reservations alone are not successful responses, but ROLE_NOT_READY is a semantic comparator result rather than a transport exception. The later role-count check could still fail if the role changed between transactions. Do not assert a particular flag or rule out concurrent change.

CurrentAdapter.read_database reuses access_check.classify_retired_role. After exact types/identity, ROLE_NOT_READY aggregates count1,login false,limit0,finite expired validity,unsafe false,memberships0,owned0,sessions0,schemaCreate false,databaseTemp false. ACL comparison occurs afterward. Thus Q10 is not evidence of direct ACL drift, nor does it establish ACL correctness. Firebase was not reached. No raw role observation was retained;the exact predicate cannot be reconstructed from these receipts.

## Concrete environment difference found

- scripts/verify-p07-payment-runtime-role.mjs:209,224 explicitly removes database PUBLIC privileges and schema PUBLIC CREATE in its owned disposable database.
- evidence/APP-013/p08-narrow-access-check-local-20261101/source/test_retired_role_postgres.py:45 similarly revokes ALL database privileges and schema CREATE from PUBLIC before each test.
- The same test file test_05 proves PUBLIC CREATE/TEMP can produce ROLE_NOT_READY while the role's direct ACL rows remain unchanged. This is existing local evidence,not a newly executed test or a live finding.
- Inspected historical provision_database in p08-restoration-local-20261028/source/legacy/controller.py:428–431 applies the role fixture and direct CONNECT grant;it does not perform those PUBLIC revocations. The inspected fixture creates NOLOGIN/NOINHERIT and direct relation/column grants,not database PUBLIC policy.
- p07-overdue-retirement-local-20261023/db-closeout.mjs changes login,connection limit,expiry and terminates role sessions only. Its CLOSED predicate and October22/23 role-closeout receipts establish those narrower historical conditions,not current privileges/memberships/ownership or effective PUBLIC rights.

Conclusion: effective PUBLIC CREATE/TEMP is a specific plausible explanation and an environment prerequisite that local tests explicitly arranged. It is NOT proven to be Q10's cause;other live changes remain possible. Historical closeout cannot be used as full current qualification. No automatic REVOKE FROM PUBLIC:that could affect other database users. Do not weaken the required denied privileges or count local setup as live readiness.

## Smallest responsible next decision

Keep full qualification/recovery on hold. A database owner must obtain one fresh read-only observation of the fixed role's readiness predicates using the existing retired_role_query and classifier,with a safe per-predicate pass/fail result. No project-number/target UUID is needed to diagnose this fixed database role;no Google SDK/cache/Firebase or full customer/job projection should be part of that diagnosis. Existing role query also reads ACL metadata,so an exact live proposal must disclose that or explicitly approve a narrower projection;do not silently substitute a new query.

The current public full-qualification entry point cannot run this SQL-only task under its existing authority. Therefore this document is diagnosis/recommendation only,not an executable packet or permission to build another helper. Before any new action,prepare a concrete SQL-only execution/cleanup method through existing interfaces and the smallest necessary owner decision. If a helper change is required,identify exact files/acceptance/tests first;do not implement it under this review approval. Preserve one-attempt,verify-full TLS,statement/lock deadlines,hidden credential handling,independent cleanup and no raw-secret persistence. Any observed PUBLIC issue requires impact assessment of affected roles before a separately approved change;no immediate fix inferred.

Completed: fixed-source classifier trace,SQL sequence inference,comparison of actual local setup with inspected historical provisioning/retirement,old receipt limitations. Remaining:current specific failed predicate UNKNOWN;DB owner observation/decision;then correction only if supported. Implementer owns bounded actionable method;DB owner owns state changes. Next observable result should identify the failed predicate,not another aggregate CURRENT_EVIDENCE_UNQUALIFIED. Existing Q10/R18 cleanup/purge verified;no password needed now.3A OPEN;accepted1A/1B/2A/2B4/8;R1newlyclosed0/27. No scope deviation.

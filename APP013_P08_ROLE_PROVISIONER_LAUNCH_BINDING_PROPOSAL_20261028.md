# APP-013 / 3A / P08 — stable exact-role provisioner launch-binding proposal

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated remaining gap

Backend `81026c8` passes the approved local lifecycle model but intentionally refuses native execution. No provider credentials/network adapter, exact private plan/approval/window binding or real permission probe exists. The earlier successful nine-permission caller probe did not request `iam.roles.create`, `iam.roles.get` or `iam.serviceAccounts.getIamPolicy`; `resourcemanager.projects.getIamPolicy` was established then but must be freshly bound to the future operation. Role creation cannot be proposed for execution until these interfaces and gates exist and pass locally.

## Alternative 1 — recommended bounded local completion

Complete the existing evidence-only helper, without touching product source, as follows:

1. add private mode-0600 plan/approval input and source/proposal/operation/window/deadline binding; ordinary native entrypoints remain refused without both files;
2. add a no-retry native adapter using existing owner gcloud authorization only after binding;
3. serialize exactly six CLI calls: owner, project, memory-only OAuth bearer, IAM service state, project policy, dedicated service-account policy;
4. serialize exactly seven HTTPS calls: one caller-project `testIamPermissions` request for `iam.roles.create`, `iam.roles.get`, `resourcemanager.projects.getIamPolicy` and `iam.serviceAccounts.getIamPolicy`; two exact-ID IAM Role GETs accepting only 404 as absence; two exact Role create POSTs with fixed bodies; two exact readback GETs;
5. require all four permissions, IAM API enabled, both exact IDs absent and unchanged source/plan/window before either create POST;
6. retain bearer and raw response/error bodies only in process memory; save fixed stages, HTTP status classifications, definition hashes, counts and ownership state only;
7. preserve one-attempt/no-retry, collision refusal, no update/undelete/delete, exact 13-call ceiling, signals/deadlines/concurrency, partial/lost-response journal and independent read-only closeout;
8. test exact URLs/methods/headers/bodies/CLI vectors and all positive, denial, collision, malformed, partial, lost-response, signal, cutoff, cleanup and privacy cases using fake subprocess/HTTP only;
9. run isolated tests and required repository gates.

The later external operation must be separately proposed and approved with a fresh ID/window. It may create at most the two fixed roles only after the read-only prerequisites pass in the same attempt. It does not add bindings. Role retention is the already approved stable-unbound model.

## Alternative 2 — stop

Keep the helper disabled and Stage A blocked.

## Scope and decision

Expected changes remain inside `evidence/APP-013/p08-exact-role-provisioning-local-20261028/`: helper, tests, manifest and sanitized local result. No `src/`, UI, schema, migration, package, runtime, provider, role, policy, credential, database, token, Stripe/payment, deployment, spending, merge or push action is included.

Owner decision requested: approve Alternative 1 for bounded local launch-binding completion and fake tests only, or choose Alternative 2. Accepted counts remain unchanged. **No scope deviation; operational binding remains unimplemented pending approval.**

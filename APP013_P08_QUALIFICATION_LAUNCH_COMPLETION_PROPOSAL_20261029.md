# APP-013 / 3A / P08 — qualification launch completion proposal

Status: PROPOSED; owner decision required before local implementation. Backend source `3eac627`; governance source `6f3d088`. This is local launch-binding completion only. It authorizes no credential resolution, external read, database/Firebase/provider action, IAM/API/key/account/runtime/token/Stripe/payment action, spending or attended window.

## Demonstrated gap and unchanged acceptance

Section remains R1-W01 / APP-013 / 3A / P08 under the unchanged same-job Sandbox payment acceptance criterion. Backend `3eac627` proves the strict five-domain qualification state machine, but its native entry deliberately returns `P08_COMPOSED_QUALIFICATION_REFUSED_UNBOUND`. It contains no subprocess, OAuth, HTTPS or PostgreSQL adapter and cannot execute an attended read. The result handoff initially said to prepare the exact operation; source inspection shows one launch-binding prerequisite remains. No command will be presented until this gap is completed and tested.

This is not a new product capability or acceptance section. It binds existing read seams to the already-approved qualification contract. Counts, order, scope and payment behavior remain unchanged.

## Alternatives and recommendation

1. **Recommended — bounded local read-only launch completion.** Add native plan/approval/source/window gates plus exact read-only gcloud/HTTPS/psql/Firebase adapters to the fresh qualification evidence source. Test every serialized command and response with fakes. Native remains unlaunchable without a future exact private plan and owner approval.
2. Run old independently pinned helpers. They are consumed, time-incompatible and cannot produce one aggregate verdict; not recommended.
3. Defer. No external read or mutation occurs.

Alternative 1 is a material operational prerequisite and requires owner approval before implementation.

## Exact local implementation boundary

Modify only `evidence/APP-013/p08-composed-qualification-local-20261029/` in a fresh source version or append-only launch files. Preserve the accepted classifier/state-machine semantics and all locked source hashes. Do not modify backend product source, UI, schema/migrations, packages, historical evidence or the unrelated backend `AGENTS.md` change.

Prepare exact read-only adapters with these maximum ceilings:

- **26 CLI calls:** owner/config checks, project/billing metadata, Cloud Run service/revision, dedicated identity, six exact secret-version states, seven exact secret policies, project/identity policies, two exact role definitions and one OAuth access token. Every command uses fixed executable, project/account/region/resource and JSON projection; no shell, wildcard, list-all or mutation command.
- **10 HTTPS requests:** six exact Service Usage state GETs, project and service-account permission tests, prospective exact key GET and exact Firebase account lookup. Bearer stays in process memory; 404 is key absence only for the exact resource. No key-string, signBlob, token exchange, account update or API enable request.
- **Two PostgreSQL statements:** one exact repeatable-read read-only qualification statement and one exact read-only session-closeout statement through hidden stdin password, verified TLS, cleared inherited `PG*`/`DATABASE_URL`, strict timeout and fixed application name.

The native launcher must verify source/proposal/plan/approval hashes, one UUID operation and prospective-operation ID, exact inventory, <=60-minute window, one attempt/no retry, USD0 and private file modes before resolving credentials. Owner OAuth token and database password are never arguments, environment files, output or evidence. Raw project number, policies, environment values, database/Firebase rows and provider errors are reduced in memory to the accepted strict domain shapes.

Native closeout-only mode accepts only the exact journal/plan, closes database and child processes, purges private plan/approval/derived metadata, and cannot resume Cloud/Firebase/database qualification. SIGINT/SIGTERM and deadline paths must invoke closeout. No API enablement exists.

## Finite tests and finish

- [ ] Exact 26 CLI/10 HTTPS/two SQL serialization, call counting and no mutation verbs/endpoints.
- [ ] Positive fake end-to-end classification and native unbound refusal before credential/config reads.
- [ ] Owner/override/project/billing, Cloud Run, identity, secret, policy, role, service, permission, key-absence, database/job/operator/role and Firebase drift/denial/malformed/extra/null cases.
- [ ] Hidden password, bearer lifetime, TLS/environment clearing, output size/JSON limits and raw secret/error non-persistence.
- [ ] Deadlines, clock rollback, one-reservation concurrency, SIGINT/SIGTERM at every adapter boundary, response loss and mandatory closeout/private purge.
- [ ] Source/approval/plan/mode/path/symlink/permission drift; closeout-only cannot perform normal reads.
- [ ] Freshly rerun the 15 accepted qualification tests and applicable unchanged read contracts; retain historical expired-fixture failures without alteration.
- [ ] Run backend baseline/architecture/whitespace and governance frozen/consistency/25 safeguards/whitespace.

Observable finish: native refuses without exact real binding; fake transport proves the finite live path; zero real credentials or external calls; sanitized result records limitations. Then present one separately approved attended read-only operation with its actual IDs/window/command and no mutation.

## Decision requested

Approve Alternative 1 for bounded local read-only launch completion and isolated tests only, or defer. Approval includes no credential resolution, external read, database/Firebase/provider action, API enablement, IAM/key/account/runtime/token/Stripe/payment action, spending, attended window, merge or push.

Accepted1A/1B/2A/2B remain4/8; newly closed R1 remains0/27, legacy6/60, intelligence0/13. P08/3A remain open. **Demonstrated launch gap disclosed before implementation; no scope deviation implemented.**

## Owner decision

Debynyhan Banks replied “yes i approve” after review of governance commit `aef3b62` and proposal SHA256 `1225d18577221bff810c6d5b4633df937a3fd9d6dd3ae91265ec4d9c6dbd247e`. Alternative 1 is approved for bounded local read-only launch completion, fake transports, isolated tests and sanitized evidence only. This decision authorizes no credential resolution, external read, database/Firebase/provider action, API enablement, IAM/key/account/runtime/token/Stripe/payment action, spending, attended window, merge or push.

# R08 initial-password method correction — locally qualified, live execution gated

## Current: R08 saved credential requires URI correction — 2026-09-16

Owner completed separate public bootstrap assignment, separate past-expiry statement, private Console reset and Secret Manager save. Combined assignment/past-expiry failed with Neon XX000; readback showed no password, and separate statements subsequently succeeded. Do not repeat bootstrap/reset. Owner screenshot19:47EDT confirmed NOLOGIN/limit0/expiry2000-01-01/password present. Secret version1 created23:45:34UTC, ENABLED; resource-level runtime accessor confirmed. Handoff exceeded the original15minute target; no LOGIN window was opened or silently extended.

After owner said "great proceed", fresh browser metadata23:49:21UTC verified child/neondb/neondb_owner/runtimeOID163840, all login/inheritance/elevated flagsfalse, memberships0, runtime sessions0, limit0, past expiry. Authorized connection preparation accessed version1 only inside a local process with captured output suppressed: URI parsing failed, PostgreSQL scheme and exact child host absent. No secret value, hash or raw exception emitted or persisted; no database authentication attempted. The earlier metadata-only checks proved a saved version, not a correct connection value. Stop before LOGIN. Owner must add one corrected version containing the complete percent-encoded limited-role child PostgreSQL URI; do not reset password or overwrite shared parent secret. Record actual returned numeric version and validate before a fresh bounded connection window. Browser policy requires action-time confirmation to enable security-sensitive login access.

R08 remains open, R08-R12five; P06unaccepted, walkthrough3/8 unchanged. No scope deviation, deployment, application records or paid verification calls. This status supersedes historical handoff-pending/zero-version statements below. Next observable result: corrected URI validated without disclosure, then supervised TLS identity/privilege proof and NOLOGIN/session closeout.


## Owner-approved staging method and private handoff — 2026-09-16

Owner said "i approve your recommendattion proceed" after the recommendation to use the existing limited staging role, check statistics access/retention, keep the final password private, use the dedicated Secret Manager resource, audit access and retain a bounded login/closeout window. This approves the limited staging method and custody preparation, not production use, blanket log safety, a paid verification run or a helper-guard bypass. Existing R07 scope and R10 run gate remain. No new P06 task.

Entry source: backend a17aa8f362ddcce2ad2a4446d81e78279e06177e / governance 4d6d6e6c82091b44cd5e1c7f7c91f599241a1e7e. Fresh metadata at 21:47:25 UTC: child br-sparkling-sun-ay6gr5e8 / neondb / neondb_owner; runtime OID163840 still NOLOGIN/NOINHERIT/no elevation/no membership, connection limit10, expiry unset. Statistics-reading privileges are held by neondb_owner and provider roles cloud_admin/neon_service; runtime has neither effective nor membership access to pg_read_all_stats. This is the inspected catalog boundary, not proof against a compromised administrator. Console shows one organization Admin and no pending invites; Datadog/OpenTelemetry export requires a plan upgrade and is not configured on the inspected integration page. No provider-internal log inventory or API-key audit is claimed.

Retention: track=top, track_utility=on, save=on, max=5000. There is no guaranteed time-based expiry for statistics; eviction/reset is not a retention SLA, and removing the extension does not erase collection. Provider-internal log retention is unknown. The owner-approved residual-risk approach must not be described as zero retention or secret-free logging. No statistics reset, extension install, logging suppression or additional canary was performed. Normal statement/duration logging is off in the inspected settings; that does not remove utility-statistics exposure.

Preparation completed: created empty projects/845074063310/secrets/signmons-staging-p06-child-database-url at 21:49:34 UTC, automatic replication, zero versions. Its only explicit binding is roles/secretmanager.secretAccessor for signmons-calldesk-runtime@signmons.iam.gserviceaccount.com. The existing project Owner retains payload access; existing Editors do not have direct versions.access but can add versions and hold broader project powers. No claim of full isolation from project administrators. Pin the exact returned secret version, never latest. Existing project IAM bindings were compared and unchanged. Added only secretmanager.googleapis.com DATA_READ audit logging with no exemptions; existing _Default sink includes data-access logs, active bucket retention30days. This is audit-event retention, not Neon query-statistics retention. No credential payload was read, generated or uploaded; no runtime service/revision/traffic changed.

Final read-only database check at 21:50:44 UTC: same runtimeOID163840, limit10, expiry unset, all elevation/inherit/login flagsfalse, memberships0, runtime sessions0, other application sessions0,26applied/0unfinished migrations. Public relation/column ACL drift fingerprint f3d51c1325945002d9af69e412ee1b21 (MD5 used only for change comparison, not password hashing or authorization). Provider monitor sessions are excluded, not terminated. This snapshot must be refreshed if the private handoff is delayed or state changes.

### Owner-only credential handoff

Owner screenshot reconciliation at 19:15–19:16 EDT: database neondb, administrator neondb_owner, runtime OID163840, all login/inheritance/elevation flags false, connection limit0, expiry blank; separate pg_authid boolean confirms password_exists=false. The original limit10 guard correctly refused this changed prestate. The proposed provider-AI replacement omitted password and expiry; its execution is not confirmed. The owner-only block below now requires the observed limit0 and an absent password, retaining every membership/session/migration/ACL check. This is a correction within approved R08, not permission to bypass a failing guard. No agent credential change or successful bootstrap/reset is claimed. R08-R12 remain five; walkthrough3/8 and P06 unaccepted unchanged. No scope deviation.

Browser/computer-use policy requires the owner to enter and submit every credential change. Do not paste or execute the credential-changing SQL through the agent, inspect the generated password, read the clipboard, or capture the secret-entry screen. The existing raw-SQL helper remains fail-closed and unchanged.

The role was passwordless at the prior failed direct reset. The qualified sequence is a disabled, expired bootstrap followed by one owner-operated Console reset. The bootstrap marker below is intentionally public, not the final credential, and must never be used to authenticate or copied into Secret Manager. Its exposure in history/statistics is expected. Neon documents NOLOGIN as non-authenticating; this run has not independently proved proxy enforcement. The owner must not enable LOGIN or change the past expiry during this handoff.

1. In the existing Neon SQL Editor, visually verify project signmons-staging, branch p06-isolated-staging-v1 (br-sparkling-sun-ay6gr5e8), database neondb. The owner copies and runs the guarded block below exactly once. It refuses a changed role/prestate, membership, application session, migration count or ACL fingerprint. It only disables the same role further (limit0, past expiry) and sets an intentionally public bootstrap; no grants, ownership, schema or app records change. It records the actual start time only when executed; no login clock runs while waiting for the owner. Finish the reset/custody handoff within15minutes of that reported start; if interrupted, leave NOLOGIN/expired/limit0 and report status before any further attempt.
2. If the block succeeds, open Postgres database > Roles for that same branch. On p06_intake_runtime only, use Reset password once. Save the generated final password privately in the owner's password manager. If it fails or outcome is unclear, stop; do not retry, recreate the role, use an administrator password or disclose the value.
3. Privately build the runtime connection URI below using only the final generated password (percent-encode it as a URI password). In the prepared Google Secret Manager tab, add exactly one version to signmons-staging-p06-child-database-url in project signmons. Do not change the existing shared database secret. The application uses node-postgres; a synthetic parse of this exact URI template confirmed TLS enabled without disabling certificate validation. This is not a live TLS/authentication test.
4. Close every password/secret-value dialog, return to a metadata-only page and report only "reset and saved" plus the nonsecret version number. The agent then checks role/expiry/grants/sessions and version/IAM metadata, without reading the payload. No actual limited-role authentication or activation is claimed until the separately bounded R08 login proof. That later step restores the reviewed limit10 and a fresh approved expiry, then closes existing sessions during shutdown. R09/R10 remain existing gates.

```sql
-- OWNER ONLY: public bootstrap, never a runtime login credential.
-- Verify the exact isolated branch in the browser before running once.
DO $r08_guard$
DECLARE r record; acl_fingerprint text;
BEGIN
  IF current_database() <> 'neondb' OR current_user <> 'neondb_owner' THEN
    RAISE EXCEPTION 'R08 wrong database or administrator';
  END IF;
  SELECT * INTO r FROM pg_roles WHERE rolname='p06_intake_runtime';
  IF NOT FOUND THEN RAISE EXCEPTION 'R08 role missing'; END IF;
  IF r.oid<>163840 OR r.rolcanlogin OR r.rolinherit OR r.rolsuper
    OR r.rolcreatedb OR r.rolcreaterole OR r.rolreplication OR r.rolbypassrls
    OR r.rolconnlimit<>0 OR r.rolvaliduntil IS NOT NULL THEN
    RAISE EXCEPTION 'R08 role prestate changed; do not retry';
  END IF;
  IF NOT EXISTS(SELECT 1 FROM pg_authid WHERE oid=r.oid AND rolpassword IS NULL) THEN
    RAISE EXCEPTION 'R08 password already present or unavailable; do not retry';
  END IF;
  IF EXISTS(SELECT 1 FROM pg_auth_members WHERE member=r.oid)
    OR EXISTS(SELECT 1 FROM pg_stat_activity WHERE pid<>pg_backend_pid()
      AND backend_type='client backend' AND usename<>'cloud_admin') THEN
    RAISE EXCEPTION 'R08 membership or application session present';
  END IF;
  IF (SELECT count(*) FROM public."_prisma_migrations"
      WHERE finished_at IS NOT NULL AND rolled_back_at IS NULL)<>26
    OR EXISTS(SELECT 1 FROM public."_prisma_migrations"
      WHERE finished_at IS NULL AND rolled_back_at IS NULL) THEN
    RAISE EXCEPTION 'R08 migration prestate changed';
  END IF;
  SELECT md5(COALESCE((SELECT string_agg(c.oid::text||':'||COALESCE(c.relacl::text,''),',' ORDER BY c.oid)
    FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='public'),'')
    ||COALESCE((SELECT string_agg(a.attrelid::text||':'||a.attnum::text||':'||a.attacl::text,',' ORDER BY a.attrelid,a.attnum)
    FROM pg_attribute a JOIN pg_class c ON c.oid=a.attrelid JOIN pg_namespace n ON n.oid=c.relnamespace
    WHERE n.nspname='public' AND a.attacl IS NOT NULL),'')) INTO acl_fingerprint;
  IF acl_fingerprint<>'f3d51c1325945002d9af69e412ee1b21' THEN
    RAISE EXCEPTION 'R08 grants changed';
  END IF;
  ALTER ROLE p06_intake_runtime NOLOGIN CONNECTION LIMIT 0
    VALID UNTIL '2000-01-01 00:00:00+00'
    PASSWORD 'P06_DISABLED_BOOTSTRAP_20260916_NEVER_FOR_LOGIN';
END $r08_guard$;
SELECT clock_timestamp() AS handoff_started_at,oid,rolcanlogin,rolconnlimit,rolvaliduntil
FROM pg_roles WHERE rolname='p06_intake_runtime';
```

Private URI template (never paste the completed value into chat, source or SQL):

```text
postgresql://p06_intake_runtime:<PERCENT_ENCODED_FINAL_PASSWORD>@ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech:5432/neondb?schema=public&sslmode=verify-full
```

Preparation validation: frozen baseline, full cross-repository consistency,21 governance regressions, backend architecture/baseline and both whitespace checks passed. No app-runtime tests or live credential proof claimed.

Remaining status: reset/secret upload/authentication are not performed by this preparation. R08-R12 remain5; P06 unaccepted; walkthrough3/8 unchanged. No new task, runtime source, provider test, production action or scope deviation. Sources: [Neon roles](https://neon.com/docs/manage/roles), [PostgreSQL statistics](https://www.postgresql.org/docs/18/pgstatstatements.html), [Google Secret Manager practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

## Approved disposable control-plane reset qualification — 2026-09-16

RESULT completed08:50EDT: owner finished one disposable Console reset after mandatory private handoff. CanaryOID172125 retained NOLOGIN/NOINHERIT/no elevated flags/memberships0/limit0/expiry2000-01-01/sessions0. Exact ALTER prefix across statistics returned2rows/2calls total (expiry plus reset), password1row/1call; password field begins SCRAM-SHA-256, explicit LOGIN tokenfalse, other-passwordrows0, CREATEcontrol1row. Unlike the inspected source candidate, live reset did not add LOGIN. Verifier retention is sensitive and is not secret-free logging; no rawSQL/verifier/final plaintext exported. Actual authentication and provider-internal logs are not proved. Exact canary172125 and test extension1.12/OID172081 removed by guarded DROP/RESTRICT79ms; independent57ms readback confirms role/extension/view absent, runtime163840 disabled/no elevation/memberships0/limit10,trackingtop/on. No outstanding test cleanup. Do not repeat this completed test or apply it to runtime automatically. Review the measured bootstrap/reset path, residual verifier/provider-log risk and private credential custody before real-role approval; no new section/helper/support-email prerequisite. Counts unchanged. Full measurements in backend qualification evidence.

Preflight08:42EDT resolved four other client backends as cloud_admin on postgres only: compute_ctl:compute_monitor, neon_compute_sql_exporter, postgres-exporter, vm-monitor; all idle, no other application clients. The no-other-client check means no unrelated application/operator work; provider monitors are not stopped. Test resources were absent at entry.

Owner agreed to proceed with the single candidate after the evaluation disclosed LOGIN side effect and endpoint disconnections. Entry backend86cd8d0/governancef59b457; clean focused worktrees/remotes refreshed; frozen/full consistency passed. Same R08/2B task and fixed child/neondb, no production or real runtime reset. Published Neon source fa504217c61bbcaf5c512d75830564541f917f8f compute_tools/src/spec_apply.rs(existing role path) and pg_helpers.rs(to_pg_options) supplies an encrypted verifier and LOGIN; source is not proof of current managed deployment or all logging.

Finite exits: preflight no other client sessions, real runtime163840 unchanged/disabled, new role p06_reset_canary_20260916c and statistics extension absent; reuse temporary pg_stat_statements observation with exact OID cleanup. Create only this role NOLOGIN/NOINHERIT/no elevation/memberships/grants/limit0 with public synthetic bootstrap, then set a past password expiry before reset. These are defense-in-depth restrictions to observe, not prior proof of Neon proxy enforcement; no application grants or use are allowed. One Console reset on this canary only, never real runtime; do not reveal/copy/export generated value. Immediately leave generated-secret screen for metadata inspection. Reset outcome must be observed once; ambiguous outcome is reconciled, not retried. Record flags/expiry/limit/memberships and filtered statistics classifications without returning raw SQL/password/verifier. Missing reset observation/visibility is INCONCLUSIVE, not safe. Known public bootstrap history is intentional, never reusable.

Cleanup exact created role (first NOLOGIN if necessary), verify zero sessions, DROP ROLE without CASCADE; remove only test-installed pg_stat_statements with RESTRICT and verify real role/extension baseline restored. Stop if other sessions or target ambiguity; do not terminate unrelated sessions. No LOGIN grant by us, real password use, runtime privilege change, logging change/reset, new provider or app code. No proof of authentication denial is claimed from metadata alone; this test qualifies state preservation and observable credential handling only. No live implementation follows automatically. Evidence in existing backend qualification file; documentation/architecture/baseline/21governance/whitespace gates. Three finite diagnostic exits, no new section or acceptance credit. No scope deviation beyond the owner-approved candidate qualification.

## Approved temporary statistics observation — 2026-09-16

RESULT: completed08:35EDT. Temporary extension1.12/OID172034 and canaryOID172078 removed with guarded RESTRICT cleanup and independently verified absence. Positive utility-control1row; exact assignment1row/1call/synthetic_literal_retained=true. Server-statistics safety criterion FAILS for the tested raw SQL literal path. This supersedes prior INCONCLUSIVE and unexecuted-instrumentation wording below. No real credential used or runtime change. Full measurements and proof limitations in backend p06-r08-private-input-qualification.md. Do not repeat this completed test or weaken guards. The remaining decision is a qualified alternative/security-policy review, not another generic diagnostic or automatic vendor-contact gate.

Owner explicitly approved the proposed temporary pg_stat_statements interface and one synthetic observation test. Entry backend14ba19e/governanced858712, clean focused worktrees/remotes refreshed. Initial frozen check was invoked from the wrong working directory and reported unavailable; rerunning in the governance root passed, along with complete consistency. No anchor changed.

Same R08/2B qualification, no new product task/helper. Three exits: (1) metadata preflight confirms exact child/neondb, extension and p06_password_canary_20260916b absent, runtime163840 disabled; install only pg_stat_statements (no IF NOT EXISTS, no CASCADE), record extension OID/version; (2) create exact disabled/no-membership/no-elevation/limit0 canary, record OID, use CREATE ROLE as positive utility-tracking control, assign one public synthetic64hex marker, query only matching counts and literal-presence booleans restricted to this database/current SQL role and exact canary command prefixes; (3) remove exact canary after OID/state check and remove only newly installed extension with RESTRICT, verify both absent and runtime/logging unchanged. No tracking reset, audit suppression, app/customer read, real password, login or provider upgrade. Inherited PUBLIC rights are disclosed, not claimed absent. Stop on any uncertain action for metadata reconciliation; no automatic duplicate CREATE/assignment. Cleanup of these exact resources is authorized. External logs remain outside this test's proof. Console synthetic history remains intentional and unsuitable for real secret entry. Evidence goes in existing backend qualification file; documentation/architecture/frozen/consistency/21regressions/whitespace gates, no app-runtime test claims. Original14/R08-R12five unchanged. No scope deviation beyond expressly approved diagnostic instrumentation.

## Owner-approved disposable canary — 2026-09-16

Owner approved the proposed disposable staging test after the documentation-first review. This supersedes waiting for a support reply as the only next action; it does not approve real runtime password assignment or weakening SAFE_LOGGING. Entry backend b4ae845 / governance b1b0970, focused remotes refreshed and baseline/consistency checks passed. Existing R08 / walkthrough 2B criterion: qualify least-privileged runtime setup needed for the connected intake journey. No new acceptance section or task.

Fixed three exits: (1) verify existing Console project soft-smoke-54063480, child br-sparkling-sun-ay6gr5e8, neondb, administrator and unchanged runtime metadata; refuse name collision; (2) create only p06_password_canary_20260916a with NOLOGIN/NOINHERIT, all elevated flags false, CONNECTION LIMIT 0, no memberships or application-object grants; initialize once with a deliberately public synthetic marker, then inspect only matching statement counts/marker-presence booleans, not other query text; (3) drop that exact newly created role after OID/flags/membership recheck and verify absence plus unchanged runtime metadata. No DROP OWNED or CASCADE. Normal inherited PUBLIC privileges are not claimed absent; NOLOGIN remains the authentication boundary. No login test or real secret used.

Reuse existing signed-in Neon SQL Editor, not another helper. Browser history will intentionally contain the synthetic marker: this is NOT a safe production-secret entry method or proof of private-client history behavior. Capture configuration and pg_stat_statements observability without changing logging, installing extensions, resetting statistics or granting privileges. Missing/inaccessible statistics or ambiguous execution yields INCONCLUSIVE, not pass. Any error stops assignment retries; reconcile role existence and clean up only the exact test-created role. Concurrent/collision protection: fixed CREATE without IF NOT EXISTS, role OID bound after creation; no parallel writer. Role cleanup belongs to this approval. Stop after result and cleanup, even on success.

No provider upgrade/new compute or customer access. Existing free staging compute may wake; no paid-plan change or additional charge authority. Evidence belongs in existing backend p06-r08-private-input-qualification.md and this review. No application code changed, so runtime build/test claims are inapplicable; run governance frozen/full consistency/21 regressions, backend architecture/baseline and both whitespace checks for documentation. No scope deviation beyond this expressly approved diagnostic action; original14 tasks and R08-R12five remain.

Correction to historical support status below: the approved inquiry was subsequently sent from debynyhan@signmons.com to security@neon.tech on2026-09-16 at08:11EDT, confirmed in Outlook Sent Items. No human response or case number is established. The owner directed documentation and bounded testing first; additional vendor contact is not automatic.

## Current support delivery status

Historical status below is superseded by the sent-mail correction above. Disposable test finished08:29EDT: initialization accepted, test OID172032 removed/absenceverified, real runtime OID163840 unchanged. Console history visibly retained the synthetic literal; database has no statistics inspection extension/view/function, so server-statistics redaction remains INCONCLUSIVE. No real password or logging change. Exact evidence and finite proposed instrumentation option (not authorized) are in backend p06-r08-private-input-qualification.md. The next decision is whether to authorize that narrowly scoped temporary statistics interface, not another support inquiry or product subsection. No safe real-password procedure is claimed from this canary.

Owner authorized sending the drafted question. On2026-09-16 it was sent through the existing Neon Console AI assistant with a human-escalation request; visible conversation confirms delivery. The assistant expressly cannot escalate and returned no human case/ticket number. It did not resolve the initialization/redaction questions. This is NOT a submitted human support ticket or provider security clearance. Console Support menu did not yield a human submission form.

Neon's published support policy limits Free to community support; its security page publishes security@neon.tech for security inquiries (https://neon.com/docs/introduction/support and https://neon.com/security). No upgrade or public community post. A private email fallback is ready, but connected Outlook profile is ben@eternityhvacr.com; owner asked to choose that sender versus debynyhan@signmons.com before sending. No email has been sent; do not duplicate the AI message or imply human response is pending. No password/config/database action or scope/count change. No scope deviation.

## Local implementation approval

Owner said "proceed" to the explicit offer to implement and locally test this bounded adaptation, not run it against Neon. Entry backendc053a2c/governance4f49c6d. The three local exits and expected existing files below are the approved implementation card; historical proposed/unapproved text describes the earlier review checkpoint. Required commands: existing Node password tests, Python private-input tests, synthetic private PG18 proof, full Jest, build, lint, architecture, cross-repository/frozen/governance tests and whitespace. No browser UI changed; no live browser/password acceptance claimed. Live assignment still requires exact fresh packet/logging/private-storage review and separate approval. No scope deviation.

Owner approved preparing an exact procedure after the Console returned `cannot update password for role without password`. This does not authorize another credential attempt. Entry backend a8421727673e3c56481226cf01daff68b1f12488 / governance40f0ea60e8559682fe6679034a6ce6813e79dc2a; focused remotes fetched. Existing R08 task, no U03 or denominator change. Source-mapped adaptation below is proposed, not implemented.

## Why the two methods failed

Native psql password assignment sent a precomputed verifier; Neon rejected it. Owner-approved Console reset was then attempted by the owner and returned the quoted passwordless-role error. The second result is owner-reported; no successful reset or current secret is inferred. Do not repeat either path. Do not delete/recreate the role or use Add role: that can change identity/grants or introduce administrative membership.

[Neon Manage roles](https://neon.com/docs/manage/roles) documents direct SQL password assignment, requires a plaintext password input and rejects hashed input. Plaintext input here means inside verified TLS, not an unencrypted network connection. It does not promise that every provider-internal log omits the value. [PostgreSQL logging](https://www.postgresql.org/docs/18/runtime-config-logging.html) warns that statement logs can include passwords. Browser SQL history, ordinary shell commands, psql history, captured screenshots and raw driver errors are not acceptable password-input paths.

## Inspected reuse and bounded proposed patch

`scripts/p06-private-role-password.mjs` already has verified-TLS admin connection, metadata guards, logging fingerprint/strict refusal, generated32-byte random hex password, one mutation, safe status codes and encrypted-volume persistence. Its `assignCore` and `writeRunner` are hard-coded to p06_migration_runner and old backup tables/directories; it MUST NOT be run or superficially relabeled. `scripts/p06_private_input.py` supplies hidden TTY input/anonymous pipe and bounded child lifetime, but its modes and result messages are migration/backup-specific.

Propose one fixed R08 mode in these existing files, preserving every existing mode unchanged. Expected code files: those two files, their existing Node/Python tests; evidence and this review only. Reuse connection, private_read/readPipe, time budget, exclusive markers and encrypted storage guards. No dependency, schema, app runtime, public endpoint, generic credential service or new provider.

Three finite local exits before any live attempt:

1. Fixed R08 packet/target/guard path: exact child soft-smoke-54063480/br-sparkling-sun-ay6gr5e8, endpoint ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech/neondb; only p06_intake_runtime. Packet binds clean source/hash, actual role OID, flags/memberships, exact grant/ownership fingerprint,26 migration checksum map, fresh read-only logging/extension inventory, no other consumers, explicit owner method/risk approval and <=15-minute assignment window. No parameter for an arbitrary role/host. No login/expiry/grant mutation. A missing/changed role or existing attempt marker refuses.
2. One direct password assignment using existing in-memory32-random-byte/64-hex generation and a dedicated encrypted-directory artifact. Proposed exclusive directory `/Volumes/Signmons-P06/r08-runtime-password-v1`; same already-approved encrypted image, verify mount identity/ownership/modes, no overwrite. Store only runtime credential (not administrator) there with0600/exclusive/no-symlink guards before mutation, plus nonsecret attempt/result receipts. The fixed SQL shape is `ALTER ROLE p06_intake_runtime PASSWORD '<internally generated 64-hex value>'`; it must never print, enter shell/psql/browser history, or execute through a captured command argument. Owner's admin input goes only through existing hidden TTY/anonymous pipe to certificate-verified client. Close admin client after one attempt. Any after-send error/timeout becomes INDETERMINATE; preserve encrypted runtime artifact for reconciliation, never regenerate/retry/delete its only copy. Success reports status only and verifies unchanged OID/flags/NOLOGIN/membership/ownership/grants. Do not query/export role verifier catalogs.
3. Local canary qualification: wrong target/OID/source/window/changed grants, wrong/missing logging settings, role absence/login/elevation, concurrent/repeated attempt, storage collision/symlink, cancellation before/after send, failed commit/connection loss, certificate refusal and redaction. Prove one SQL password statement only, NOLOGIN preserved, secret absent from stdout/stderr/receipt/errors, encrypted artifact preserved on uncertain post-send outcome. Use synthetic private PG18 fixture and existing Node/Python tests; tests prove local behavior, NOT Neon acceptance. No new live role/backup/provider call for testing.

## Logging and execution gates — no silent weakening

Reuse LOGGING_SQL/SAFE_LOGGING and assertLogging unchanged as the starting refusal policy: statement/duration/error/parameter/statistics/audit/extension checks and exact fingerprint. Read current settings before proposing execution; inherited settings are not assumed safe. Do NOT automatically change global/session logging, disable audit, modify permissions or bypass a refusal to make a password command pass. If current settings fail, identify the exact setting and present a narrowly scoped alternative for review; do not create another framework or email prerequisite.

Provider/control-plane logging cannot be proved absent from pg_settings or local tests. Record that residual risk explicitly for owner review before one live assignment; do not label an owner attestation as provider certification or invent a support response. No guarantee of memory zeroization in JavaScript or absence from OS swap/crash dumps; use the private workstation and existing encrypted-at-rest boundary.

After local qualification, execution needs reviewed exact patch/packet, fresh operational allowance/window and local private interaction access. Current computer-use tool refuses Terminal control; do not bypass that safety refusal with AppleScript. Use an allowed owner-operated native Terminal invocation (no secret in command) when its reviewed command exists. Do not ask for a password before preflight is ready. Code adaptation approval is not live assignment approval.

After successful assignment only: owner privately saves the generated runtime credential from the encrypted artifact into their password manager and the already-approved new child-only Secret Manager destination, without assistant screen/clipboard/value inspection. Secret provisioning/version readback, bounded LOGIN proof and subsequent disabled release remain existing R08/R09 gates; no automatic upload or activation. Cleanup follows verified handoff/retention approval; uncertain results retain the encrypted recovery artifact and NOLOGIN. Preserve old migration/backup artifacts and inherited administrator credential.

## Review boundary and status

### Authorized credential-method review completed, 2026-09-16

Owner authorized the bounded investigation after the live refusal. Reviewed Neon Manage roles, CLI roles, Create role and Reset role password references; PostgreSQL18 ALTER ROLE/role attributes/logging/pg_stat_statements; CloudNativePG maintainer advisory GHSA-w3gf-xc94-wvmj. This is documentation research, not another live attempt. Entry backend3f81133/governanceb027080; both focused remotes fetched.

Findings and decision:

- Neon explicitly requires plaintext for SQL password assignment and rejects hashed input. The native verifier route is therefore incompatible, not a user-entry mistake. [Neon roles](https://neon.com/docs/manage/roles).
- Active utility tracking is a distinct exposure path from ordinary statement logging. The CloudNativePG maintainer advisory documents literal passwords captured by pg_stat_statements for its affected implementation. It is evidence for the mechanism, NOT evidence that Neon runs CloudNativePG or that any Signmons password leaked. Do not weaken the runtime helper's guard. [Primary advisory](https://github.com/cloudnative-pg/cloudnative-pg/security/advisories/GHSA-w3gf-xc94-wvmj), [PostgreSQL18 statistics](https://www.postgresql.org/docs/18/pgstatstatements.html).
- Correction to shorthand: log_parameter_max_length=-1 permits full bound-parameter values when qualifying statements are logged; it does not itself enable statement logging and is not the primary protection for a password interpolated as a SQL literal. Keeping its guard is conservative; changing this one value would not resolve utility tracking. [Logging](https://www.postgresql.org/docs/18/runtime-config-logging.html).
- Console/API reset documents replacement of an existing password, not a confirmed initialization path for this passwordless role. Owner-reported reset failure remains unresolved; no API retry justified. [Reset API](https://neon.com/docs/reference/api/branches/reset-project-branch-role-password).
- New Console/API/CLI roles receive neon_superuser membership. The reviewed official docs do not establish that this administrator can remove that managed membership and all associated privileges. Creation followed by stripping privileges is NOT execution-ready and is not recommended without proof. It also changes identity and temporarily adds broad access. [Neon roles](https://neon.com/docs/manage/roles).
- API no_login exists, but CLI docs explicitly call the corresponding option passwordless; it is not evidence of obtaining a generated password while preserving NOLOGIN. Do not assume it solves this problem. [Create API](https://neon.com/docs/reference/api/branches/create-project-branch-role), [CLI](https://neon.com/docs/cli/roles).
- A disposable bootstrap password followed by reset would still write a credential through the refused path and rely on unverified reset/NOLOGIN behavior. It is not a qualified workaround. No new credential experiment is proposed.

Recommendation: preserve current role/grants and fail-closed helper; obtain one provider-supported initialization/redaction answer before another attempt. No additional implementation, scope/task or email contact authorized. Support is a recommendation, not an invented mandatory product acceptance criterion. If owner declines provider clarification, report that no verified safe live path was established; do not promise an immediate alternative or silently accept credential exposure. This review is complete and must not be re-proposed as another review subsection.

Draft support question (not sent):

> We need to initialize a password for an existing SQL-created limited role, p06_intake_runtime, on our isolated staging branch. It is NOLOGIN/NOINHERIT with no elevated flags or memberships. Native psql password assignment is rejected with “Neon only supports being given plaintext passwords”; Console reset reports “cannot update password for role without password.” pg_stat_statements.track=top and track_utility=on; our neondb_owner lacks SET authority on that setting. What supported method initializes this existing role without putting a usable password into SQL/query-history/statistics, adding neon_superuser membership, or enabling LOGIN? If direct SQL is the required method, what documented redaction protects this exact path, and does it cover pg_stat_statements, activity visibility and provider logs? Please distinguish a supported initialization method from reset of an existing password. No credentials or customer records are included in this request.

No contact sent; no credentials viewed; no database/config/permission changes. Documentation/frozen/cross-repository and architecture/whitespace gates apply; earlier runtime tests are not represented as new. R08-R12five remain; packages5/60 and walkthrough3/8 unchanged; ETA unvalidated. No scope deviation implemented.

Owner reviewed local commit859ec4c and requested continuation. Live read-only preflight2026-09-16 found log_parameter_max_length=-1 and pg_stat_statements.track=top/track_utility=on; neondb_owner lacks SET authority on both relevant parameters. Helper correctly refuses; no settings/password/reset/privilege changes. Role OID163840 remains NOLOGIN/NOINHERIT, no elevation/membership,limit10. Encrypted image unmounted. No executable window/packet. See latest backend p06-r08-private-input-qualification.md preflight. Local compatibility assumptions were not live qualification; no silent guard relaxation. Current blocker requires reviewed provider-compatible credential handling, not another helper or automatic retry. Three local exits remain complete but live execution is not admitted.

Owner approved the local adaptation; all three finite local exits are now implemented and locally qualified in backend commit859ec4c. Existing Node password tests including both disposable private PG18 modes:15 passed; Python hidden-terminal tests:12 passed; shared backup guards25 passed. Full backend regression:2359 passed,3 skipped; build/lint/architecture passed. Cross-repository consistency/frozen baseline and21 governance tests passed. No live credential attempt occurred. Evidence: backend evidence/APP-013/p06-r08-private-input-qualification.md. Historical proposal language above records the original decision, not an outstanding implementation approval.

Next review the patch, then prepare/read-only verify the exact fresh execution packet and separately authorize one live child-only assignment. Do not reuse an old window or assume safe provider logging. The private terminal command is not an invitation to run before those gates. No feature/task added: original12+approvedU01+approvedU02=14; R08-R12five remain; packages5/60(8.3%),walkthrough3/8(37.5%),P06unaccepted,ETAunvalidated. No scope deviation.

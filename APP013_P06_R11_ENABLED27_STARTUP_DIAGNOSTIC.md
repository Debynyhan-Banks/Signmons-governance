# APP-013/P06 R11 enabled27 startup diagnostic decision

Status: proposed; owner approval pending. Operation `6b086d07-9dee-422f-8c77-3492b8f63acc`. Proposed execution: once after approval, before September 25, 2026, 9:30 AM Eastern (13:30Z). No query has run and no diagnostic authorization or attempt exists.

## Demonstrated failure

Plan `22db1c2a-c9ab-4025-891a-91dc7118e971` opened LOGIN and activated successfully. Its single deployment failed before browser handoff: Cloud Run and the existing local CLI log report that enabled27 failed to start listening on port 8080. ContainerHealthy became False with HealthCheckContainerError at 13:00:31.644784Z. The image imported successfully. This approximately 26-second failure was not the controller's 180-second timeout.

The deployed image, runtime envelope, referenced secret versions and disabled flags match the approved packet. The existing compiled pure parser accepts that envelope at startup time. These checks cannot establish injected secret contents or live database startup authorization. The actual startup cause remains unresolved; no port, timeout, application or image change is justified yet.

Closeout is CLOSED with no failures; revocation is REVOKED with one matching audit. Runtime LOGIN is disabled, connection limit and sessions are zero, the enabled tag is absent, and normal traffic remains 100% on app013bounds. The failed revision is retired, not deleted. Latest Ready remains enabled25. Evidence: backend `evidence/APP-013/p06-r11-enabled27-startup-stop-closeout.md`; source backend edd2b7a/governance 3865ec2.

## Alternative 1 — one sanitized read-only startup-log diagnostic

Authorize one Cloud Logging read for project signmons, service signmons-calldesk-staging, exact revision signmons-calldesk-staging-app013p06enabled27, and historical interval 13:00:06Z–13:00:32.999999Z on September 25. Read only container stdout, stderr and system startup streams, excluding request logs. Use one invocation, ascending timestamps, a 200-record limit, no pagination and no automatic retry.

Exact filter:

```text
resource.type="cloud_run_revision"
resource.labels.project_id="signmons"
resource.labels.service_name="signmons-calldesk-staging"
resource.labels.revision_name="signmons-calldesk-staging-app013p06enabled27"
timestamp>="2026-09-25T13:00:06Z"
timestamp<="2026-09-25T13:00:32.999999Z"
(logName="projects/signmons/logs/run.googleapis.com%2Fstderr" OR logName="projects/signmons/logs/run.googleapis.com%2Fstdout" OR logName="projects/signmons/logs/run.googleapis.com%2Fvarlog%2Fsystem")
```

The command is `gcloud logging read` with that filter, `--project=signmons`, `--order=asc`, `--limit=200`, and `--format=json(timestamp,severity,textPayload,jsonPayload.message,jsonPayload.error.message)`. Capture its response only in process memory and pass it immediately through the sanitizer. Never print or save raw logs.

Install only a fresh private authorization, binding and one-attempt diagnostic wrapper. Reserve the operation exclusively before querying; enforce the exact identity/window/source and no-retry guard. No database helper, password or browser action is needed.

Retained output is limited to allowlisted classes, counts, severity and minimal first/last timestamps. Classes: CONTROLLED_INTAKE_STARTUP_UNAVAILABLE; CONTROLLED_RUNTIME_CONFIGURATION_UNAVAILABLE; CONTROLLED_RUNTIME_UNAVAILABLE; PRISMA_CLIENT_INITIALIZATION_ERROR; DATABASE_AUTHENTICATION_FAILED (P1000); DATABASE_UNREACHABLE (P1001); DATABASE_TIMEOUT (P1002); DATABASE_ACCESS_DENIED (P1010); DATABASE_LOGIN_DENIED; MISSING_MODULE; MISSING_REQUIRED_FILE; OUT_OF_MEMORY; CONTAINER_FAILED_TO_START_OR_LISTEN; BOOTSTRAP_INITIALIZATION_FAILED; UNCLASSIFIED_STARTUP_ERROR; NO_ALLOWLISTED_STARTUP_ERROR; RESULT_LIMIT_REACHED.

Do not retain or display raw messages, stack traces, paths, query text, connection strings, environment values, secret payloads, HMACs, account/participant identifiers, names, addresses, phones or codes. Unknown text is not printed. Saturation or unclassified results remain unconfirmed; neither permits a second query automatically.

## Alternative 2 — remain closed

Retain verified shutdown and do not query logs or attempt another live run.

## Bounded card

- Acceptance: existing APP-013/2B, P06-R11 connected phone/address/reviewed submission and full R12. This diagnostic identifies a startup failure; it awards no acceptance.
- Reuse: existing exact packet, markers/readbacks, Cloud CLI and sanitization pattern. No new subsystem, schema, provider, application source, image or protocol.
- Checklist: owner approval; prepare private wrapper; local filter/sanitizer checks; one query in the window; retain sanitized evidence; update handoff; propose a repair only if the evidence supports it. No automatic new run.
- Tests: exact operation/window/filter/limit/reservation checks; all classifier cases; secret-bearing unknown text must never appear in output; limit, unclassified and no-match cases. Run required governance baseline/docs/21 tests, architecture and whitespace checks. Tests use synthetic records, not live logs.
- Roles: owner approves this diagnostic; implementer runs and reviews it once. No owner password is needed.
- Exclusions: no database access or write, LOGIN, activation, deployment, traffic change, provider request or mutation, code, browser/customer action, job retry, hold release, secret/IAM/billing change, image build or automatic retry.
- Finish: one sanitized startup classification or a truthful unconfirmed result. Runtime remains closed. P06 stays 12/14; R11/full R12 open; accepted 1A/1B/2A unchanged. No scope deviation.

## Owner decision

Pending. The prior approval covered the consumed execution plan and closeout. This new log-diagnostic scope requires a separate owner decision.

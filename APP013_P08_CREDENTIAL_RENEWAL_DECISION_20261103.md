# APP-013 / 3A / P08 — one SDK credential-renewal decision

**COMPLETED / CONSUMED:** one command ran 13:01:06–13:01:07 UTC, exited 0; one sanitized cache postcheck passed validity beyond 13:30 UTC. Owned leader reaped/group absent; output discarded, no private token/plan file. SDK auth request count not observed; zero qualification resource requests. Evidence backend CREDENTIAL_RENEWAL_RESULT_20261103.md and renewals/20261103-1300/ under the existing narrow-access evidence directory. This renewal approval cannot be reused; the fresh six-read packet remains pending separate approval.

**OWNER APPROVED THE EXACT EXCEPTION — November 3, 2026:** owner replied “i approve” to the explicit SDK retry/cache-maintenance exception and November 3 8:00–8:05 a.m. EST window, strict 8:02 start cutoff, one command/60-second limit/hidden output/one validity postcheck. Approval observed 12:54:08 UTC. The pending language below is retained as preapproval history. The six-read qualification keeps its no-refresh/no-retry rule and remains separately gated. Renewal reservation label: renewal-20261103-1300; exclusively created sanitized receipts will be retained in backend evidence/APP-013/p08-narrow-access-check-local-20261101/renewals/20261103-1300/. No token/private plan is stored there. No renewal has started.

**Owner approved beginning credential renewal on November 3 (“im back, i approve lets begin”). That approval is recorded, not requested again. A specific SDK retry/cache-maintenance exception remains PENDING. No renewal command has run.**

## Demonstrated gap and decision

The November 1 operation dff9307d-e7fb-4e5a-873c-22179faf0958 remains consumed: CACHED_TOKEN_EXPIRED, cache 1/HTTPS 0, verified private-plan purge and no residuals. Current backend af4c27f and governance 3e48d96 confirm that result. A new cached token is the prerequisite for a fresh narrow access qualification; neither is a completed customer/payment capability.

The reviewed six-read module deliberately cannot renew credentials. Installed Google SDK 583.0.0 offers `auth print-access-token ACCOUNT`; its actual command calls LoadCredentialsWithScopes, which loads and refreshes expiring credentials and caches the result. Ordinary OAuth refresh has an internal retry loop. The November 1 synthetic test demonstrated three attempts for repeated 503; reauthentication paths can involve further authentication requests, so three is not claimed as a total network-request ceiling. The SDK store can maintain/migrate its local credential/cache metadata. A single CLI invocation does not enforce a single HTTP attempt.

On November 3, all 21 SDK source hashes in the existing test manifest still matched the inspected sources, and the unchanged qualification source validator passed. No real credential/configuration state was read for this investigation. Current credential usability and renewal success remain UNKNOWN.

**Recommended exception:** permit one invocation of the installed SDK's existing credential resolver/renewal for the exact owner, including SDK-managed authentication retries and normal SDK credential/cache metadata maintenance. Keep the six-read qualification's no-refresh/no-retry rules unchanged. This exception does not authorize resource API probes, IAM/API/billing changes, new scopes, alternate credentials or another invocation after failure.

**Alternative:** retain strict zero authentication retries and defer renewal. Do not implement another authentication subsystem or silently patch SDK internals. A custom one-attempt renewer would require its own demonstrated need, approved card and local proof; none is proposed for implementation here.

The existing AGENTS rule requires advance approval for changed substantial prerequisites. The additional decision is specifically the SDK's retry/cache behavior, not whether the owner wants renewal. A general renewal approval is not interpreted as silently relaxing that rule.

## Exact proposed renewal boundary

- Identity: debynyhan@signmons.com, existing default SDK root `/Users/debynyhanbanks/.config/gcloud`; no alternate account, ADC or impersonation requested.
- SDK executable `/opt/homebrew/bin/gcloud`, resolving to the pinned 583.0.0 installation. Relevant source hashes are in backend `evidence/APP-013/p08-narrow-access-check-local-20261101/source/test-manifest.json`; actual executable hash remains `8628b9f971d07c5e52fd2c6d469ee4a0940c75eb51820d628c3dd068981bd260`.
- Proposed November 3 window: start at or after **13:00 UTC / 8:00 a.m. EST**, strictly before **13:02 UTC / 8:02 a.m. EST**; finish and closeout by **13:05 UTC / 8:05 a.m. EST**. If the exception/verification is not complete by cutoff, do not launch or roll the window forward.
- Exactly one CLI invocation, maximum 60 seconds; SDK-managed authentication request count is not asserted as one or three. No automatic or manual second invocation, login fallback, browser sign-in, forced refresh, scope/lifetime flags or recovery rerun.
- Exact command arguments: `/opt/homebrew/bin/gcloud auth print-access-token debynyhan@signmons.com --quiet --verbosity=none`.
- Run with stdin closed and stdout/stderr directed to the operating system null device, never captured in the conversation or a file. Child-only settings disable SDK file logging, HTTP logging, prompts and usage reporting. Reject pre-existing credential/proxy/config overrides before adding these output-control settings; do not silently hide an override.
- Use the existing strict `config_snapshot` and source/executable checks immediately before invoking; no new resolver or SDK patch. Unknown/unsupported configuration is a stop. This is authorization for the supported SDK-managed renewal path, not certification of a particular current stored credential type or provider outcome.
- The owner-approved exception would permit the SDK's normal persistent credential/token/cache metadata changes required by renewal, including maintenance/migration. Do not copy, print, back up, restore, delete or revoke credential stores as rollback. On failure, classify cache state UNKNOWN until the permitted postcheck; no cleanup claim that reverses SDK maintenance.
- On a clean command exit only, perform one bounded read-only cached-token validity postcheck using the existing `read_cached_token` boundary, with token retained in process memory only and cleared afterward. Require validity strictly beyond **13:30 UTC / 8:30 a.m. EST**. Report only VALID_THROUGH_CUTOFF or a sanitized refusal. Do not retain raw token or expiry. Do not interpret CLI exit 0 alone as renewal success.
- No private operation plan/token file is needed for this renewal. Retain only sanitized invocation reservation, start/end/exit/timeout, owned-process closeout and postcheck classification. On timeout, terminate/reap only the directly owned live process group and report uncertainty; do not signal guessed/reused PIDs or claim success.
- USD 0 incremental spending authority; no resource creation, grants, service enablement, deployment, customer/job/payment/Stripe action. No push or merge. The old operation and R10 remain consumed.

## Readiness, finite work and owners

| Prerequisite | Inspected evidence / status | Owner |
| --- | --- | --- |
| Prior operation and cleanup | Immutable result/closeout at backend af4c27f; consumed and closed | Implementer |
| Existing CLI behavior | SDK surface/auth/print_access_token.py, command_lib/auth/auth_util.py, credentials/store.py, credentials/creds.py and google/oauth2 refresh sources; 21 hashes match November 1 diagnostic | Implementer |
| Internal retries/cache maintenance | Demonstrated; incompatible with an unqualified zero-retry promise; proposed exception pending | Owner |
| Output secrecy/deadline/one invocation | Exact command and null streams/60-second owned-process boundary above; no new runtime adapter or source modification requested | Executor |
| Actual configuration/credential usability | UNKNOWN; strict preflight and one postcheck are part of the proposed bounded renewal | Owner/credential custodian |
| Fresh six-read qualification | Not scheduled or approved; old source remains cached-only/no retry | Owner after successful renewal |

Finite checklist after the specific exception is approved: (1) record exact decision, recheck source/clock/config and exclusively reserve one renewal invocation; (2) run the exact SDK command once with hidden output and bounded owned-process handling; (3) on clean exit perform one sanitized existing-cache validity check; (4) verify process closure and retain only non-secret result; (5) if valid, prepare a fresh separately reviewable six-read qualification packet using unchanged source. No project/API read is part of renewal itself.

Local reconciliation checks: source validator and 21 SDK evidence hashes PASS; frozen/cross-repository/docs checks PASS. Final documentation/architecture/whitespace and governance safeguards are recorded at closeout. No new runtime tests or live credential proof are claimed. No implementation subsection or acceptance criterion is added.

Official method references: [print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token) specifies account selection and that lifetime overrides apply to service-account impersonation, which is excluded here. [auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) is a separate authorization workflow and is not an automatic fallback in this proposal.

APP-013/3A open; accepted 1A/1B/2A/2B **4/8**; newly closed R1 **0/27**. Next observable result is the owner's specific SDK exception decision, followed only if approved by bounded renewal or refusal. **Explicit policy-exception proposal; no deviation implemented.**

Final local verification, 2026-11-03 12:51:44 UTC: source validator/21 SDK hashes, backend architecture, frozen/cross-repository/docs consistency, 25 governance safeguard tests and both tracked whitespace checks PASS. No runtime or live credential test was run. This proposal and handoff updates are local and uncommitted pending the specific exception decision.

# APP-013 / 3A / P08 — fresh bounded SDK credential renewal

**PENDING OWNER APPROVAL.** Preparation only; no credential/configuration read, SDK invocation or provider action. Old renewal20261103-1300 and token check112f0eed-6230-4137-8f16-d4ec1beb9675 are consumed. The token check at14:20:17 showed insufficient validity beyond14:35, not necessarily already expired. Existing14:25–14:35 key packet stays blocked and must not be reused.

## Exact decision requested

Permit one invocation of the installed SDK's existing credential resolver for debynyhan@signmons.com, including **SDK-managed authentication retries and normal persistent credential/cache metadata maintenance**, maximum60 seconds, hidden output, verified owned-process closure and one bounded read-only validity postcheck only on clean exit. No second invocation or fallback. Authentication request count is not asserted as one or three. This exception applies only to renewal; later key qualification remains cached-only/no-refresh/no-retry and separately approved. Alternative: defer; no custom renewer or SDK patch is proposed.

Reservation **renewal-20261103-1440**, sanitized evidence location backend evidence/APP-013/p08-narrow-access-check-local-20261101/renewals/20261103-1440/. November3,2026 start at/after **14:40 UTC /9:40 a.m. EST**, strictly before **14:42 /9:42**; finish and independently verify closeout by **14:45 /9:45**. If late, expire unstarted; no sliding window. On clean exit, one existing-cache read must establish validity strictly beyond **15:10 UTC /10:10 a.m. EST**. That is a validity target, not an approved downstream launch/window. No actual renewal directory or private plan created during preparation.

Exact command, only after approval:

```sh
/opt/homebrew/bin/gcloud auth print-access-token debynyhan@signmons.com --quiet --verbosity=none
```

## Inspected source and configuration boundary

Source commit5be6d5772394062395f735e23c7ae32423180d14; runtime SHA256495258008e1e6454fda779724a3c3cfc85b27459af7e217ba39dd2ab24472d9e; manifest3db5e61e6ec460a8425819c6ea0272dda8cf63606230ee9dd1fb63e1fa31528b; corrected test-manifest SHA256dc12ace939abfa306fbf5672b3e40a744e18c8c3ca1ddbc8f77765d8e320031d. Installed gcloud583.0.0 executable /opt/homebrew/bin/gcloud resolves /opt/homebrew/share/google-cloud-sdk/bin/gcloud, hash8628b9f971d07c5e52fd2c6d469ee4a0940c75eb51820d628c3dd068981bd260. Preserve exact same-file resolution/hash rather than assuming Caskroom symlink spelling. Exact Python /opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 (-I -B), hash2cbb3ee843d8abcf93ed35bb9102391f18eefccb03d47908547bd8db67bc395c.

Existing reviewed SDK surface/auth/print_access_token.py → auth_util.LoadCredentialsWithScopes → credential store/refresh path can retry auth and maintain/migrate local SDK credential metadata. Prior synthetic tests demonstrate retries, not a total request ceiling. All21 sdkReviewFiles hashes match at2026-11-03T14:32:33Z. Existing strict config_snapshot must validate actual default root /Users/debynyhanbanks/.config/gcloud, accountdebynyhan@signmons.com/projectsignmons and dynamic supported config immediately before invocation. Reject existing CLOUDSDK_/GOOGLE_/GCLOUD_/PG/database/proxy/certificate overrides using the existing guard; do not suppress them. Current credential type/usability and renewal outcome UNKNOWN. No alternate account/ADC/impersonation or new scopes.

## Finite execution and cleanup procedure

1. Record actual owner approval against this exact proposal and commit. Read approved bytes via existing committed reader; compare command/source/executable/dependency hashes, authority and clock immediately before launch. Same current source gate and strict config_snapshot, no credentials read for preparatory source comparison. Exclusively reserve renewal directory0700 and exclusive entry.lock; collision or active lock stops. Reserve sanitized attempt.json0600 before launching once.
2. Spawn exact command as a directly owned new process session/group. stdin/stdout/stderr all OS null device, never capture output in memory/conversation/file. Only after existing environment/config guard add child settings CLOUDSDK_CORE_DISABLE_FILE_LOGGING=true, CLOUDSDK_CORE_LOG_HTTP=false, CLOUDSDK_CORE_DISABLE_PROMPTS=true, CLOUDSDK_CORE_DISABLE_USAGE_REPORTING=true. No SDK source modifications or general logging exception.
3. Bound invocation to60 seconds with monotonic elapsed time. On timeout/interruption terminate/reap only the still-owned live process group (TERM then bounded KILL if necessary); never signal guessed/reused PID/group. Verify leader reaped/group absent. Unknown process outcome is a stop, not success; retain sanitized uncertainty. No retry, manual second invocation, browser/login fallback, forced refresh, scope/lifetime flags or alternate credentials.
4. Only clean exit0 and verified process closure allow one existing read_cached_token(CONFIG_ROOT, utc('2026-11-03T15:10:00Z')) under http_deadline(8). Reserve postcheck count before invoking. Keep return in process memory only and clear in finally; no raw token/expiry retained or secure-memory-erasure claim. Report VALID_THROUGH_CUTOFF or sanitized Stop/UNKNOWN. Exit0 alone is not renewal proof; success proves usable cache at observation, not necessarily new token issuance.
5. Before14:45 independently verify owned directory/lock, exact sanitized receipt inventory (attempt.json, result.json, entry.lock, receipt-verification.json if generated by verifier), regular0600 single-link files and source/decision/hash/count binding, owned-process closure, no raw output/private plan/token/scratch. No private token/plan file is needed. Interrupted or missing result stays UNKNOWN, never rerun to reconstruct it. Persistent writes/process uncertainty must be reported without a cleanup-success claim.
6. Retain SDK's authorized credential/cache maintenance. Do not copy/print/back up/restore/delete/revoke stores as rollback. After success only, prepare a fresh exact three-read qualification packet, current source/target/window and separate owner decision. Failure stops for separately scoped remedy; no substitute offline implementation.

## Readiness, owners and exclusions

| Prerequisite | Evidence/status at2026-11-03T14:32:33Z | Owner |
| --- | --- | --- |
| Source/manifest/executable/SDK consistency | Four committed files match; corrected manifest regression and101 focused tests PASS;21 SDK hashes/executable match; source gate passes locally only | Implementer rechecks prelaunch |
| Output/serialization/cache parsing | Existing SDK behavior inspected, output discarded; existing actual synthetic-cache tests cover missing/schema/null/expiry/locks/closure; no new auth implementation | Executor; future outcome UNKNOWN |
| Exact configuration/credentials | Existing strict dynamic guard reused; current configuration/credential usability UNKNOWN and checked only under approval | Credential custodian |
| Retries/cache maintenance | SDK behavior known; this fresh explicit exception PENDING | Owner |
| Timing/one invocation/concurrency/interruption | Exclusive reservation/lock, exact cutoff,60-second owned-process bound, no second invocation; prior same procedure closed successfully but not future proof | Attended executor |
| Privacy/cleanup | Null streams, no token files, existing memory-only postcheck, independent receipts/process check; no rollback of SDK maintenance | Executor |
| Downstream API/key/payment/full qualification | UNKNOWN; no provider-resource request permitted | Existing owners, later approval |

Approval permits SDK auth traffic and described local credential/cache maintenance only. USD0 incremental spending authority. No resource API probes, key actions, IAM/services/billing changes, production/database/Firebase/job/customer/payment/Stripe action, deployment/merge/push. Accepted criterion remains APP013_REMAINING_EXECUTION_CONTRACT3A same admitted-job Sandbox payment with matching signed settlement; this prerequisite adds no acceptance section or denominator. No runtime code change.

Completed preparation: corrected manifest approved/proved, prior renewal/stop recovery, exact command/pins/window/exception/readiness/cleanup. Remaining owner: approve this exact renewal exception or defer; executor: one bounded outcome and independent closeout if approved; then implementer: fresh separately approved qualification packet. Accepted1A/1B/2A/2B4/8, R1 newly closed0/27, 3A open. **Earlier evidence drift corrected under explicit approval; no further scope deviation. Fresh SDK exception proposed, not executed.**

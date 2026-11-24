# VM2 R3 — one exact metadata diagnosis after the reporting correction

**Qualification only; pending exact owner approval and reachability.** APP-013 / 3A / P08. The previous VM2 attempt is consumed and BD7 billing is complete. This new operation uses the corrected reporter; it does not repeat billing or launch the payment workflow.

## Reviewed source and exact action

Backend source `7dff026642106719ea3990c53f5723f9199e36b0`; manifest `0c3c90cdad6cf8a1c742a37de20d9cbf8f9fcd7ad772f97fbd486dbfe71bec78`. Routine correction under original local approval874ce21 changed only the three VM2 files, preserving 43 fixed documented googleapis.com error labels. All60VM2 and100SQ1 tests passed; independent review and governance checks are recorded in APP013_P08_VM2_REASON_VALIDATION_20261124.json. The earlier response's discarded reason remains UNKNOWN.

Operation `0d360f5b-2f79-476c-a1d1-0434c7a8a210`; scope `APP013_P08_VM2_SCOPE_20261124_0d360f5b.json`, canonical digest `b961a79f3ce262f7f6b8de0ecd023485ce447550d3dfbec13085ce8186647b9e`. A later owner-approved governance commit must contain the exact scope and `APP013_P08_VM2_APPROVAL_20261124_0d360f5b.json`. The decision draft is explicitly not authorization.

Maximum **2 CLI reads, 1 credential-cache read and 1 HTTPS metadata GET**, with no SQL or provider mutation. Ordered commands are `/opt/homebrew/bin/gcloud auth list --filter=status:ACTIVE --format=json(account,status)` and `/opt/homebrew/bin/gcloud projects describe signmons --format=json(projectId,projectNumber,lifecycleState)`. The active owner must match debynyhan@signmons.com and the project number must match the pinned canonical digest before request composition.

The only resource request is `GET https://secretmanager.googleapis.com/v1/projects/<verified-number>/secrets/signmons-staging-p07-payment-database-url/versions/1?fields=name,state`. No secret payload, redirect, alternative resource, operator retry or second metadata request. Request deadline8seconds; response limit65536bytes. Each CLI has at most30seconds within the main deadline.

Exact executable: `/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B`, existing isolated runpy bootstrap, module directory `/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110`, script `vm2_metadata_read.py`, followed by approved governance commit, scope filename and approval filename above. Before launch compare actual command/source/manifest/configuration/authority/clock and absent exclusive root `/private/tmp/p08-vm2-0d360f5b-2f79-476c-a1d1-0434c7a8a210`. Do not remove consumed markers to replay.

## Fixed window, credential gate and cleanup

November24,2026 Eastern: start8:43a.m.; **launch strictly before8:58a.m.; reads end9:00; independent closeout by9:03**. Owner reachability through9:03 is pending. No Terminal attendance, password entry or browser sign-in is required.

Current credential coverage is UNKNOWN. The proposed exception `SDK_EXISTING_OWNER_REFRESH_CACHE_INTERNAL_RETRIES_NO_TOKEN_EXPORT` permits only the existing SDK's owner refresh/internal authentication retries/cache maintenance during its two reads. The single cache check must then prove token expiry strictly beyond9:03 before the GET. Otherwise stop. No explicit refresh/login/token export/alternate account is included; SDK-internal network totals are UNKNOWN, distinct from logical ceilings.

Retain only safe HTTP/status, finite metadata state, fixed reason/domain/equality flags, operation/source hashes, counts and cleanup flags. Tokens, raw responses/messages, arbitrary metadata and numeric project identity remain in memory and are discarded. Unknown and conflicting details remain conservative; a recognized reason is a current provider report, not proof of historical cause or usable payment readiness. NOT_FOUND is not independent absence proof.

Independently close/read back actual owned process handles and responses, compare nonsecret configuration, check result digest/interruption veto and process exit/absence, and remove only owned temporary inputs. No provider cleanup, additional credential read or SDK cache deletion. SIGKILL/operator death remains UNKNOWN requiring local inspection; no disk PID is adopted for destructive cleanup.

## Readiness and decision

APP013_P08_VM2_R3_READINESS_20261124.json records the actual current-clock preflight against committed source, transitive SDK/runtime guards, exact descriptors, nonsecret configuration and absent root. Synthetic actual-boundary tests cover output contracts, domain/unknown/conflict handling, privacy, deadlines, replay, concurrency, interruption and independent cleanup. Source, tests and independent review are complete; **current credential horizon, API availability, usable permission, version state and response remain UNKNOWN**, precisely the purpose of this bounded qualification. No source or acceptance guard is bypassed.

$0 additional allowance; no cost-hold release or hard cloud-billing cap claim. No secret payload, SQL, provider/IAM/billing/key/webhook changes, sign-in, payment/refund, customer/support contact or deployment. No automatic connected payment retry follows.

Owner decision: approve VM2 R3's exact metadata diagnosis, single cache read, stated SDK exception, spending limit and independent cleanup, and confirm reachability through9:03. This separate approval is necessary because the previous one-attempt read is consumed and its fixed window expired. Implementer owns final launch comparison and closeout; cloud/credential custodian owns external state. Next observable result is one current metadata state or safe denial classification with verified closure, or a finite stop. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1newlyclosed0/27. No scope deviation.

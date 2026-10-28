# APP-013/3A/P08 — explicit project fingerprint contract and fresh caller probe

PROPOSED; no correction/execution authorized yet. Operation7b88581c-b602-428f-bf1f-1bac667110ea. Sources backend73e902a plus current consumed caller-probe evidence; governancea8e8138 plus current result. Prior attempts remain consumed. This proposal does not modify a helper/application, change a project binding or grant permission.

## Demonstrated gap and choice

Current probe stopped after2CLI/noHTTP because SHA256(raw decimal UTF8) did not equal prior projectNumberSha256. Earlier saved evidence omitted the producer's serialization contract; bounded local source searches did not recover it. Actual project drift versus encoding mismatch UNKNOWN. Nineteen local request/parser checks did not cover this boundary. Implementer responsibility, not owner credential failure. No actual numeric project identifier retained or disclosed.

Alternative1 recommended: explicit owner-approved two-encoding comparator, local tests first, then one fresh three-CLI/one-HTTPS qualification. For the same numeric project number returned by exact gcloud projects describe signmons, compute only (a) SHA256(decimal string UTF8) and (b) SHA256(canonical JSON string of that decimal string, including quotes). Compare each against unchanged prior fingerprint37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54. Exactly one match proves the same data under that encoding; neither or both matches stops. Retain only RAW_DECIMAL_MATCH/JSON_STRING_MATCH/NO_MATCH and booleans, never current number/new hashes/raw output. No direct use of current value to replace the stored fingerprint. This explicitly approves the possible serialization correction; it does not retroactively prove why the prior attempt stopped.

Alternative2 defer: no further reads, preserve unknown binding/permissions and disabled state. No new acceptance section/count, MVP scope or provider allowance. Current3A acceptance remains APP013_REMAINING_EXECUTION_CONTRACT.md same-job authentic Sandbox event/payment recovery, not a project probe.

## Finite local card before external reads

Reuse exact nine-permission payload/strict parser and config/owner/project/bearer/deadline/privacy/cleanup seams from approveda8e8138. No persistent helper/application modification. Expected files only local checks/approval/attempt/result evidence. Validate both explicit encodings using synthetic decimal strings and integer/string documented projectNumber forms; reject booleans/nondecimal/foreign project/missing values. Assert original saved fingerprint remains unchanged and no output retains raw number or new digest. Negative tests: neither match, both match, wrong-project exact number, number changes, unsupported encoding; no consumer/identity fallback. Run19existing payload/parser checks unchanged. Positive/subset/empty/omitted/negative response tests retained. Two-encoding test fixtures establish contract only, not actual project identity. No SQL/browser/concurrency change or unnecessary fixture. Reserve exclusive new attempt; existing signal/deadline/reap cleanup unchanged. Stop before credentials if any check fails.

## Exact external operation and boundaries

Maximum3CLI/oneHTTPS, no operation/request retry. Same exact inventory as APP013_P08_CALLER_PROBE_CORRECTION_OPERATION_20261028.md, subject only to comparator change above:
1. Existing active CLI owner must privately match debynyhan@signmons.com.
2. gcloud projects describe signmons --format=json(projectId,projectNumber). Require exact signmons plus decimal numeric/string scalar, normalize to decimal string without guessing another project; run exact two-encoding match against prior fingerprint. Stop before bearer on no/ambiguous match.
3. gcloud auth print-access-token only after match; bearer process memory only.
4. POST https://cloudresourcemanager.googleapis.com/v1/projects/signmons:testIamPermissions with x-goog-user-project:signmons, existing owner bearer and JSON Content-Type. Exactly:

```json
{"permissions":["serviceusage.services.get","serviceusage.services.enable","serviceusage.services.use","serviceusage.operations.get","apikeys.keys.create","apikeys.keys.get","apikeys.keys.delete","apikeys.keys.getKeyString","resourcemanager.projects.getIamPolicy"]}
```

No six-service reread, API Keys/Policy Troubleshooter call, method execution or actual permission grant. Same output parser: object/optional unique string subset permissions; absent means empty; malformed/null/foreign/duplicates stop. Save requested/returned/not-returned names/UTC only. On errors save HTTPstatus/fixedsafeclassification, unknown stays unknown; no raw error/body/header/token/currentnumber/newhash. No policy/IAM/credential expansion. This checks project caller only; target runtime/signer/future key/service-scoped bind/organization policy access remains unqualified even if allnine returned.

Existing host owner configuration/cache refresh allowed; config override/impersonation/auth file/token overrides refused; no login/ADC/switch. No prompts/file/HTTP logs. Each command/request<=10seconds plus remaining deadline;65536byteHTTP cap, no redirects. No SDK internal retry-disable claim. Start on fresh exact approval todayOctober28 strictly before2:00p.m.Eastern, reads<=10minutes and process closeout<=15minutes, latest2:15p.m. No password/Terminal/attendance. Late approval refuses unstarted, no renewal. Drop raw/token refs; close handles/end/reap owned children on every exit; save truthful closeout and no-mutation evidence. No DBsession/private target plan; no invented purge/session check. Read-only rollback: no provider state changed.

Excludes API enable/dependencies, new key/payload/restrictions, IAM grants/role/policy change, account/Firebase-user/database lookup/write, signing/user-token exchange, runtime reactivation/deploy, Stripe/payment/events/messages/spending. API states remain dated12:02; full permission/lifecycle/currentaccount/job/role and separate owner service-retention/access/authentication/restoration/payment decisions still needed. No overnight secret/target plan retention.

Finish: exact prior fingerprint match classification plus nine project caller findings or fixed stop; no3Aacceptance or resource activation. Governance baseline/consistency/25safeguards/backendarchitecture/bothwhitespace before/after evidence/docs; preserve unrelated AGENTS.md.4/8walkthrough,0/27newlyclosedR1,6/60legacy,0/13intelligence unchanged. **Explicit serialization correction proposal before implementation; no silent rebind or retry.**

Official permission/payload references: https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage ; https://docs.cloud.google.com/api-keys/docs/access-control ; https://docs.cloud.google.com/resource-manager/docs/access-control-proj ; https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions . Public docs describe API contracts, not current authorization or historical producer encoding.

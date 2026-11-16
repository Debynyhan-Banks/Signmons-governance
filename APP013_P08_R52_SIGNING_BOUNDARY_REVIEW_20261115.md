# APP-013 / 3A — R52 signing-boundary local review

Read-only local source review completed on November 15, 2026. Inspected backend source: `e4212d9c11856fb6b75684773b96c244ef497743` in `/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery`. R52 native operation: `5f34f28c-318c-4f70-a88f-fb0504712a85`. This record authorizes no external read, credential action, signing request, runtime change or payment attempt.

## Observed boundary and evidence limits

R52 retained `SIGN_EXCHANGE_REFUSED` at `TOKEN_INTENT`, with authentication stage `SIGN`, failure category `HTTP` and HTTP status `403`. No Checkout or payment occurred. Independent closeout and private purge completed; the final residual is `AUTH_OUTCOME_UNKNOWN`. Preserve that original result and all consumed receipts unchanged. This review does not retroactively clear the residual or identify the historical provider cause.

The actual client dispatches signing before key retrieval and token exchange. A SIGN HTTP403 therefore locates the refusal at the IAM Credentials signing request. It does not, by itself, establish a particular permission, credential-scope, service, policy or propagation cause. The client retains the safe stage/category/status, not the provider denial body; discarded detail cannot be reconstructed from local source.

## Exact inspected request and caller

All source paths below are relative to the backend checkout above.

| Boundary | Inspected source | Finding |
| --- | --- | --- |
| Effective client import | `evidence/APP-013/p08-real-client-binding-local-20261031/source/bound-clients.mjs:1-2,29-46` | The assembled client uses the current coordinator-auth `client.mjs`, after exact owner/binding and database checks. It does not invoke the historical adapter directly. |
| Signing request | `evidence/APP-013/p08-coordinator-auth-local-20261031/source/client.mjs:9,15` | POST to `https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com:signBlob`. JSON body is a `payload` containing the base64 unsigned JWT. Headers are `Authorization: Bearer <owner access token>`, `x-goog-user-project: signmons`, and `Content-Type: application/json`; redirects are refused. No token or payload is reproduced here. |
| Signer identity binding | `evidence/APP-013/p08-coordinator-auth-local-20261031/source/authority.mjs:99-117` | `signing.serviceAccount` derives from the approved `plan.runtimeIdentity`, matching the runtime service account. The caller cannot supply an alternate signer URL. |
| Native owner token | `evidence/APP-013/p08-native-entry-local-20261101/source/native_io.py:85-105` | The native parent checks the active owner and absence of impersonation/credential-file/token-file overrides, then obtains an access token using `gcloud auth print-access-token --account=debynyhan@signmons.com`. The token stays in memory and is passed through the existing child credential interface. |
| Child owner recheck and HTTP status | `evidence/APP-013/p08-native-entry-local-20261101/source/transports.mjs:45-57,80-96` | The child rechecks owner/configuration and uses the supplied owner token. The HTTPS transport restricts hosts and preserves the actual bounded HTTP status. This is not independent proof of the token's claims or the provider's denial reason. |

No deterministic local target, method, header, caller-source or signer-identity mismatch was found in this bounded inspection. This finding is source review, not a new provider observation or a claim that signing is usable.

## Matching role, service and effective-access checks

The exact signing role is `projects/signmons/roles/signmonsP08ServiceAccountSignBlob`, containing `iam.serviceAccounts.signBlob`. The runtime conditional binding names `user:debynyhan@signmons.com` on the same runtime service account, bounded by the operation's start/workEnd timestamps. Role and binding definitions are validated before use.

Relevant source:

- `evidence/APP-013/p08-https-output-category-local-20261029/source/composed_qualification.py:20-27` pins owner, runtime identity, custom role and required services, including `iamcredentials.googleapis.com`.
- `evidence/APP-013/p08-https-output-category-local-20261029/source/qualification_launch.py:690-696,724-738,902-921` checks current services, consumer-project permissions including `serviceusage.services.use`, identity-management permissions, exact role definition and retired bindings. Its initial identity `testIamPermissions` list does not include signBlob; the later native effective-access check below is separate.
- `evidence/APP-013/p08-native-bridge-local-20261029/source/bridge.py:95-100,109-129` constructs and validates the exact operation-conditioned signing binding. `evidence/APP-013/p08-restoration-local-20261028/source/restore.py:64-70,88-89,218-228` preserves the corresponding owner/member/role/condition checks.
- `evidence/APP-013/p08-live-binder-local-20261029/source/coordinator.py:160-170` requires exact IAM bind/readbacks and then all four Policy Troubleshooter results to be `CAN_ACCESS`, before key creation and authentication.
- `evidence/APP-013/p08-access-sequence-local-20261028/source/diagnostics_stage.py:23,34-38,141-150` includes the tuple `debynyhan@signmons.com` / `//iam.googleapis.com/projects/signmons/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com` / `iam.serviceAccounts.signBlob`, sent to the existing v3 IAM troubleshooter with request receive-time condition context. `evidence/APP-013/p08-native-bridge-local-20261029/source/bridge.py:161-169` supplies the current observation time and validates the returned access state.

Reaching SIGN through this source means the preceding mandatory effective-access prediction gate passed. Thus this is not merely a missing policy-membership check. The prediction and the later signing request are different observations; neither the source nor the HTTP403 alone explains why the latter was refused.

## Specific UNKNOWN and smallest next decision

The unresolved fact is the provider's reason for refusing this exact R52 IAM Credentials request despite the preceding checks. No local code correction is justified by this review alone. Do not repeat the full connected run, sign another payload, renew credentials, change IAM or add a new diagnostic mode on that basis.

The smallest proposed next decision belongs to the owner/cloud custodian: inspect an existing Google audit record for this precise R52 `signBlob` failure, if available. Limit any separately authorized read to the relevant time, principal, target resource, method, status and safe denial reason; exclude request payloads, tokens, keys and unrelated records. This document creates no live packet or request authority. Audit-record availability and whether it contains a useful denial reason remain UNKNOWN. An absent or inconclusive record must remain inconclusive and does not authorize a signing retry or configuration change.

Completed: actual client/request/token-source trace, matching role/service/effective-access review, and known-versus-UNKNOWN reconciliation. Remaining: the specific provider refusal reason, actual same-job authentication/payment/event/application-gate evidence, any future attempt's final cleanup and owner acceptance. R52's own independent restoration and private purge have completed. Implementer owns exact source/evidence reconciliation; owner/cloud custodian owns any new external read decision. Next observable result, only after separate approval, is a safely bounded existing audit-record finding or an explicit unavailable/inconclusive result.

No runtime, manifest, pointer or historical-result file changed. No provider, credential/cache, SQL, browser or signing action was performed for this review. No new runtime tests were run or provider fix claimed. Documentation validation passed: frozen baseline before/after, cross-repository consistency, backend governance baseline, architecture, 25 governance tests and whitespace in both repositories. Accepted 1A/1B/2A/2B remain **4/8**; **3A OPEN**; R1 newly closed **0/27**. **No scope deviation.**

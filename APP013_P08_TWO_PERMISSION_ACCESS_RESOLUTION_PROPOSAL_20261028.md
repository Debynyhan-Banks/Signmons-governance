# APP-013 / 3A / P08 — two-permission access-resolution proposal

Status: PROPOSAL ONLY. The owner's “i approve” authorizes this finite planning result, not implementation or external action. Section R1-W01 / APP-013 / 3A remains unchanged.

## Acceptance trace and verified gap

The unchanged 3A criterion is the same admitted job completing authentic Stripe Sandbox payment, matching signed settlement and recovery, followed by owner acceptance. The connected workflow is payment-policy enforcement → payment → booking/dispatch readiness. Authentication and runtime access remain prerequisites; they are not new acceptance sections.

Stage A result `APP013_P08_STAGE_A_RESULT_20261028.md` establishes exactly two missing effective permissions:

1. the dedicated P07 runtime identity cannot `firebaseauth.users.get` on project `signmons`;
2. the approved owner cannot `iam.serviceAccounts.signBlob` on that exact dedicated runtime identity.

The owner can already perform Firebase user get/update. Policy Troubleshooter is enabled and retained. These facts do not establish whether suitable custom roles already exist and do not authorize any role, binding, Firebase action, signature, token, API key, runtime restoration or payment.

## Existing implementation to reuse

The tested disabled restoration controller in backend evidence `evidence/APP-013/p08-restoration-local-20261028/source/restore.py` already models the narrow future branches:

- a preexisting active project custom role containing exactly `firebaseauth.users.get`, conditionally bound to the dedicated runtime identity on the Signmons project;
- a preexisting active project custom role containing exactly `iam.serviceAccounts.signBlob`, conditionally bound to the owner on the exact dedicated runtime service account;
- absolute operation-start/work-end IAM conditions, exact readback, and same-block removal/readback;
- strict refusal of role creation (`ROLE_CREATION_NOT_BOUND`) and any role with extra permissions, wrong scope, wrong stage, deleted state or unpinned identity.

Therefore a second grant framework is unnecessary. The missing fact is the exact existing custom-role inventory and definitions. The current restoration source can be bound only after those facts and the later lifecycle decision are explicit.

## Alternatives

1. **Recommended — qualify exact preexisting one-permission roles first.** Prepare and test one disabled, source-locked role-candidate reducer. A later separately approved read-only operation lists project custom-role metadata once, keeps raw output only in process memory, and retains only zero-to-two exact candidate role IDs, definition hashes, active/deleted classification and counts. If both exact roles exist, pin them for the later restoration operation. No grant or policy mutation occurs.
2. **If an exact role is absent — stop and present a separate creation/lifecycle decision.** The smallest technical option is one custom role per missing permission. Creation, retention versus retirement, titles/descriptions, role IDs, conditions and cleanup must be owner-approved before implementation or external action. Do not silently create roles during qualification.
3. **Use predefined broad roles — reject for the current card.** Firebase Viewer/Admin and Service Account Token Creator contain authority beyond the two demonstrated gaps. They would enlarge the security boundary without evidence that 3A requires it.
4. **Redesign authentication/runtime — defer.** Replacing the current owned-account, dedicated-identity and signing flow expands architecture and does not resolve the immediate verified gap more safely.

## Recommended bounded local preparation

Source SHA at proposal time: backend `5536fb3`; governance `cb7f1da`. Existing restoration/authentication sources and tests are inputs and remain unchanged.

Expected new files are limited to a fresh disabled evidence copy containing one role-inventory parser/controller test pair, a source manifest and sanitized local evidence. The controller will not contain credentials, a live target plan, provider mutations or IAM binding commands. Repository application/runtime files remain unchanged.

Finite checklist:

- accept only canonical `projects/signmons/roles/<role>` names and project `signmons`;
- consume a serialized role-list response through a fake command adapter and reject malformed, duplicate, foreign-project, deleted, disabled/deprecated, extra-permission, missing-permission and over-cap outputs;
- classify independently the exact lookup and signing permission, including zero/one/multiple candidates; multiple candidates must stop for owner selection rather than choose by order;
- hash canonical candidate definitions and retain only candidate role IDs, hashes, exact permission, stage/deleted state and aggregate counts; prove raw unrelated role names/descriptions/permissions are absent from saved evidence;
- enforce one attempt, source/decision binding, bounded command deadline, SIGINT/SIGTERM child cleanup, no retry and truthful unknown-output reporting;
- prove the native/external adapter is disabled and refuses before owner authorization or any command;
- reuse the restoration controller's exact role-definition checks in an integration test so the qualifier cannot accept a role that restoration later rejects;
- remove synthetic fixtures and verify zero child processes/scratch files; run required governance baseline/consistency/safeguard, backend architecture and both whitespace checks.

Positive, negative, concurrency and recovery tests are required. Browser tests are not applicable because no browser or product UI changes. Database tests are not applicable because no database path changes. Existing Stage A/restoration/authentication test results remain historical and must not be presented as new passes.

Local rollback removes only the fresh disabled evidence copy and synthetic fixtures. No accepted milestone, pointer denominator, runtime resource or provider state changes.

## Later read-only qualification, not authorized here

After the bounded local proof, present one exact operation for separate approval. Proposed limits: existing owner gcloud authorization; owner/project binding checks plus one project custom-role metadata list; raw response in memory only; at most two exact candidate records saved; one attempt/no retry; USD 0 incremental allowance; no attendance or password. The exact source hash, operation ID, date/window, command ceiling, deadline and closeout must be fixed in that later document.

If both candidates are uniquely qualified, a still-later exact restoration operation may use the already-tested conditional binding/readback/removal seams. If either is absent or ambiguous, stop without grants and return the smallest owner decision. No permission or role will be inferred from a name.

## Remaining independent Stage B blocker

Resolving these two permissions alone does not make Stage B ready. `APP013_P08_ACCESS_BLOCKERS_RESULT_20261028.md` records that the existing exchange key has browser restrictions incompatible with the native Node exchange path. A separately approved compatible temporary API-only test-key lifecycle, or an already owner-designated compatible key, remains required. API Keys enablement, key string access, key creation/deletion, Firebase activation, signing/token exchange, runtime restoration and payment remain outside this proposal.

## Decision requested

Approve Alternative 1 for bounded local role-candidate qualifier preparation and isolated tests only, or defer. This decision would authorize no provider read, IAM role or binding creation/change, Firebase action, signing/token, API key action, runtime restoration, database action, Stripe/payment, deployment, spending or attendance window.

Accepted 1A/1B/2A/2B remain 4/8; 0/27 newly closed R1, 6/60 legacy and 0/13 intelligence remain unchanged. **No scope deviation; this proposal resolves one demonstrated prerequisite fact before any access action.**

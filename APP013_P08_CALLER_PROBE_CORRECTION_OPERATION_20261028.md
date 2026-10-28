# APP-013 /3A/P08 — specific caller-probe correction and fresh read

Status: PROPOSED; no correction/external follow-up implemented or authorized yet. Operation 0f717eaa-9f12-4bd2-8059-caf1c6370c07. Backend source d635958 plus preserved result evidence; governance source4c59d72 plus this result/correction proposal. Owner decision pending. Prior ac8a8999-8836-46a5-83e1-c4aab8bafca4 is consumed; do not reuse it.

## Demonstrated gap and alternatives

The approved ten-entry payload returnedHTTP400 without a permission verdict. It included policytroubleshooter.iam.troubleshoot, an API method identifier without verified IAM-permission mapping. Prior sanity checks validated lexical/response contracts but missed this semantic gap. Actual provider cause is UNKNOWN, not retrospectively attributed to that entry. Six completed service reads and their evidence remain unchanged. API Keys and Policy Troubleshooter were DISABLED; four other named services ENABLED.

Alternative1 recommended: remove only the unverified method identifier; validate nine existing names against the explicit public permission references below; after fresh exact approval and successful bounded local contract checks, run one reduced caller-project probe. Alternative2: defer, retaining disabled resources and unknown owner permissions. Neither alternative enables APIs, grants permissions, creates keys or changes authentication. No new subsystem, application code, acceptance section/count or MVP feature. Effort limited to payload/parser checks plus at most3CLI/oneHTTPS. No new spending allowance.

## Complete finite section card

Section R1-W01/APP-013/3A/P08; acceptance remains APP013_REMAINING_EXECUTION_CONTRACT.md3A same-job Sandbox payment/recovery, not this diagnostic. Reuse current operation config/owner/project/bearer/deadline/privacy/read sanitation and process cleanup seams. Source/read evidence: result.json at backend evidence/APP-013/p08-access-prerequisites-result-20261028; prior contract-checks.json at p08-access-prerequisites-preparation-20261028. Expected changed interfaces: only one ephemeral request payload and its local sanity/result evidence; no persistent helper/application change or new permission.

Finite checklist BEFORE any external read: verify immutable proposal/owner decision/source/clean unrelated changes; validate all nine permissions against explicit documentation; exact serialized payload/URL/header/request count; reject the removed method identifier/duplicates/wildcards/foreign names; valid complete/subset/empty/omitted responses; reject null/duplicate/foreign/nonlist responses; prove zero allowed service-state requests and no mutation endpoints. All must pass locally or stop before credentials/provider reads. Retain commands/results/failed checks. Existing one-attempt reservation/refusal, deadlines/signals/child reaping reused unchanged; no browser/SQL/concurrency implementation change, so no new browser/database fixture claims. No fake fixture is live permission proof.

## Exact fresh external inventory

One new attempt; no request/operation retry or consumer fallback. Existing-owner host gcloud configuration/cache refresh only. No login/ADC/impersonation/credential overrides; prompts and file/HTTP logs disabled. Reuse local_environment_gate before credentials. Each command/request<=10seconds and remaining deadline; bounded outputs/65536byteHTTP/no redirects. No SDK internal retry-disable claim.

1. gcloud auth list --filter=status:ACTIVE --format=value(account); privately require established owner debynyhan@signmons.com, save match boolean only.
2. gcloud projects describe signmons --format=json(projectId,projectNumber); require exact signmons and valid decimal project number; compare its in-memory SHA256 to prior bound fingerprint37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54; no number persistence. Drift stops, no rebinding.
3. gcloud auth print-access-token; bearer only in process memory, no arguments/environment/files/logs/chat.
4. Exactly one POST https://cloudresourcemanager.googleapis.com/v1/projects/signmons:testIamPermissions; Authorization bearer plus x-goog-user-project:signmons; Content-Type application/json. Exact body:

```json
{"permissions":["serviceusage.services.get","serviceusage.services.enable","serviceusage.services.use","serviceusage.operations.get","apikeys.keys.create","apikeys.keys.get","apikeys.keys.delete","apikeys.keys.getKeyString","resourcemanager.projects.getIamPolicy"]}
```

This POST reads caller permissions only; no requested method is executed. No six-service reread and no Policy Troubleshooter/API Keys method call. Successful object has optional permissions list; absent means empty; present must be unique strings/subset of request. Save requested/returned/not-returned names and UTC only. HTTP error retains status and existing safe fixed classification, no raw error; unknown cause stays unknown. No retry/loosened parser/header removal/alternate identity on stop. API state/organization constraints may independently block future actions even if names returned. This does not establish service-scoped servicemanagement.services.bind, dedicated runtime/signer/key effective access or full restoration qualification.

## Fresh timing, privacy, closeout and exclusions

Start on exact owner approval todayOctober28 strictly before2:00p.m.Eastern; reads within10minutes, all child/request process closeout within15minutes and no later than2:15p.m. Refuse expired-unstarted; no automatic renewal. No Terminal/password/attendance. Reserve exclusive attempt before first credential command. Drop bearer/raw references, close handles and end/reap children on success/stop/signal/deadline; save truthful sanitized result and closeout times. No private target plan/database session created, no invented purge/session readback. No provider mutation/rollback. Existing resources remain disabled.

Excludes API enable/dependency activation, key creation/value/restriction change, grants/custom-role creation/policy changes, account/DB/Firebase-user reads or changes, signing/user-token exchange/runtime restoration/deployment, Stripe/payment/event/customer action or spending. Rollback is no changed provider state; failed probe stops. Result is nine caller-project findings or fixed stop, never3A acceptance. Owner separately decides later service-enable/retention and full lifecycle/authentication actions after remaining access facts. Current owned account/job/role still unqualified.

Checks before/after governed documentation/evidence: frozen baseline/cross-repository consistency,25governance safeguard tests, backend architecture and both whitespace. Existing dirty backend AGENTS.md preserved and excluded from commits. Accepted1A/1B/2A/2B,4/8;0/27newlyclosedR1,6/60legacy,0/13intelligence unchanged. **Specific preparation correction proposed before implementation/fresh external action.**

## Public permission mapping

- serviceusage.services.get/enable/use and serviceusage.operations.get: https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage
- apikeys.keys.create/get/delete/getKeyString and serviceusage.operations.get for API-key LRO: https://docs.cloud.google.com/api-keys/docs/access-control
- resourcemanager.projects.getIamPolicy: https://docs.cloud.google.com/resource-manager/docs/access-control-proj
- Probe request/optional response: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions
- Removed entry is documented as a method: https://docs.cloud.google.com/policy-intelligence/docs/reference/policytroubleshooter/rest/v1/iam/troubleshoot ; https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_policytroubleshoot_v1

Public documentation does not prove actual authorization or diagnose the savedHTTP400.

## Consumed result — October28

R1-W01/APP-013/3A/P08. Owner approveda8e8138 via call_65682567dedc44eeaae97265f158219d.19local payload/parser checks passed before credentials; nine permission names mapped to official references. One attempt0f717eaa-9f12-4bd2-8059-caf1c6370c07 at12:11:35–12:11:36Eastern used2CLI/zeroHTTP. Owner matched; current signmons project output reached the numeric fingerprint check, where raw UTF8 decimal SHA256 did not equal the saved fingerprint. P08_CALLER_PROBE_STOP_PROJECT_BINDING_DRIFT; no bearer requested or permission verdict. Process closeout verified/on time; no mutations/retry. Backend evidence/APP-013/p08-caller-probe-result-20261028/. Original consumed attempts preserved.

Preparation uncertainty: prior saved fingerprint lacks its exact encoding contract; current comparator assumed raw decimal UTF8, and local checks did not cover historical fingerprint serialization. Therefore actual project drift versus digest-contract mismatch is UNKNOWN. The original producing source was not recovered from local evidence/current-day session tool records; no provider reread attempted. Implementer owns this missing shift-left check. Proposed APP013_P08_PROJECT_FINGERPRINT_CONTRACT_OPERATION_20261028.md explicitly allows raw-decimal or canonical JSON-string digest of the same exact current numeric project number, always against the unchanged prior fingerprint. No guessed/replaced binding or alternate project. Only after fresh owner approval, local two-encoding tests and an exact match may the existing nine-permission probe proceed in a new attempt; neither match stops. No correction/external follow-up implemented under consumed authority.

Remaining: caller permission verdict, diagnostic API enable/retention decision, compatible temporary-key lifecycle and effective target-resource/current account/job/role qualification, then separately approved authentication/restoration and same-job Sandbox payment/3A acceptance. Next observable result exact historical fingerprint match classification plus project caller findings, or precise stop. No Terminal/password/attendance; no API/key/IAM/account/database/authentication/runtime/payment/spending action authorized by this result. Accepted1A/1B/2A/2B,4/8;0/27newlyclosedR1,6/60legacy,0/13intelligence unchanged. **Preparation uncertainty disclosed; explicit comparator correction proposal before implementation.**

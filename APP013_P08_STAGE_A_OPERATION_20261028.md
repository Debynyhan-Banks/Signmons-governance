# APP-013 / 3A / P08 — exact Stage A diagnostic operation

Status: PROPOSED; owner decision: PENDING. R1-W01 / APP-013 / 3A / P08. Decision ID `43bfb0a9-f37c-4cb8-8a7c-a708129016a6`. Backend source `d19df960d22b53665485cbecc3a6a414067928e8`; source-manifest SHA256 `869cc37faab44ed294e5625c75075e2cb26ee4ceaf8d7d0459a1457db9be667e`; governance preparation source `e758c79`.

This is an exact external-operation proposal, not current authority. Separate owner approval must be recorded in this document and committed before the private one-use plan can bind or credentials can be resolved.

## Purpose and acceptance boundary

This operation establishes four current access facts required by the already-tested P08 authentication design. It does not itself satisfy 3A, authenticate the test operator, restore runtime resources, enter Stage B, create an API key or perform a payment.

The operation may conditionally enable `policytroubleshooter.googleapis.com` if its exact initial state is `DISABLED`. If enabled by this operation, it will remain enabled under the explicit retention decision `RETAIN_IF_ENABLED`. There is no disable, force, dependency-disable or usage-bypass action. Published Policy Intelligence pricing indicates no additional charge for features outside listed premium cases, but this is not a zero-cost guarantee. Incremental spending allowance is USD 0; any displayed paid requirement or incompatible dependency stops the operation.

## Exact window and authority

- Date: October 28, 2026, Eastern time.
- Start: 1:15 p.m.; start strictly before 1:30 p.m.
- Normal work ends: 1:38 p.m.
- Process closeout and sanitized result: by 1:43 p.m.
- Private-plan purge: before 1:45 p.m.
- One operation attempt; no retry. The operation is consumed by start, success, refusal, interruption or unknown provider outcome.
- No attendance, Terminal input or password is required. Existing signed-in owner `debynyhan@signmons.com` host authorization/cache refresh only.

After approval is recorded, the implementer may create one private `0600` plan containing the already-established numeric project binding and unchanged canonical JSON-string fingerprint. The plan must bind this document's committed SHA256, governance commit, decision ID, a fresh operation UUID, source-manifest hash and exact timestamps. The private plan is deleted with absence readback by the purge deadline. Project number and bearer remain private and are never written to public evidence or chat.

## Exact action sequence

1. Verify source manifest, this committed approval document and private plan hashes before credentials.
2. Verify current owner, exact `signmons` project ID, numeric project number and unchanged canonical project-number fingerprint.
3. Acquire one OAuth bearer in process memory. Never print, persist or export it.
4. GET exact Policy Troubleshooter Service Usage state.
5. If already `ENABLED`, do not mutate it. If exactly `DISABLED`, submit one enable request, poll only its returned operation up to six bounded reads, require exact enabled response and perform one enabled readback.
6. Submit exactly four Policy Troubleshooter requests:
   - dedicated P07 runtime identity / Signmons project / `firebaseauth.users.get`;
   - owner / Signmons project / `firebaseauth.users.get`;
   - owner / Signmons project / `firebaseauth.users.update`;
   - owner / exact dedicated P07 service account / `iam.serviceAccounts.signBlob`.
7. Accept only the five pinned overall-access states. Only four `CAN_ACCESS` results mark Stage A as a Stage B candidate; Stage B action remains unauthorized.
8. Clear the bearer, terminate tracked child processes, purge controller scratch, write sanitized result/closeout and delete the private plan.

Maximum commands/requests: three exact `gcloud` commands; thirteen HTTPS requests when conditional enable reaches the maximum six polls, or five HTTPS requests when preenabled. Redirects, oversized/malformed output, foreign operation/resource, unsupported state, changed identity/project/fingerprint, deadline/clock rollback, raw provider error or any unlisted host/action stop safely.

## Unknown outcome and stop rules

A lost or ambiguous response after enable submission is `ENABLE_OUTCOME_UNKNOWN`. Do not resubmit, diagnose adjacent resources or disable the service. Preserve only a sanitized residual and require a separately approved reconciliation. Interruption must clear credentials and terminate children; it cannot claim provider rollback. If closeout is unconfirmed, report `CONTAINMENT_UNCONFIRMED` and stop.

No API Keys/API-key lifecycle, Firebase user lookup/update, signing, token exchange, database, runtime restoration, IAM grant/role, secret, Stripe/payment/event/customer, deployment, billing change or new allowance is included. No old consumed plan or approval may be reused.

## Observable result and next dependency

The result is exactly one of: four current diagnostic verdicts plus verified process closeout; pre-credential refusal; provider-safe stop; or enable-outcome unknown plus verified local containment. Successful Stage A facts permit preparation of the separate complete Stage B card only; they do not authorize it.

Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **No scope deviation; this is the separately governed external action anticipated by the approved local launch-binding card.**

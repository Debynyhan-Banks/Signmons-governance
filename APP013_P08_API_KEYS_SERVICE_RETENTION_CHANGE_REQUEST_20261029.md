# APP-013 / 3A / P08 — API Keys service cleanup change request

**Owner decision: Alternative 1 approved for local cleanup design and tests only. No provider action.** Section R1-W01 / APP-013 / 3A remains the same-job Sandbox payment acceptance. The owner first selected disable/readback of the API Keys service after deletion of the one owned test key, then approved the narrower Alternative 1 below after reviewing the provider contract and pricing. Backend `9ea5306` proves an after-cutoff independent closeout seam, but the combined binder is not launch ready.

## Demonstrated gap

The existing packet's `serviceRetention` is `UNDECIDED_REFUSE_LIVE`; its cleanup marks `SERVICE_RETENTION_DECISION_PENDING` after enabling the service. The [Google Service Usage disable API](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable) applies to the project service and can reject dependent services. Its `CHECK` option rejects disablement if the service or dependents had usage in the prior 30 days. A test operation that uses API Keys to create/read/delete its key therefore cannot count on `CHECK` yielding an immediate verified disable. `SKIP` would omit that usage protection and could affect other project use. Neither branch supports a guaranteed same-block disable/readback under the current evidence. This is an inference from the provider contract; actual service usage and dependencies are not yet qualified.

[Google's API Keys pricing page](https://cloud.google.com/api-keys/pricing) states the API Keys API is free of charge; [Service Usage pricing](https://cloud.google.com/service-usage/pricing) is also currently free. That does not price the future authentication, Cloud Run, database or other services and does not itself authorize any spend.

## Recommended Alternative 1 — retire the owned key; retain the management API enabled

Change the future cleanup acceptance from “disable API Keys service after test” to: delete the exact newly owned API key, verify its `deleteTime`/ownership and absence of usable key string, remove the two temporary IAM bindings, revoke/disable the test account, retire temporary runtime/database/secrets, verify normal traffic and sessions/private plans, and retain `apikeys.googleapis.com` enabled. Record service state and the owner decision in the final readback; no broad service disable is attempted. This preserves capability for other project keys and avoids relying on a disable call that may fail after recent use. The future external operation still needs a finite allowance, current-state qualification and separate exact approval. No additional walkthrough section or R1 denominator change; local binder work remains within P08 and precedes same-job 3A payment.

Cost/effort: no direct API Keys or Service Usage fee according to the cited provider pricing pages. Other operation costs remain unknown until the exact plan is prepared. Engineering work is a narrow service-retention branch plus local negative/closeout tests and the existing authentication/restoration journal binding; no new subsystem is proposed.

## Alternative 2 — keep the owner's disable target, but accept a possible residual

Attempt `services.disable` with `checkIfServiceHasUsage=CHECK` and `disableDependentServices=false` after key deletion. If Google returns `FAILED_PRECONDITION` or the readback is not `DISABLED`, leave `SERVICE_DISABLE_UNCONFIRMED` and stop. Do not use `SKIP`, force or retry. This preserves the desired target but cannot meet the current same-block verified-containment requirement, so it is **not recommended for a live launch** without an owner-approved residual policy and a separate cleanup plan. It could delay 3A again.

## Alternative 3 — isolated project

Create a dedicated test project so the service lifecycle is isolated. This adds project, IAM, billing, Firebase and runtime identity decisions and potentially new costs; it materially expands scope and is not recommended for the first same-job Sandbox proof.

## Decision and boundaries

The owner approved Alternative 1. The prior local disable preference is superseded for the future design; this decision authorizes only local binder design and tests, **not** provider reads/changes, keys, IAM, authentication, deployment, Stripe/payment or spending. The next implementation card must still prove one source-locked journal, actual auth/restoration adapters, independent closeout, one-use/cutoff/signal/residual rules and private purge. R10 remains consumed. Accepted walkthrough 4/8; R1 newly closed 0/27. **Explicit owner-approved cleanup-design deviation; no external action.**

# APP-013 / 3A / P07 deployment, destination and read-path readiness proposal

Status: **prepared for owner review; not authorized for execution**. Proposed replacement attended window: **October 20, 2026, 10:30–11:45 a.m. Eastern**, with the operation starting strictly before **10:45 a.m.**, readiness work ending by **11:15 a.m.**, mandatory containment by **11:35 a.m.** and support through **11:45 a.m.** This is a new operation after three contained preflight stops; none of the consumed operations is retried.

Plan `84e0824b-71c1-491a-89b6-b25fa695d1f7`; packet `fdaf1a0b-1100-4dd8-b993-a5976144dd85`; proposed operation `08472fce-01ec-445f-92cd-06ddbd08d860`.

## Replacement-controller repair

The consumed 9:00 operation stopped before mutation because its subprocess environment discarded the signed-in Cloud SDK environment. The consumed 9:30 operation stopped before mutation because its Firebase helper required unavailable Application Default Credentials. The consumed 9:45 operation passed the repaired Cloud preflight and then stopped before mutation because its database preflight incorrectly required role membership that the reviewed zero-membership boundary intentionally forbids. Every mandatory closeout verified `p06_intake_runtime` closed with zero sessions and no change.

The third repair preserves the validated authenticated Cloud/Firebase path and checks the actual administrator capability, `rolcreaterole`, instead of membership in the runtime role. Nineteen focused tests exercise the full remaining controller path with mocked provider/database responses, the exact deployment envelope, cumulative mutation classification, new-secret reconciliation and tag/traffic containment. The controller retains fixed sanitized receipts, hidden private input, exact resources, no retry and mandatory closeout. The exact image, safety flags, event set, database query, cost ceiling and success/rollback states below are unchanged.

## Requirement traceability and purpose

- Approved section: APP-013/3A/P07. The frozen finish remains one same-job Sandbox payment whose authentic matching Stripe event clears the persisted payment gate while redirect-only, failed, foreign, duplicate and late outcomes fail closed.
- Release source remains backend `cec82163bd67fe939d88aacb6fedf2d9c126b90e`; the latest contained-stop evidence head is backend `c426c319c240879dfb7c7ebf2f5aabfa5161c9d7`; governance includes the second repair preparation at `8ef85b1`. No application source changed.
- Reviewed image: `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:a88e64566133b9e734d245a928d0ade10b5064ff76d8e4fc712a4e3def3f0191`, produced by build `2cfff9d9-bfe1-4166-a5a2-4d8d2acdb0b8` from exact source archive SHA-256 `6b499c4431a2e10d2fd032d167232bfb710209b9d6fa5056df1de236cc5b8400`.
- Accepted customer-workflow input: retained job `9180bef4-561d-47a0-869f-925e6a3dfd96`, recorded `CREATED` after accepted 2B.
- Demonstrated missing evidence: the image is undeployed; the connected-accounts destination is absent; its API version and signing-secret binding are therefore unknown; and the child runtime is closed, leaving no approved exact-job read path. Evidence: backend `evidence/APP-013/p07-stripe-runtime-qualification-result-20261020.md` and `evidence/APP-013/p07-backend-image-build-result-20261020.md`.
- Customer-workflow advance: leave one isolated P07 revision at zero normal traffic, one disabled exact Stripe Sandbox destination with a numeric signing-secret binding, and a verified exact-job read path. This removes the four named P07 readiness blockers so a later P08 proposal can cover one Checkout and authentic event proof.

This proposal changes no acceptance criterion, section ID, dependency, denominator or payment policy. It is the already-recorded next P07 operation. **No scope deviation.**

## Exact resources and disabled target state

| Boundary | Exact target |
| --- | --- |
| Cloud | Project `signmons`, region `us-east5`, service `signmons-calldesk-staging` |
| Preserved normal route | 100% normal traffic on `signmons-calldesk-staging-app013dbrot2`; no normal traffic transfer |
| Candidate revision/tag | `signmons-calldesk-staging-app013p07ready1`; tag `app013-p07-ready`; 0% normal traffic |
| Candidate URL | `https://app013-p07-ready---signmons-calldesk-staging-p572d6wipq-ul.a.run.app` |
| Stripe endpoint | Candidate URL plus `/webhooks/stripe`; Signmons LLC Sandbox/Test; Connected accounts |
| Database | Existing child secret `signmons-staging-p06-child-database-url:2`; existing role `p06_intake_runtime` |
| Existing Stripe key | `signmons-staging-stripe-secret-key:1`; payload never read or copied |
| Webhook secret | One new numeric version of existing `signmons-staging-stripe-webhook-secret`; returned version recorded, never assumed or printed |
| Runtime identity | Existing `signmons-calldesk-runtime@signmons.iam.gserviceaccount.com`; no IAM change |
| Local operator preview | Backend `cec8216` UI bound only to the candidate URL; 61 files, archive 469,315 bytes, SHA-256 `f0fe3458de5aa94885e973c86df8985971d9e9d2988f1e8971f2e5f3af2c7a31`; secret-pattern scan passed |

The candidate must explicitly keep `DEV_AUTH_ENABLED`, `SCHEDULING_ENABLED`, `STRIPE_WEBHOOK_LIVEMODE`, `SMS_DELIVERY_ENABLED`, `BACKGROUND_WORKERS_ENABLED` and `STAGING_PHONE_TEST_ENABLED` false. Controlled-intake runtime configuration is absent. The existing customer return URL remains the staging HTTPS `/payment/status` URL. The reviewed runtime envelope is pinned at 1 CPU, 512 MiB memory, concurrency 40, timeout 60 seconds, maximum instances 1, minimum instances 0, ingress `all`, CPU throttling true, startup CPU boost true and the existing runtime identity.

Official behavior checked for this proposal: Cloud Run supports a tagged `--no-traffic` revision and removal of its tag; tagged zero-traffic revisions can be addressed directly. Stripe connected-account webhook endpoints bind a URL, exact event list, API version, enabled/disabled status and a unique secret returned at creation. Cloud Run secret environment variables should use a numeric version. See [Cloud Run tagged zero-traffic revisions](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration), [Stripe webhook endpoints](https://docs.stripe.com/api/webhook_endpoints), and [Cloud Run secret references](https://docs.cloud.google.com/run/docs/configuring/services/secrets).

## One attended operation, no retry

### 1. Fresh no-write preflight

Before any mutation, read and compare:

1. Both repository heads and the immutable registry digest against the anchors above.
2. Cloud Run normal revision, 100% normal traffic, identity, limits, current tags and proposed revision/tag absence. Refuse if `app013dbrot2` is not the sole normal route or the target/tag already exists.
3. Existing numeric secret metadata only: child database version 2, Stripe key version 1 and webhook version 5 enabled; never access payloads.
4. Child database controls: `p06_intake_runtime` is `NOLOGIN`, connection limit zero, expired and has zero sessions.
5. Stripe: Signmons LLC Sandbox/Test, exactly one enabled connected account, and no current connected-accounts event destination. Read the account-default event API version offered by Workbench. Stop before creation if it is hidden, preview/beta, requires an account-wide upgrade or cannot be recorded exactly.
6. Existing isolated Firebase user metadata only: staging owner identity remains disabled and bound to the accepted tenant with role `owner`. Do not enable it or mint a token in P07.

Any drift, missing visibility, real/live mode, extra connected account, existing unknown destination, secret payload exposure, broad database lookup or required IAM grant stops the operation before mutation.

### 2. Create and contain the Sandbox destination

In the already signed-in Stripe Sandbox/Test account, create exactly one **Connected accounts** event destination named `Signmons P07 same-job sandbox` at the candidate `/webhooks/stripe` URL. Select only:

- `checkout.session.completed`
- `checkout.session.async_payment_succeeded`
- `checkout.session.async_payment_failed`
- `checkout.session.expired`
- `payment_intent.payment_failed`
- `charge.refunded`

Use the exact stable account-default API version recorded at preflight; do not upgrade the account or choose a preview. Do not send, resend or generate an event. Capture the one-time signing secret only through hidden local input and add it as one new version of `signmons-staging-stripe-webhook-secret`; no clipboard/chat/log/file persistence and no secret output. Immediately disable the destination and read back Sandbox mode, Connected accounts scope, disabled state, URL suffix, exact six-event set and API version. Record only booleans, bounded state and the returned numeric secret version.

If the destination cannot be disabled immediately, if any delivery appears, if the secret cannot be stored without disclosure, or if the returned metadata differs, disable or delete the new destination, disable the new secret version if created, record the stop and proceed to mandatory containment. Never recreate or retry.

### 3. Open the exact child read path temporarily

The owner enters the saved CHILD administrator password privately in Terminal; it never enters chat, arguments, logs or receipts. Reuse the previously reviewed child-role control boundary to set only `p06_intake_runtime` to `LOGIN`, connection limit 10 and an expiry no later than 11:15 a.m. Eastern, with zero sessions before activation.

Using the existing version-2 child connection and `p06_intake_runtime`, run one repeatable-read, transaction-level read-only query restricted to the accepted job and its tenant. Confirm only:

- exact job found once, `CREATED`, undeleted and unchanged tenant binding;
- no `Payment` row, no calendar event and no calendar operation;
- saved intake admission still has a payment approval timestamp and 64-character digest;
- current pricing/policy binding is not yet applied;
- tenant connected-account value is present, equals the single enabled Sandbox account and `chargesEnabled` is true.

Rollback the read-only transaction. Retain only booleans, counts bounded to 0/1, state names and equality results. Never retain provider IDs, customer fields, policy payloads, URLs, credentials or raw rows. A missing/changed/foreign job, payment/calendar activity, stale approval, account mismatch or disabled charges stops before deployment.

### 4. Deploy the exact isolated revision

Deploy the exact image digest once as revision `app013p07ready1` with tag `app013-p07-ready`, `--no-traffic`, the existing runtime identity, child database secret version 2, Stripe key version 1 and the newly returned numeric webhook-secret version. Preserve service resource limits and set the six safety flags false. No migration runs.

Read back and require:

- candidate image digest exactly matches `sha256:a88e64566133b9e734d245a928d0ade10b5064ff76d8e4fc712a4e3def3f0191`;
- candidate is Ready, tag URL exact and normal traffic remains 100% on `app013dbrot2`;
- candidate receives 0% normal traffic and minimum instances are zero;
- database/Stripe references are the exact numeric versions above, with test mode explicit;
- liveness returns 200 and readiness returns 200 only while the bounded child role is open;
- Stripe destination remains disabled, so no webhook is delivered.

Serve the prepared operator preview only on loopback and verify its compiled API origin equals the candidate URL. Do not enter a Firebase token, apply policy, create/recover a payment request or publish the UI.

### 5. Mandatory closeout and retained ready state

Whether the operation passes, refuses or becomes uncertain:

1. Set `p06_intake_runtime` to `NOLOGIN`, connection limit zero and expired; terminate only that role's child-database sessions; verify zero sessions.
2. Verify the Stripe destination is disabled and no event delivery was attempted.
3. Verify normal traffic remains 100% on `app013dbrot2`.
4. On full success, retain the Ready 0%-traffic P07 revision/tag, disabled destination and enabled numeric webhook-secret version for a later P08 decision. With the role closed and destination disabled, no Checkout or webhook can run.
5. On any failed or uncertain deployment/configuration step, remove the candidate traffic tag, leave the destination disabled, disable the new webhook-secret version, preserve the old normal revision and version 5, and record a named stop. Do not delete or destroy secret versions without a later decision.
6. Erase private local input and temporary secret transport. Preserve only sanitized receipts and the local preview archive until P08 review.

Closeout is authorized to finish after the ordinary action window if required for containment. It does not authorize a retry or corrective provider transaction.

## Observable result and evidence

Success is `P07_READY_DISABLED`: exact image Ready at 0%, normal route unchanged, exact job/account read checks pass, destination disabled with exact six events and recorded stable API version, numeric signing-secret reference present, child role closed and zero sessions, and local preview bound to the tag. The four prior blockers become closed as readiness evidence; no payment result is claimed.

Failure is one named stop with `possibleMutation`, containment result and remaining cleanup owner. `READY`, HTTP 200, a Stripe destination row or a secret version alone is not success.

Sanitized receipts must include attempt reservation, preflight, destination metadata, secret-version number only, child activation/read/closeout, deployment/readiness, traffic readback, final result and evidence index with hashes. Raw provider responses, secret material, database rows, account/customer identifiers and private browser links stay outside repository evidence.

## Cost and authority requested

If approved, the owner authorizes exactly:

- one connected-accounts Sandbox destination creation and immediate disable/readback;
- one new version on the existing webhook secret and candidate reference to its returned numeric version;
- one bounded child-role LOGIN/read-only-query/NOLOGIN lifecycle;
- one exact-image tagged Cloud Run deployment at 0% normal traffic and its readiness requests;
- the mandatory rollback/containment actions above.

Proposed operational allowance: **USD 1.00** for Cloud Run/request/log usage, not a hard billing cap, plus at most one retained active secret-version cost, **up to USD 0.06 per month above the billing account's free tier** until P08 or explicit retirement. Stripe destination configuration itself creates no payment. No Checkout, card entry, payment, refund, event test/resend, customer contact, booking, SMS, email, migration, normal-traffic shift, source build, IAM grant, Firebase-user activation, token mint, UI publication, repository merge or production action is included.

Debynyhan Banks owns the exact operation approval, private CHILD input, signed-in Stripe attendance, any later P08 approval and final 3A acceptance. The implementer owns exact binding, preflight, sanitized evidence and mandatory closeout. P08 remains a separate proposal and approval after `P07_READY_DISABLED`.

Accepted progress remains **6/60 packages, 4/8 walkthrough milestones and 0/13 fully accepted pilot rows** until owner acceptance changes a recorded denominator.

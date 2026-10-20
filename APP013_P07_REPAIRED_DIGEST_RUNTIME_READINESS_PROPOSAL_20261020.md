# APP-013 / 3A / P07 repaired-digest runtime-readiness proposal

Status: **Alternative 1 and its startup correction owner-approved; disabled package locally tested; no external action is authorized**. On October 20, 2026, Debynyhan Banks approved the dedicated-role/secret/identity and 24-hour retirement proposal, then approved the four-secret correction in `APP013_P07_STARTUP_CREDENTIAL_CORRECTION_PROPOSAL_20261020.md`. Fresh private package `/private/tmp/p07-repaired-runtime-readiness-20261020-prep1` passes 28 focused tests and no-action verification; live modes refuse without a window and exact live approval. The supplied 6:45–8:15 p.m. Eastern availability block remains unattempted and unconsumed. No database, IAM, secret, Stripe, deployment, cost-bearing or cleanup authority exists.

## Requirement traceability and customer workflow

- Approved section: R1-W01 / APP-013 / 3A / P07.
- Acceptance criterion served: the retained accepted job must open one authorized Stripe Sandbox Checkout from its current approved policy, and only an authentic signed event for the exact Sandbox account, connected account and stored Stripe resource may settle it and clear the persisted payment gate. Redirect-only, forged, foreign, failed, duplicate, late and out-of-order outcomes remain fail-closed.
- Accepted workflow input: job `9180bef4-561d-47a0-869f-925e6a3dfd96`, historically accepted in `CREATED` state at 2B. Current state must be refreshed through an exact-job read before any readiness mutation.
- Repaired application source: commit `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd`.
- Exact built image: `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da`, from build `9ee7772a-62b1-4a07-86ad-0c3b9daf3032` and uploaded source SHA-256 `893432c1de02c8068237711908099d452dd8e18dde6603240007bc61db5ed456`.
- Tested payment-role boundary: `scripts/fixtures/p07-payment-runtime-role-review.sql`, SHA-256 `35785d3857f6fc9b01042d6dee3137eebb18950601fb1b8e7644e340be8fb83c`; current verifier SHA-256 `f8c5b02e8909e2b6c8d239e8f2340b414a083da69efc42bf73af0744913ca967`.
- Demonstrated missing behavior: no live `p07_payment_runtime` role or credential exists; the repaired image is unused; the connected-accounts destination is absent; exact API/signing-secret binding is unknown; and current same-job payment/calendar absence has not been refreshed.
- Customer-workflow advance: leave one isolated repaired revision at zero normal traffic with a dedicated least-privilege payment credential, a disabled exact Sandbox destination and verified containment. This enables a later separately approved P08 Checkout/event proof without weakening the accepted P06 intake boundary.

This is a prerequisite inside the existing P07 section. It does not add a feature, acceptance section, ledger row or denominator. **Approved architecture deviation before implementation:** introduce a dedicated P07 runtime identity and two dedicated P07 secrets instead of reusing the shared P06 child secret and shared runtime identity. Only local package preparation follows from this decision; external implementation remains separately approval-gated.

## Credential-isolation decision

| Alternative | Security and operational effect | Decision status |
| --- | --- | --- |
| 1. Dedicated P07 database role, dedicated database secret and dedicated Cloud Run service identity | Keeps the stronger payment credential outside the accepted P06 secret and its existing accessors; lets the candidate receive only the secret access it needs | **Owner-approved for package preparation; live action still separate** |
| 2. New version of the existing P06 child secret with the existing runtime identity | Fewer resources, but every accessor to that secret can reach the stronger payment credential; a numeric version pin does not isolate access | Not recommended |
| 3. Expand `p06_intake_runtime` or use an administrator credential in the app | Breaks the accepted intake boundary or gives the app excessive authority | Rejected |

The recommended design follows the existing locally proved grant map and preserves `p06_intake_runtime`, its password, `signmons-staging-p06-child-database-url:2`, original fixture and negative tests unchanged. It uses a user-managed service identity with resource-level access to only the exact required secrets. Google documents user-managed least-privilege service identities for Cloud Run and recommends numeric secret-version pins for environment variables.

## Exact proposed resources and retained disabled state

| Boundary | Exact proposal |
| --- | --- |
| Project/region/service | `signmons` / `us-east5` / `signmons-calldesk-staging` |
| Preserved normal route | 100% normal traffic on `signmons-calldesk-staging-app013dbrot2` |
| Candidate revision/tag | `signmons-calldesk-staging-app013p07atomic1`; tag `app013-p07-atomic`; 0% normal traffic; min instances 0 |
| Candidate image | Exact repaired digest above; no tag-only image reference |
| Database role | New `p07_payment_runtime`; exact reviewed grants only; no membership, inheritance, ownership, superuser, CREATEDB, CREATEROLE, replication or BYPASSRLS |
| Database secret | New `signmons-staging-p07-payment-database-url`, returned numeric version only, expected first version but never assumed |
| Service identity | New `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com` |
| Secret access | Resource-level `roles/secretmanager.secretAccessor` for that identity only on the new P07 database secret, the existing test Stripe-key secret and the new P07 webhook secret |
| Stripe key | Existing `signmons-staging-stripe-secret-key:1`; value never displayed, copied or persisted |
| Webhook secret | New `signmons-staging-p07-stripe-webhook-secret`, returned numeric version only |
| Stripe destination | Signmons LLC Sandbox/Test, Connected accounts, candidate `/webhooks/stripe`, exact six-event set, immediately disabled |
| Runtime safety | `DEV_AUTH_ENABLED=false`, `SCHEDULING_ENABLED=false`, `STRIPE_WEBHOOK_LIVEMODE=false`, `SMS_DELIVERY_ENABLED=false`, `BACKGROUND_WORKERS_ENABLED=false`, `STAGING_PHONE_TEST_ENABLED=false`; no controlled-intake runtime configuration |

The existing service identity remains unchanged for the currently serving revision. Attaching the new identity to the zero-traffic candidate must not grant it project-wide roles. Before any grant, the operation must read the effective resource policies and stop if broader inherited access makes the proposed isolation claim false. The deployer must also prove its exact `iam.serviceAccounts.actAs` authority; if a new grant is required, it must be separately enumerated in the executable package, temporary where supported, removed during closeout and read back absent.

## Finite preparation checklist after architecture approval

1. After the startup-credential correction decision, create a fresh private plan/packet/controller with new IDs, exact UTC/Eastern window, strict start cutoff, one-attempt reservation, hidden input, command deadlines, signal containment and mandatory cleanup. Old readiness packages remain immutable and unusable.
2. Bind the exact backend/governance heads, repaired image digest, source/build receipts, role fixture/verifier hashes, accepted job, proposed resources, event set, safety flags, dollar allowance and retirement deadline.
3. Implement only the resource operations below and a cleanup-only recovery mode. The controller must refuse before provider access when approval, hashes, time, identity, target state or cost bindings differ.
4. Add local tests for positive, refusal, partial-failure, concurrent invocation, signal interruption, command timeout, post-mutation uncertainty, cleanup-only recovery and truthful persistence failure. No mocked success can substitute for live readback.
5. Run the required governance baseline/consistency/safeguard checks, backend architecture check and both whitespace checks. Application behavior tests remain the already recorded repaired-image evidence unless source changes.

Any newly demonstrated need for broader grants, another secret, another identity, schema/application changes, normal traffic, a second destination or a new UI is a stop and another owner-reviewed change proposal.

## Proposed one-operation sequence

### 1. Fresh read-only preflight

Before mutation, verify the exact repository/image/source bindings; normal traffic and current revision; absence of the proposed role, secret names, service identity, revision/tag and connected-accounts destination; numeric metadata for existing Stripe key version 1; Signmons LLC Sandbox/Test with exactly one enabled connected account; and the accepted job's exact tenant identity through the CHILD administrator connection. Read current IAM policies without secret payloads.

The exact-job administrator transaction is read-only and restricted to that job and tenant. It must confirm one undeleted `CREATED` job, saved payment approval timestamp and digest, no Payment row, no calendar event and no CalendarOperation, no applied payment pricing/policy snapshot, one present tenant connected-account value matching the single enabled Sandbox account, and `chargesEnabled=true`. It rolls back and retains only bounded booleans/counts/state/equality results. A mismatch or unavailable read path stops before mutation.

### 2. Provision the isolated payment credential

Using the current CHILD administrator password through hidden local input, create exactly `p07_payment_runtime` initially `NOLOGIN`, connection limit zero and expired. Apply the exact reviewed grant fixture and read back role attributes, zero memberships/ownership and the bounded column/table privileges. Generate one random role password only in memory; create the dedicated database URL with certificate/hostname verification; create the new P07 database secret and one version without placing the credential in arguments, files, chat or receipts.

Open the role only for the bounded readiness window, with connection limit 6 and expiry no later than the ordinary-operation end. Verify direct `current_user=session_user=p07_payment_runtime`, exact database and zero foreign sessions. Run only the existing safe read/display path and transactionally rolled-back permission probes needed to confirm the deployed Prisma shape; do not bind policy or persist Payment, StripeEvent or AuditLog rows on the accepted job.

### 3. Create the dedicated identity and secret access

Create only `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com`. Grant it resource-level Secret Accessor on the new P07 database secret and existing Stripe test-key secret. Create the new P07 webhook secret resource empty, then grant that same resource-level access. No project-level role, service-account key, token-signing role, runtime impersonation grant, Firebase role or access to any P06 secret is included.

Read back exact allowlisted bindings and reject any extra member/role created by the operation. If the deployer lacks already valid attach authority, stop before deployment unless the later exact approved package explicitly lists one bounded `roles/iam.serviceAccountUser` binding and its mandatory removal/readback.

### 4. Create and contain the Stripe Sandbox destination

Create exactly one Connected accounts endpoint at the candidate tagged URL with only:

- `checkout.session.completed`
- `checkout.session.async_payment_succeeded`
- `checkout.session.async_payment_failed`
- `checkout.session.expired`
- `payment_intent.payment_failed`
- `charge.refunded`

Use the exact stable non-preview API version observed at preflight. Do not upgrade the account, send/resend/generate an event or create a Checkout. Capture the creation-only signing secret through hidden transport, write it as one numeric version of the new P07 webhook secret, immediately disable the destination and read back Sandbox mode, Connected accounts scope, disabled status, exact URL, exact event set and API version. If immediate disable or secret persistence is uncertain, disable/delete the new destination, disable the new secret version and enter containment without retry.

### 5. Deploy one exact zero-traffic candidate

Deploy the repaired digest once as the exact revision/tag above, `--no-traffic`, with the dedicated service identity, numeric P07 database secret version, Stripe key version 1 and numeric P07 webhook-secret version. Preserve the reviewed 1 CPU / 512 MiB / concurrency 40 / timeout 60 seconds / max 1 / min 0 / request-based CPU envelope. No migration runs.

Require exact digest, Ready state, exact tag, 0% normal traffic, normal route still 100% on `app013dbrot2`, numeric secret pins, explicit test mode, all six safety flags false, liveness 200 and readiness 200 while the role is open. The Stripe destination remains disabled. No Firebase token, policy bind, payment request, Checkout, event delivery or UI publication is allowed.

### 6. Mandatory containment and retained state

Always set `p07_payment_runtime` to `NOLOGIN`, limit zero and expired; terminate only its sessions; verify zero sessions. Verify the destination disabled, no attempted delivery, normal traffic unchanged and no candidate minimum instances. Erase private input and transient secret transport.

On full success, retain only the zero-traffic revision/tag, disabled destination, dedicated disabled-at-database role, two enabled numeric secret versions and the three exact resource-level secret bindings for a later P08 decision. The executable package must bind a retirement deadline no later than 24 hours after readiness: if P08 has not begun under separate authority, cleanup removes the tag, disables the two new secret versions, removes the three secret-access bindings, disables the dedicated service identity and confirms the database role remains closed. Cleanup authority does not authorize a retry or payment.

On failure or uncertainty, remove the tag, keep normal traffic unchanged, disable/delete the new destination as safely supported, disable both new secret versions, remove every binding added by the operation, disable the new identity, close the database role and record any unconfirmed residual with its responsible owner. Do not destroy secret versions or drop the role automatically; those are separate irreversible cleanup decisions.

## Verification matrix and observable result

The live package must cover:

- positive exact resource/identity/digest/IAM/database/destination/deployment readback;
- foreign or stale job, existing payment/calendar work, wrong account/mode/API version, extra destination/account, source/digest/flag/traffic mismatch and unavailable administrator authority;
- role collision, grant drift, membership/elevation, hidden-input failure, secret-output detection and unexpected inherited access;
- destination created but disable/secret write/readback fails;
- identity/secret grants partly applied, deployment failure, readiness failure, signal interruption and command timeout;
- mandatory role/session/destination/tag/traffic/IAM containment and cleanup-only recovery;
- immutable attempt/result/consumed receipts and sanitized evidence with no provider IDs, customer fields, raw rows, URLs carrying private tokens or secret payloads.

Success is `P07_REPAIRED_RUNTIME_READY_DISABLED`: the exact repaired image is Ready at 0% normal traffic; normal traffic is unchanged; exact-job read checks pass; the dedicated role/grants/credential work only through the dedicated identity; the destination is disabled with the exact six events and stable API version; both secret references are numeric; the payment role is closed with zero sessions; and the retirement deadline is recorded. This is readiness evidence only and awards no 3A acceptance.

Failure is one named stop with `possibleMutation`, exact completed stages, containment result, unconfirmed residuals and responsible owner. `READY`, HTTP 200, an endpoint row, a secret version or a closed role alone is not success.

## Cost, authority and exclusions

The later executable proposal should request a **USD 1.00 operational allowance** for bounded Cloud Run/log/request use, not a provider-enforced cap. It would create two active secret versions. Google currently lists six active versions per billing account per month in the free tier and USD 0.06 per active version-month above it, prorated; therefore the conservative retained-secret allowance is **up to USD 0.12 per month above free tier**, plus access operations only if aggregate account usage exceeds the free tier. Actual billing remains unverified. Creating a service account, IAM bindings and a Stripe Sandbox destination does not itself create a payment.

No external action, spend, role/credential/secret/IAM change, destination, deployment or cleanup is authorized by this proposal. It also excludes Checkout/card entry, charge/refund, event generation/test/resend, normal-traffic shift, migration, Firebase activation/token mint, UI publication, booking, dispatch, SMS/email/customer contact, production action, repository push/merge and P08/3A acceptance.

## Decision and next step

Owner decision recorded: **Alternative 1 approved** for the proposed dedicated role, database secret, webhook secret, service identity, exact resource-level access and 24-hour retirement boundary. The owner next supplies one attended Eastern window of at least 90 minutes, with Terminal, the current CHILD administrator password and signed-in Stripe Sandbox access available. Passwords and authentication codes never enter chat. The implementer then prepares a fresh hash-bound no-action package, runs its local guard tests and presents that finished exact operation separately before any external action. Debynyhan Banks owns the later external-action decision and 3A acceptance; the implementer owns exact preparation, sanitized evidence and mandatory containment.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. The approved architecture decision changes no acceptance count or denominator.

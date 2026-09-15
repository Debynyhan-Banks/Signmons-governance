# APP-013 / 2B controlled activation packet

## Current: P06 item 3 release packet — preparation only, NOT executable

### Approved build attempt stopped — disabled build identity

Owner answered "yes" to the one-attempt, 20-minute, USD1 operational allowance request. This supersedes the older build-not-authorized statement below **only for that attempt**, not for IAM, retry, deployment or paid verification. At 2026-09-15 00:29 UTC (2026-09-14 local), submission uploaded a clean 520-file / 3.7MiB tracked source export from 53037fbd118cc4547061dfaf373c45b20a05962b, then Google rejected CreateBuild: `Provided service account ... signmons-build@signmons.iam.gserviceaccount.com ... is disabled`. Readback confirms disabled=true; latest build remains September12 build688616b2. No new build ID, build compute, image or digest was produced. No retry or identity substitution performed.

Uploaded source object remains `gs://signmons_cloudbuild/source/1789432140.891187-431a2066d4ef4ac3a5304a6d495f897b.tgz`, generation1789432141830104, 882435 bytes. Upload/storage may incur small charges; no invoice claim or zero-total-cost claim. No real credentials, .env, git history or untracked files included. Existing artifacts were not deleted. Current blocker is **disabled build service account**, owned by the project/IAM owner. Re-enabling it or selecting another identity requires explicit approval; a fresh build retry also requires authorization under the no-retry condition. Do not create a new build account or grant permissions by inference. Item3 remains open, item4 unchanged; no new section. No scope deviation.

Owner continuation "proceed" after startup review authorizes this documentation/read-only preparation. Source backend **53037fbd118cc4547061dfaf373c45b20a05962b**, governance **7e54dd35bf73833ee43ec1efb0a3183281c80766**. Existing backend PR21 remains open. No image build, release, key creation/access, IAM change, paid request or acceptance is authorized. This current section supersedes every older implementation-not-started, blanket Google-wait and next-card statement below; those are historical records, not current blockers.

### Item 3 qualification update — build-only approval request

Read-only continuation from backend b912ef5 / governance ed95c13 resolves the numeric metadata and build-cost inputs below; source to package remains 53037fbd118cc4547061dfaf373c45b20a05962b. No new image exists yet. Docker executable was not found locally; no installation attempted. Existing Cloud Build is the proposed path, not a new service.

Current enabled numeric versions, metadata only: signmons-staging-database-url **2**; signmons-staging-admin-token **2**; signmons-staging-conversation-data-key **2**; signmons-staging-openai-api-key **1**; signmons-staging-resend-api-key **1**; technician-link-secret **1**; signmons-staging-stripe-secret-key **1**; signmons-staging-stripe-webhook-secret **5**; signmons-staging-twilio-account-sid **1**; signmons-staging-twilio-auth-token **1**; signmons-staging-sms-consent-hash-key **1**. These are proposed immutable references for later review, not proof of payload correctness, access permissions or schema compatibility. No secret values accessed or bindings changed. Old phone-only key references remain version1 and must not be repurposed.

Last successful build 688616b2-30e1-4172-abd4-8c1765713348 used E2_HIGHCPU_8, a 1200s timeout, existing signmons-build@signmons.iam.gserviceaccount.com, source bucket signmons_cloudbuild, CLOUD_LOGGING_ONLY and the existing registry. Actual execution 2026-09-12 19:46:41.125–19:48:38.696 UTC was about 118 seconds; this is a historical sample, not a promised duration for the new source.

Build-only proposal for owner decision: **one attempt**, source53037fb from a clean tracked export containing only Docker-required source/build inputs (no .env, git history, private files or credentials), existing build identity/bucket/registry, E2_HIGHCPU_8, **1200-second timeout**, default disk/no private pool/no extra disk, unique artifact tag `p06-53037fbd118c`, no tag overwrite, no automatic retry, no deployment or provider test. Return resulting digest/provenance and measured duration/storage for review. Inspect actual existing build configuration before submission and stop rather than add permissions or resources if incompatible.

Cost basis verified 2026-09-14: [Cloud Build pricing](https://cloud.google.com/build/pricing) lists e2-highcpu-8 at USD0.0156/minute. Thus 20 minutes is **USD0.312 compute** before taxes; the 118-second historical sample would be about USD0.031. The listed free build allowance applies to e2-standard-2, not this worker; do not claim this build is free. [Artifact Registry pricing](https://cloud.google.com/artifact-registry/pricing) lists paid storage at USD0.000136986/GiB-hour above the account allowance (about USD0.10/GiB for 730 hours). Actual incremental layer size is not known before building. Existing repository readback is 3036.756MB, so do not assume free capacity remains. Repository scanning reports SCANNING_DISABLED because Container Scanning API is not enabled; do not enable scanning or invoke on-demand scanning in this action. Source storage/logging and any applicable transfer/tax charges remain additional; account discounts/credits were not verified.

**Requested operational allowance: USD1 for this one build/artifact action**, not a provider-enforced billing cap or recurring storage budget. Stop without retry at failure/timeout; do not claim artifact retention stops accruing storage after the build. No deletion of old artifacts, IAM change, secret access or Cloud Run action authorized. Owner must explicitly approve the build allowance before submission. New secret injection and schema qualification remain separate existing item3 release inputs; they do not block a build-only artifact but still block deployment/activation. No new section or package.

### Fixed checklist — unchanged

- [x] 1. Browser phone-code -> address -> job, locally proven with synthetic external providers.
- [x] 2. Default-disabled startup and packaged assets, locally proven at source above.
- [ ] 3. Exact release packet and owner review: this draft records verified bindings and explicit unresolved release inputs. **Not complete or deployment-ready.**
- [ ] 4. Separately approved capped staging run, closeout and owner acceptance.

Two fixed items remain. The work below belongs to item 3, not additional sections/packages. Prior full runtime evidence: backend evidence/APP-013/p06-startup-wiring.md, 2,359 passed / 3 skipped plus eight startup-path HTTPS browser cases. Those tests were not rerun for this documentation-only change.

### Current read-only resource evidence (2026-09-14)

| Binding | Verified value / status |
| --- | --- |
| Project / region / service | signmons / us-east5 / signmons-calldesk-staging |
| Runtime identity | signmons-calldesk-runtime@signmons.iam.gserviceaccount.com |
| Latest created/ready revision | signmons-calldesk-staging-00065-guw; old phone-preflight candidate |
| Old candidate image | us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:25e194acfd96299bb670de84e63b932d9dc69528e6f421ae42699f80fc9b3d75 — **not source 53037fb** |
| Normal traffic | 100% signmons-calldesk-staging-app013bounds; all nine existing tag mappings preserved |
| Candidate settings | 8080, 1 vCPU, 512 MiB; service template maximum instances 1 |
| Six candidate safety flags | DEV_AUTH_ENABLED, SCHEDULING_ENABLED, STRIPE_WEBHOOK_LIVEMODE, SMS_DELIVERY_ENABLED, BACKGROUND_WORKERS_ENABLED, STAGING_PHONE_TEST_ENABLED all literal false |
| New startup variables | Neither CONTROLLED_INTAKE_RUNTIME_JSON nor CONTROLLED_INTAKE_SECRETS_JSON present on old candidate |
| New customer-purpose secrets | Metadata list filtered to signmons-staging-customer returned no entries. No numeric versions established; no secret payload read |
| Existing bindings | Several existing secret bindings use latest; Stripe webhook is version 5 and old phone-only session/digest keys version 1. None qualifies new purpose keys by substitution |

The CLI selected metadata and environment names/secret references only; literal values were emitted only for the six public safety flags. This is not current database, Twilio account, Google quota/IAM or billing evidence. No real tenant or secret payload was queried.

### Proposed disabled-candidate diff — owner approval still required

1. Build/package exactly the source SHA above using the existing Dockerfile and registry. Bind the resulting digest and build provenance **before deployment approval**. Image does not yet exist; do not label the old image as this source or invent a digest. A charged build/push requires a separately approved cost allowance; none is assumed here.
2. Proposed candidate revision suffix `app013p06disabled` (full name `signmons-calldesk-staging-app013p06disabled`) and proposed new tag `p06-intake-disabled`. Check both for collision immediately before any approved operation; do not overwrite a collision. Preserve normal traffic at 100% baseline and all existing tags; no `--to-latest`, no replacement of phone-preflight. New tag origin is only a proposal until provider readback.
3. Set only new controlled envelope `CONTROLLED_INTAKE_RUNTIME_JSON={"enabled":false}` for this disabled candidate; leave controlled private material absent. Keep all six flags false. Use existing service/runtime identity/port/resources; no new service, public IAM grant, scaling change or tenant activation. The disabled path does not require provisioning new customer-purpose keys.
4. Before final exact diff, qualify current numeric versions for inherited required secrets without reading values; do not roll or rewrite old revisions. Review which inherited versions the new candidate uses rather than silently trusting mutable latest bindings. Verify staging database schema compatibility through an approved read-only method, without logging connection values or migrating a real database.
5. Itemize build, artifact storage, candidate startup/request/runtime and any secret-version/access costs with current account allowances. **No verified incremental cost or spending ceiling is established in this draft.** The old proposed USD0.70 verification allowance does not authorize infrastructure charges.
6. After owner approval of the resulting exact digest/config/cost diff only: deploy disabled/no-normal-traffic candidate, read back digest/revision/tags/flags, verify intake routes return 503 and unrelated health/webhook behavior remains intact. No phone/address call or real session/job is part of disabled deployment verification.

### Enabled-run bindings — remain separate from disabled release

The existing startup expects a strict server envelope plus separately injected `CONTROLLED_INTAKE_SECRETS_JSON`, not automatic Secret Manager fetching. That private JSON must map the exact numeric references to actual independently provisioned material. Resource labels alone do not prove that mapping. **The delivery/provisioning mapping is not yet qualified:** do not put secret values in a release YAML, command, repository or evidence, or assume Cloud Run composes independent secrets into JSON. Review the exact protected injection method and its resource/IAM diff before provisioning or enabling. If it requires changing the reviewed implementation, disclose that bounded correction before coding; do not silently add a new subsystem.

Required distinct purpose references: customer session (at most two keys), verification digest, dedicated mailbox fingerprint plus fingerprint version, and the correct Twilio token. No old phone-only, encryption or cross-purpose key reuse. Proposed session/digest names in the historical packet have not been created; fingerprint numeric reference remains unset. No project-wide secret access or service-account key download.

Exact run envelope must bind the deployed service/configuration/revision/HTTPS origin, current active tenant/integration/category, reviewed organization/payment/priority policies, DB-backed controlledRuntimeApproval and controlledPhoneApproval digests, current provider ownership/restrictions/rates, participant HMAC/notice, address account/policy, finite shared request limits and fresh absolute UTC start/end. No fixture defaults or test-database identities. Preserve existing liabilities. Current tenant/operator status, schema and provider restrictions have **not** been refreshed by this metadata-only pass.

Historical proposed run ceiling remains USD0.50 phone + USD0.20 address = USD0.70 verification liability, one START/up to five CHECKs, two explicit address requests, maximum 15 minutes. These are proposals, not current rate evidence or spending approval; no automatic resend, cap reset or extra correction. Phone proof is not SMS consent. Job creation is not payment/booking/dispatch/send authority. Stop/closeout must specify how pending requests settle, current approval is disabled, session is closed and unknown holds are reconciled; preserve committed job/audit records.

### Approval/finish conditions and next action

Implementer must first resolve **image/provenance, numeric inherited-secret bindings/schema, protected new-material injection, and current itemized costs** within this same item 3. Product owner then approves the exact external diff; no blanket approval of blanks. The minimal next decision requiring external authority is a **bounded image build/artifact action with an explicit cost allowance**, once its estimate is established; it is not deployment or a paid Verify test. Read-only qualification can continue without treating this draft as executable.

Item 3 closes only when the exact packet is populated and owner-reviewed, not because this draft exists. Item 4 remains the only subsequent fixed item. No new coding section promised or invented. Accepted packages **5/60 (8.3%)**, walkthrough **3/8 (37.5%)**, provisional **4–8 weeks at 25–30 collaborative hours/week plus external waits**, low confidence, unchanged. No scope deviation.

## Historical P06 runtime-wiring card — 2026-09-14 UTC

P06 item 2 source/interface/test inspection is complete in `APP013_P06_RUNTIME_WIRING_CARD.md`; implementation has not started. The card confirms the customer page is test-only and absent from the runtime image, no same-origin BFF is recorded, request budget is process-local, and existing phone admission is fixture-only or bound to the closed fixed-session staging runner. It defines a default-disabled loader, server-owned Cloud Run HTTPS mapping, controlled customer phone admission, shared PostgreSQL-backed admission/budget, existing-page phone states, same-origin delivery and finite integration matrix. Smallest owner decision: approve the recommended backend-served same-origin assets and shared database-backed patch, or identify the existing BFF/load-balancer path. Item 2 implementation/local proof and items 3–4 remain. No runtime/schema/cloud/provider/customer change or scope deviation implemented. Accepted 5/60; walkthrough 3/8; estimate unchanged.

## Historical P06 entry reconciliation — 2026-09-14 UTC

Owner said "proceed" after the bounded correction repair and the proposed P06 preparation. This authorizes preparation, not deployment or paid execution. Entry sources: backend 3667cda, governance 7be5f00; focused worktrees clean/fetched, backend PR21 open. P01–P05 locally accepted (5/60), walkthrough still 3/8. The historical preparation status below is superseded by this reconciliation; P06 is not complete. No scope deviation.

Read-only Cloud Run readback confirms service signmons-calldesk-staging / us-east5, runtime signmons-calldesk-runtime@signmons.iam.gserviceaccount.com, candidate phone-preflight -> signmons-calldesk-staging-00065-guw, normal traffic 100% signmons-calldesk-staging-app013bounds. Existing candidate image digest sha256:25e194acfd96299bb670de84e63b932d9dc69528e6f421ae42699f80fc9b3d75 is historical, NOT the new source. Six inspected candidate flags are false: DEV_AUTH_ENABLED, SCHEDULING_ENABLED, STRIPE_WEBHOOK_LIVEMODE, SMS_DELIVERY_ENABLED, BACKGROUND_WORKERS_ENABLED, STAGING_PHONE_TEST_ENABLED. Other tags unchanged. No secrets read or resources modified.

### Historical P06 checklist (superseded by fixed checklist above)

1. **Entry/packet reconciliation — complete locally:** record actual source, staging readback, completed local evidence and remaining wiring. Google support reply plus approved minimal-record/correction contract removes the stale blanket support-wait gate; no legal certification and no expansion of retained fields. Correction UUID stays in volatile server memory up to five minutes/session expiry, one-use; missing state refuses. P01 durable allowlist remains.
2. **Connected runtime wiring — source card complete; owner design decision and implementation/local proof remaining:** `APP013_P06_RUNTIME_WIRING_CARD.md` maps the exact loader/config/managed-HTTPS/phone/shared-budget/page/lifecycle interfaces and negative tests. It records that main.ts has no resources, controlled composition has no loader, browser phone/end paths are fixture-only, the budget is not shared, and the same-origin page is absent from the image. Do not promote the old phone runner or fixture modes. Owner must approve backend-served same-origin assets plus PostgreSQL-backed shared admission/budget and the controlled customer admission adapter, or name the existing external BFF/load-balancer path. Then implement one default-disabled patch and prove the same page from phone START/CHECK through one local job with synthetic external ports. Preserve raw webhook bytes and every tenant/session/policy/budget guard.
3. **Immutable disabled release packet — remaining, implementer prepares / owner approves:** bind source/image, resource names and numeric secret versions, database schema readback, tenant/organization/payment/category approvals, exact config/IAM diff, attribution/notices, managed ingress restrictions and itemized release costs. Current readback does not establish those gates. Re-read tenant/operator state and provider restrictions/rates; no old authorization reuse. Do not deploy until explicit approval of this exact diff; then verify disabled candidate and unchanged traffic.
4. **Capped connected run and closeout — remaining, owner authorizes and accepts / implementer executes:** one new protected session, phone code, eligible owner-confirmed real address, explicit submit and one test job; optional one correction. Proposed 15-minute window and USD0.70 verification envelope below remain proposals, not current spending permission. Privately confirm participant data and exact UTC window at execution. Capture truthful outcome and held liabilities, disable and read back, obtain 2B acceptance before P07/payment work.

Next observable result: a source-complete, default-disabled runtime-wiring card for item 2; then its same-page local phone-to-job proof. No invented config values, secret creation, migration, paid request, image build or deployment in this preparation checkpoint. Current evidence: backend evidence/APP-013/p06-entry-packet.md. Documentation/architecture/frozen/full consistency/21 governance regressions and whitespace checks apply to this docs-only checkpoint; prior 2,301 runtime tests are historical, not rerun here.

Status: **prepared for design review; NOT executable or approved for activation**. Owner authorized preparation after reviewing the bootstrap qualification. Source: backend f59dd78, governance 1cb2adb. Supplements APP013_2B_IMPLEMENTATION_CARD.md and the unchanged frozen five-section walkthrough. No scope deviation; accepted 3/8 (37.5%) unchanged.

## One observable result

One owner-participant, one new protected session, current phone verification and eligible confirmed address, one customer-reviewed draft and exactly one test job automatically created by Signmons after explicit submission and current approved tenant-policy checks. Routine operator approval is not required; separately authenticated operators handle exceptions without bypassing proof. This adopts APP013_2B_AUTOMATIC_ADMISSION_CHANGE.md; it does not activate the path. No payment, appointment, dispatch, customer confirmation message or production customer record. Correction stays in that same journey. An uncertain or expired result stops admission and preserves permitted draft state.

## Exact proposed reuse bindings

| Binding | Proposed value / qualification |
| --- | --- |
| Cloud project / region / service | signmons / us-east5 / signmons-calldesk-staging |
| Runtime identity | signmons-calldesk-runtime@signmons.iam.gserviceaccount.com |
| Candidate origin | https://phone-preflight---signmons-calldesk-staging-p572d6wipq-ul.a.run.app |
| Existing candidate | signmons-calldesk-staging-00065-guw; not the future integrated image |
| Normal traffic baseline | 100% signmons-calldesk-staging-app013bounds; must remain unchanged |
| Tenant proposed for reuse | a1adcfd4-15be-404b-9ac3-5edb1fda20f0; historically SUSPENDED; re-read status/ownership before any activation |
| Separate operator proposed for reuse | staging-phone-owner-20260912; historical disabled/revoked Firebase identity; exact tenant claim, owner role and stagingOnly restriction must be reverified |
| Server customer integration label | Proposed `integration:app013-controlled-intake`; server configuration only, not a provisioned identity or browser claim |
| Twilio Verify service | VA9aee2b6f81cdf797d4af79e939ab04f0, recorded account ending c417; verify exact account ownership and current restrictions before use |
| Google API | Address Validation in project signmons; deployed runtime authorization is not established by the earlier owner's local OAuth tests |
| Participant | Previously willing owner; privately reconfirm destination/address and current notice, never commit either value or OTP |
| Session / conversation | Fresh server-generated identifiers after approved activation; never reuse the closed test session |

Tenant/operator reuse is a proposal for this isolated test, not a claim that old permission covers job admission. The operator identity is for exception/recovery access, not the automatic service actor. Bind that service's exact internal authority and tenant automation policy in the completed card; never reuse a staff token for automatic admission. Existing historical records and all cost holds remain intact. No changes to the Eternity website or production tenant are involved.

## Proposed purpose-bound key references (not created)

Reserve proposed Secret Manager names in project signmons: `signmons-staging-customer-session-key` for CustomerConsentCredentials and `signmons-staging-customer-digest-key` for controlled recipient/proof binding. They are distinct from the old phone-only keys. Existence and collision checks must precede any separately approved creation; never overwrite an existing secret or assume its purpose. Customer session signing uses the existing 32-byte key requirement, with an explicit active key ID and versioned reference; no key material in this packet.

Numeric secret versions, runtime environment field names and exact least-privilege access diff will be bound to the implemented loader before execution review. No `latest` version, project-wide secret access, browser key, service-account key download or shared-key fallback. Do not create these speculative references before the Google retention/design gate closes. Existing encryption storage uses its reviewed key path; these proposed keys do not grant storage permission.

## Proposed bounded execution envelope

- One fresh 15-minute UTC window; literal start/end are intentionally unset until the owner is ready and gates pass. Missing times make the packet invalid, not renewable by an agent.
- One phone START, at most five CHECKs, no automatic resend or alternate channel. Proposed phone liability ceiling USD 0.50, subject to refreshed rates and explicit spending approval; not renewed historical authorization.
- At most two explicit address requests in that session: initial validation and, only if required, one customer-requested correction revalidation. Proposed address liability ceiling USD 0.20 total, subject to rates, approved content handling and explicit spending approval. More corrections preserve the draft and stop; no cap increase or background retry.
- Proposed combined verification liability ceiling USD 0.70 for this packet. This is a proposed application bound, not an invoice/account hard cap; unrelated traffic, build/runtime/storage and taxes are not covered. Separately itemize and approve release costs before deployment.
- Every dispatch reserves durable liability first; timeout, crash or ambiguous result keeps it held. Prior phone and Google holds must neither be subtracted nor reset to make this packet fit.
- Participant proof, exact source account, policy digest, tenant/session/revisions, current time and expiry are checked again at admission. A raw provider success or browser confirmation alone cannot admit a job.

## Release and execution approval checklist

All are mandatory; none is completed by approving preparation.

- [ ] Google or authorized terms review resolves permitted candidate/derived coverage/admission retention with exact fields, lifetime and deletion treatment. No inferred permission from encryption or a boolean.
- [ ] Owner reviews the complete 2B implementation card and proposed tenant/operator/key/ingress design; implementer resolves Google runtime authorization and exact loader interfaces without changing IAM by inference.
- [ ] Implement the existing finite patch map; required backend/UI/integration/security/recovery gates pass with version-matched dependencies. This packet is not a substitute for implementation.
- [ ] Bind immutable source SHA, image digest, numeric secret references, runtime identity, candidate revision, exact config/IAM diff and separately capped release cost. Preserve all normal traffic and existing unrelated tags; no production migration.
- [ ] Owner explicitly approves those configuration/release changes. Read back the disabled deployment and all safety defaults before issuing a session. Do not use old phone-only scripts to activate this flow.
- [ ] Refresh exact provider accounts, US-only/Fraud Guard, rates/caps, participant notice, tenant/operator state and privately held destination. Fill absolute UTC window and bind a canonical packet digest to durable approval.
- [ ] Owner explicitly approves one connected run with that exact packet and allowance. Keep general SMS delivery, scheduling, background workers, dev auth and Stripe live-mode disabled; the old STAGING_PHONE_TEST_ENABLED route stays disabled. Only the separately implemented controlled path can receive temporary authority.
- [ ] Demonstrate the same-session result, obtain owner acceptance, stop and reconcile all observed/unknown liabilities. Record sanitized receipts and actual outcome, not raw provider responses or identity tokens.

## Stop, recovery and closeout

Implementer stops new reservations immediately on owner stop, expiry, policy mismatch, cap exhaustion or ambiguous provider outcome; no auto-retry. An in-flight request cannot be recalled. Disable the controlled approval, close the session, revoke temporary operator credentials, restore tenant/operator inactive state and remove only this packet's temporary grants/mappings after readback. Keep necessary accepted test-job/audit/evidence records under approved retention; do not delete them as routine cleanup. General traffic remains on the baseline revision. Rollback the candidate only under the exact release plan; never remove unrelated tags/resources.

Closeout evidence: packet digest/window, source/image/config references without secrets, allowed request counts, actual provider result categories, current-proof/admission correlation and job count, stop/refusal result, final inactive readback, retained unknown holds and billing-reconciliation owner. Product owner accepts the user-visible result; implementer owns technical evidence/closeout. No claim of zero risk or total provider bill from application ceilings.

## Historical stop point (superseded)

This document prepares the requested configuration proposal. Implementation, release and run checkboxes remain open. The next decision is review of this proposed reuse/key/budget design, with provider retention resolution still required before completing the implementation card. Do not create another demo or new acceptance section while blocked.

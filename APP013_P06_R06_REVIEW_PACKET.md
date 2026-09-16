# P06-R06 consolidated staging setup review packet

Status: R06 review preparation, NOT executable and NOT R07 authorization. Current source backend23206a9/governance0157c8b; owner reviewed U02 and requested continuation. Owner approved regular-only initial diagnosis with one USD99 deposit. No emergency case, real charge, booking, dispatch or confirmation send. The full USD150 after-hours replacement business rule remains documented, not implemented. No new task authorized this turn.

Update: owner subsequently approved U02 to resolve the demonstrated bootstrap gap. See APP013_P06_U02_BOOTSTRAP.md and backend p06-u02-bootstrap.md for completed local implementation and exact exported interface. The historical draft below is not live execution authority. Bootstrap writes now have a tested atomic service/CAS/audit/readback/suspension path; final profile wording, actual prestate digest/timestamp, stable category binding, source/artifact check and fresh execution authorization must be included in R07/R08. U01's runtime activation remains separate. Original12+U01+U02=14; seven locally closed/seven original tasks open. No further addition.

## Current qualification delta and decision

Read-only refresh after U02: exact tenant still SUSPENDED at2026-09-12T22:46:30.011Z, profile/payment keys absent, runtime/phone enabled fields absent, zero categories/jobs/address operations/address-held micros. No raw settings or credentials read. Current non-system role inventory contains provider-managed cloud_admin/neon_service/neon_superuser; application-owner neondb_owner; and NOLOGIN p06_migration_owner/p06_migration_runner. There is **no existing limited application login**. neondb_owner has CREATEDB, CREATEROLE, REPLICATION and BYPASSRLS; it is not an appropriate credential to silently promote into the app. Earlier owner approval was for supervised operator backup/migration, not unattended runtime use or parent-capable credential exposure.

Smallest decision: approve preparing the child-only limited runtime-role configuration within the existing R06/R07/R08 least-privilege boundary. Proposed name p06_intake_runtime (not created): no object ownership, role memberships, SUPERUSER, CREATEDB, CREATEROLE, REPLICATION or BYPASSRLS; connect only to this child/neondb and use only the runtime's required tables/sequences. Exact object grants, credential handoff, expiry/revocation and local privilege tests must be qualified before R07 authorizes creation. Do not reuse migration roles or reset inherited administrator credentials. No code/helper expansion is authorized by this proposal; disclose any demonstrated need before implementing it.

Alternatives: reuse inherited owner at higher privilege/parent-credential risk (not recommended, would require explicit risk acceptance); leave runtime disabled (safe, no connected test). Recommendation is the restricted role, not another provider or product feature. This finding completes the privilege inventory, but prevents R06/R07 being called execution-ready. No further task/count added.

## Exact cloud permission proposal

Observed project policy etag BwZbetDk92Y=: named runtime has only direct project roles/firebaseauth.viewer; no service-account resource bindings. Existing Twilio-token secret already grants that runtime roles/secretmanager.secretAccessor. Owner principal user:debynyhan@signmons.com already has project roles/owner; read-only testIamPermissions on existing Twilio token returned versions.access, versions.add, secrets.setIamPolicy. No payload was accessed and no new owner role is proposed. This is not an assertion of every resource's effective permissions: recheck each exact created resource before payload operations.

| Exact principal / scope | Before | Proposed additive change |
| --- | --- | --- |
| serviceAccount:signmons-calldesk-runtime@signmons.iam.gserviceaccount.com / projects/signmons | Direct firebaseauth.viewer only | Add roles/serviceusage.serviceUsageConsumer; preserve all existing bindings |
| Same runtime / projects/signmons/secrets/signmons-staging-controlled-intake-material | Resource absent | After authorized creation, add roles/secretmanager.secretAccessor on this resource only |
| Same runtime / projects/signmons/secrets/signmons-staging-p06-child-database-url | Resource absent | After authorized creation with qualified limited-runtime credential, add roles/secretmanager.secretAccessor on this resource only |
| Same runtime / three new source-key resources | Resources absent | No accessor grant; read delivered bundle instead |
| Existing owner / new five resources and existing Twilio token | Owner authority already present; token access verified | No additional project/owner grant; action-specific permission checks before use |

Review-only command shapes: `gcloud projects add-iam-policy-binding signmons --member=serviceAccount:signmons-calldesk-runtime@signmons.iam.gserviceaccount.com --role=roles/serviceusage.serviceUsageConsumer`; and `gcloud secrets add-iam-policy-binding NAME --project=signmons --member=serviceAccount:signmons-calldesk-runtime@signmons.iam.gserviceaccount.com --role=roles/secretmanager.secretAccessor`, where NAME is **only** either new delivery bundle or child URL above. None executed. Fresh policy readback and additive merge required; never replace a whole policy or remove existing access. Consumer role includes additional read-only quota/policy/monitoring permissions, not just services.use. No token-creator, API enablement, downloaded key or project-wide secret accessor.

## Stable proposed bindings and numeric inherited versions

These are proposed metadata, not provisioned resources or owner policy approvals. Do not regenerate on retry:

- Category: c8fdb27a-abc6-4c70-86f2-4296a3262dcb, regular initial visit/diagnosis; use this same UUID in U02 and allowedServiceCategoryIds.
- Address account: c8c98ce0-ea9c-4ab3-b8a3-1c2957061fd3 maps permanently to Google project signmons for this controlled ledger. Zero current child operations established before choosing it. Never rotate it to evade holds. Previous local USD0.20 remains separate external liability; new ledger allowance USD0.20 gives USD0.40 combined address exposure, not a reset.
- Disabled revision signmons-calldesk-staging-app013p06disabled, tag p06-intake-disabled (already proposed). Enabled proposal signmons-calldesk-staging-app013p06enabled, tag p06-intake-enabled. Neither revision/tag appears in fresh listing. Expected enabled URL https://p06-intake-enabled---signmons-calldesk-staging-p572d6wipq-ul.a.run.app is a proposal, NOT an observed deployed origin; exact provider URL must match before R10. Preserve all nine existing tags and100% app013bounds traffic.
- Phone flow reserve500000micros, account ceiling1000000micros includes existing500000 hold; oneSTART/up to5CHECK, no resend. Address per-call100000micros, account/tenant/session each200000micros and2requests; manual combined-ledger ceiling400000 includes prior local holds. Browser proposal total/tenant/session60 each, starts1,inFlight2, <=15minutes; these are application-operation limits, not a Cloud Run request or invoice cap.
- Inherited numeric versions, metadata checked: ADMIN_API_TOKEN2; CONVERSATION_DATA_ENCRYPTION_KEY2; STRIPE_WEBHOOK_SECRET5; OPENAI_API_KEY1; RESEND_API_KEY1; TECHNICIAN_LINK_SECRET1; STRIPE_SECRET_KEY1; TWILIO_ACCOUNT_SID1; TWILIO_AUTH_TOKEN1; SMS_CONSENT_HASH_KEY1; STAGING_PHONE_SESSION_KEY1; STAGING_PHONE_DIGEST_KEY1. All selected versions ENABLED. Pin these on the new candidate only; preserve existing revisions. DATABASE_URL must instead use the new limited-child resource's actual returned numeric version, not the shared parent resource.
- New key IDs/versions: propose customer session key label p06-v1 and fingerprint version p06-v1; actual Secret Manager version numbers come from authorized creation/readback, not guessed1. Final runtime packet UUID/window, participant HMAC, policy approvals/digests and bootstrap settings digest are bound privately at their existing R08/R10 gates. Source entry for U02 is23206a9; no runtime-image rebuild for the operator tool.

## Bounded cost/control worksheet

Directory CLI lookup unavailable (Unknown command); directory site not readable through web tool. No install/upgrade; official sources used. Public list rates refreshed, not negotiated invoice evidence. Proposed approval envelope stays **USD2.70 one-time operating allowance** (USD0.70 verification plus USD2.00 infrastructure), **plus up to USD0.30/month gross for five retained secret versions**, separate from prior USD0.70 holds and existing account recurring charges. No spend approved here.

Finite scenario: one disabled release and one enabled release, no rebuild; preapproved shutdown returns the new enabled tag to disabled state after digest revocation. Up to60 supervised minutes overall (setup30/run15/closeout15), with R10's enabled window at most15minutes. Model conservatively three revision-hours at2vCPU/0.5GiB,1000requests,10MiB logs,100MiB North-America egress and1000secret accesses: CPU/memory USD0.5319, requests0.0004, logging0.004883, network0.011719, accesses0.003; approximatelyUSD0.56 gross before shared free allowances. The scenario is a buffer calculation, **not enforceable byte/instance/invoice limits**; startup/retries/public traffic/late metering can differ. Neon remains Free with no paid upgrade; displayed1.89/100CUh,0.04/0.5GB,0/5GB is delayed, recheck before execution. Existing0.25CU child for one hour is0.25CUh, not a new paid plan.

Stop initiating work at the authorized deadline or observed/estimated allowance exhaustion; revoke matching runtime/phone approval and remove only new test routing under preapproved closeout authority. No repeated deployment/send, new build, extra secret version, paid tier or silent window extension. Billing alerts are not hard caps; a guaranteed invoice maximum cannot be promised for the public service. Runtime scaling remains existing1vCPU/512Mi, revision max1/service max2; normal traffic/tags unchanged. Public request exposure persists until cleanup, even when intake is closed.

Secret-cost correction: **disabled versions remain billable**. Disabling is a safety measure, not cost elimination. Destruction after explicit retention/recovery review is separately authorized; do not automatically delete secrets or revoke unrelated consumers. Each new purpose secret uses automatic replication for one billed location; no rotation notifications or extra regional replicas proposed.

Sources: [Cloud Run](https://cloud.google.com/run/pricing), [network](https://cloud.google.com/vpc/network-pricing), [logging](https://cloud.google.com/products/observability/pricing), [Secret Manager](https://cloud.google.com/secret-manager/pricing). Verify lists USD0.05/success plus USD0.0083/US SMS; one successful one-SMS exampleUSD0.0583 fits proposed0.50 reserve before applicable extras, not an account-specific invoice guarantee: [Twilio](https://www.twilio.com/en-us/verify/pricing). Address reserve remains conservative and unchanged; [Google SKU rules](https://developers.google.com/maps/billing-and-pricing/sku-details) identify direct ValidateAddress as Pro; no Autocomplete session/new product proposed.

## Earlier review draft (superseded where updated above)

## Fixed targets and verified reuse

| Binding | Value |
| --- | --- |
| Google project / number | signmons /845074063310 |
| Cloud Run | signmons-calldesk-staging,us-east5; runtime signmons-calldesk-runtime@signmons.iam.gserviceaccount.com |
| Image | us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:ea47a8371a04f773a5c51fc4f939250b7045eba92d3cbbeb68e49ceb0240be35 |
| Image source |53037fbd118cc4547061dfaf373c45b20a05962b; registry digest refreshed read-only this turn; SLSA level unknown |
| Existing traffic |100%signmons-calldesk-staging-app013bounds; preserve every existing unrelated tag |
| Child | Neon soft-smoke-54063480/br-sparkling-sun-ay6gr5e8; ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech/neondb |
| Isolated tenant | a1adcfd4-15be-404b-9ac3-5edb1fda20f0; currently SUSPENDED, zero categories and no usable policy approvals |
| Integration label | integration:app013-controlled-intake, server-side label from existing activation proposal; no browser-supplied authority |
| Provider | Existing Signmons Twilio account endingc417/Verify service endingab04f0; token secret has one enabled numeric version1 (metadata only, payload/account correspondence still checked privately at authorized preparation) |
| Google | OAuth runtime identity, quota projectsignmons; API enabled,5/minute,10/day. No API-key injection |

## Proposed external delta — review before any execution

1. In project signmons create only the following absent purpose resources; refuse any collision instead of overwrite: signmons-staging-customer-session-key, signmons-staging-customer-digest-key, signmons-staging-customer-email-fingerprint-key, signmons-staging-controlled-intake-material, signmons-staging-p06-child-database-url. Three independent32-byte random keys; one delivery map; one exact child connection. Numeric versions are returned/read back after creation; never latest. No private values in repo, shell arguments, logs or clipboard. Existing encrypted/private-input safeguards apply. Do not alter shared parent DATABASE_URL or old phone/encryption keys.
2. Runtime Secret Accessor only on the new delivery bundle and child database resource, retaining required existing reviewed access. Preparing owner reads only three new source-key versions and existing Twilio token version1, and writes/reads the new bundle under exact source-bound authorization. No project-wide accessor grant. Full current principal/resource permission diff must be attached before R07 sign-off; this prose is not an executable IAM command.
3. Proposed runtime Google grant: project-level roles/serviceusage.serviceUsageConsumer to the named runtime only, if no equivalent usable grant is established. Live role metadata includes serviceusage.services.use plus read-only service/quota/policy and monitoring.timeSeries.list permissions. It cannot be described as a single-permission role. No Editor/Owner, API enablement, key download, impersonation or token-creator grant. A narrower custom role is an alternative requiring a separately explicit exact diff; do not silently choose it.
4. Exact isolated tenant only: separately authorized transactional setup changes SUSPENDED to ACTIVE, records current owner-approved organization and restricted fixed-deposit policy, and creates one regular initial-visit/diagnosis category. Preserve unrelated settings, history and all holds; audit changes. Controlled runtime/phone approvals stay disabled until R10/R11. Existing U01 tool does NOT create policies/categories or activate tenant status; exact setup command and rollback/readback must be reviewed before R07. Do not misuse synthetic fixture writers.
5. R09 disabled candidate uses the pinned image and numeric child secret reference; no phone/address calls. Later enabled revision/tag/origin are fixed and reviewed at R10, not a guessed existing revision. Preserve normal traffic. No new build, backup, migration, paid tier, number or provider change.

## Restricted policy and customer-facing draft

Use ETERNITY_PILOT_OPERATING_RULES.md's exact approved99USD deposit object; service fee disabled, no second deposit or surcharge. Organization draft: company Eternity Mechanical Services LLC; timezoneAmerica/New_York; hours Mon-Fri7am-7pm,Sat9am-5pm,Sunday emergency-only. Services for this test: regular initial HVAC visit/diagnosis only. Proposed greeting: Hello, I am the automated assistant for Eternity Mechanical Services LLC. Proposed tone:warm. Proposed fallback: We can collect your request for follow-up during business hours. Emergency service is subject to confirmed availability; this staging test does not dispatch a technician. Proposed FAQ: What area do you serve? / Our pilot serves Cuyahoga County, Ohio. Your address must be verified before submission. / Source: owner-approved service-area policy. Exact profile wording requires review, not fabricated approvedAt/actorId.

## Proposed allowance — not a hard invoice cap or spending approval

| Bucket | Proposed control |
| --- | --- |
| New phone verification |0.50USD reserve, oneSTART/up to5CHECK, no resend/fallback; prior0.50 hold preserved so account ceiling must include at least1.00 total liability |
| New address validation |0.20USD reserve,two explicit requests maximum; child ledger zero, prior local0.20 holds still tracked separately, never reset |
| New verification total |0.70USD, separate from prior0.70 holds |
| Setup/run/closeout infrastructure |Proposed2.00USD incremental operating allowance excluding the verification bucket and pre-existing account recurring charges; operational stop threshold, NOT enforceable provider invoice ceiling. Includes compute/logs/network/accesses; no build or paid tier. Exact total estimate remains sensitive to setup duration and network usage |
| Retained five secret versions |Up to0.30USD/month gross at previously verified list rate, before shared allowances/proration. This is recurring exposure and must be explicitly approved and retired after safe closeout under separate deletion/retirement authority |
| Existing artifact storage |Continues unchanged; same-region image reuse has no new upload or same-region transfer charge. Existing storage remains billable per account allowances |

Reference scenario:900active seconds1CPU/0.5GiB=0.022725USD;1000requests=0.0004USD;10MiB logs=0.004883USD gross. These are scenarios, not measured totals or guaranteed caps. No assumption of unused free quotas. Existing Neon Free capacity is sufficient for the recorded small scenario, subject to fresh quota check and no upgrade. See backend p06-r06-qualification.md for sources and calculations.

## Stop and closeout

Before any write: verify source, target, backup/recovery validity, fresh quota/resource state, exact action authorization and private handling. Stop on changed target, permissions, unexpected existing resource, stale approval, missing current binding, uncertain write or exceeded window. No automatic retry. R10 defines one15minute absolute window, participant readiness, packet digest, exact revision and preapproved shutdown.

For enabled-run closeout: revoke only matching runtime/phone digests using U01, read back disabled state, close/purge the session through the approved existing path and restore disabled candidate state without altering baseline traffic. Retain held liabilities, job/audit evidence and unknown outcomes. Secret retirement must not replace DB revocation, and no unrelated resource is deleted. Any unknown upload/commit is reconciled read-only before another action.

## Explicit unresolved items — no approval request for unknown execution

- Implementer must attach exact IAM before/after. The owner-approved U02 bootstrap now supplies the tenant/category setup/CAS/audit/readback/suspension interface; bind the actual source, profile, category UUID, prestate and action window for review rather than using synthetic values. U01 runtime activation still cannot perform bootstrap itself.
- Bind addressAccountId and category UUIDs as stable approved metadata, not newly generated per retry; specify aggregate hold accounting. Never reset allowance by switching account IDs.
- Finalize policy wording review, exact public HTTPS origin/tag and disabled/enabled revision names; numeric versions become evidence after R08, final packet/window atR10.
- Validate final infrastructure allowance against exact setup/closeout and network plan;2.00USD is a proposal, not a verified maximum.

R06 stays open for the limited database-runtime identity decision and exact privilege/handoff qualification above. Original12+approvedU01+approvedU02=14,7locally closed,7open; packages5/60(8.3%),walkthrough3/8(37.5%),P06unaccepted,ETAunvalidated. Cloud bindings/cost proposals above supersede earlier blanks, but no live-action approval is requested against the remaining credential gap.

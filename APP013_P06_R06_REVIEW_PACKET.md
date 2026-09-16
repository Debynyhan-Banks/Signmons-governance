# P06-R06 consolidated staging setup review packet

Status: documentation review draft, NOT executable and NOT R07 authorization. Sources backendc0b19af/governancea37452b. Owner approved regular-only initial diagnosis with one USD99 deposit. No emergency case, real charge, booking, dispatch or confirmation send. The full USD150 after-hours replacement business rule remains documented, not implemented. No scope deviation or new task.

Update: owner subsequently approved U02 to resolve the demonstrated bootstrap gap. See APP013_P06_U02_BOOTSTRAP.md and backend p06-u02-bootstrap.md for completed local implementation and exact exported interface. The historical draft below is not live execution authority. Bootstrap writes now have a tested atomic service/CAS/audit/readback/suspension path; final profile wording, actual prestate digest/timestamp, stable category binding, source/artifact check and fresh execution authorization must be included in R07/R08. U01's runtime activation remains separate. Original12+U01+U02=14; seven locally closed/seven original tasks open. No further addition.

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

These remain within R06/R07's existing deliverables; no new implementation or task is authorized. R06 stays open until resolved. Original12+approvedU01=13,6locally closed,7open; packages5/60(8.3%),walkthrough3/8(37.5%),P06unaccepted,ETAunvalidated. Do not ask owner to approve live actions against this incomplete draft.

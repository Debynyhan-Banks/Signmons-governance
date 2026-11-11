# APP-013 / 3A / CR-K1-R2 — KR7 exact reuse, deployment and independent cleanup

PENDING EXACT OWNER APPROVAL. Local implementation approved under CR-K1-R2; no external action by preparation. Source 3cd66507576f5e17f713282e414067ae84c4a742; manifest 2cb2ca24cb2e1e605c4595eefa3525a097efb6fa16e8e58bfe1a4eda0a4bf0d7. Operation 7e45dc51-2e17-481c-9128-63fa568725a4; unique candidate signmons-calldesk-staging-p07key7e45dc512e17. Source and actual launch.verify pass for both proposed specs, including SDK/full source chain and immutable KC1 receipt. New operation root absent. No KC1 replay.

## Current evidence and unresolved history

QD2 succeeded November11 and closed at13:48:38 UTC: key/account/test-mode/disabled-endpoint, full retired-role ACL and cloud preflight passed; qualification digest dec7be0ea34afbd2930214cc24a5e82f07dc316f14670a72fd47937a63601b01. Receipt backend3cd6650, qd2-result.json, source10466ab, approval639ca99. SD1 previously confirmed one SQL read. KR6 historical failure remains UNKNOWN; neither success explains it retrospectively. All prior operations consumed/closed. No runtime changes since the qualified source; source above includes safe result evidence.

Fresh preflight and exact qualification-hash comparison are repeated before writes. Existing reuse_version_check must confirm numeric version2 DISABLED before enabling; VM1 is historical context only. Any drift stops. No automatic retry. Current corrected candidate is not yet deployed/adopted.

## Exact actions

1. Numbered hidden inputs: sk_test_ Sandbox secret API key, then we_ Destination ID only. The existing bounded child FIRST checks exact endpoint input and key format; mismatch returns safe boolean/length flags with zero provider calls and no SQL prompt. If local inputs pass, at most3 Stripe GETs verify connected account, test mode and existing disabled endpoint. Only then perform cloud/SQL preflight, prompting for SQL administrator password when needed: current owner/config/project/billing/services/effective permissions/full role ACL/retired resources/environment/new-candidate absence, compared to QD1 digestdec7be0ea34afbd2930214cc24a5e82f07dc316f14670a72fd47937a63601b01. Fresh drift refuses writes. No stored secret payload read; version2 provenance is the immutable KC1 receipt. No automatic correction or input/provider retry.
2. Read exact signmons-staging-stripe-secret-key version2 metadata and require DISABLED. Pin original operation392807bd-8c43-4a01-b82d-3292f19fd222, receipt commitff18dbee2a4c7d94338b549f9d16d725a03b58ca and digest9a2066e1c99ec6e50262a3ad0f05a489ac275ebf49b63e8044189e96160464d2. Journal before enabling2, then verify ENABLED. Creation is prohibited in reuse mode by driver and port; no addVersion request/permission, new secret, replacement value, rotation or assumed version.
3. Enable existing identity signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com. Enable version1 of six existing secrets: signmons-staging-p07-payment-database-url, signmons-staging-p07-stripe-webhook-secret, signmons-staging-p07-disabled-openai-key, signmons-staging-p07-admin-token, signmons-staging-p07-conversation-key, signmons-staging-p07-technician-link-key. Add seven resource-level secretAccessor bindings for that identity (six plus Stripe). Both add/remove commands explicitly select JSON and read back actual policies. No project IAM or signing grant.
4. Activate existing p07_payment_runtime LOGIN/connection limit6/expiry9:25am Eastern, preserve qualified ACL; no password/schema/customer-data change. Database connections use existing verified TLS and owner input only in memory.
5. One candidate deployment to signmons-calldesk-staging, project signmons, region us-east5. Same image us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da; candidate named above; no image build. Existing exact environment replacement including QD2 return URL https://signmons-calldesk.web.app/payment/status; six version1 refs and Stripe version2. --no-traffic, tag app013-p07-atomic,1CPU/512Mi, concurrency40, timeout60, min0/max1, ingressall, CPU throttling/startup boost. Normal revision signmons-calldesk-staging-app013dbrot2 stays100%, candidate0%. Read back exact image/identity/environment/secrets/envelope/traffic and liveness/readiness HTTP200.
6. Mandatory in-process cleanup: role NOLOGIN/limit0/expired, terminate only its sessions; remove owned tag; remove temporary seven bindings; disable six startup versions and version2; disable identity. Independent authoritative retirement readbacks and bounded Stripe key/account/mode/disabled-endpoint check. Foreign tag refused. No deletion of versions/revisions.
7. After run exit, separate already-approved independent closeout against same exact journal/root, fresh hidden inputs and own immutable marker/lock. Only owned cleanup and readbacks; no creation/deployment replay. Complete before absolute cutoff. A failure with residuals is containment-unconfirmed, not accepted success.

## Boundaries and timing

November11 Eastern: start8:49am; launch and initial hidden inputs strictly before9:10am; work ends9:25am; mandatory cleanup and independent closeout strictly before9:45am. One run and one closeout, no retry/retiming. Owner remains available for both sessions. No credentials requested during preparation.

Per process enforced limits180 CLI,40 HTTPS,40 SQL,2 Node children with at most3 Stripe GET each. Initial work is restricted to half each limit, remainder reserved for cleanup. Separate closeout has same total limits: combined maximum360 CLI/80 HTTPS/80 SQL/4 children (12 Stripe GET). SDK dispatch counts are not underlying HTTP counts. Deployment bounded300seconds. Time/call gates and journal locks enforced; no dollar-metering mechanism.

Requested new incremental infrastructure planning allowance USD1, release only for these enumerated actions. NOT a hard billing cap or cost estimate; actual cost UNKNOWN. Existing disabled version2 may continue storage charges; immutable revision metadata may remain after cleanup. No new version created. KC1 allowance is not carried forward. No charge/payment/refund/checkout, endpoint enablement/event resend, customer contact/booking, normal-traffic change or source adoption.

## Readiness and finish

Readiness inspected November11 approximately08:50 Eastern, source/manifest above: current launch.verify/execute, correction.run/cleanup/closeout, NativePorts preflight/reuse/JSON binding/deployment/readbacks, NativeIO SQL classification, current source/test manifests and QD2 receipt. Actual launch.verify passed for both proposed scopes using explicitly proposed decisions in memory only; not live authority. Complete committed source/full chain/SDK/provenance checked and new root absent. Existing local evidence:51 correction Python,19Node,30native tests; not rerun for this documentation-only packet. Governance25/baseline/docs/architecture/diff checks required before review.

Actual source covers strict output parsing/missing-null refusal, numeric version pins, full dynamic environment, billing/API/effective-permission and key compatibility checks. QD2 supplies current observation; all facts must still pass before writes. Deployment success and retirement are UNKNOWN until observed. Deadline/no-retry/lock/partial-failure journal and independent cleanup paths reused. Inputs remain private memory; closeout requires process-exit verification and owned-file removal. Required CLI serialization and SQL categories are source-locked. No new behavior or changed acceptance criteria.

Finite checklist: prerequisite reconciliation/source verification/exact two scopes prepared; owner authority and attendance pending; one bounded run and independent closeout pending; safe receipts/process/file closeout pending. Implementer owns both operations and comparison of actual command/source/pins/authority/timing against this card; owner supplies hidden inputs and exact spending/operation approval. Unresolved live state is evaluated at its existing blocking gate, not waived by a fixture. No browser test applies to this candidate readiness operation; connected browser/payment acceptance follows separately. No new runtime implementation.

Observable success: candidateReadyObservedtrue, exact source/environment/envelope/normal100/candidate0 and health200, followed by independent CORRECTION_CLOSED with residuals[], failure null, version2 DISABLED, role/identity/startup retired, bindings/tag absent. Retained resources only existing disabled2 and revision metadata if deployed. Safe receipts persist; raw inputs cleared on exit, owned private specs/launchers removed after process verification. A readiness fixture or cleanup success without candidate readiness does not finish correction.

Implementer owns launch, bounded receipts and both cleanup/process closeouts. Owner approves exact operations/spending limitations and supplies hidden inputs; custodians resolve live permission drift. After success, reviewed source adoption and same-job connected payment/authentic event/application/browser/owner acceptance remain. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. Approved CR-K1 plus CR-K1-R2 amendment only; no further deviation.

## Exact authority

Both decisionCommit fields remain null. Actual approval must be committed separately for each mode in APP013_P08_KEY_CORRECTION_DECISION_20261110.json; no proposed decision is authority. Commands from backend: /opt/homebrew/bin/python3.14 -B evidence/APP-013/p08-key-correction-20261110/launch.py /private/tmp/p08-kr7-<mode>-7e45dc51-2e17-481c-9128-63fa568725a4.json. Files600/launcher700; reverify source, SDK, actual decisions, timing, resource/receipt pins and root before launch. Independent closeout uses same plan, not a fresh deployment plan.

### run

APP013_P08_KR7_RUN_SPEC_20261111.json; scope 415ab8b85680019b948dfdc65b9ea1d0b8654cd8f2eabdec040cf31cc234e4c0.

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_RUN",
  "scopeSha256": "415ab8b85680019b948dfdc65b9ea1d0b8654cd8f2eabdec040cf31cc234e4c0",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": true,
  "costHoldReleased": true
}
```

### closeout

APP013_P08_KR7_CLOSEOUT_SPEC_20261111.json; scope 4be615396d2f7daf42f74dae7eb31742e4ad21d6c19e5d5516f3eda2085fb03b.

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_CLOSEOUT",
  "scopeSha256": "4be615396d2f7daf42f74dae7eb31742e4ad21d6c19e5d5516f3eda2085fb03b",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": true,
  "costHoldReleased": true
}
```

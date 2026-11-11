# APP-013 / 3A / CR-K1-R2 — KR2 exact reuse, deployment and independent cleanup

PENDING EXACT OWNER APPROVAL. Local implementation approved under CR-K1-R2; no external action by preparation. Source 1648cf82084d0299ecf88348144bf18cc20866b2; manifest dc2c4319d39dd916e5229e297dc0f2b4bdceac7b8d95597de8a3b1f04c729bf3. Operation 5cdba516-cbbf-4219-8112-c60d498fc30d; unique candidate signmons-calldesk-staging-p07key5cdba516cbbf. Source and actual launch.verify pass for both proposed specs, including SDK/full source chain and immutable KC1 receipt. New operation root absent. No KC1 replay.

## Exact actions

1. Hidden inputs in order: sk_test_ Sandbox secret key, we_ Destination ID, then SQL administrator password when prompted. Current preflight checks owner/config/project/billing/services/effective permissions/full role ACL/retired resources/environment and candidate absence. Compare QK5 environment/ACL/return URL qualification digest dec7be0ea34afbd2930214cc24a5e82f07dc316f14670a72fd47937a63601b01; three bounded Stripe GETs verify owner-entered key/account/test mode and existing disabled endpoint. Fresh drift refuses work. No secret payload read is included; stored version provenance is KC1's exact create and successful independent-closeout receipt, not a new claim that its payload was read.
2. Read exact signmons-staging-stripe-secret-key version2 metadata and require DISABLED. Pin original operation392807bd-8c43-4a01-b82d-3292f19fd222, receipt commitff18dbee2a4c7d94338b549f9d16d725a03b58ca and digest9a2066e1c99ec6e50262a3ad0f05a489ac275ebf49b63e8044189e96160464d2. Journal before enabling2, then verify ENABLED. Creation is prohibited in reuse mode by driver and port; no addVersion request/permission, new secret, replacement value, rotation or assumed version.
3. Enable existing identity signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com. Enable version1 of six existing secrets: signmons-staging-p07-payment-database-url, signmons-staging-p07-stripe-webhook-secret, signmons-staging-p07-disabled-openai-key, signmons-staging-p07-admin-token, signmons-staging-p07-conversation-key, signmons-staging-p07-technician-link-key. Add seven resource-level secretAccessor bindings for that identity (six plus Stripe). Both add/remove commands explicitly select JSON and read back actual policies. No project IAM or signing grant.
4. Activate existing p07_payment_runtime LOGIN/connection limit6/expiry7:50pm Eastern, preserve qualified ACL; no password/schema/customer-data change. Database connections use existing verified TLS and owner input only in memory.
5. One candidate deployment to signmons-calldesk-staging, project signmons, region us-east5. Same image us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da; candidate named above; no image build. Existing exact environment replacement including QK5 return URL https://signmons-calldesk.web.app/payment/status; six version1 refs and Stripe version2. --no-traffic, tag app013-p07-atomic,1CPU/512Mi, concurrency40, timeout60, min0/max1, ingressall, CPU throttling/startup boost. Normal revision signmons-calldesk-staging-app013dbrot2 stays100%, candidate0%. Read back exact image/identity/environment/secrets/envelope/traffic and liveness/readiness HTTP200.
6. Mandatory in-process cleanup: role NOLOGIN/limit0/expired, terminate only its sessions; remove owned tag; remove temporary seven bindings; disable six startup versions and version2; disable identity. Independent authoritative retirement readbacks and bounded Stripe key/account/mode/disabled-endpoint check. Foreign tag refused. No deletion of versions/revisions.
7. After run exit, separate already-approved independent closeout against same exact journal/root, fresh hidden inputs and own immutable marker/lock. Only owned cleanup and readbacks; no creation/deployment replay. Complete before absolute cutoff. A failure with residuals is containment-unconfirmed, not accepted success.

## Boundaries and timing

November10 Eastern: start7:10pm; launch and initial hidden inputs strictly before7:35pm; work ends7:50pm; mandatory cleanup and independent closeout strictly before8:10pm. One run and one closeout, no retry/retiming. Owner remains available for both sessions. No credentials requested during preparation.

Per process enforced limits180 CLI,40 HTTPS,40 SQL,2 Node children with at most3 Stripe GET each. Initial work is restricted to half each limit, remainder reserved for cleanup. Separate closeout has same total limits: combined maximum360 CLI/80 HTTPS/80 SQL/4 children (12 Stripe GET). SDK dispatch counts are not underlying HTTP counts. Deployment bounded300seconds. Time/call gates and journal locks enforced; no dollar-metering mechanism.

Requested new incremental infrastructure planning allowance USD1, release only for these enumerated actions. NOT a hard billing cap or cost estimate; actual cost UNKNOWN. Existing disabled version2 may continue storage charges; immutable revision metadata may remain after cleanup. No new version created. KC1 allowance is not carried forward. No charge/payment/refund/checkout, endpoint enablement/event resend, customer contact/booking, normal-traffic change or source adoption.

## Readiness and finish

Inspected November10 after source1648cf8:41Python+18Node pass, actual lifecycle numeric2/JSON binding serialization/full-role readback, no-create on success/failures, disabled/foreign version refusal, committed provenance, interruption, concurrency/duplicates, independent cleanup and exact approval separation covered. Historical broader suite not claimed rerun. Current governance25/baseline/docs/architecture/diff checks accompany this proposal. This preparation is zero provider calls. QK5 is historical live observation reused with mandatory fresh preflight; version2 last observed disabled at KC1 closeout, current state UNKNOWN until this approved operation checks it. Current source candidate binding remains LEGACY.

Observable success: candidateReadyObservedtrue, exact source/environment/envelope/normal100/candidate0 and health200, followed by independent CORRECTION_CLOSED with residuals[], failure null, version2 DISABLED, role/identity/startup retired, bindings/tag absent. Retained resources only existing disabled2 and revision metadata if deployed. Safe receipts persist; raw inputs cleared on exit, owned private specs/launchers removed after process verification. A readiness fixture or cleanup success without candidate readiness does not finish correction.

Implementer owns launch, bounded receipts and both cleanup/process closeouts. Owner approves exact operations/spending limitations and supplies hidden inputs; custodians resolve live permission drift. After success, reviewed source adoption and same-job connected payment/authentic event/application/browser/owner acceptance remain. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. Approved CR-K1 plus CR-K1-R2 amendment only; no further deviation.

## Exact authority

Both decisionCommit fields remain null. Actual approval must be committed separately for each mode in APP013_P08_KEY_CORRECTION_DECISION_20261110.json; no proposed decision is authority. Commands from backend: /opt/homebrew/bin/python3.14 -B evidence/APP-013/p08-key-correction-20261110/launch.py /private/tmp/p08-kr2-<mode>-5cdba516-cbbf-4219-8112-c60d498fc30d.json. Files600/launcher700; reverify source, SDK, actual decisions, timing, resource/receipt pins and root before launch. Independent closeout uses same plan, not a fresh deployment plan.

### run

APP013_P08_KR2_RUN_SPEC_20261110.json; scope a08bb1697549255b7ee6620f977f974557dc36fff892cf7cdcef069ec66ab264.

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_RUN",
  "scopeSha256": "a08bb1697549255b7ee6620f977f974557dc36fff892cf7cdcef069ec66ab264",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": true,
  "costHoldReleased": true
}
```

### closeout

APP013_P08_KR2_CLOSEOUT_SPEC_20261110.json; scope 375f165bf44cef829dfd3da11308b4e7c73494189e526c58999ebe48162bcdac.

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_CLOSEOUT",
  "scopeSha256": "375f165bf44cef829dfd3da11308b4e7c73494189e526c58999ebe48162bcdac",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": true,
  "costHoldReleased": true
}
```

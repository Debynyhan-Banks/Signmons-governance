# APP-013 / 3A / CR-K1 — KC1 correction and independent cleanup

PENDING EXACT OWNER APPROVAL. Preparation only; no external calls. Owner approved CR-K1 scope/local implementation at ed64d49. This packet implements that existing prerequisite, not a new acceptance section. Source a7ae8b3e82b302343d4c17c97721accdb806a3ae; manifest f18cbb8bdb686d2a1848e3100d3a50b2787bb1bd3264edccbb06104cf24b44b4. QK5 successful receipt backend af4e05e, governance 7a4fff8; qualification digest dec7be0ea34afbd2930214cc24a5e82f07dc316f14670a72fd47937a63601b01. Operation 392807bd-8c43-4a01-b82d-3292f19fd222; candidate signmons-calldesk-staging-p07key392807bd8c43. Current binding stays LEGACY until a later reviewed adoption.

## Exact finite actions

1. One exclusive attempt with hidden sk_test_ secret API key, then we_ Destination ID. Existing SQL administrator password is separately prompted. Unlike qualification's reordered input validation, run invokes current cloud/SQL preflight before its key check; neither creates resources. Recheck QK5 environment/ACL/return URL hashes, current owner/config/project/billing/API/effective permissions, all retired resources, candidate absence, and three Stripe GET checks. Any drift refuses writes.
2. One POST addVersion on signmons-staging-stripe-secret-key. Numeric version is taken only from the validated returned resource, must be greater than1; no latest alias, no assumed2, no retry. Existing version1 untouched. Lost response means unknown ownership and STOP, never a second creation.
3. Temporarily enable existing signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com; enable version1 of the six existing startup secrets listed below; add seven resource-level roles/secretmanager.secretAccessor bindings for that identity, including Stripe secret. No project-level grant, signing grant, new role or new identity.
4. Temporarily activate existing PostgreSQL p07_payment_runtime: LOGIN, connection limit6, expiry at work end. Preserve full qualified ACL; no password/ACL/schema/customer-data change.
5. One gcloud run deploy of signmons-calldesk-staging in signmons/us-east5, candidate above, same image digest sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da. Full existing environment replacement plus qualified return URL; seven exact numeric secret refs. --no-traffic, tag app013-p07-atomic,1CPU/512Mi, concurrency40, timeout60, min0/max1, ingressall, CPU throttling/startup boost. Normal revision signmons-calldesk-staging-app013dbrot2 remains100%; candidate0%. Read back exact image, environment, identity, traffic and health/liveness plus health/readiness HTTP200. No image build.
6. Mandatory in-process cleanup: role NOLOGIN/limit0/expired and terminate only its sessions; remove owned tag; remove temporary secret bindings; disable six startup versions and new Stripe version; disable identity. Read back full retirement and unchanged disabled Stripe endpoint/key/account/mode. Foreign tag refused, never overwritten.
7. Separate independent closeout invocation against the same journal after the run exits, with fresh hidden inputs. Verify owned transitions and retirement, complete only needed owned cleanup; never rerun creation/deployment. Separate immutable attempt marker and lock. This is included in the requested approval.

Startup secrets (each version1): signmons-staging-p07-payment-database-url, signmons-staging-p07-stripe-webhook-secret, signmons-staging-p07-disabled-openai-key, signmons-staging-p07-admin-token, signmons-staging-p07-conversation-key, signmons-staging-p07-technician-link-key. New Stripe numeric version is the seventh deployment reference. All exact command renderers are committed in correction.py Deployment and legacy/controller.py deploy; lifecycle vectors in restore.py command/role SQL and binding.py. No raw credentials in command arguments or files.

## Timing, bounds and spending decision

November10 Eastern: start6:50pm; launch/input strictly before7:15pm; all work ends7:30pm; cleanup and independent closeout finish strictly before7:45pm. No automatic retry or retiming. Owner remains available for both hidden-input sessions; no payment/card entry. If insufficient time remains, do not launch.

Each run or closeout process has enforced total ceilings180 CLI dispatches,40 HTTPS dispatches,40 SQL dispatches,2 Node key-check children (at most3 Stripe GET each). Run work initially limited to half each ceiling, remainder reserved for cleanup. Independent closeout has its own same total ceiling; combined maximum360 CLI/80 HTTPS/80 SQL/4 children (at most12 Stripe GET). CLI counts logical SDK dispatches, not SDK internal HTTP calls. The direct addVersion call is non-retried; SDK deployment bounded300seconds. Time and call checks are implemented, no billing polling exists.

Proposed incremental infrastructure allowance: USD1 for this single correction and cleanup, with release limited to these actions. This is an owner planning allowance, NOT an enforced dollar cap or cost estimate: costAllowanceUsd is approval-bound but not metered by source. Actual incurred cost is UNKNOWN. Disabled Secret Manager versions may continue to incur storage costs after the window; retained revision metadata remains. No deletion is authorized. Owner must explicitly accept these spending/retention limitations; otherwise execution remains blocked. No payment charge, customer transaction, refund or recurring application service is authorized.

## Readiness and finish evidence

Inspected November10 after QK5: successful live qualification binds environment b3b3e19722bbd8f5ceadb94323e86612e4b26b8bc896b1d0223e74e683f67cc8, full role ACL 649d517af81c235f8045894d73207b7d892b3607ee165418151af6b9975c1560, return URL https://signmons-calldesk.web.app/payment/status. It proved current key/account/test-mode/disabled endpoint and owner/environment/retirement checks at that observation, not future access. Run revalidates before mutation; unique new candidate checked live by run. New-version/deploy behavior remains locally tested, not live demonstrated.

Current actual launch.verify validates both proposed specifications, committed source/full native source chain/SDK pins/exact qualification/window; fresh root absent. Existing focused25Python+18Node tests and historical full suite reused, not represented as new test runs. Current governance/baseline/architecture/whitespace checks required before review. No browser/customer capability acceptance claimed. Failure/duplicate/journal/interrupt/no-retry/readback fixtures already cover the existing driver; no implementation change in this packet.

Observable finish: run readiness records exact image/environment, normal100/candidate0 and both health200; independent closeout returns CORRECTION_CLOSED, residuals[], candidateReadyObservedtrue, failure null, new numeric Stripe version disabled, identity/role/startup versions retired, bindings/tag absent. Safe receipts retained; raw inputs cleared on process exit. Expected retained resources: one disabled owned secret version plus revision metadata. Unknown ownership/cleanup produces containment-unconfirmed, never success or adoption. Process exit and owned launcher/private spec removal separately verified by implementer. No source adoption in this packet.

Responsible roles: implementer launches approved exact commands and preserves safe receipts/closeout; owner approves both exact actions and spending limitations and supplies hidden inputs; provider/DB custodians resolve any current access drift. Remaining after this packet: reviewed candidate/version adoption and original connected same-job Sandbox payment/authentic event/application/browser/owner acceptance. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. Approved CR-K1 scope deviation only; no further deviation.

## Exact approval bindings

Both specs have decisionCommit null until actual approval is committed. Separate committed decisions use APP013_P08_KEY_CORRECTION_DECISION_20261110.json; retain both commit references. Launch command for each is /opt/homebrew/bin/python3.14 -B evidence/APP-013/p08-key-correction-20261110/launch.py /private/tmp/p08-kc1-<mode>-392807bd-8c43-4a01-b82d-3292f19fd222.json from backend. Private specs mode600, launcher700. Never launch during preparation.

### run

Spec APP013_P08_KC1_RUN_SPEC_20261110.json; scope 262f07d65c5e5a13b7f2b1701e8857fe0e68aafa0303196efa4cdf2a54653b12.

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_RUN",
  "scopeSha256": "262f07d65c5e5a13b7f2b1701e8857fe0e68aafa0303196efa4cdf2a54653b12",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": true,
  "costHoldReleased": true
}
```

### closeout

Spec APP013_P08_KC1_CLOSEOUT_SPEC_20261110.json; scope 144f903d8f879bc19482c2e6e230e493fbbdda92fd14bea3acdc496a4737a834.

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_CLOSEOUT",
  "scopeSha256": "144f903d8f879bc19482c2e6e230e493fbbdda92fd14bea3acdc496a4737a834",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": true,
  "costHoldReleased": true
}
```

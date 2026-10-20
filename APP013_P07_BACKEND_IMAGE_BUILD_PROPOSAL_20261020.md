# APP-013 / 3A / P07 backend image build proposal

Status: Alternative 1 completed once during the approved October 20 window. Exact source/image verified and all three temporary grants independently verified absent. No deployment or live payment journey authorized.

## Decision requested

Choose Alternative 1 or Alternative 2 for the isolated P07 backend candidate. The proposed execution window for Alternative 1 is **7:15–8:00 a.m. Eastern on October 20, 2026**, with submission starting strictly before 7:35 a.m. and mandatory permission cleanup allowed to finish after 8:00 if necessary.

### Alternative 1 — one exact build

Approve one Cloud Build from exact archive `tmp/p07-release-candidate-20261020/backend-source.tar.gz`, SHA-256 `6b499c4431a2e10d2fd032d167232bfb710209b9d6fa5056df1de236cc5b8400`, 984,980 bytes, 576 files, to candidate tag:

`us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p07-6b499c4431a2`

Approve a USD 1 Cloud operational allowance, the existing three temporary least-privilege build memberships with mandatory removal/readback, one submission and no retry.

### Alternative 2 — retain local candidate

Perform no Cloud or registry action. Keep the locally validated artifacts for a later reviewed window.

## Traceability

Approved section: APP-013/3A/P07. The exact acceptance criterion remains a same-job Sandbox Checkout whose authentic event clears the payment gate while foreign, failed, duplicate, late and redirect-only outcomes fail closed.

The October 20 read-only qualification proved `P07_DEPLOYMENT_REQUIRED`. This build advances that existing workflow by producing one immutable image for later zero-traffic deployment review. It does not address the separate `DESTINATION_DISABLED`, `API_VERSION_UNCONFIRMED` or `READ_PATH_UNAVAILABLE` blockers and does not authorize P08.

Source evidence: backend `evidence/APP-013/p07-release-candidate-preparation-20261020.md`. The candidate starts from the exact accepted 2B image source and replaces only nine reviewed P07 backend files. Manifest SHA-256: `478b0187b10cab6f44587c172ceb76a401ab34be9c5845c89e38da3f78fb180c`.

## Finite Alternative 1 sequence

1. Create fresh one-use plan and operation identities bound to the owner decision, exact archive bytes/hash, manifest hash, candidate tag, window and USD 1 allowance. Local guards reject early/late/consumed execution, archive drift, tag collision, grant drift, uncertain submission and cleanup failure.
2. Read-only preflight project `signmons`: require the existing `signmons-build` identity enabled, existing source bucket and `us-east5/signmons` Docker repository present, candidate tag absent, and all three temporary memberships absent. Any mismatch stops. No identity re-enable, replacement resource or permission repair is implicit.
3. Journal before mutation. Temporarily grant only `roles/storage.objectViewer` on the existing Cloud Build source bucket, `roles/artifactregistry.writer` on repository `signmons` in `us-east5`, and `roles/logging.logWriter` on project `signmons` to the existing build identity.
4. Submit the exact reviewed archive once through its included `cloudbuild.deploy.yaml`, explicit global build region, `e2-highcpu-8`, 1,200-second timeout, existing build identity and exact candidate tag. Do not rebuild from the mutable checkout. Any uncertain submission consumes the attempt.
5. Require terminal build success, record build ID/source object generation, download and hash the uploaded source, and require registry/build immutable digests to agree. Do not deploy the image.
6. In mandatory cleanup after success, failure or uncertainty, remove every possibly applied temporary membership and independently read all three absent. Preserve only sanitized build/provenance/digest/cleanup receipts.

## Output classification

The operation ends with exactly one of:

- `P07_IMAGE_BUILT`: exact source and uploaded-object hashes match, build succeeds, registry/build digests agree and all temporary grants are absent;
- `PREFLIGHT_STOP`: identity/resource/tag/grant state differs before mutation;
- `BUILD_FAILED`: one submitted build reaches a failed terminal state;
- `BUILD_UNCERTAIN`: submission or result cannot be proven and no retry is permitted;
- `CLEANUP_FAILED`: any temporary membership cannot be proven absent.

No success label is allowed from image-tag presence alone.

## Cost, exclusions and rollback

At the previously reviewed default-pool `e2-highcpu-8` rate, 20 minutes of compute was estimated at USD 0.312 before storage, logging, registry, transfer, tax or account adjustments. USD 1 is an operational allowance, not a provider-enforced billing cap or invoice estimate. Actual charges remain unverified.

Excluded: Cloud Run revision/tag/traffic change, runtime or database-role activation, secret payload access/change, migration, Stripe destination/configuration/event, Checkout, payment, customer or booking action, UI publication, repository commit/push/merge and retry. No Twilio or address-provider allowance applies.

Rollback is mandatory permission removal and leaving any successfully built image unused. A later digest-bound proposal must separately cover zero-traffic deployment, child-database/runtime containment, an operator identity, UI preview binding, Stripe connected-accounts destination creation/new signing-secret storage and the exact-job read. **No scope deviation.**

## October 20, 7:19 a.m. Eastern — approved image built; cleanup verified

The owner replied **“yes i approve”** to Alternative 1. Plan `17ebaa53-d51c-4fc1-ad74-8937f83404aa` / operation `5a568564-29d5-4462-a88c-80aed97698fc` executed once inside the 7:15–8:00 a.m. Eastern window. Fresh preflight passed. Exactly one submission created build `2cfff9d9-bfe1-4166-a5a2-4d8d2acdb0b8` at 7:15:25; terminal status was `SUCCESS` at 7:19:11.

The exact 984,980-byte uploaded source object was downloaded by its recorded generation and matched approved SHA-256 `6b499c4431a2e10d2fd032d167232bfb710209b9d6fa5056df1de236cc5b8400`. Build and registry digests agree at `sha256:a88e64566133b9e734d245a928d0ade10b5064ff76d8e4fc712a4e3def3f0191`. All three temporary memberships were removed and read back absent at 7:19:21; an independent post-operation readback again confirmed build success, digest agreement and all three absent. The operation is consumed and cannot be retried.

Receipts: backend `evidence/APP-013/p07-backend-image-build-result-20261020.md`; private control/result directories `/private/tmp/p07-build-control-20261020-0715` and `/private/tmp/p07-build-run-20261020-0715`. No deployment, Cloud Run change, Stripe/database/secret/customer/payment action, commit, push or merge occurred. The image remains unused. Actual invoice cost is unverified. Accepted progress remains 6/60, 4/8 and 0/13. Next is a separately reviewed digest-bound deployment/destination/read-path proposal. **No scope deviation.**

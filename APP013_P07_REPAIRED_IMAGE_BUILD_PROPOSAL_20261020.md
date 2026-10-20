# APP-013 / 3A / P07 — one repaired-image build proposal

Status: **owner-approved Alternative 1 completed once; `P07_IMAGE_BUILT`; temporary permissions `VERIFIED_ABSENT`; operation consumed**. Owner explicitly answered **“Approve one exact build”** to this operation, its conditional transformation, USD 1 allowance, three temporary memberships, mandatory cleanup and no-retry boundary. Approval at October 20, 21:50:10 UTC bound plan SHA-256 `e8520021bc4f31abd3902623e82bb772b2799a354d39efa8acac64ace51d193c` and detached receipt SHA-256 `3e08516d957b69c165df676effad85d76fc3f32c94b9c2f90b5f1514110992ac`. The one build succeeded, source/image provenance matched and all three temporary memberships were removed and independently read back absent. The repaired image remains unused. No replay or renewed approval of this consumed build is requested.

The reviewed proposal below is preserved as historical decision detail, including its then-prospective window/transformation wording. The actual-result section at the end supplies current execution evidence and supersedes those prospective status statements; no deployment, runtime or payment authority follows from the completed build.

## Decision and proposed window

**Alternative 1:** approve the exact conditional plan transformation below and one build-only operation on **Tuesday, October 20, 2026, 6:00–6:45 p.m. Eastern daylight time**, with submission **strictly before 6:15 p.m.** Mandatory permission containment and original-attempt cleanup-only recovery remain authorized through **7:00 p.m.** No owner attendance, Terminal session or administrator password is needed for this build-only operation.

**Alternative 2:** retain the verified local source/controller without any Cloud, registry or IAM action. If the proposed window expires without approval/start, stop; do not move the window or infer renewed authority.

| Boundary | Exact UTC value |
| --- | --- |
| Start | `2026-10-20T22:00:00Z` |
| Submit strictly before | `2026-10-20T22:15:00Z` |
| Ordinary operation end | `2026-10-20T22:45:00Z` |
| Mandatory containment/recovery end | `2026-10-20T23:00:00Z` |

## Traceability and immutable bindings

Section **R1-W01 / APP-013 / 3A / P07** remains open. Its unchanged acceptance is an authentic matching Sandbox event settling the same accepted job and clearing its durable payment gate, with failure/replay safeguards. This build produces an unused repaired image for later readiness review; it accepts no customer capability. Source: repaired application commit `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd`, with archive lineage in backend `evidence/APP-013/p07-atomic-repaired-source-preparation-20261020.md`.

Preparation entry heads: backend `2bf3f5f91faac5538924a5f99e7a4e93279790c5`; governance `1328c2f8a5a928ad05634a1ca87bf7e17af458f3`. Local controller evidence is backend `evidence/APP-013/p07-repaired-build-preparation-review-20261020.md`: **45/45 mocked/isolated test methods pass**, including original eight, process races, termination, guard, provenance, persistence and bounded recovery cases. This is local controller evidence, not an executed build. No application/runtime tests are claimed as newly run for this proposal.

Private root: `/private/tmp/p07-repaired-build-review-20261020-z4_gul98`. Plan `a04a6ccd-4465-4f55-b60a-60881b8a0f64`; packet `787dcdcc-ec16-4a6c-b555-6e4154042d59`; operation `006c9b9e-8171-4595-9128-10fdedf3660f`.

| Artifact | SHA-256 / quantity |
| --- | --- |
| `source.tar.gz` | `893432c1de02c8068237711908099d452dd8e18dde6603240007bc61db5ed456`; 986,100 bytes; 576 regular files |
| `release-manifest.json` | `28f51e7c79dfe21d54c0a8302ec615e408fc91769a60afa217f1d48702aaadb5` |
| `cloudbuild.deploy.yaml` | `7a0fb42b31a1ab26a419ed4f109f36464e881d0c6bfaa42d014366dcb48ba5c5` |
| Corrected `controller.py` | `00859bcef49739b7a891fc7cd2e993a18833e29ab79eabe6ad40f29251ba0eb0` |
| `controller_tests.py` | `36f5db7a51d24822213b17107bb61578725211fbc272a8890c486c222e0ab49b` |
| Preserved `controller_tests.original.py` | `cb2b540535483764a03574641eb0fcdf7f417bb578fa0a39232afe99d0ad96e5` |
| Current disabled `plan.json` | `6d0efe7c3860f67edf786ac5a94860c9ceff1e48cac518d13748d3eac86970b4` |
| Proposal-only `build-operation-proposal.json` | `984b9e71a2cc4e8b6a1fb530b47871cbaf089e6ec4090259d14239bf00fcd67d` |

## Conditional transformation — only after actual explicit approval

The reviewed transformation starts from the exact disabled plan above and changes **only five fields**: `status` to `APPROVED_UNUSED`; `preparationOnly` to false; `allowanceStatus` to `APPROVED`; `ownerDecision` to `APPROVED`; and `window` to the four exact UTC fields `startUtc`, `submitBeforeUtc`, `endUtc`, `cleanupEndUtc` in the table. All other fields, identities, action/resource limits and artifact hashes stay unchanged.

Canonical UTF-8 JSON with sorted keys, indentation of two spaces and one trailing newline produces target plan SHA-256 **`e8520021bc4f31abd3902623e82bb772b2799a354d39efa8acac64ace51d193c`**. This target is calculated for review; no executable candidate plan has been written and no transformation is authorized yet.

Only an actual explicit owner approval of **this operation and transformation** permits applying it and then creating the separate `owner-approval.json`. That exact receipt must bind the final plan bytes, owner, section, plan/packet/operation, permitted actions, window, USD1 allowance and actual approval timestamp under the controller's validated schema. The local-correction receipt cannot substitute. No approval is invented or prewritten, and the plan's `approval` field remains null because the external receipt is detached.

## Exact build-only envelope

| Resource | Target |
| --- | --- |
| Project / build region | `signmons` / global Cloud Build |
| Existing build identity | `signmons-build@signmons.iam.gserviceaccount.com` |
| Source bucket / prefix | `gs://signmons_cloudbuild` / `source` |
| Existing Docker repository | `signmons` in `us-east5` |
| Candidate image | `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p07-atomic-893432c1de02` |
| Build envelope | Existing config; `e2-highcpu-8`; 1,200-second provider build timeout; one submission, no retry |

Proposed **USD1 Cloud operational allowance** is unapproved until this decision. It is neither a current provider price nor a provider-enforced billing cap. Actual charges require later reconciliation. No database/webhook-secret retained-cost allowance is included.

Only three temporary memberships are proposed: `roles/storage.objectViewer` on the existing source bucket, `roles/artifactregistry.writer` on the existing repository, and `roles/logging.logWriter` on the project, all for the exact existing build identity. No identity creation/re-enable, resource replacement, additional grant or IAM repair is implicit.

## Finite operation and mandatory containment

1. Verify exact local plan/receipt/source/config/controller/test bindings, real window and no prior attempt/stop/result/consumed marker. Atomically reserve before any provider command. A second process or restart cannot replay the operation; synthetic clocks cannot authorize it.
2. Run fresh read-only preflight of the existing identity/resources, candidate-tag absence and all three temporary memberships absent. Any mismatch stops before mutation. A pre-existing grant is preserved; its discovery is not permission to remove it.
3. Journal each exact possible grant before its command, recheck time before every grant and submission, and read back the three applied memberships. Submit the exact archive once; do not build from the mutable checkout. Uncertain submission consumes the attempt.
4. Observe one terminal build result within bounded polling/ordinary end. Require exact build/project/image identity, recorded source object generation, downloaded source bytes/hash and matching build/registry immutable digest. A tag alone cannot prove success. The repaired image digest is currently unknown.
5. On success, error, uncertainty, SIGINT or SIGTERM, enter cleanup once. Remove each possibly applied exact temporary membership independently and independently read all three scopes; preserve unrelated bindings. Leave any resulting image unused. Receipt/journal errors must retain truthful uncertainty and cannot skip remaining cleanup.
6. Cleanup-only recovery is restricted to the original exact approval, exclusive attempt lock and validated journal; it cannot submit/retry or remove a later binding after verified absence. It stays within the original cleanup deadline, with no extended window or new allowance. After that deadline, unconfirmed containment remains unconfirmed and requires direction; no provider commands are permitted by this packet.

Commands are bounded to at most 30 seconds, preflight/grant and cleanup invocations to 180-second budgets, and build polling to 1,300 seconds and ordinary end. Cleanup budget is further limited by remaining time before 7:00 p.m.; it cannot renew authority. Partial mutation is reported separately from cleanup status.

## Observable result, rollback and exclusions

Success is `P07_IMAGE_BUILT` only with exact source/build/registry proof, required durable receipts and freshly `VERIFIED_ABSENT` temporary memberships. Other outcomes retain a named preflight stop, build failure/uncertainty or `CONTAINMENT_UNCONFIRMED`. `NOT_REQUIRED`, known present and unknown are not verified absence. Sanitized evidence records identities/hashes, one attempt, stage/result, source generation/digest and independent cleanup; no secret/provider payload is retained.

Rollback is removal/readback of this operation's possibly applied temporary memberships and leaving any image unused. Preserve the old consumed operation, old images/archives/UI artifacts, local proof and all receipts. No retry, rebuild from different source or corrective provider transaction is authorized.

Excluded: Cloud Run deployment/tag/traffic change; live database, role or credential work; secret access/change; Stripe account/configuration/destination/event/test/resend; Checkout, card, charge/refund; Firebase activation/token mint; booking/dispatch, messaging/customer contact; UI publication; repository commit/push/merge; production migration/change. No password or customer input belongs in this operation.

Runtime remains a later digest-bound dependency: live payment-role/credential isolation choice, numeric database/signing secrets and costs, exact accepted-job readback, Sandbox destination/API bindings and isolated deployment/containment require their own concrete approval. No secret/IAM architecture is selected here. P08/payment and owner acceptance remain separate after readiness.

Implementer owns this exact build/provenance/containment work if approved; Debynyhan Banks owns the build decision, later external decisions and 3A acceptance. Counts remain **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. Queue, criteria, section order and denominators are unchanged. **No scope deviation from proposal preparation; no external execution is approved or performed by this document.**

## Actual result — October 20, 2026, build and containment complete

The exact approved operation reserved once and started at **22:00:14.842394 UTC**. One submission at **22:00:29.352577 UTC** created build `9ee7772a-62b1-4a07-86ad-0c3b9daf3032`. Terminal `SUCCESS` was observed at **22:04:16.613430 UTC**; exact uploaded-source and build/registry digest verification completed at **22:04:20.182211 UTC**. All three temporary memberships were read back absent at **22:04:26.168708 UTC**; final result at **22:04:26.168857 UTC** records `P07_IMAGE_BUILT`, `VERIFIED_ABSENT`, cleanupAllAbsent=true and persistenceConfirmed=true.

The repaired immutable image is:

`us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da`

Uploaded object `source/1792533626.326269-f765af6ec7ff4edcbd652fd3a06998f7.gz` in the exact source bucket, generation `1792533627176523`, was downloaded and verified at **986,100 bytes**, SHA-256 `893432c1de02c8068237711908099d452dd8e18dde6603240007bc61db5ed456`. Build and registry agree on the full image digest above.

An independent authorized readback completed at **22:05:15.902895 UTC** using six actual read commands covering Cloud Build, registry, source content and all three IAM policies. Its eight checks passed, failures=[], mutations=0. This independently confirmed successful exact build/provenance and absent temporary memberships; it was not another build or paid test.

| Actual receipt | SHA-256 |
| --- | --- |
| Local final result | `eccd03c1bcb0fe68b286423ad56ab9bbc0ccf25af6caf5c76b35b4efbbf94355` |
| Operation journal | `5b690e028a2a76952d428694a3154be179f8472e78f40e4b47fabd017d9c18aa` |
| Independent readback | `91ef910ba0402db107b238389d4ac09928b0ad4432e48395292acffdfd0b67ea` |

Evidence: backend `evidence/APP-013/p07-repaired-image-build-result-20261020.md`. Original eight consumed-package files and bound source/config/manifest inputs remain unchanged. The new ATTEMPT and CONSUMED markers are retained; the plan's literal `APPROVED_UNUSED` status does not override those immutable replay guards. No retry is allowed.

The build ran under the approved USD1 operational allowance; actual invoiced cost remains unverified, and that allowance was not a provider-enforced billing cap. No deployment, database/role/credential action, secret access/change, Stripe/payment, UI publication, customer/booking/message action or repository push/merge occurred. The image remains unused. **No scope deviation from the exact owner-approved build and mandatory containment.**

Next is preparation only of a concrete proposal bound to this digest for runtime readiness, including the unresolved credential-isolation choice, secret/destination bindings/costs and isolated zero-normal-traffic deployment/containment. That operation is not approved or ready for execution. P08 and authentic same-job payment acceptance remain separate. Progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**.

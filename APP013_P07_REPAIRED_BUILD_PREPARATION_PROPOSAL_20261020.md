# APP-013 / 3A / P07 — repaired-image preparation and local guard correction proposal

Status: **proposal preparation only; local controller corrections and every external action remain unapproved**. The owner's “begin” authorizes preparing a reviewable proposal, not implementing a newly demonstrated material prerequisite. No executable window is selected. The fresh review copy is disabled; its window and owner approval are null. Do not invoke the consumed controller or turn the copy into an approved operation.

## Traceability and inspected source

Existing section: **R1-W01 / APP-013 / 3A / P07**. Exact acceptance remains one authentic matching Sandbox payment for the accepted job, with the correct mode/account/resource/job/amount/currency, durable gate clearance, safe replay and no regression from late events. Image preparation advances that same workflow; neither an image nor a controller test accepts payment or closes 3A.

Backend entry head: `1c60cdab8b3cd66c7c78304875a8927f7eddbedd`. Governance entry head: `a149ec2a2715e69732bcad3c8362244b53a86366`. The repaired application commit is `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd`; its local validation is 97 affected unit cases and 22 reported real-role checks, with no grant expansion. Those results are historical evidence for this documentation step, not newly rerun tests.

Sources: `APP013_3A_PAYMENT_SECTION_CARD_20261020.md`, `APP013_REMAINING_EXECUTION_CONTRACT.md`, backend `evidence/APP-013/p07-webhook-atomicity-local-repair-20261020.md`, `p07-atomic-repaired-source-preparation-20261020.md` and `p07-repaired-build-preparation-review-20261020.md`.

The original consumed build root is `/private/tmp/p07-build-control-20261020-0715`. Its controller, config, eight-test suite, plan, archives and receipts remain immutable. The fresh **non-executable review copy** is `/private/tmp/p07-repaired-build-review-20261020-z4_gul98`.

| Bound artifact | SHA-256 / identity |
| --- | --- |
| Repaired source archive | `893432c1de02c8068237711908099d452dd8e18dde6603240007bc61db5ed456`; 986,100 bytes, 576 regular files |
| Repaired release manifest | `28f51e7c79dfe21d54c0a8302ec615e408fc91769a60afa217f1d48702aaadb5` |
| Original controller / unchanged review copy | `d02e2ff31e43963d982e17047a5227f850256d0c592645ae0b693b2be18b8884` |
| Original eight-test suite | `cb2b540535483764a03574641eb0fcdf7f417bb578fa0a39232afe99d0ad96e5` |
| Original and repaired-source build config | `7a0fb42b31a1ab26a419ed4f109f36464e881d0c6bfaa42d014366dcb48ba5c5` |
| Original consumed plan | `03b9298e5825080992eccc1aba336643e84c78582b68784ac0ee0a0baa36e949` |
| Fresh disabled review plan | `afe7e823222c0bbff750e8d2f0e6b4416fb0217867a1d48073910eceee5299b8` |

Fresh preparation identities: plan `a04a6ccd-4465-4f55-b60a-60881b8a0f64`; packet `787dcdcc-ec16-4a6c-b555-6e4154042d59`; operation `006c9b9e-8171-4595-9128-10fdedf3660f`. Status is `PENDING_LOCAL_GUARD_REPAIR_AND_OWNER_APPROVAL`. These identifiers reserve no external action and confer no authority.

## Demonstrated controller gaps — correction proposed before implementation

The specification/source audit inspected the original `controller.py`, `controller_tests.py`, `plan.json` and `cloudbuild.deploy.yaml`. The following are source findings; no new live operation was used to demonstrate them.

| Gap | Inspected behavior | Required local correction |
| --- | --- | --- |
| Clock override can reach execution | CLI accepts `--now` without restricting live execution; injected time controls window checks | Reject clock overrides on every provider-capable entry path; synthetic clock injection stays confined to isolated tests/no-action checks |
| Reservation is not exclusive | Only final result/CONSUMED markers prevent reuse; parallel starts or interrupted execution can pass the same precheck | Atomically reserve once before any provider call, with exclusive/no-follow creation, durable identity-bound receipt and restart refusal |
| Interruption can skip containment | `execute()` catches Exception, cleanup is outside finally, KeyboardInterrupt escapes, and SIGTERM has no handler | Route SIGINT/SIGTERM through one finally-driven cleanup path; record uncertain interrupted work and prevent duplicate cleanup entry |
| Guard fields are not enforced | Static validation checks status/hashes but not exact allowance, retry/deployment flags, grant targets, window ordering or owner receipt | Validate the full immutable action envelope and exact owner-approval binding before provider access, refusing missing, altered or extra authority |
| Commands/window use is unbounded | subprocess.run has no timeout; preflight may consume the window; each grant lacks a current deadline check | Bound commands and total stages; recheck real time before each mutation and submit; preserve a separate bounded containment deadline |
| Cleanup can be falsely reported verified | Empty `applied` becomes cleanupAllAbsent=true even when preflight found a pre-existing grant | Separate unattempted/unknown/present/verified-absent states; never remove a pre-existing grant or infer absence from an empty list |

These gaps affect the proposed release operation's authority and containment boundaries. Correcting them is a **new material local prerequisite**, not routine artifact rebinding already approved by “begin.” AGENTS.md therefore requires the explicit local decision below before implementation. This proposal does not retroactively alter the completed old build result or claim its actual cleanup failed.

Alternatives: (1) correct only these existing controller/test seams locally, then review a fresh build operation; (2) retain the repaired source and disabled packet without building until a later decision. Replaying the consumed package or approving the unchanged controller would leave demonstrated gaps in the promised safeguards and is not a recommended launch path. The proposed correction changes neither the customer feature set nor counts/dependencies outside this existing image-readiness path. It adds bounded local safety work; its effort has not yet been measured. Actual owner decision: **pending**.

## Finite local correction card — owner decision required

Reuse the existing controller, config, eight tests and receipt/provenance seams **only inside the fresh private review root**. No replacement build service, queue or customer subsystem is proposed. Preserve all original consumed files and both original and repaired source archives.

Expected local files: `controller.py`, `controller_tests.py`, `plan.json`, `README.txt` and the preparation manifest/preservation receipt in that root. The config and source archive remain byte-identical inputs. Backend evidence is limited to `evidence/APP-013/p07-repaired-build-preparation-review-20261020.md`; this proposal and normal governance status references may record actual approved work afterward. No application, UI, schema, migration, dependency or production file changes are included.

Finite implementation checklist, **if approved**:

1. Make provider-capable execution reject `--now`/injected clocks. Keep no-action checks local and distinguish disabled preparation from executable readiness.
2. Validate the exact plan/packet/operation, section, owner receipt, source/manifest/controller/config/test hashes, fixed resource/action set, USD allowance and flags. Require retryAllowed=false and deploymentAllowed=false. Bind approval to the final plan digest and prospective ordered UTC window; no self-generated approval or old receipt reuse.
3. Create one exclusive durable reservation before external preflight; fail on an existing attempt, result, stop or consumed marker, unsafe path/mode/link, identity mismatch or concurrent winner. Journal possible mutation before each grant/submission.
4. Add real-time checks before every grant and submission, finite subprocess timeouts and stage deadlines. A timeout/ambiguous submission consumes the attempt; never resubmit. Keep action cutoff/end distinct from bounded mandatory containment and its support/recovery state.
5. Use a single finally-driven cleanup entry for normal success, errors, SIGINT and SIGTERM. Track possibly applied exact grants before commands, continue independent removal/readback after another cleanup step fails, and retain truthful receipts when output/journal persistence fails.
6. Make cleanup idempotent within an execution and interruption-safe; a repeated signal cannot start competing removal loops. Recovery examines the original reservation/journal and only its possibly applied grants; it cannot restart build submission. Abrupt loss without confirmed readback is unconfirmed containment, never false verified absence.
7. Preserve unrelated/pre-existing bindings. A preflight-discovered existing grant is a stop, not permission to remove it. Emit verified absence only after fresh exact readback; keep build outcome, mutation possibility and containment outcome separate.
8. Run the finite mocked/isolated tests below, source/hash preservation checks and required governance checks; publish exact corrected hashes, test commands/results and remaining gates. Leave the plan disabled with null window/approval until a later exact external decision.

### Required local test matrix

Retain all eight original cases: early/open/late checks; consumed refusal; archive drift; tag collision; grant-failure cleanup tracking; uncertain submission/no retry; grant-remains cleanup failure; nonzero removal accepted only with confirmed absent readback.

Add these finite cases with mocked provider commands and scratch receipts; no Cloud, registry, IAM, database, Stripe or browser access:

| Boundary | Required observable result |
| --- | --- |
| Positive complete path | One reservation/submission, exact uploaded-source and build/registry digest agreement, all exact temporary grants verified absent, truthful final receipt |
| Every guard field | Missing/altered approval, identity, allowance, retry/deployment flag, grants/targets, hashes, action set or window order refuses before provider calls |
| CLI and clock | Provider-capable `--now`/injected clock refused; local test clocks cannot authorize execution; early/cutoff/end boundaries use real execution time |
| Concurrency/restart | Two isolated processes compete for one reservation: one winner and zero provider calls from loser; existing attempt/result/stop refuses replay |
| Window exhaustion | Preflight delay/cutoff before each grant or submit stops further mutation; already possible grants still enter containment |
| Command ambiguity | Hung/failing preflight, grant, submission, polling, source verification and cleanup commands terminate within assigned bounds and never trigger a retry |
| SIGINT and SIGTERM | Actual isolated signals during simulated grant/submission/polling each reach cleanup once; repeated signals cannot bypass or duplicate it |
| Partial failure/recovery | Interrupted reservation/journal, uncertain grant response and failed receipt write preserve mutation uncertainty; bounded cleanup recovery cannot submit |
| Cleanup truth | Empty applied list/pre-existing grant/readback error never means verified absence; unrelated bindings preserved; one cleanup error cannot skip remaining steps |
| Provenance/privacy | Wrong source generation/bytes/hash, image name/digest or missing terminal result cannot succeed; logs retain bounded classifications and no raw secret/provider payload |

Commands after approval: Python syntax/compile check for the fresh files; `/opt/homebrew/bin/python3 -B -m unittest -v controller_tests.py` from that root; local-only disabled-entry/no-action checks; source/config/archive preservation hashes. Any subprocess-based concurrency/signal tests must use a fake executable/provider transport and private scratch, never installed gcloud.

Governed validation: backend `SIGNMONS_GOVERNANCE_REPO=<resolved governance> node scripts/check-governance-baseline.mjs`; governance frozen-baseline/consistency and the 25 safeguard regressions; backend architecture; both repositories' `git diff --check`. Do not claim old application/runtime tests as newly run for controller/documentation changes. No new browser run is needed for this correction.

Observable local finish: corrected guard behavior and complete passing finite local evidence, original resources preserved, explicit unconfirmed outcomes retained where appropriate, fresh plan still disabled and no external calls. Implementer owns implementation/testing/evidence if approved; Debynyhan Banks owns the local prerequisite decision and every later external approval. Size is bounded to the existing controller/test seams; effort is not yet measured and no launch ETA is promised.

Rollback/disabled state: discard only the new local correction delta or retain its private review copy; preserve all old artifacts/receipts and leave external systems untouched. Any need for application changes, another subsystem, extra privileges or an expanded action set is a stop and a further proposal before implementation.

## Separate future build-only envelope — proposed, not approved

After local corrections pass, prepare a final hash-bound operation for one new prospective window. Neither the old morning build window nor October 20's selected 4:00–5:15 p.m. availability authorizes it. No start/end/cutoff is chosen here; no launch command or executable approval exists.

- Exact repaired archive/manifest above; existing config; project `signmons`; global Cloud Build; existing `signmons-build@signmons.iam.gserviceaccount.com`; source bucket `gs://signmons_cloudbuild`; Docker repository `signmons` in `us-east5`.
- Proposed candidate `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p07-atomic-893432c1de02`; require absence before mutation. Existing e2-highcpu-8/1,200-second build envelope is a proposed reuse, not a new execution approval.
- Only the same three temporary memberships: bucket storage.objectViewer, repository artifactregistry.writer and project logging.logWriter. Fresh preflight must find them absent and the existing resources/identity valid. No enabling identity, replacing resource or repairing IAM by inference.
- Proposed **USD 1 operational allowance**, unapproved and neither a current price quote nor a provider-enforced cap. No cost-bearing action occurs under this preparation/local-correction proposal; later decision must bind the allowance and exact window.
- One upload/submission; no retry after uncertainty. Require exact source generation/download/hash, terminal SUCCESS and matching build/registry immutable digest; remove/read back all possibly applied temporary memberships even after ordinary action time ends. Leave any resulting image unused.

The repaired **image digest is unknown** until that build succeeds and verification/containment finish. Local source hashes are not an image digest. Keep build outcome and cleanup independent; missing evidence cannot be called P07_IMAGE_BUILT.

## Later runtime dependency map — not an operation approval

Only after a verified repaired digest exists can a concrete runtime proposal bind it. Remaining decisions include live dedicated payment-role/hidden-credential provisioning with the locally tested grants; exact same-job/tenant/policy/payment/calendar readback; credential storage/access isolation; fresh Sandbox account/API/destination/signing bindings; numeric secret versions/costs; exact isolated deployment flags/envelope; and mandatory role/session/destination/tag/traffic containment.

The P06 role, password, numeric child-URL version2 and original negative boundary must remain preserved. The split-read helper correction is local/mock-tested and refuses execution; it does not provision a payment runtime. A new version of the existing child secret would remain accessible to that secret's existing accessors/shared runtime identity. Numeric pins do not isolate the stronger credential. A separate secret/runtime-identity/IAM arrangement is an alternative requiring its own exact decision; **no architecture option is selected here**. The old one-secret allowance cannot cover an assumed pair of new database/webhook versions.

Runtime provisioning, disabled destination/readiness and zero-normal-traffic deployment may share a later fully bound proposal; they cannot piggyback on build approval. P08 remains a separate authentic same-job Checkout/payment decision after readiness. No new customer acceptance section or denominator is created by these dependencies.

## Exact decision requested and exclusions

Decision requested now: **approve or decline only the finite local controller guard corrections and mocked/isolated tests in this card**. The owner's current authorization is preparation only; no such local correction approval is recorded. A finished corrected packet, prospective window and separate explicit build decision must follow before any provider call.

Excluded now: Cloud/IAM/registry access or mutation, source upload/build, live database or role/credential action, secret access/change, Stripe configuration/event delivery/test/resend, Checkout/card/charge/refund, Firebase activation/token mint, deployment/normal traffic, booking/dispatch, SMS/email/customer contact, production change, UI publication, repository push/merge and paid-test retry. Preparing this file does not approve these exclusions later.

Counts remain **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. APP-013 stays sole Now, the existing queue and 3A→3B→3C→3D order remain fixed, and no overall MVP percentage is inferred. **Explicit scope-deviation proposal before implementation:** the newly demonstrated local guard prerequisite is unapproved; no retrospective no-deviation claim or new subsystem is introduced.

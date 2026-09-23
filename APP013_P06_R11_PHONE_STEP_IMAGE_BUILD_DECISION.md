# APP-013/P06 R11 phone-step repair image build decision

Status: local decision/source preparation only. Owner said “proceed” after local repair evidence, authorizing this preparation, not an external build. Build window and exact build approval pending. No upload, external refresh, build, IAM change, packet or execution occurred.

## Reviewed source and purpose

Source `6d8ba541ca4cab8ef2d905defb1edcc9bacac046` adds the controlled browser guard requiring successful code CHECK before preview/submission and retains server authority. Diagnostic UTC module is a local tool; it is not added to the runtime image. Existing Dockerfile copies only the two reviewed browser assets into the final stage. Backend evidence `evidence/APP-013/p06-r11-phone-step-repair.md` records 26 mocked browser cases, 13 diagnostic tests, 111 focused tests, lint/build/architecture/governance checks. These are local results, not live R11 acceptance or proof all prior failures are fixed.

Tracked Docker inputs were archived locally to `/private/tmp/signmons-r11-phone-step-build-inputs-6d8ba54.tar`, extracted to `/private/tmp/signmons-r11-phone-step-build-6d8ba54` and the two browser assets matched to the exact source revision. 627 entries, 4,782,080 bytes, SHA-256 `89e49d29214b40ee0b71959df6b47760e97ba5df3590c313e681827a4d240abc`. Only tracked build inputs; no .git, private input, runtime packet, credentials, diagnostic results, node_modules or dist included. Source review metadata is outside the upload directory. No upload occurred.

## Alternative 1 — one repair-image build

Within a fresh owner-selected build window, after exact approval:

1. Read-only qualify the existing build identity, source bucket, repository, exact candidate tag and three relevant IAM bindings. Prior build observations are historical. Require exact source/archive contents, existing enabled `signmons-build@signmons.iam.gserviceaccount.com`, target tag absent and temporary memberships absent; otherwise stop before mutation. No database, Twilio or secret access in this build decision.
2. Submit exactly one build from source above, existing `cloudbuild.deploy.yaml` and `Dockerfile`, existing `signmons_cloudbuild` bucket, `E2_HIGHCPU_8`, timeout 1,200 seconds and USD1 operational allowance. Allowance is not a provider-enforced hard billing cap. Require enough time in the selected window for build and mandatory cleanup; do not start near its end.
3. Push only `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-6d8ba541ca4c`. Record build/source provenance, terminal result and immutable digest; do not deploy.
4. Temporary grants only: `roles/storage.objectViewer` on bucket `signmons_cloudbuild`, `roles/artifactregistry.writer` on repository `us-east5/signmons`, and `roles/logging.logWriter` on project `signmons`, all for that existing identity. Track possible application of each grant, including ambiguous command results; remove and read back all three after success/failure. Cleanup remains mandatory if the normal window expires. Cleanup ambiguity stops further work.
5. One submission, no automatic retry. Preserve one-attempt evidence on uncertain outcome. No reuse of previous consumed build helpers/IDs. Execution controller must bind exact source, window and approval before any mutation.

## Alternative 2 — retain local result

Do not build. Keep tested source and evidence for later. P06 remains 12/14.

## Subsequent gates, deliberately unresolved here

The previous one-packet capacity approval was used by enabled22. Do not infer remaining capacity or authorize a higher ceiling. Preserve every hold. After a build, a separately authorized provider/target/policy/participant/retained-liability refresh must establish whether any capacity remains before a packet decision. A browser run is separately approved with exact packet/window and mandatory closeout. No further diagnostic read or replay is included.

Exclusions: LOGIN, activation, deployment, traffic/tag routing change, database access/mutation, provider request or verification code, browser/customer action, hold release, ceiling change, secret access/change, other IAM, billing-account changes, packet preparation and live execution. Owner approval of this build decision is not permission for any of these.

Owner selects window and approves/refuses alternative 1; implementer owns one-attempt build and mandatory cleanup if approved. Finish: immutable image/source provenance plus verified cleanup, or preserved stop evidence. No image success guarantees R11. Existing disabled/closed runtime state is unchanged; no fresh runtime readback claimed. P06 remains 12/14; R11/full R12 open, accepted 1A/1B/2A unchanged. No scope deviation implemented; exact bounded build approval is pending.

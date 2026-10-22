# R1-W01 / APP-013 / 3A / P07 owner-operated account handoff card

Status: complete before preparation; approved local preparation/testing now complete. External execution remains gated.

## Authority, source and reuse

Owner approved Alternative 1 in `APP013_P07_OWNER_OPERATED_ACCOUNT_HANDOFF_PROPOSAL_20261022.md`, including the prospective owner-only clipboard exception. Backend source `1554967e19c8ef467996eefd2f460df7d638d754`; governance source `cac0af865ffb77b7e59e1ccd9aa503ea2a46a447`.

Unchanged 3A criterion: approved-policy Checkout and authentic matching Sandbox event clear the same admitted job's payment gate. Missing prerequisite: exact tenant binding remains absent/malformed per diagnostic evidence. One wrong-account hash stop and one unsupported automated Terminal handoff are consumed; mandatory closeout for the latter is independently verified. This local preparation enables a supported owner-operated handoff to the same reviewed tenant-binding transaction; it does not accept 3A.

Reuse `/private/tmp/p07-tenant-stripe-binding-handoff-repair-20261022-prep1/controller.py` and its fourteen controller/five PostgreSQL tests. Preserve the controller transaction, predicates, audit, same-job identities, account hash/double entry, readback/recovery, deadlines, no-retry and closeout logic. Change only private package path, plan/packet/operation/audit/source bindings, the exact approval action name for owner-operated handoff, and owner instructions. Do not import the unsupported direct-in-memory handoff test or renew old bindings/receipts.

## Data, state and interface boundaries

Fresh private directory `/private/tmp/p07-tenant-stripe-binding-owner-handoff-20261022-prep1`, mode 0700. Exactly six mode-0600 files: controller, existing two test files, README, disabled plan and manifest. No window or live approval at local finish. During later exact execution the owner enters the current CHILD password, then uses the unique Enabled row on **Connected accounts**, opens its account detail and copies that connected-account ID into both existing hidden prompts. The personal-details membership ID and platform URL ID are invalid sources. If the correct account-detail control is unavailable, stop.

Only the owner may use/clear the clipboard for that one account identifier. Automation cannot read/write the clipboard or operate Terminal. Account/password values stay out of chat, files, logs, arguments, saved screenshots, receipts and audit metadata. Existing hash/format/double-entry guards run before database preflight; exact tenant update plus sanitized audit remains atomic. No policy/payment gate, grants or runtime is changed by preparation. Preserve sanitized evidence/receipts; do not purge unrelated data. Fresh ID generation is recorded in the resulting package/evidence.

## Finite checklist and verification

- [x] Fresh unused package/source/approval bindings, exact owner instructions and disabled manifest.
- [x] Normalized controller comparison proves only the listed identity/approval-action substitutions; SQL and existing behavior unchanged.
- [x] Existing `python3 -B -m unittest -v test_controller.py` fourteen cases pass.
- [x] Existing `python3 -B -m unittest -v test_postgres_contract.py` five disposable PostgreSQL cases pass: commit/audit, rollback, competing writers, lost response recovery, replay refusal; cluster removed.
- [x] Syntax/private inventory/hash checks and `python3 -B controller.py --check` pass.
- [x] Run/recovery refuse without a window; synthetic scratch binding proves no-approval refusal before hidden input without external access. No executable live binding is retained.
- [x] Frozen baseline/consistency, 25 safeguards, architecture and whitespace gates; update tracker and local evidence.

Browser QA is inapplicable during local preparation: no browser/UI action is authorized; identifying the current connected-account detail/control remains a fresh read-only qualification during the later approved operation. No product build/full test claim for this private identity/instructions-only work.

## Owners, disabled state, rollback and finish

Implementer prepares/tests; owner supplies later attended block, exact approval and private inputs. Local proof depends only on existing schema/test seams and installed PostgreSQL. External action additionally requires fresh Stripe Sandbox/admin/one-enabled-account/destination-absence evidence and unchanged exact tenant/job preflight. No new helper/subsystem, live database read, provider configuration, session termination, secrets/IAM/grants, deployment, Checkout, payment, booking, messaging, merge or push.

Pre-commit failure rolls back; uncertain commit recovery is read-only and never repeats a write. Original consumed packages remain immutable. Observable finish: fresh disabled package, unchanged reviewed transaction, fourteen/five tests and all refusals verified; later bound operation still requires separate approval. Measures stay 0/27 R1, 6/60 legacy, 4/8 walkthrough, 0/13 intelligence. **Approved procedural deviation only; no additional scope deviation.**

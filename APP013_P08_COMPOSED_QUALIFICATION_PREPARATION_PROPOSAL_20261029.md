# APP-013 / 3A / P08 — composed current-state qualification preparation proposal

Status: PROPOSED; owner decision required before local implementation. Backend source `514bc8c`; governance source `cf2b063`. This proposal prepares one disabled read-only qualification coordinator and isolated tests. It authorizes no external read or mutation, credential resolution, IAM binding, API enablement, key action, account activation, runtime restoration, token, Stripe/payment, deployment, spending or attended window.

## Section, acceptance and workflow connection

Section remains R1-W01 / APP-013 / 3A / P08. The unchanged 3A criterion requires authentic same-job Stripe Sandbox settlement with exact account/mode/amount/currency, gate clearing and duplicate/out-of-order/forged/foreign/lost-response safety. P08 qualifies the exact operator and retired runtime needed to reach the existing same-job payment supervisor. This proposal adds no feature, section, acceptance criterion, dependency or denominator.

Connected workflow: admitted job -> exact disabled test operator and policy state -> bounded authentication envelope -> reviewed payment request -> Sandbox settlement. The proposed coordinator proves only the prerequisite reads needed to bind the already-tested authentication envelope. Local or later read-only success will not complete P08 or 3A.

## Inspected evidence and exact missing behavior

Stable roles are complete and retained unbound by R06. Local parent/child authentication composition is complete at backend `514bc8c` and governance `cf2b063`. It still correctly refuses native launch because current external facts are not bound.

Existing sources to reuse:

- Role closeout in `p08-exact-role-provisioning-local-20261028/source/role_provisioner.py` already reads the exact owner/project, project/identity policies and both exact role definitions without mutation.
- Restoration preflight in `p08-restoration-local-20261028/source/restore.py` already reads current candidate image/environment, traffic, dedicated identity, six retired secret versions/seven policies, database role ACL/session state and exact custom-role definitions.
- Operator qualification in `p08-operator-diagnostic-local-20261022/controller.py` already performs allowlisted read-only SQL for the exact job, tenant, payment/calendar counts, eligible operators and closed runtime database role, with hidden password and mandatory session closeout.
- Authentication adapters already define exact disabled application-user and Firebase-user reads. The disabled account ownership receipt was previously created and closed; it must be hash/permission checked, never treated as current state without reread.
- Access-resolution source already models exact Service Usage, API Keys metadata and permission-diagnostic request/output contracts, but native transport is deliberately unavailable.

These helpers are independently pinned to old operations, plans and windows. None can produce one current, source-bound qualification for the composed parent, and replaying any consumed command is prohibited. The old operator helper also includes Stripe and historical actor-selection assumptions that are not needed for this prerequisite. A new narrow wrapper is therefore required; rewriting the product or duplicating the underlying readers is not.

## Alternatives and recommendation

1. **Recommended — local-only composed read coordinator and isolated tests.** Prepare one disabled wrapper that verifies and calls copied locked read seams through injected adapters, emits one strict sanitized classification, and refuses native launch without a later exact plan/approval/window. Keep Cloud, database and Firebase reads in one later attended qualification; exclude Stripe and every mutation.
2. Run separate old Cloud, role, operator and account operations. Each requires fresh authority and produces independently timed facts that may drift before composition. This repeats windows and cannot truthfully bind one parent; not recommended.
3. Defer P08. Roles remain unbound and the disabled runtime/account remain unchanged.

Alternative 1 is a material operational prerequisite and requires owner approval before implementation. It reuses existing readers; no new provider capability, role, database contract or product path is introduced.

## Exact intended qualification contract

The future read-only qualification, separately approved after local proof, will bind one operation ID, exact source manifest/proposal/plan hashes, exact prospective composed-operation ID and deterministic key ID, current date/window, one attempt/no retry, USD 0, command/request ceilings, existing owner OAuth authority and hidden current CHILD database administrator password. It will return exactly one of `QUALIFIED`, `NOT_READY`, `DRIFT`, `UNKNOWN` or `CONTAINMENT_UNCONFIRMED`; no partial pass becomes restoration authority.

### Cloud facts

- Exact active owner with no impersonation, credential-file or access-token override; exact project ID and privately handled canonical project number.
- Current billing link enabled/open classification only as needed to distinguish service denial; no account ID, balance, invoice or payment detail retained.
- Current candidate revision image, one-container environment-name/value digests, Ready state, dedicated identity, normal100/candidate0/tag absent and current retired identity state.
- Six exact version-1 states, seven exact secret-resource policies reduced to dedicated-runtime binding presence/absence, with no secret payload.
- Both exact custom-role definitions and both exact policies; require exact active definitions and initial absence of target bindings.
- Enabled/disabled state for only the APIs required by the later approved operation: Service Usage, IAM, IAM Credentials, Identity Toolkit, API Keys and Policy Troubleshooter. Disabled required service returns `NOT_READY`; the qualification has no enable path.
- Exact effective owner lifecycle permissions needed to inspect/update the two policies and create/get/getKeyString/delete/read operations for one owned key. Use documented read-only permission-test or diagnostic endpoints only; `UNKNOWN` or unsupported results stop. Do not infer authorization from Owner label or metadata visibility.
- Exact prospective deterministic key resource must be typed `NOT_FOUND`; denial is not absence. No list, adoption, undelete or key-string request.

### Database and account facts

- One repeatable-read, read-only, allowlisted statement for the exact tenant/job. Return only strict classifications/hashes for job lifecycle/version, policy/payment gate basis, payment/calendar counts, tenant status and the exact disabled test administrator row by owned UUID. Do not return customer, address, phone, conversation, pricebook or payment-provider payload.
- Exact `p07_payment_runtime` role remains NOLOGIN, limit 0, expired, safe attributes, zero memberships/ownership/sessions and expected ACL digest. A separate read-only closeout statement verifies zero matching sessions even after interruption.
- Ownership receipt path/hash, mode 0600/non-symlink and operation identity must match the previously verified disabled-account result. It is provenance only; current application row must independently be DISABLED.
- One Firebase `accounts:lookup` for the exact owned UID using the owner OAuth bearer held only in memory. Require one disabled user, exact email/display name, exact tenant/admin/testOnly claims and revoked-token boundary compatible with the saved closeout. No account update, enable, disable, revoke, signBlob, custom token or user token.

### Privacy, timing and closeout

Raw OAuth bearer, database password/URL, project number, account identifiers, user email, UUIDs linked to private records, policies, environment values, Firebase record and provider error bodies remain in memory only. Sanitized evidence may retain operation/source hashes, fixed classifications, counts, definition digests, ACL digest and residual categories.

All reads have live wall-clock deadlines. SIGINT/SIGTERM stops normal reads and runs mandatory database/session/process/private-input closeout. One exact closeout-only invocation may verify session/process/private-plan absence and cannot resume normal reads. Private plans/receipts are mode 0600, nonsymlink and purged with absence readback by the same block end. No overnight readiness retention.

## Proposed files and interfaces

Create a new evidence-only directory `evidence/APP-013/p08-composed-qualification-local-20261029/` containing a disabled coordinator, tests, source manifest, README and sanitized local result. Reference locked sources by hash; do not edit them. Do not modify backend `src/`, UI, schema/migrations, packages/lockfiles, existing evidence or the unrelated backend `AGENTS.md` change.

The coordinator accepts injected `cloud`, `database`, `firebase`, `closeout` and clock adapters. Its native entry verifies its own/locked manifests and prints a fixed unbound refusal before reading credentials or host configuration. A later live adapter and exact operation binding are outside this local proposal and require separate review; local tests inspect the exact serialized CLI/HTTPS/SQL contracts proposed for that adapter.

## Finite checklist and required tests

- [ ] Verify current backend/governance/source hashes and the prior account ownership receipt's path/hash/permissions without opening private account contents during local work.
- [ ] Implement strict parent plan/approval/manifest/window/no-retry gates and one exclusive reservation.
- [ ] Compose the exact Cloud, role/policy, runtime/secret, database-role, job/policy/operator and Firebase read classifications; exclude Stripe.
- [ ] Serialize a finite exact read inventory and allowlisted SQL. Refuse extra command, endpoint, SQL, field, identifier, permission or service.
- [ ] Produce one aggregate verdict only when every fact is exact and closeout is verified. Preserve per-domain `NOT_READY`, `DRIFT`, `UNKNOWN` and containment residuals without raw data.
- [ ] Prove positive synthetic qualification and negative cases: owner/override/project drift; API disabled; denial vs 404; role definition/binding drift; runtime image/env/traffic/identity/secret drift; malformed/extra output; job/tenant/policy/payment state drift; wrong/active/multiple account; ownership mismatch; Firebase claims/status/revocation drift; unsafe DB role/ACL/session; raw value/error injection.
- [ ] Prove actual serialization, one-attempt reservation race, deadlines/clock rollback, response loss, SIGINT/SIGTERM at each adapter boundary, closeout-only behavior, private mode/symlink/purge rules, secret non-persistence and zero mutation verbs.
- [ ] Freshly rerun applicable unchanged role, restoration, operator/database and authentication read tests. Use disposable PostgreSQL only for the allowlisted read/closeout contract; no browser claim because no UI changes.
- [ ] Run backend governance baseline, architecture and whitespace; governance frozen baseline, consistency, 25 safeguards and whitespace. Retain initial failures and final commands.

Observable finish: all local cases pass, native launch refuses before credential access, locked sources are unchanged, local result states zero external actions and no current readiness claim. Then present one exact attended read-only qualification operation; do not silently proceed to mutation.

## Dependencies, exclusions and rollback

Implementer owns the local wrapper/tests/evidence. Owner approves this prerequisite before implementation and separately approves any later external reads and attendance. The owner supplies the hidden current CHILD database administrator password only to the later Terminal prompt; never chat. Google Cloud/Firebase and the database remain authoritative for current state.

Excluded: API enable/disable, IAM binding, role change/deletion, key create/getKeyString/delete, account mutation, signing/token exchange, runtime restore/deploy, Stripe/payment, booking, customer message/data, billing action, merge or push. Local rollback is deletion of the fresh uncommitted directory or normal revert of its isolated commit; existing sources and evidence remain untouched.

## Decision requested

Approve Alternative 1 for bounded local composed-qualification preparation and isolated tests only, or defer. Approval includes no credential resolution, external read, database/Firebase/provider action, IAM/API/key/account/runtime/token/Stripe/payment action, spending, attended window, merge or push.

Accepted 1A/1B/2A/2B remain 4/8. Newly closed R1 remains 0/27, legacy remains 6/60, intelligence remains 0/13. Stable roles and local authentication composition are complete; P08 and 3A remain open. **Explicit prerequisite change proposed before implementation; no scope deviation implemented.**

## Owner decision

Debynyhan Banks replied “i approve” after review of governance commit `747eec6` and proposal SHA256 `8f28bfdeb3b924e6a9c282c9579338ae352ad1fccda93531b7bf5f908849d157`. Alternative 1 is approved for the disabled evidence-only composed-qualification coordinator, isolated tests and sanitized local evidence described above. This decision does not authorize credential resolution, an external read, database/Firebase/provider action, IAM/API/key/account/runtime/token/Stripe/payment action, spending, attended window, merge or push.

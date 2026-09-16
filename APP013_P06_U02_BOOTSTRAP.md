# P06-U02 — bounded isolated staging bootstrap

## Owner decision and cause

Owner replied "i approve proceed" to the proposal for one bounded staging-bootstrap change reusing the existing policy services, activating only the isolated tenant and creating its regular-diagnosis category, tested locally before separately gated live execution. This expressly adds U02; it does not authorize live writes or approve the final profile wording. Entry backend b699bb2117bbcb58c821d53303cb0ab254537f6c / governance 1d008f7f5a843d0015b3a195b9175cf93f3f7d5e.

Missed prerequisite: R06 found SUSPENDED tenant, no categories or usable approved policies. TenantsController creates a new tenant, not this tenant's activation; OrganizationPaymentPolicyController is not registered in TenantsModule. JobsService's private category creation is coupled to job creation. U01 deliberately requires already-approved ACTIVE setup. Direct fixture promotion or a new public endpoint would bypass or expand the intended boundary. Chosen alternative: operator-only atomic bootstrap, reusing existing service validation/CAS/audit and U01 fixed-child connection/schema guards. No new endpoint, dependency, schema, image or provider.

## Fixed implementation card (recorded before coding)

Acceptance served: existing 2B connected verified intake; remove only its isolated setup gap, not claim admission acceptance. Exactly three exits:

1. Review a strict nonsecret packet binding source SHA, fixed child/tenant, expected timestamp/settings digest, stable category UUID, approved profile draft and fixed USD99 deposit. Bind explicit owner/action/operation/digest and <=15-minute execution window. Reject extra fields, changed source binding, invalid policy, active approvals, replay and wrong target. No private credential in packet.
2. Apply once in one guarded transaction: lock SUSPENDED tenant, compare expected state, require zero categories and absent profile/payment records, set ACTIVE/timezone, call existing profile/payment services to save then approve with actual timestamps/owner audit, create one regular category, append operation audit. Preserve all unrelated settings/holds. Recheck DB time before commit. Readback reports matching audit/current setup; separately authorized suspension uses exact post-setup timestamp/settings digest, retains category/policies/audits, refuses active runtime/phone approvals or newer state. No automatic compensation or retry after uncertain commit.
3. Prove validation/refusal, atomic rollback, duplicate/concurrent apply, stale state, readback after lost caller result, suspension and preservation using disposable PG18 and 26 real migrations. Run U01 regression, full Jest, build/lint/architecture and governance gates. No UI changes; browser acceptance not applicable to operator interface and no live journey claimed.

Expected files: scripts/p06-runtime-packet.mjs (reuse branded handles and guardDatabase; add separate bootstrap review/operation exports), scripts/verify-p06-runtime-packet.mjs (same local cluster harness), backend evidence/APP-013/p06-u02-bootstrap.md, governance card/packet/current handoffs. Existing services remain unchanged. No new command that silently consumes DATABASE_URL.

Packet category is regular diagnosis only, zero catalog base/surcharge (deposit comes exclusively from approved payment policy); existing 60-minute schema duration is staging metadata, not an appointment or quoted duration. Category ID is fixed by the reviewed packet, never regenerated on retry. Approval actor is the named owner attestation, not a fabricated Firebase authentication event. Source SHA is checked by operator against clean checkout/built artifacts before future live invocation; a JSON approval is not cryptographic proof of human authorization.

Reuse request-context AsyncLocalStorage inside the operator call and adapt existing service transaction callbacks to the single outer transaction; never start independent policy commits. No runtime module registration. Strict profile parser is reused; only exact regular fixed-deposit policy supported. Retention: business setup and audit only, no customer/provider data or credentials. Runtime/phone approval fields remain unchanged and disabled/absent.

Commands: npm run build; node --test scripts/p06-runtime-packet.test.mjs scripts/p06-migrate-once.test.mjs; node scripts/verify-p06-runtime-packet.mjs; npm run lint; npm test -- --runInBand; npm run arch:check; governance frozen/full consistency and 21 regression tests; both git diff --check. Local harness creates a private Unix-socket cluster, never reads live credentials. Before-write failure rolls everything back; uncertain outcome requires readback, not retry. Suspension is not deletion or authority to undo newer work.

Dependencies/owners: implementer completes these three local exits; owner reviews result. R06 retains IAM/cost/bindings qualification; R07 approves exact external diff; R08 owns any eventual setup execution, R10/R11 enable/run authority. Exclusions: emergency pricing, public onboarding, resource provisioning, secrets/IAM, deployment, charges, actual tenant mutation, provider calls, job/payment/booking creation and original baseline rewriting.

Size: bounded operator composition plus real-DB proof; moderate confidence, no day estimate. Observable finish: three tested exits and review evidence, then return to R06. Original12 + approved U01 + approved U02 =14; at entry six closed/eight open; after local U02 completion seven closed/seven original tasks open. Packages5/60 (8.3% tracked plan), walkthrough3/8 (37.5%), P06 unaccepted. Explicit approved scope addition U02; no further addition authorized.

## Completion

All three exits locally complete; see backend evidence/APP-013/p06-u02-bootstrap.md. The added verifier is scripts/verify-p06-bootstrap.mjs, imported by the existing disposable PG18 harness (not a new runner or live connector). No external execution occurred. Return to the seven existing R06-R12 tasks, not a new U02 subsection. This card does not approve live profile wording or an actual execution packet.

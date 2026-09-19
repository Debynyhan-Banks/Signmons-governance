# APP-013 / P06 / R10 sequence change request

## Decision status

Proposed after the stopped 2026-09-18 first attempt. Not approved or implemented. This remains within existing R10; it adds no task or acceptance criterion and grants no deployment, database LOGIN, activation, provider request, paid verification or customer action authority.

## Demonstrated gap

Approved runtime source `59f2dabc022e3c9d91a1233aece6d8c67fe6c3b4` and plan `b228f87a-ed6e-4253-a62a-b33128bb094a` required this order: open limited database LOGIN, deploy and read back the healthy zero-traffic enabled revision, then write/read back the exact runtime and phone approvals.

The actual no-traffic revision failed before listening. The runtime startup path calls the approval reader before `listen` and requires the exact active digest and current window. The approved sequence therefore required deployment health before activation while the executable required activation before deployment health. Local synthetic loader/browser evidence had active approvals in place before startup and did not prove the deploy-before-activate sequence.

The attempt remained bounded: no activation record, verification start, Address Validation request, customer session, submission or job; normal traffic stayed 100% on `app013bounds`. Mandatory failed-attempt closeout is verified: enabled tag absent, no active controlled approvals, runtime role `NOLOGIN`/limit0/past expiry/sessions0. Backend evidence: `evidence/APP-013/p06-r10-first-attempt-closeout.md` and `p06-r10-first-attempt-result.json`.

## Alternatives

1. **Recommended: transactionally activate immediately before no-traffic deployment.** Use a fresh packet/window/revision and exact digest. Read back the approval, deploy the still-zero-traffic target, and revoke immediately on deployment failure, mismatch, timeout or ambiguous result. The approval is bound to a target revision/origin that does not yet exist, so it cannot authorize the disabled revision or normal traffic. This changes the approved order but requires no product-runtime code change or new image.
2. Change runtime startup so the process can listen while approvals are inactive and keeps every controlled route closed until the approval becomes active. This changes the security model and image, and requires broader code/browser/database proof plus a new build/release review.
3. Stop P06 without another R10 attempt. This preserves the current safe state but leaves R10/R11/R12 and 2B acceptance open.

## Proposed finite correction

If the owner approves alternative 1, preparation may do only the following before a separate exact execution approval:

1. Bind a new immutable revision suffix, the stable `p06-intake-enabled` tag origin, a fresh at-most-15-minute runtime window, new packet ID/digests and new activation/revocation operation IDs. The failed revision and consumed packet remain retained and unusable.
2. Repair the guarded controller order to: complete preflight; open limited LOGIN; verify target absence and normal traffic; activate and read back the exact approval; deploy with zero traffic; verify exact revision/image/config/secrets/health; then expose the tag only for the same-session R11 journey.
3. Treat every failure after activation as mandatory revoke/readback first, then tag removal, role `NOLOGIN`/limit0/past expiry/session termination and normal-traffic readback. Unknown activation or deployment outcome gets read-only reconciliation, never automatic replay.
4. Add controller tests for successful activate-before-deploy ordering, activation failure before deployment, deployment failure after activation with mandatory revoke, ambiguous deployment reconciliation, expired window and consumed-attempt refusal. Re-run the existing runtime/startup/browser/database gates and required governance checks.
5. Produce one fresh review packet. Execution still requires the owner's explicit approval of that exact packet and absolute window.

## Impact and boundaries

- Task count remains 14; P06 remains 11/14. R10/R11/R12 stay open.
- No changes to R08 bundle, R09 disabled candidate, participant binding, caps, provider restrictions, payment/booking exclusions or normal traffic.
- No secret/IAM change, deployment, LOGIN, activation or paid request is authorized by this proposal.
- Rollback remains: revoke exact digests, remove only the enabled tag, restore runtime role inactive, terminate only its sessions and verify `app013bounds` at 100%.
- Owner decision required before implementation because this materially changes the previously approved R10 sequence. No scope deviation has been implemented.

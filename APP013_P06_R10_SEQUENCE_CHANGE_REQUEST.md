# APP-013 / P06 / R10 sequence change request

## Decision status

Owner approved alternative 1 for local controller repair and testing only: `I approve R10 sequence change alternative 1 for local controller repair and testing only. No deployment, LOGIN, activation, provider request, verification code, or execution until I separately approve the fresh packet and window.` This remains within existing R10; it adds no task or acceptance criterion. No external action or fresh execution packet/window is authorized.

## Approved local implementation card

- **Approved section and criterion:** APP-013 / P06 / R10. Repair the demonstrated controller-order defect so a future exact packet can activate/read back its bound approval before attempting a zero-traffic deployment, and guarantee ordered closeout after any activation/deployment stop. This advances the same connected phone -> address -> reviewed-submit workflow without attempting it.
- **Source and evidence:** backend `08a9e8ea56684c7eb90e3e085d222ce23c53fd6a`; governance `5aa43ad`. Reuse `scripts/p06-runtime-packet.mjs` only through injected ports in a future private wrapper. The missing behavior is established by the first-attempt evidence and the startup approval check; the private consumed controller is evidence, not a file to modify or reuse.
- **Expected files/interfaces:** add `scripts/p06-r10-controller.mjs` with no CLI and no side effect on import. Export a bounded plan/window validator, exclusive mode-0600 reservation helper, an activate-before-deploy orchestrator and an explicit closeout orchestrator. All database/Cloud/provider behavior is dependency-injected; this module must contain no credentials, target phone/address, provider client, shell command or live resource call. Add `scripts/p06-r10-controller.test.mjs` using only synthetic ports and disposable temporary files. Add backend evidence after validation.
- **State and identity boundaries:** a successful local orchestration may report only `READY_FOR_R11` after activation readback precedes deployment reservation/mutation and exact deployment readback follows it. Every mutation port is called at most once. Any failure after a possibly committed activation first performs read-only activation reconciliation; exact ACTIVE state is revoked/read back before tag removal and runtime-role shutdown. Unknown approval state is never guessed or overwritten and remains unconfirmed after best-effort tag/runtime containment. Plan validation binds a fresh revision, stable tag origin, at-most-15-minute runtime, later closeout interval and non-consumed IDs; it rejects the consumed plan/revision.
- **Finite checklist:** (1) implement pure guards/reservation; (2) implement success ordering; (3) implement activation/deployment failure reconciliation and ordered closeout; (4) implement explicit success closeout; (5) run focused positive, negative, ambiguity, ordering, single-call and recovery tests; (6) run full Node packet/controller tests, lint/build/architecture and required governance checks; (7) record evidence and stop before fresh packet preparation.
- **Test cases:** success; inactive activation failure; committed-but-unconfirmed activation; deployment throw; deployment readback mismatch; unknown approval state; revoke/readback failure; tag-removal failure; runtime shutdown/readback failure; expired/not-started/overlong/misaligned window; consumed plan/revision; duplicate reservation; explicit active and inactive closeout. Assert operation order and at-most-once calls. No browser test is claimed because no browser/runtime/provider is started; existing browser proof remains historical and must be rerun for a future exact packet.
- **Dependencies and approval owners:** local implementation is owner-approved. Any fresh packet/window, private helper installation, database LOGIN, activation, deployment, provider request, code send or R11 execution still requires a separate exact owner approval after current provider and target readbacks.
- **Exclusions:** no production runtime or schema change; no image/build, deployment, traffic/tag, database, secret/IAM, Twilio/Google, billing, participant, job, payment, booking, scheduling, dispatch or messaging action. Do not access the encrypted participant binding or secret bundle.
- **Rollback/disabled state:** the new module is unreferenced by application startup and has no CLI; deleting its files reverts the local repair. Existing service remains on `app013bounds`; runtime role and approvals remain inactive from verified closeout.
- **Observable finish:** focused and required gates pass; backend evidence names exact interfaces and test results; synchronized governance points to a future fresh-packet review. P06 stays 11/14 and R10/R11/R12 stay open.

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

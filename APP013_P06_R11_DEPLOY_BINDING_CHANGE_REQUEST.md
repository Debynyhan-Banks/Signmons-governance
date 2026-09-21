# APP-013/P06 R11 deploy-binding change request

Status: ALTERNATIVE 1 APPROVED AND LOCALLY COMPLETE. Section APP-013/P06/R11 remains open; P06 remains 12/14.

## Decision and implementation result

The owner approved alternative 1 for local repair/testing only. Backend `33d7735` adds exact plan-derived Cloud Run suffix derivation/validation and accepts an already-revoked approval only when both controlled digests match the reviewed plan. Focused controller/runtime-packet suites pass 33/33; a read-only fixture rejects the consumed enabled14 helper's stale enabled13 suffix before action. Build, lint, architecture, formatting, backend/governance consistency, frozen baseline and all 21 governance regressions pass. No packet or live action occurred. Backend evidence: `evidence/APP-013/p06-r11-deploy-binding-local-repair.md`.

## Demonstrated gap

Consumed plan `093447e7-c3cb-4db4-bdf2-53088a14729f` bound target revision `signmons-calldesk-staging-app013p06enabled14`, but its generated Cloud Run command retained the prior shorter suffix `app013p06enabled13`. The installer replaced the full prior revision string only. The no-action check validated plan hashes and current Cloud state without validating the command's suffix. Activation succeeded and was read back, deployment reserved once, Cloud Run refused the already-existing immutable enabled13 name, and automatic containment revoked the approval. No browser or provider action occurred.

Explicit closeout reached and verified the safe final state, but returned a non-fatal `APPROVAL_UNCONFIRMED` detail because the controller accepts `INACTIVE` at entry while treating the exact matching already-`REVOKED` state as unknown. Its final readback normalizes both to inactive and returned `CLOSED`. Independent Cloud readback confirms enabled14 absent, enabled tag absent and baseline traffic 100% `app013bounds`.

## Existing criterion and inspected sources

R11's existing finish remains one owner-visible protected phone/address/reviewed-submit journey with exactly one correlated job. R12 still requires complete shutdown and reconciliation. This repair changes neither criterion nor the 12/14 denominator.

Inspected sources/evidence:

- private consumed plan, controller, installer and stage records for plan `093447e7-c3cb-4db4-bdf2-53088a14729f`;
- backend `scripts/p06-r10-controller.mjs` and `scripts/p06-r10-controller.test.mjs`;
- backend `evidence/APP-013/p06-r11-1115-deploy-binding-stop-closeout.md`;
- current Cloud Run service readback after closeout.

## Alternatives

1. **Recommended: bounded local repair and testing.** Add one reviewed plan-to-Cloud-Run suffix derivation/validation seam and require private deployment helpers to obtain the suffix from that seam rather than copying a prior literal. Make no-action validation fail when the command suffix and plan revision differ. Update closeout containment to accept only an exact matching `REVOKED` approval as already contained, without issuing another revoke, while retaining final closed-state readback. Add focused tests for correct derivation, stale suffix rejection, unrelated revoked digest rejection, failure containment and exact already-revoked closeout. This is local code/private-helper repair only.
2. Continue manual string substitution and add another checklist review. This leaves the demonstrated class of mismatch structurally possible and is not recommended.
3. Stop R11. This avoids another controlled run but leaves APP-013/2B acceptance incomplete.

## Expected files and boundaries for alternative 1

- Backend `scripts/p06-r10-controller.mjs`: exact revision-suffix derivation/validation and matching-revoked closeout classification.
- Backend `scripts/p06-r10-controller.test.mjs`: focused positive, negative, containment and recovery coverage.
- One private consumed-helper fixture or local generated fixture: prove `enabled14` cannot pair with an `enabled13` deploy suffix and that no-action validation catches the mismatch. Do not create a live packet or authorization.
- Evidence and synchronized governance status after checks.

The repair preserves current packet schema, digests, activation ordering, zero-traffic requirement, normal-traffic baseline, one-use reservations, no-retry behavior, private input, cost holds and mandatory final readback. It creates no new provider, database, UI or acceptance section.

## Approval boundary

Alternative 1 requires explicit owner approval before implementation. Approval covers local repair and tests only. It does not authorize packet preparation, a new phone ceiling allowance, database LOGIN or mutation, activation, deployment, provider request, verification code, browser/customer action, secrets/IAM, billing change or live execution. Any future run requires a fresh window, read-only qualification and packet preparation authorization, then separate exact execution approval.

No scope deviation implemented.

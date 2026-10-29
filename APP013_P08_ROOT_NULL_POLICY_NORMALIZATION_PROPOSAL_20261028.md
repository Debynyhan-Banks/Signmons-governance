# APP-013 / 3A / P08 — root-null projected-policy normalization proposal

Status: OWNER DECISION REQUIRED BEFORE IMPLEMENTATION. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated gap and workflow connection

Operation `743447a5-f14f-4a48-8dd0-f674d024a94c` consumed all five permitted CLI reads and stopped before HTTPS or mutation at `CLI_5_IDENTITY_POLICY`. Safe classification proved the project policy is a valid nonempty binding list and the dedicated-identity projection is invalid under the current object-only contract. Created and unknown counts were zero. Because the command projects only `bindings` and raw output was intentionally not retained, a root-level JSON null for an identity with no projected bindings is the narrow likely cause, but remains an inference.

The current APP-013 / 3A / P08 acceptance criterion and customer workflow remain unchanged. The stable unbound roles remain a prerequisite for bounded owner authentication; this proposal changes no permission, role, dependency, section, denominator or acceptance criterion.

## Alternatives

1. **Alternative 1 — recommended: accept root JSON null only as an empty projection.** Add fixed classification `ROOT_NULL`; normalize only a root null to an empty binding set. Continue to reject root lists, strings, numbers and booleans; unexpected object fields; malformed bindings; and either exact target-role binding. Retain only fixed shape classifications in evidence.
2. Add more safe sub-classifications and run a diagnostic-only provider read. This confirms the exact invalid form but adds another external operation without advancing role creation.
3. Defer P08. This preserves the stop and leaves 3A blocked.

Alternative 1 is the smallest semantic correction: null at the root and null in the projected field both represent no projected binding data, while every populated or malformed structure remains subject to existing fail-closed checks.

## Complete correction card

- **Approved section if authorized:** R1-W01 / APP-013 / 3A / P08.
- **Source/evidence:** backend `334a7a3`; `p08-exact-role-creation-r04-stop-20261028`; project `NONEMPTY_LIST`, identity `INVALID`, CLI5/HTTPS0, created0/unknown0.
- **Files/interfaces:** only the existing evidence helper, focused tests, manifest/result and governance result/pointer documents. Exact five-CLI/nine-HTTPS serialization remains unchanged.
- **State/identity/retention:** same owner, project, dedicated identity, two role names and exact permissions. Store only fixed classifications; no role/member/policy body/bearer/raw output.
- **Finite checklist:** add `ROOT_NULL`; normalize root null only; retain rejection of every other root scalar/container drift; prove target-binding and malformed-policy refusal; prove exact external serialization; run repository gates; save sanitized local evidence.
- **Tests:** root-null positive; field-null/absent/empty-list positives; root list/string/number/boolean negatives; unexpected fields/malformed binding negatives; target and unrelated nonempty bindings; interruption/deadline/private-input cleanup; exact call contract.
- **Concurrency/recovery/browser:** existing reservation, signals, deadlines and no-retry behavior remain; browser testing is inapplicable.
- **Dependencies/approvals:** owner approval required before implementation; any later provider action requires fresh exact approval.
- **Exclusions:** no credential resolution, provider/gcloud read, role or binding action, IAM/API/secret/account/database/token/runtime/deployment/Stripe/payment/customer action, spending or acceptance update.
- **Rollback/disabled state:** helper remains disabled and bound-launch-only. Revert only this normalization/classification commit if checks fail.
- **Observable finish:** focused matrix and all required repository checks pass; sanitized evidence confirms zero external calls; any fresh operation is proposed separately.

## Decision requested

Approve or defer Alternative 1 for bounded local correction and isolated tests only. Approval would not authorize a provider read, retry or mutation. **Demonstrated parser prerequisite proposed before implementation; no scope deviation implemented.**

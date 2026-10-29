# APP-013 / 3A / P08 — empty projected-policy normalization proposal

Status: OWNER APPROVED ALTERNATIVE 1 FOR LOCAL CORRECTION AND ISOLATED TESTS ONLY. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: On October 28, 2026, the owner approved Alternative 1 against this document's pre-decision SHA256 `8213221e444df5c87feabbbc376561a3532bb50918d660720bc59f9b1591c9d1`. Authority is limited to the local files, normalization, safe classifications and isolated checks below. It does not authorize any provider read, retry or mutation.

## Demonstrated gap and workflow connection

Operation `d45f0618-c8a9-4c85-910a-c60c9352e9cc` consumed all five permitted CLI reads and stopped before HTTPS or mutation at `CLI_5_IDENTITY_POLICY`. The fixed reason was `ROLE_DRIFT`; created and unknown counts were zero. The controller requested only `json(bindings)`, so the narrow likely cause is an empty projected policy represented as a null `bindings` field rather than a list. Raw output was intentionally not retained, so this cause is an inference, not a confirmed provider fact.

The current APP-013 / 3A / P08 acceptance criterion still requires the same exact-job owner authentication and payment-supervisor workflow. The stable unbound lookup/signing roles are a prerequisite for the bounded authentication path; this proposal changes no customer behavior, role permission, dependency, section ID, denominator or acceptance criterion.

## Alternatives

1. **Alternative 1 — recommended: narrow null-as-empty normalization plus explicit safe classification.** In the existing disabled helper only, accept `bindings` when absent, an empty list, or null; normalize null to an empty list. Continue to reject every other top-level type, every non-list/non-null value, malformed binding, target-role binding and unexpected definition. Add a fixed safe policy-shape classification to distinguish `ABSENT`, `NULL`, `EMPTY_LIST`, `NONEMPTY_LIST` and `INVALID` without retaining roles, members, policy bodies or raw output.
2. Add only the safe classifier, then request another read-only provider diagnostic before changing normalization. This confirms the shape but adds another governed external operation and does not advance the launch path.
3. Defer P08. This preserves the current stop but leaves 3A blocked.

Alternative 1 is smallest because null and an absent field are equivalent empty projections for the exact gate, while all nonempty bindings still receive the existing exact target-role check. The new classification makes the next stop auditable without exposing policy content.

## Complete correction card

- **Approved section if authorized:** R1-W01 / APP-013 / 3A / P08.
- **Source/evidence:** backend `a64e933`; `p08-exact-role-creation-r03-stop-20261028`; fixed stage `CLI_5_IDENTITY_POLICY`, `ROLE_DRIFT`, CLI5/HTTPS0, created0/unknown0.
- **Files/interfaces:** only the evidence-contained `role_provisioner.py`, its focused test file, local manifest/result, and governance result/pointer documents. Native call count and command serialization remain five CLI/nine HTTPS.
- **State and identity boundaries:** exact project `signmons`, owner `debynyhan@signmons.com`, dedicated identity, two fixed role names and exact permissions remain unchanged. No policy body, member, bearer, identifier, credential or raw stderr is retained.
- **Finite checklist:** normalize only absent/null/empty-list; preserve nonempty exact-role detection; add five safe classifications; prove native serialization unchanged; test result/cleanup behavior; run required backend/governance gates; save sanitized local evidence.
- **Tests:** positive absent/null/empty-list; negative scalar/object/malformed binding; target role present; unrelated nonempty binding; interruption/deadline/private-input cleanup; exact five-CLI/nine-HTTPS native contract; repository baseline, consistency, architecture and whitespace checks.
- **Concurrency/recovery/browser:** no shared state or browser surface changes. Existing attempt reservation, signal cleanup, deadline and no-retry behavior remain. Browser testing is inapplicable to this parser-only correction.
- **Dependencies/approval owners:** owner approval is required before implementation. Any later provider read or role creation requires a new exact operation and separate approval.
- **Exclusions:** no gcloud/provider call, credential resolution, policy read/body retention, custom-role creation/binding, IAM/API/secret/account/database change, runtime restoration, deployment, Stripe/payment/customer action, spending or acceptance update.
- **Rollback/disabled state:** helper remains disabled and cannot launch without a fresh private exact binding. Revert only the normalization/classification commit if tests or checks fail.
- **Observable finish:** focused tests and all required repository checks pass; sanitized evidence states no external call occurred; a fresh operation proposal is presented separately.

## Decision requested

Owner approved Alternative 1 for bounded local correction and isolated tests only. Approval does not authorize any new provider read, retry or mutation. **Demonstrated parser prerequisite approved before implementation; no scope deviation.**

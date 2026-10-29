# APP-013 / 3A / P08 — omitted false-valued role-deletion normalization proposal

Status: OWNER DECISION REQUIRED BEFORE IMPLEMENTATION. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated gap and workflow connection

R05 created both exact roles and recorded unknown0. The first lookup-role GET returned HTTP 200 in both the creation readback and independent closeout, but strict definition validation rejected the response before reconciliation. Both target-role policy checks passed unbound. The current validator requires `deleted` to be explicitly false. Google IAM documents `deleted` as a read-only boolean in the Role resource; JSON serialization commonly omits false/default fields. Because raw output was intentionally not retained, omission of `deleted` is the narrow likely cause, but remains an inference.

The APP-013 / 3A / P08 acceptance criterion and customer workflow remain unchanged. This proposal changes no role, permission, policy, dependency, section, denominator or acceptance criterion. It only permits exact verification of the two roles already created.

## Alternatives

1. **Alternative 1 — recommended: normalize omitted `deleted` to false and add safe definition classifications.** Accept an absent `deleted` field as false only when every retained field is otherwise exact; continue to reject explicit true, non-boolean values, missing/mismatched name/title/description/permission/stage, extra fields and malformed roots. Record only fixed definition classifications such as `EXACT_ACTIVE_EXPLICIT`, `EXACT_ACTIVE_DEFAULTED`, and `INVALID`, never role bodies.
2. Add safe sub-classifications first, then perform a diagnostic-only GET. This confirms the exact mismatch but requires an extra external operation and still leaves definitions unverified.
3. Defer P08. The two created unbound roles remain present but unverified, blocking 3A.

Alternative 1 matches the documented boolean contract while preserving exact verification of every security-relevant field. A later operation would be read-only closeout only; creation must not be retried.

## Complete correction card

- **Approved section if authorized:** R1-W01 / APP-013 / 3A / P08.
- **Source/evidence:** backend `c165a92`; `p08-exact-role-creation-r05-stop-20261029`; created2/unknown0; lookup HTTP 200 with repeated definition `ROLE_DRIFT`; policies passed unbound.
- **Files/interfaces:** only the existing evidence helper, focused tests, manifest/result and governance result/pointers. Creation serialization remains unchanged; independent closeout remains five CLI plus two read-only HTTPS GETs.
- **State/identity/retention:** same project, owner, dedicated identity, role names and exact permissions. Retain only fixed classifications/hashes/counts; no role body, bearer, policy member or raw output.
- **Finite checklist:** classify exact explicit/defaulted/invalid definitions; default only absent `deleted`; reject explicit true/non-boolean/all other drift; verify both-role closeout continues after exact defaulted lookup; run focused and repository gates; save sanitized local evidence.
- **Tests:** explicit false and omitted deleted positives; explicit true, null/string/number deleted negatives; missing/mismatched security fields; extra fields; both-role read-only closeout; unbound policy checks; signal/deadline/private-input cleanup; exact external serialization.
- **Concurrency/recovery/browser:** existing attempt reservation, signals, deadlines and no-retry behavior remain; browser testing is inapplicable.
- **Dependencies/approvals:** owner approval required before implementation. A later read-only closeout requires fresh exact approval. No creation retry is permitted.
- **Exclusions:** no credential resolution, provider/gcloud call, create/update/delete/undelete/binding action, IAM/API/secret/account/database/token/runtime/deployment/Stripe/payment/customer action, spending or acceptance update.
- **Rollback/disabled state:** helper remains disabled and bound-launch-only. Revert only this definition normalization/classification commit if checks fail.
- **Observable finish:** focused matrix and all required repository checks pass; sanitized evidence confirms zero external calls; a read-only closeout proposal is presented separately.

## Decision requested

Approve or defer Alternative 1 for bounded local correction and isolated tests only. Approval would not authorize a provider read, role creation retry or mutation. **Demonstrated verification prerequisite proposed before implementation; no scope deviation implemented.**

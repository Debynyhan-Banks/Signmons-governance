# APP-013 / 3A / P07 runtime-envelope preflight correction proposal

Status: **Alternative 1 owner-approved for local correction/testing only; no external action authorized**. On October 20, 2026, Debynyhan Banks replied **“yes”** to the exact decision request below.

## Demonstrated gap

The approved repaired-runtime operation stopped once during `CLOUD_PREFLIGHT` with `P07_STOP_RUNTIME_ENVELOPE_DRIFT`, before mutation. Sanitized receipts report `possibleMutation:false`, empty mutation sets, verified database-role absence/zero sessions and no containment failure. The operation is consumed.

Read-only Cloud Run evidence confirms 100% traffic remains on `signmons-calldesk-staging-app013dbrot2`. The preserved normal revision has 1 CPU, 512 MiB, concurrency 40, timeout 60, maximum instances 2, startup CPU boost enabled and no explicit CPU-throttling annotation. The approved P07 candidate is intentionally narrower: maximum instances 1 with explicit request-based CPU.

The controller calls the target-candidate envelope validator on the existing normal service during preflight. This incorrectly requires the preserved normal revision to equal the new candidate envelope. The mismatch is a controller readback-model defect, not evidence of a provider mutation.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Separate normal-revision and candidate-envelope validators | Preflight reads the exact 100%-traffic normal revision and verifies its observed preserved envelope; deployment/readback continues to require the stricter candidate envelope. | **Recommended** |
| 2. Change the candidate to maximum 2 with implicit CPU allocation | Makes both envelopes alike but expands the approved candidate capacity/cost boundary and weakens explicit configuration. | Reject |
| 3. Remove runtime-envelope validation | Avoids this stop but could miss traffic, identity, capacity or execution-policy drift. | Reject |

## Exact proposed local change

- In a fresh private copy, make Cloud preflight describe the exact revision named by the single 100%-traffic route.
- Add a normal-revision validator bound to: existing runtime identity, timeout 60, concurrency 40, 1 CPU, 512 MiB, maximum 2, minimum absent/zero, startup CPU boost true and CPU-throttling annotation absent. Continue to require service ingress `all` separately.
- Preserve the existing candidate validator unchanged: dedicated P07 identity, timeout 60, concurrency 40, 1 CPU, 512 MiB, maximum 1, minimum absent/zero, explicit CPU throttling true, startup boost true and ingress all.
- Add focused tests proving: exact normal state passes; normal identity/capacity/resource drift fails; candidate maximum 2 or missing explicit throttling still fails; traffic must remain exactly 100% on the named normal revision.
- Re-run all package tests, syntax/no-action/refusal checks, governance baseline/consistency/safeguards, backend architecture and both whitespace checks.

No provider/database/Stripe action, role/secret/IAM change, deployment, payment, customer action, new acceptance section or denominator change is included. After review, any new live operation requires fresh plan/packet/operation IDs, a new attended window and separate exact external approval. The consumed operation cannot be replayed.

## Decision requested

**Decision recorded:** Alternative 1 approved for local correction and testing only. The observable result is a fresh disabled, tested package proposal; it is not a live command. Any new live operation still requires fresh IDs, a new attended window and separate exact external approval.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Approved correction to unintended controller-assumption drift; local implementation/testing only.**

# APP-013 / 3A / P08 — ET1 local correction completed

ET1 is implemented and locally verified at backend source `4173ec0b3b8bf3dc81d607275a427101615a4c35`, under the owner's exact local approval `32cabcd`. The approved proposal remains unchanged, SHA256 `3305612d4aca2cd7c5af481103d5876cdced1dba2e86f98adb652649cbea5507`. This record completes that local correction; it grants no external authority.

## Requirement and demonstrated gap

The unchanged section 3A exit is an owner-completed Sandbox payment on the admitted job, with a matching signed account/mode/amount/currency event clearing its gate; negative and replay cases must remain safe. See `APP013_REMAINING_EXECUTION_CONTRACT.md:62` and the PaymentPolicy/payment-state contracts. ET1 advances the existing authentication prerequisite for that same workflow, without replacing the payment stack.

KQ1's immutable result at backend `53925c43f95c2a713341dafdbba0be8d44c65668` proved the same active key UID at both metadata observations, with etags different from the creation receipt. Authentication stopped before keyString. The separately authorized cleanup confirmed CONTROL_PLANE_DELETED, private purge, process absence and empty residuals. Why the provider changed the etag remains UNKNOWN; R46's historical cause remains UNKNOWN. KQ1 is consumed and must not be replayed.

## Completed finite checklist

1. Recorded owner approval before editing, with source, demonstrated gap, interfaces, state boundaries, exclusions and rollback in the approved proposal.
2. Reused the current native `Ports.normalized_key` seam to validate the full metadata contract, exact owned UID and retained lifecycle provenance, then atomically update only the current etag. Original creation time, creation operation/intent, absence observation, root/source/request identity and deletion fields remain unchanged. In-memory state updates only after persistence succeeds.
3. Preserved inherited authentication and conditional deletion. Pending/deleted states cannot authorize authentication or another delete. A later version race still fails the conditional delete without retry. No additional provider or cache call was added.
4. Kept KQ diagnostic comparisons against the original creation etag held only in memory. The historical KQ1 result, historical bridge/coordinator and KD cleanup implementation are unchanged.
5. Added meaningful assembled positive, negative and recovery coverage: distinct versions through creation/authentication/cleanup; exact ownership/restrictions/provenance; timestamp equivalence and nanosecond drift; interrupted persistence; fresh-process cleanup; deleted/pending state; conditional conflicts; and Handoff compatibility. Existing deadline, concurrency, privacy, no-retry and cleanup tests remain intact.
6. Refreshed current manifests with the existing helper, passed all applicable suites and checks, obtained independent read-only review, and verified the actual operator's current-plus-committed source guard in 0.462232 seconds under its 8-second bound. The unbound future template is correctly refused with KQ1_OPERATION.

## Local evidence

Backend evidence: `evidence/APP-013/p08-connected-packet-20261110/et1-local-verification-20261114/verification.json`, its hashed logs, and `et1-source-verification.json`.

| Verification | Result |
| --- | --- |
| Native Python suite | 119 passed |
| Connected Python suite | 136 passed |
| Qualification Python suite | 290 passed |
| Correction Python suite | 52 passed |
| Node transport/payment tests | 25 passed |
| Governance tests | 25 passed |
| Total, without double-counting focused subsets | 647 passed |
| Lint, build, architecture, frozen baseline, cross-repository consistency and whitespace | Passed |
| Independent runtime/test diff review | Passed, including the final provider-deleted metadata case |

All suites exercised the final runtime bytes. The native suite reran after the last additional negative test and manifest refresh; unchanged suites were not rerun solely for that test-file change. Local lifecycle fixtures reported servers reaped and scratch absent. ET1 used zero credential reads, provider calls, external SQL calls or payment attempts. KQ1's earlier live counts remain separately recorded as 4 CLI, 2 cache and 10 HTTPS reads/requests; ET1 does not erase or relabel them.

## Readiness, remaining work and responsible owners

`APP013_P08_ET1_LOCAL_READINESS_20261114.json` records prerequisite-to-source/evidence traceability. `APP013_P08_ET1_FUTURE_QUALIFICATION_TEMPLATE_20261114.json` binds the corrected source and actual command interface, but intentionally has no operation UUID, window or external approval. It is not executable authority. The runtime's 360-second minimum cleanup reserve is distinct from the prior live packet's reviewed 480-second operational reserve; future timing must be reviewed against the actual permitted calls.

Local implementation, regression verification and source binding are complete. Current provider keyString behavior, usable authentication and same-job payment/application-gate evidence under this source remain UNKNOWN. The next observable result is a new, separately approved qualification reaching the keyString/inert-sink boundary and proving independent deletion/private purge, or one bounded recorded failure. A full payment run still requires its own readiness and owner decision after prerequisites are resolved. No live retry or attendance session is started here.

The implementer owns current source/configuration/readiness checks and evidence; the owner/cloud custodian owns any new external authorization and credential coverage; the product owner owns section 3A acceptance. Rollback remains the approved source-before overlay/manifests at `53925c4`, with the native path disabled pending review. No provider rollback is part of ET1.

Accepted 1A/1B/2A/2B remain **4/8**; **3A OPEN**; R1 newly closed **0/27**. No promotion to 3B. **No scope deviation:** this is the owner-approved ET1 internal correction; no acceptance criterion, section count, external budget or payment scope changed.

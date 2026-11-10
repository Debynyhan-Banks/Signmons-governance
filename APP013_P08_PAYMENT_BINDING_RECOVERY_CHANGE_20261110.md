# APP-013 / 3A / P08 — payment binding recovery contract correction

Status: OWNER DECISION PENDING; proposal only, no implementation or external authority. This is a material read/retention contract change to the existing recovery seam, not another acceptance section or a new subsystem. Existing local integration approval159b9e7 remains valid for its approved scope. This record does not retrospectively claim that expanded recovery business-data retention was approved.

## Demonstrated gap and source

Backend7f7b7b7eea370cb9b7deb5f11505f14b7f2955d0; governanceec68838. Sanitized exact byte inventory: backend evidence/APP-013/P08_PAYMENT_BINDING_PRODUCER_AUDIT_20261110.json.

qualification_launch.py:152–164 selects job/policy information but omits Job.updatedAt, connected account and charges status. recovery_values:1676–1688 returns only projectNumber/targetId; read_recovered_bindings:1756–1766 rejects extra fields. Native authority.py:163–180 requires payment amount/currency/approvedAt/policyDigest/jobUpdatedAt/account hash before the qualification scope is accepted. The current connected fixture supplies these synthetically. The custody test transfers an already-constructed envelope; it does not produce the payment binding from real recovery SQL output.

Therefore another unmodified recovery/full qualification would still lack the fields needed for the connected payment packet. The previous local proof of payment/session/cleanup remains valid. The statement that checklist5 local closeout was complete was too broad with respect to packet input production; it is reopened for this bounded contract decision and implementation. No accepted milestone is reset.

## Proposed exact change

Extend only version2 of the existing recovery seam. Version1 output, query and historical pinned evidence remain unchanged. No additional read round or standalone qualification helper.

The version2 recovery SQL remains one fixed, repeatable-read READ ONLY transaction on the existing CHILD database and exact tenant/job/operator. Reuse the existing projection/query boundaries; include Job.status/deletedAt/updatedAt/calendarEventId/serviceWindowStart/serviceWindowEnd/policySnapshot/pricingSnapshot; tenant status/chargesEnabled/stripeConnectAccountId and organizationPaymentPolicyV1; exact disabled test ADMIN; and exact payment/calendar counts. Serialize Prisma timestamp without timezone explicitly as UTC with milliseconds, matching the existing native payment projection. Keep the two existing independent session-closeout queries. No writes, broad row enumeration, new table, credential read or provider call.

Derive through the actual source-pinned organization-payment-policy.profile implementation, not a second policy parser: paymentBinding exactly {amountTotalCents,currency,approvedAt,policyDigest,jobUpdatedAt,connectedAccountSha256}. Validate current fixed-policy types/amount, controlled-v2 admission digest, same tenant/job, no prior payment/scheduling activity, active charges-enabled tenant and pinned account hash. Recovery expects the operator DISABLED; payment execution still requires ACTIVE. Never fabricate one phase's actor/role state to satisfy another validator. Hash canonical application profile serialization, not sorted-envelope serialization.

Version2 recovered-inputs.json becomes exactly {projectNumber,targetId,paymentBinding}; version1 retains its two-field schema. Store only derived binding fields; discard raw policy/account/SQL response from memory after derivation. Retain within the existing owned0600file/0700root, same guard, same purgeEnd and ownership readback; no new private file or longer retention. Transfer into the exact nativeScope before qualification and compare again at native payment entry. Drift refuses and cleans up; no implicit reapproval, new key or retry. Endpoint raw identifier remains a separately approved exact manual Dashboard binding, hash-checked against the existing observation; this correction does not add endpoint enumeration or secret access.

Expected files: active qualification_launch.py and tests/manifests; active connected_payment.mjs and its tests if a reusable derivation export is needed; native manifest locks for changed qualification source. Preserve all historical locked modules. Existing guarded recovery, transfer, actual native consumer, payment policy profile and local TLS fixture are the reuse components. No new launcher subsystem, application payment logic, SDK, schema, deployment or fee.

## Finite checklist and observable finish

1. Complete the version2 SQL/output/retention contract and shared actual-profile derivation; preserve version1. Bind exact changed source/manifest bytes and approved read contract before any external use.
2. Prove production and consumption in one local test: actual owned TLS SQL recovery output → actual derivation → guarded transfer → full qualification scope → actual native payment child → independent cleanup/purge. Do not inject fixture paymentBinding after recovery. Test null/missing/extra/foreign/stale fields, disabled-versus-active actor phase, timezone serialization, account/policy drift, occupied private roots, concurrency, interrupted transfer and purge deadline.
3. Recompute all reservation counts using actual interfaces; proposed recovery remains2CLI/3SQL with identical deadlines and no new call. Run focused/full affected qualification/native tests, browser/TLS gates where changed, build if compiled application dependency changes, lint/architecture, both governance checks/25safeguard tests and whitespace. Update the original connected live proposal and exact readiness record before scheduling or requesting execution approval.

Finish: source-pinned local evidence demonstrates the payment binding is produced from actual recovery SQL and consumed unchanged by the existing workflow. Then assemble the single connected live packet with current bindings, exact timing and separate owner/custodian approval. Until then no Terminal attendance, SQL-password prompt, provider read or recovery/full qualification is scheduled.

## Decision, alternatives and impact

Requested owner decision: approve this specific expansion of the version2 recovery read/retention contract and its bounded local implementation/tests. It does not authorize running the expanded query externally. Owner-approved native payment authority remains a later concrete decision after readiness, not an automatic consequence of this change.

Alternative: owner supplies all six current payment-binding fields from an independently verified record for the same job/policy/account, plus private identity/endpoint bindings through the approved channel; freshness and exact scope still require validation. Replaying existing recovery without either correction or independently supplied binding is not a viable path. Pausing3A is also possible.

Impact: three implementation/checklist items inside the existing connected prerequisite; no change to section count, acceptance criteria, fees or order2B→3A→3B→3C→3D. Additional local correction/testing effort is required; no external session estimate until it passes. Rollback: retain current version1 and version2 code, no new external authority; do not schedule a non-consumable qualification. Implementer owns correction/test/packet; product owner owns read/retention contract decision; credential/DB/provider custodians retain separate external authority.

Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. Explicit prerequisite contract deviation proposed; none implemented. Current provider/key permissions, payment fields and authentic delivery remain UNKNOWN.

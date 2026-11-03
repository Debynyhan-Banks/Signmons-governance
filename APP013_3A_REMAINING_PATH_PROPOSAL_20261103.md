# 3A remaining path — bounded proposal

Status: documentation-only proposal requested by owner “proceed”. No implementation or external execution authority inferred. Section R1-W01 / APP-013 / 3A / P08. No new acceptance sections.

## Outcome and remaining work

Finish the existing same-job Sandbox payment journey. Local role/ACL proof is complete; it does not complete payment acceptance. Three work blocks remain:

| Block | Required finish | Current status / owner |
| --- | --- | --- |
| Local readiness integration | Current facts bound to one exact operation; complete column ACL checked at entry, enabled-state readback and retirement/independent closeout; actual transport and cleanup boundaries proved | Incomplete; implementer |
| Fresh qualification and attended journey | Current prerequisites pass, approved temporary access/authentication is closed, same admitted job completes Sandbox Checkout and authentic settlement | Live facts UNKNOWN; provider/DB/credential owners and product owner |
| Acceptance | Same-job evidence, refusal/replay cases and authoritative cleanup reviewed by owner | Pending; product owner |

This is a remaining-work inventory, not a claim that three commands or three approvals suffice. A failure may require a specific correction; it must not silently expand this inventory.

## Acceptance trace and inspected missing behavior

APP013_REMAINING_EXECUTION_CONTRACT.md §3A requires owner-completed Sandbox payment on admitted job9180bef4-561d-47a0-869f-925e6a3dfd96, matching mode/account/amount/currency signed event clearing its gate; redirect alone and unpaid/failed/forged/foreign events cannot clear it. Duplicate/out-of-order and lost-response replay must neither duplicate logical requests nor regress settlement. DATA_CONTRACTS payment policy preserves fail-closed fee/deposit gating. Reuse payment-requests.service.ts, stripe-checkout.provider.ts, stripe-webhooks.service.ts and existing customer controls after current source inspection; no payment-stack replacement.

Inspected authority.py100–108 requires exactly nine true checks, same operation ID, exact scope digest, qualification validity through cleanupEnd, runtimeEnvironmentSha256 and roleAclSha256. Existing local role evidence intentionally emits neither this qualified object nor live authority. Inspected restore.py NativeAdapter.role/readback omits column ACLs and compares only the legacy projection; the new real-PostgreSQL test proves a column grant can change without that digest changing. These are demonstrated integration gaps in the prerequisite to the same customer journey, not new product features.

## Proposed local boundary — complete before scheduling any live window

1. Trace the existing actual native-entry, restore and independent-closeout call chain and source manifests. Specify the smallest integration seam that checks complete ACLs in retired and temporarily enabled states while preserving the existing phase-specific role predicates. Do not use the retired-only classifier during enabled operation. Preserve historical locked modules/receipts; any required change to a locked dependency needs an explicit versioned change record.
2. Complete the current-state producer contract using the existing nine-check map in APP013_P08_CURRENT_STATE_SCOPE_PROPOSAL_20261103.md. Independently pin expected runtime environment and full ACL before comparison; never accept hashes computed from arbitrary observed drift. Bind source, decision, target, scope, observation time and expiry to the same future operation. Partial/stale/cross-operation evidence stays unqualified.
3. Resolve actual cached-token/HTTPS/SQL credential ingress and effective-access diagnostics, including dynamically derived settings, output contracts, limits and independent session/process cleanup. Reuse proved transports. The old launcher’s26 CLI/10 HTTPS/2 SQL descriptors are historical implementation counts, not an approved minimum or retry guarantee. SDK renewal authority is consumed and cannot transfer.
4. Produce one finite integration card listing exact changed files/interfaces, immutable dependency impact, commands, approved expectations, owners and rollback before coding. Acceptance tests must cover positive flow; missing/null/foreign/stale data; column drift before/during/after operation; active/retired phase mismatch; scope/source mismatch; single-use concurrency; deadline/clock rollback; interruption/partial-failure; actual SQL/TLS/session cleanup; sanitized output and purge. Reuse existing unit, disposable PostgreSQL, native-entry and real-client tests. No customer browser work is needed for this local prerequisite; browser payment gates remain required for the journey.

This proposal does not pretend that the exact integration card is already complete. Unresolved local decisions: chosen manifest-safe seam; full-ACL binding representation compatible with existing authority; approved independent environment expectation; effective-access proof and actual credential/transport selection. Implementer owns these before an execution request. No live read is needed merely to inspect these local contracts.

Recommended approach: extend existing interfaces with complete ACL validation and a scope-bound producer. Alternatives: administrator-supplied facts still require the same provenance/freshness checks and do not repair lifecycle ACL coverage; deferral preserves the disabled state. No subsystem/service or arbitrary all-true qualification object is proposed.

## Minimum live evidence categories — exact read budget still to be derived

After local proof, a qualification-only packet must specify actual fixed requests/SQL, source hashes, resource pins, credential method, one attempt, start cutoff, expiry, cleanup deadline and independent closeout. Only these existing prerequisites belong in its scope:

- Owner/project identity and credential validity; current billing linkage/open state; exact required services and usable effective access.
- Existing safely retired role, full expected ACL and effective exposure; exact database/operator/tenant; same admitted job and current policy; calendar absence.
- Exact owned disabled Firebase test identity and required revocation/claims facts.
- Exact candidate/normal runtime, approved environment digest, retired identity/secret/binding/tag state and prospective-key state where required by the actual operation.
- Current owned private inventory, process/session state and scope/expiry binding.

Historical observations are supporting evidence only. Current values are UNKNOWN. Combine compatible reads within the same approved scope where possible; do not promise a request count or schedule until actual interfaces and token lifetime are proven. Qualification permits no grants, role enablement, key creation, billing change or customer/payment action. Fresh temporary restoration/authentication and Sandbox payment need their exact action approval; no expired packet may be replayed. Failure means stop and report the responsible owner, not retry or invent substitute offline work.

## Final customer proof and finish

Inspect current payment code/configuration and run applicable existing unit/integration/browser gates. Under exact approved Sandbox actions, present Checkout for the existing admitted job; owner completes test payment; correlate provider test event, verified signed webhook and application gate/state. Demonstrate negative/replay criteria from §3A. Retain sanitized event/state correlation and authoritative closure, not screenshots alone. End at owner acceptance. No booking/calendar writes, real charges, new fee/routing, refunds, Twilio Pay, SDK upgrade, deployment/merge/push or next-stage action is authorized by this proposal.

Completed now: inspected acceptance, current local result, authority and role readback; separated local gaps/live evidence/customer acceptance; recorded finite next design work and owners. Remaining: integration card and approved implementation, then current qualification, attended journey and acceptance. Rollback for this proposal: withdraw documentation; runtime remains unchanged/disabled. Accepted1A/1B/2A/2B4/8; R1 newly closed0/27;3A open. **No scope deviation.**

## Inspection provenance

Inspected at 2026-11-03T15:30:07.117329+00:00; backend 2972104745134d42062afdf259d9c9f34bc7833f; governance 7fcfc2729624acffeaa9e3e395de812ddd97b3a0. Existing backend AGENTS.md changes preserved.

- `evidence/APP-013/p08-native-entry-local-20261101/source/authority.py` SHA256 `763dd24f5dac70b3ec87d350ab2efc6d0fe110aae9f261708aba8c54e481e365`.
- `evidence/APP-013/p08-restoration-local-20261028/source/restore.py` SHA256 `a0bf4bc90cca0bd52935915d710ccb44e065dd3deed841a12ab49cb3ac4a1cb9`.
- `evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py` SHA256 `50994959a47400f651ee37ad4591cde486fbcf417d31b4eccecddf1564f7bf70`.
- `evidence/APP-013/p08-narrow-access-check-local-20261101/source/test_retired_role_postgres.py` SHA256 `819569f9e1b503e12c5684624f12630b7c9ace117e7ba5dceeb229fcc70fa579`.

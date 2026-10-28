# APP-013 / 3A / P08 — split diagnostic and key-lifecycle preparation proposal

Status: PROPOSED; owner decision pending. R1-W01 / APP-013 / 3A / P08. Backend source `ba2336d0587d332de8bf79cc75871872d874d6af`; governance source `3ea7eb4ca05c27b101b454b14ae061057b698399`. This is planning and local-preparation authority only if approved. No provider read/change, API enablement, key, IAM, account, database, authentication, runtime, Stripe action, spending allowance or attended window is included.

## Acceptance and demonstrated gap

The unchanged 3A finish is the authentic same-job Sandbox payment and matching signed settlement in `APP013_REMAINING_EXECUTION_CONTRACT.md`. This proposal corrects one operational prerequisite; it creates no new acceptance section, milestone or MVP feature.

Current evidence establishes the exact Signmons project binding and all nine requested caller-project lifecycle permissions. At 12:02 p.m. Eastern on October 28, `policytroubleshooter.googleapis.com` and `apikeys.googleapis.com` were both observed `DISABLED`; Service Usage, Resource Manager, IAM Credentials and Identity Toolkit were `ENABLED`. The later successful caller-permission probe did not reread those states or execute any requested method.

Source inspection found a sequencing defect in the disabled local access model. `access_readiness.py` lines 188–199 reads/enables only Policy Troubleshooter, while lines 200–210 immediately use API Keys GET/create/readback and lines 211–216 then run all five diagnostics. No API Keys state/readback/enable prerequisite exists. Because the API Keys API is currently observed disabled, the existing model cannot be bound to a live operation. Its 40 passing fake-provider tests prove the modeled state machine, not this missing real prerequisite. Evidence: backend `evidence/APP-013/p08-access-sequence-inspection-20261028/`.

The model also creates a key before four existing-resource permissions are known. The first four tuples—runtime `firebaseauth.users.get`, owner `firebaseauth.users.get`, owner `firebaseauth.users.update`, and owner `iam.serviceAccounts.signBlob`—do not depend on a new key. Only owner `apikeys.keys.getKeyString` on the exact future key does. Creating a key before resolving those four facts would add exposure and cleanup work without advancing a blocked design.

## Alternatives and recommendation

1. **Recommended: split the local controller into two disabled stages.** Stage A owns Policy Troubleshooter service readiness plus the four existing-resource diagnostics. Stage B owns API Keys readiness, exact temporary-key create/read/use-binding/delete and the fifth key-specific diagnostic. Stage B refuses unless Stage A has a current, exact, complete result accepted by the future operation. Both remain native-unbound after local tests. Future external actions receive separate exact approvals.
2. **Combined two-service operation.** Enable Policy Troubleshooter and API Keys, create/delete the key and run five diagnostics in one block. This is technically possible but increases mutation count and cleanup complexity before existing-resource access is known. It is not recommended.
3. **Owner-supplied compatible key/evidence or defer.** A separately designated compatible key and sufficient effective-access evidence could avoid one lifecycle, but existence and suitability are unknown and no discovery is authorized. Deferral keeps both services disabled.

This correction changes one approved local operational prerequisite, so owner approval is required before implementation. Impact is limited to the existing evidence-only helper and tests. No `src/`, UI, schema, migration, package, deployment or product interface changes. No role creation/grants, authentication rewrite, acceptance denominator or execution order change.

## Stage A — exact local diagnostics-only behavior

Prepare a fresh disabled controller/test pair by copying the source-locked local model into a new evidence directory. Preserve old evidence and hashes. The Stage A plan must pin:

- exact project `signmons`, project-number fingerprint contract and owner `debynyhan@signmons.com`;
- exact service `policytroubleshooter.googleapis.com`;
- retention decision value `RETAIN_IF_ENABLED`, modeled locally but never treated as external approval;
- exactly four existing-resource tuples listed above;
- one attempt/no retry, exact deadlines, signal handling, exclusive reservation, bounded output, memory-only bearer, no raw policy/error retention;
- result states `CAN_ACCESS`, `CANNOT_ACCESS`, `UNKNOWN_INFO`, `UNKNOWN_CONDITIONAL`, or `OVERALL_ACCESS_STATE_UNSPECIFIED`, with only four `CAN_ACCESS` values producing a Stage A candidate result;
- explicit refusal of all API Keys hosts, key IDs, key resources, key strings, create/delete/get/undelete operations, Firebase-user operations, signing, token exchange, database/runtime/Stripe actions and grants.

Stage A local tests must prove disabled/preexisting-enabled service branches; exact Service Usage GET/enable/LRO/readback; four exact Policy Troubleshooter requests; incomplete organization visibility/unknown states; unsupported resource or permission; malformed/null/extra output; enable submission/lost response/poll/readback failures; dependency or unexpected enable output; no automatic disable; no extra hosts; no raw policies/tokens; cutoff/read/cleanup deadlines; clock rollback; reservation race; SIGINT/SIGTERM at each modeled transition; closeout truth; and native unbound refusal before credentials.

The future external recommendation is to retain Policy Troubleshooter enabled after a successful Stage A operation. Google documents that Policy Intelligence features outside its listed premium cases have no additional charge, while enabling a service still associates it with the project and can enable billing for applicable use. Immediate disable is not the default because Google documents dependency and recent-usage safeguards; no force, dependency-disable or usage-bypass path is proposed. This is an explicit future owner decision, not authority in this proposal. Actual dependencies, organization-policy visibility and charges remain `UNKNOWN` until the separately approved operation reports them.

## Stage B — exact local key-lifecycle behavior

Stage B remains unimplemented in this proposal except for the minimum interface split needed to ensure Stage A cannot create a key. Preserve the existing key lifecycle source as disabled future work. Its next card must separately establish current API Keys state, enable/retention decision, exact key restriction security decision, create/get/delete/LRO permissions and current Stage A binding before implementation or action.

The future Stage B operation must not start merely because Stage A ran. It requires a fresh source/approval/window/allowance binding, current owned disabled test account/job/role, compatible `identitytoolkit.googleapis.com`-only restriction decision, collision refusal, exact resource/UID/etag ownership, memory-only key string, same-block authentication/revocation/runtime retirement and verified key deletion. API Keys is published as free of charge, but Identity Toolkit/other service use and project billing remain separately governed. No zero-cost guarantee.

## Finite checklist, evidence and finish

- [ ] Record exact owner decision against this immutable proposal before implementation.
- [ ] Create a fresh source-locked disabled copy; never edit or relabel the old 40-test result.
- [ ] Separate Stage A and Stage B request allowlists, plans, results and source hashes.
- [ ] Implement only Stage A plus the minimum Stage B refusal/interface boundary.
- [ ] Run all new positive/negative/concurrency/recovery/signal/deadline/privacy tests through exact serialized request/output contracts.
- [ ] Rerun unchanged applicable access-model, restoration and authentication local tests; report exact fresh counts and every initial failure.
- [ ] Prove no network/host credentials/provider calls in tests and native refusal before credentials.
- [ ] Run backend governance baseline, architecture and whitespace; governance frozen baseline, consistency, 25 safeguards and whitespace.
- [ ] Publish sanitized source, manifests, commands, logs, failures, results, teardown and limitations.

Observable finish: reviewable disabled Stage A source/tests with native refusal and a separately pinned Stage B refusal/interface; no live client, API enablement, permission verdict, key, authentication or payment readiness. If source reuse needs wider changes, tests expose another hidden prerequisite, or any provider request occurs, stop and report the exact blocker.

Dependencies/owners: Debynyhan Banks approves/refuses this local correction and later separately approves any provider configuration/read/action. Implementer owns source locks, exact contracts, tests and truthful evidence. Google owns provider output/dependency behavior. No attendance or password is needed for local work.

Exclusions: production/product code, database/schema, Firebase account/user action, runtime identity/secret/tag/role restoration, IAM/custom-role grants, service disable, force/bypass flags, key creation/value retrieval, signing/token exchange, Stripe/payment/event/customer action, deployment, merge/push, spending or scheduling.

Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **Explicit prerequisite-sequence correction proposed before implementation; no implemented scope deviation.**

References: [Policy Troubleshooter prerequisites](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access), [Policy Intelligence billing](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions), [enabled-service effects](https://docs.cloud.google.com/service-usage/docs/enabled-service), [enable/disable services](https://docs.cloud.google.com/service-usage/docs/enable-disable), [Service Usage disable contract](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable), [API Keys pricing](https://cloud.google.com/api-keys/pricing). Documentation establishes public contracts and published pricing, not current Signmons dependencies, visibility, charges or live readiness.

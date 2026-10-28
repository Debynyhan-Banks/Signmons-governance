# APP-013 / 3A / P08 — Stage A launch-binding completion proposal

Status: PROPOSED; owner decision pending. R1-W01 / APP-013 / 3A / P08. Backend source `2822820`; governance source `74e8309`. If approved, this authorizes bounded local implementation and isolated tests only. It does not authorize a Google request, service enablement, credential use, permission diagnosis, API Keys work, account/database/runtime action, payment, deployment, spending or an attended window.

## Acceptance criterion and demonstrated gap

The unchanged 3A acceptance criterion is one authentic same-job Stripe Sandbox payment request and matching signed settlement. The current prerequisite must first establish whether the existing owner and dedicated runtime identities have the four exact permissions needed by the already-tested authentication design.

Backend `2822820` proves the disabled Stage A state machine and serialized Service Usage/Policy Troubleshooter contracts with 24 new tests. It also deliberately has no credential resolver or native HTTPS transport and refuses with `P08_DIAGNOSTICS_STAGE_REFUSED_UNBOUND`. Therefore it cannot execute the separately approved provider operation yet. Treating the passing model as executable would violate shift-left verification and the repository rule that a helper or passing test is not a completed customer capability.

This is the smallest missing behavior. It does not create another acceptance section or product subsystem. Stage B/API Keys remains excluded and blocked.

## Alternatives and recommendation

1. **Recommended: add one disabled native Stage A launcher and fake-bound adapter tests.** Reuse the proven controller unchanged. Bind only existing owner identity/project checks, memory-only OAuth acquisition and the controller's exact Service Usage and Policy Troubleshooter requests. Keep launch disabled until a later immutable plan, source hash, exact approval and time bound are present.
2. **Use an ad hoc inline script during the external operation.** Rejected because its credential, timeout, output, interruption and request contracts would first be exercised against Google.
3. **Defer Stage A.** Safest for provider state but leaves P08 and 3A blocked.

Approval of Alternative 1 is recommended. Impact is one evidence-only launcher/test pair and source manifest. No `src/`, schema, migration, UI, package, deployment or product interface changes.

## Exact expected implementation

Create a fresh source-locked directory under backend `evidence/APP-013/`. Copy, do not rewrite, the Stage A controller from `p08-access-sequence-local-20261028`. Add only:

- a disabled launcher that verifies its source manifest, immutable operation-plan hash, owner `debynyhan@signmons.com`, exact project `signmons`, and the existing project-number fingerprint contract before requesting a bearer;
- one adapter for bounded existing-owner `gcloud` identity/project/token commands and HTTPS requests, with bearer held only in memory and cleared during closeout;
- exact host/method/path/body allowlists for Service Usage GET, conditional `:enable`, operation polling, enabled readback and the four Policy Troubleshooter POSTs already pinned by the controller;
- strict response size/schema/state parsing, fixed safe failure classifications, redirect refusal, request deadlines, clock rollback detection, SIGINT/SIGTERM handling, exclusive reservation and authoritative process closeout;
- a capability gate that refuses unless a future immutable external plan pins source hashes, attempt ID, decision ID, exact window, one attempt/no retry, service retention `RETAIN_IF_ENABLED`, and the owner's separate external-action approval;
- sanitized evidence output containing booleans, state classifications, counts, timestamps and hashes only. Never persist a bearer, raw policy, raw provider error body, project number, principal email beyond the already-governed identity label, or organization-policy details.

The launcher must not contain or call API Keys hosts, create/delete/get a key, retrieve a key string, access Firebase users, sign or exchange tokens, touch the database/runtime/Stripe, modify IAM, disable a service, use force/dependency-disable/bypass flags, or automatically retry.

## State, identity, retention and recovery boundaries

- **Identity:** only the existing signed-in owner is eligible to acquire the process-memory bearer. Exact owner/project/fingerprint mismatch stops before bearer or HTTPS.
- **State:** the future provider mutation is at most enabling `policytroubleshooter.googleapis.com` when an exact initial GET reports `DISABLED`. Preexisting `ENABLED` skips enable. Any other state or malformed output stops.
- **Retention:** future enablement is intentionally retained. The launcher must never disable the service during normal or interrupted cleanup. This persistent configuration decision requires explicit external approval later; local approval does not make it.
- **Unknown outcome:** a lost response after enable submission must stop as `ENABLE_OUTCOME_UNKNOWN`; it must not resubmit. A separately approved read-only reconciliation would be needed.
- **Closeout:** clear bearer and in-memory responses, terminate child processes, release reservation and write a sanitized final marker. Closeout may report containment of local credentials/processes but cannot claim provider rollback.

## Finite task checklist

- [ ] Record the owner decision against this immutable proposal.
- [ ] Pin controller, launcher, adapter, test and reused-source hashes.
- [ ] Implement only the disabled launcher and narrow adapter described above.
- [ ] Test exact owner/project/fingerprint checks before bearer acquisition.
- [ ] Test preenabled and conditional-enable/LRO/readback branches through fake CLI/HTTPS transports.
- [ ] Test the four exact diagnostic requests and all supported verdict states.
- [ ] Test malformed/oversized/null/extra/error/redirect responses and private error suppression.
- [ ] Test timeout, clock rollback, reservation race, child-process failure and SIGINT/SIGTERM at every modeled transition.
- [ ] Test lost enable submission response as unknown with zero resubmission.
- [ ] Test closeout bearer clearing/process termination/reservation release and truthful retained-service reporting.
- [ ] Test refusal of API Keys, Firebase, IAM mutation, signing, token exchange, database/runtime/Stripe and unbound native launch.
- [ ] Rerun the 24 Stage A controller tests and applicable 40 access-model, 31 restoration and 60 authentication tests without changing their sources.
- [ ] Run backend baseline, architecture and whitespace; governance frozen baseline, consistency, 25 safeguards and whitespace.
- [ ] Publish sanitized source, manifests, commands, initial failures, final results and limitations.

No real network, host credential/cache, OAuth token, Google provider, database or browser is permitted in local tests. Use fake subprocess and HTTP adapters; assert every serialized request and response contract.

## Dependencies, exclusions and observable finish

Debynyhan Banks owns approval/refusal of this local implementation and later separately owns the persistent service-enable/retention and external diagnostic action. The implementer owns source locks, request contracts, tests and truthful evidence. Google owns actual service dependencies, organization-policy visibility and provider results. Published pricing is not a zero-cost guarantee; no spending allowance is requested here.

Observable finish: reviewable disabled launcher/adapter source whose isolated tests prove the real execution interface and which still refuses without a future exact operation plan. It is **implemented and locally tested only**. It is not live-demonstrated, owner-accepted 3A evidence or payment readiness.

Rollback/disabled state: source is evidence-only and native execution remains capability-gated. Reverting the new commit removes the local launcher. No provider state exists to roll back from this work.

Exclusions: any external read/change; credential resolution during tests; service enable/disable; API Keys or key lifecycle; IAM/grants/custom roles; Firebase account/user action; signing/token exchange; database/runtime/Stripe/payment/customer action; deployment, merge/push, allowance or scheduling.

Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **Explicit execution-interface prerequisite proposed before implementation; no implemented scope deviation.**

## Approved local result

Debynyhan Banks replied “i approve” to the exact Alternative 1 request against governance commit `e758c79`. Backend commit `d19df960d22b53665485cbecc3a6a414067928e8` implements the disabled, source-locked launcher/adapter and sanitized evidence only. No external request, host credential/cache access, OAuth token, service enablement, API Keys action, database/account/runtime action, payment, deployment or spending occurred.

Final PASS: 16 launch-binding tests plus 24 unchanged Stage A, 40 unchanged access-model, 31 unchanged restoration and 60 unchanged authentication tests, 171 total. The first launch-binding run exposed one fake-provider tuple-indexing defect; the fake now matches principal/resource/permission without weakening controller behavior or assertions. Shift-left review then found and corrected interrupted CLI-child tracking with a direct termination regression test. Authentication scratch was deleted with absence verified.

Observable finish met: native execution refuses without a committed exact approval document/private plan; exact owner/project/fingerprint, memory-bearer, Service Usage/Policy Troubleshooter, deadline/unknown-outcome and process-closeout paths are fake-bound and tested. This is implemented/local-tested only. Exact external proposal `APP013_P08_STAGE_A_OPERATION_20261028.md` is separately pending owner approval. **No scope deviation within approved local work.**

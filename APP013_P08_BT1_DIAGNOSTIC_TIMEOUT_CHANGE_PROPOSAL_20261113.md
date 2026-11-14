# APP-013 / 3A / P08 — BT1 diagnostic socket-timeout proposal

PROPOSED, NOT APPROVED. Local implementation only; no external operation or schedule authorized. Source backend2491a9173f206620947d3961c9d1ff93ea048e9a. R41 and BD3 are consumed and independently closed. Existing credential/attendance windows do not authorize this change or a new live attempt.

## Demonstrated gap and source trace

R41 billing_project failed PROCESS_TIMEOUT after28013ms; BD3 independently reproduced28013ms after owner/project matched. No HTTP status or billing result was obtained. Source qualification_launch.py NativeIO.cli limits each process to30seconds; _owned_run reserves2seconds for cleanup and discards raw stderr on timeout. BillingDiagnosticIO classifies only a completed nonzero response. No assertion that billing is disabled or permissions denied is supported.

Installed SDK583.0.0 surface/billing/projects/describe.py Run calls api_lib/billing/billing_client.py ProjectsClient.Get; billing/utils.py GetClient requests cloudbilling/v1 without a timeout override. apis.py GetClientInstance passes None to apis_internal.py, which selects transport timeout unset. core/credentials/transports.py delegates to core/requests.py _CreateRawSession; core/transport.py GetDefaultTimeout returns core.http_timeout or300seconds. Generated cloudbilling_v1_client.py selects GET v1/projects/{projectsId}/billingInfo. Current governed config rejects extra core properties and ambient override variables. Thus the SDK default socket timeout exceeds the outer process lifetime. This is a diagnostic observability limitation, not proof of DNS, TLS, network, authentication, service latency or retry cause. SDK internal retry behavior may still exhaust the outer limit even with a shorter socket timeout.

## Alternatives and recommendation

Do not replay the full payment workflow or raise its outer timeout. Repeating unchanged BD3 adds little diagnostic value. A direct REST implementation would add a larger transport/credential boundary. Recommend a narrowly scoped diagnostic-only10second SDK socket timeout using child-local CLOUDSDK_CORE_HTTP_TIMEOUT=10 for the exact billing_project command only. No global gcloud config change, ambient override acceptance, normal qualification change or payment change.

## Complete local section card

Acceptance: exact BillingDiagnosticIO billing_project child receives the approved10second timeout; owner/project commands and normal QualificationIO retain existing environment; all existing30second outer/2second cleanup bounds remain. Existing exact authority must explicitly bind the new diagnostic behavior so old BD1/BD2/BD3 approvals cannot execute it. Source/SDK manifests must pin inspected timeout-resolution files. No silent rebaseline.

Reuse qualification_launch.py BillingDiagnosticCapability/BillingDiagnosticIO and existing SDK environment, error classifier, owned process runner and independent closeout. Expected files: qualification_launch.py, its existing focused tests/source/test manifests, existing manifest-refresh dependency inventory if required, BT1 local verification evidence. No unrelated runtime modules, packages or customer UI.

Data/identity: same exact owner/project/billing-account pins and three-command order; no extra token/cache reads, raw error/log storage, private data or identifiers. Retain only existing safe categories/booleans/counts/timing. Unexpected transport prose stays UNKNOWN unless an inspected exact format receives explicit bounded tests; do not infer status from arbitrary strings. No new classifier expansion is authorized by this proposal.

Finite checklist: inspect exact SDK property resolution and retry boundary; add diagnostic-only bound and authority binding; test through actual child environment selection; refresh current dependency manifests without touching historical receipts; verify unchanged normal path; required full affected suites and governance checks; record local proof and stop for separate external approval. Resolve any unanticipated material interface change before coding it.

Tests: positive exact billing diagnostic override; negative ambient overrides/wrong descriptor/old approval; normal qualifier and owner/project unaffected; fake transport verifies SDK resolves10seconds without network; process timeout, output overflow, interruption, concurrent/existing root refusal and independent closure remain covered by existing actual-boundary tests. No browser/SQL tests required for this environment-only diagnostic. Run affected qualification/native/connected/correction suites according to source manifest dependencies, baseline, architecture, frozen-baseline, docs-consistency,25governance tests and both git diff checks. Local tests are not external readiness.

End-to-end contribution: isolate the billing prerequisite blocking current3A connected payment qualification. Observable local finish is verified bounded behavior with no provider/credential calls. Subsequent live result could still be UNKNOWN; no promised successful payment or root-cause discovery.

Dependencies/owners: owner approves this explicit internal diagnostic expansion; implementer source/tests/cleanup/readiness; owner separately authorizes future diagnostic reads and SDK exception; billing/platform custodian owns any external remediation. Scope/acceptance denominator unchanged: accepted4/8,3A OPEN,R1newlyclosed0/27. Effort is one local diagnostic correction plus one separately reviewed qualification if warranted, not a new acceptance section.

Rollback/disabled state: no live action during implementation; existing normal workflow unchanged. Unapproved/new diagnostic refuses; preserve original code in git for reviewable rollback. Do not weaken checks or increase deadlines. Excludes billing/IAM/secrets changes, deployments, SDK installation, payment, sign-in, production/customer actions and spending.

Owner decision PENDING. Scope deviation proposed before implementation: a diagnostic-specific SDK timeout and exact-authority binding. No implementation performed.

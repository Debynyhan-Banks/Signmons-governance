# VM2 safe reason reporting — routine local correction

APP-013 / 3A / P08; existing VM2 section only. Local correction is within owner approval `874ce21` for the three VM2 files and the owner's current instruction to proceed. The original approved card requires safe allowlisted ErrorInfo reason/domain/equality reporting. This is not a new execution allowance or acceptance section. Independent scope/source review agrees that the existing approval covers this routine defect correction; SQ1 and its shared allowlists remain unchanged.

## Traceability and inspected gap

Baseline backend `2bfb60630ae0cd0180767696ac0face172706e3d`, runtime `1e21bb87a3640ef5f5ceb3f76fe569ca6ea4a612`; governance `5e2bfc0`. The section 3A criterion remains same-job Sandbox payment, matching authentic signed webhook, settled payment gate and owner acceptance. This correction advances safe diagnosis of one prerequisite preventing that connected workflow, not the payment capability itself.

VM2 R2 retained a valid HTTP 403 / PERMISSION_DENIED envelope, matching googleapis.com service/consumer flags and UNKNOWN reason; the raw response was discarded. Current BD7 independently observed billingEnabled true and completed cleanup. Neither result identifies the earlier denial's cause. Inspection of vm2_metadata_read.py:188 and sq1_signing_boundary.py:42,235 shows VM2 delegates reason projection to a signing-specific finite list. A synthetic BILLING_DISABLED ErrorInfo is replaced with UNKNOWN; recognized permission/service/scope reasons survive. Supplemental non-ErrorInfo details conservatively produce UNKNOWN rows. Do not claim BILLING_DISABLED was the actual historical reason or infer the two discarded detail types.

Google's documented ErrorReason enum defines fixed symbolic reasons for the googleapis.com domain, including BILLING_DISABLED and USER_PROJECT_DENIED: https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/error_reason.proto (reviewed November 24, 2026). The exact metadata GET contract requires secretmanager.versions.get and cloud-platform scope: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/get. These public documents are contracts, not current permission evidence.

## Exact implementation and boundaries

Only these already-approved backend files may change:

- evidence/APP-013/p08-connected-packet-20261110/vm2_metadata_read.py
- evidence/APP-013/p08-connected-packet-20261110/test_vm2_metadata_read.py
- evidence/APP-013/p08-connected-packet-20261110/vm2-source-manifest.json

Reuse strict_json, existing SQ1 non-2xx validation/projection and VM2's actual bounded request/orchestration/receipt interfaces. Locally recognize the fixed documented non-default Google ErrorReason labels only for the exact googleapis.com domain. Do not mutate SQ1 globals or shared code. Keep existing result fields and conservative conflict/UNKNOWN rules, including supplemental unknown details. Newly recognized conflicting reasons must collapse conservatively, not silently replace or misalign rows. Unknown strings/domains, messages, arbitrary metadata and supplemental payloads must never be retained. Successful metadata acceptance still requires exact name/state. No inference of resource existence, usable permissions, billing cause or authentication from a label alone.

The exact owner/project/resource pins, single metadata GET, no payload access, 2 CLI / 1 cache / 1 HTTPS ceilings, no retry, deadlines, source/config/authority guards, exclusive attempt custody, interruption handling, independent owned-process/response closure and purge are unchanged. All credential/provider seams are synthetic in local tests. Historical receipts and their digests remain immutable. No sign-in, credentials, provider action, payment, IAM/billing/secret change, deployment, support contact or spending is included.

## Finite checklist and readiness

1. DONE before coding: focused worktrees and owner AGENTS changes preserved; canonical pointer/board/handoff/ticket and remaining contract reconciled; baseline/complete consistency/backend wrapper passed November 24. Current external permission/state and credential horizon UNKNOWN.
2. Reproduce the finite reason loss through existing classifier and actual request seam with synthetic inputs; record baseline observation.
3. Correct only finite reason retention in VM2; do not broaden transport, confidence policy or shared sources.
4. Test documented labels and unrelated-domain refusal; supplementary details; conflicting old/new/new reasons; unknown and private strings; malformed envelopes; exact200 metadata and independent cleanup. Verify retained receipts exclude private sentinels. Reuse existing deadline/replay/interruption/concurrency cases.
5. Run pinned Python -I -B VM2 and SQ1 suites through their existing discovery interface, verify current manifests and no shared-source or historical-receipt changes. Reuse unchanged prior cache/qualification test evidence; do not portray it as newly executed.
6. Run backend architecture/governance wrapper, governance frozen-baseline/complete consistency/25 governance tests and both whitespace checks. Independent reviewer checks the actual diff and validation.
7. Record source commit, exact results, completed/remaining checklist, UNKNOWNs and next observable result before proposing any external action. No live packet or attendance request precedes local verification.

No browser tests apply: this diagnostic has no browser interface. Implementer owns source/test/manifest/readiness and independent reviewer owns review. Owner/cloud custodian retains any fresh exact external-read decision; expired VM2/BD7 allowances cannot be reused. Credential horizon, current secret state/access and whether Google will return a recognized reason remain UNKNOWN. A future bounded read could resolve current metadata state or a safe denial reason; it cannot reconstruct the historical response.

Rollback/disabled state: the diagnostic remains unavailable without separately committed matching live scope/decision; revert only this local correction if necessary, leaving immutable receipts and unrelated work untouched. Observable local finish is the tested source-pinned three-file correction and independent review, not a completed live diagnosis. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation.

## Completed local checklist

All seven local items completed at backend7dff026. Baseline actual synthetic HTTPError lost BILLING_DISABLED; corrected reporter retains documented reasons through HTTPError, run, immutable receipt and digest readback while excluding private values. 60VM2 tests (53existing+7new) and100SQ1 regressions passed; independent review also passed. Initial SQ1 run was blocked by the restricted local process/socket test environment (2failures/15errors); unchanged tests passed with the authorized local-test sandbox escalation. No test or shared source was weakened. APP013_P08_VM2_REASON_VALIDATION_20261124.json retains actual logs/hashes and review. Architecture/backend governance and25governance tests passed; final document/whitespace checks are recorded with the prepared read packet.

Current committed source/SDK/runtime/configuration and actual-clock preflight passed for fresh VM2R3. Only new external approval and reachability through9:03Eastern remain pending. Existing live attempts are consumed; no provider/cache action occurred during this correction. Current secret access/state and historical reason remain UNKNOWN. Observable next result and precise authority are in APP013_P08_VM2_R3_LIVE_PROPOSAL_20261124.md. No scope deviation.

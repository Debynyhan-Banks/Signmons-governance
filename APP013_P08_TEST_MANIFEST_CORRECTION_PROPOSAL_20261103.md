# APP-013 / 3A / P08 — renewal preparation stopped on evidence-manifest drift

## November 3 — owner approved manifest correction before implementation

Owner “i approve” authorizes APP013_P08_TEST_MANIFEST_CORRECTION_PROPOSAL_20261103.md at196485e: fix only test-manifest runtime link, add current/negative manifest regression checks in existing test module, update its file hash, validate and finish renewal proposal. Backend entryd6b729b; unchanged runtimece36c11. Proposal finite card, acceptance trace, tests, files, local-data boundaries, exclusions and rollback incorporated here. Baseline PASS before editing. No runtime/provider/credential action authorized.


Owner “proceed” authorized preparation of a fresh credential-renewal proposal. Backend08fab473a178a586f65377a5f078038d09845c70/governance882c94e56b4931de56c496d609e77533453d0019 entered with unrelated backend AGENTS.md modification preserved. No credential read, SDK invocation, provider action or new live window.

## Demonstrated preparation error

At November3 14:26:08 UTC, test-manifest.json runtimeManifestSha256 remains816b1c774f46bb515b20ad9beeeaa3e4d30332884b4750faa8f6a66083974715 (V3). Actual source-manifest.json hash is3db5e61e6ec460a8425819c6ea0272dda8cf63606230ee9dd1fb63e1fa31528b (approved V4). The earlier V4 update changed file hashes but omitted this cross-reference. Implementer owns the error. All21 sdkReviewFiles hashes and test_access_check.py hash match; gcloud executable hash8628b9f971d07c5e52fd2c6d469ee4a0940c75eb51820d628c3dd068981bd260 matches. Runtime committed source remains unchanged.

Existing tests contain no reference to test-manifest/runtimeManifestSha256; --check-source validates runtime/SDK sources, not this test-manifest link. Thus99 passing tests and source checks did not establish complete manifest consistency. Earlier complete-manifest verification wording was too broad. Actual credential stop CACHED_TOKEN_EXPIRED and independent cleanup remain unchanged evidence; no provider-access result is invalidated or invented. No silent hash rebaseline performed.

Repository AGENTS.md says: “If unintended drift is found, stop, disclose it and seek direction; do not retrospectively claim no deviation.” Renewal readiness is therefore STOPPED pending the narrow correction below.

## Concrete correction requested before implementation

Approve only (1) correct runtimeManifestSha256 in existing source/test-manifest.json to the current approved V4 manifest hash, (2) add a regression assertion in existing source/test_access_check.py that validates this link and its test-file byte hash, rejects mismatches, and checks the recorded SDK review hashes, then update that test-file hash in the same manifest, (3) run full focused tests, actual source, architecture, frozen/cross-repository/docs checks,25 governance safeguards and whitespace; record current evidence and resume renewal proposal preparation. No runtime adapter, dependency, acceptance criterion, provider path or production behavior changes. No new module or subsystem.

Acceptance trace: R1-W01/APP-013/3A/P08 remains the same admitted-job Sandbox payment journey. The existing credential qualification seam requires internally consistent source evidence; this correction repairs that evidence only and adds no accepted milestone. Sourcebasece36c1195acf31726e560e97b2c05432d19e79d1. Reuse existing test module/manifests. Inputs are local public source bytes only, no credential/customer data/retention changes. Positive current-link/file-hash/SDK validation; negative altered link/file hash; no concurrency/browser/database gate applies to this metadata-only proof. Rollback these two files only to08fab47 if rejected; keep immutable receipts. Observable finish: exact consistent manifests plus passing test, then concrete renewal packet. Owner approves correction; implementer fixes/proves; credential custodian later decides renewal.

## Recovered renewal boundary, not yet decision-ready

Reuse the prior consumed APP013_P08_CREDENTIAL_RENEWAL_DECISION_20261103.md procedure with fresh reservation/window only after correction: one /opt/homebrew/bin/gcloud auth print-access-token debynyhan@signmons.com --quiet --verbosity=none invocation,60-second bound, stdin/stdout/stderr null, output-control child environment after strict actual config guard; owned process closure; one existing-cache validity postcheck on clean exit. SDK internal authentication retries and normal credential/cache metadata maintenance require an explicit fresh exception; one invocation does not mean one HTTP attempt. No forced refresh/login/browser/alternate credentials/scopes, resource probes, key/IAM/API/billing actions or spending. Old renewal and token qualification are consumed. No current credential state read during this preparation. Fresh exact timing/validity deadline and owner approval remain unset; do not reuse the blocked14:25 packet.

Completed: recovered prior procedure and immutable stop/cleanup; actual source/executable/21 SDK/test-file checks; identified precise missed manifest link. Remaining: owner correction decision, implementer correction/proof then final renewal proposal, separate credential-renewal authorization. Key absence and full P08 UNKNOWN. Accepted4/8, R1 newly closed0/27, 3A open. **Unintended evidence-manifest drift disclosed; explicit narrow correction proposed before implementation.**

COMPLETED under owner approval: backend5be6d5772394062395f735e23c7ae32423180d14,101 focused cases PASS; runtime unchanged. See backend MANIFEST_CORRECTION_RESULT_20261103.json.

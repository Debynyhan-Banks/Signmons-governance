# APP-013 / 3A — RB1 local identity-readback diagnostics proposal

Status: PREPARED FOR OWNER REVIEW; NOT APPROVED OR IMPLEMENTED. Local code and tests only. No Terminal attendance or deadline is required.

## Approved section and demonstrated gap

3A remains the existing Sandbox payment on the admitted job section. Its unchanged finite-work criterion is: “map admitted job/current policy to existing request → expose existing Checkout link → consume authentic matching Sandbox event → demonstrate payment gate and failure recovery. Patch only gaps found in this sequence; no replacement payment stack.” Accepted 1A/1B/2A/2B remain 4/8; R1 newly closed remains 0/27.

R48 ran source `45c4da2c4a87ff9c90147ec0a0dd5a3884d4376a` under native approval `e28a72fe1ae74e2be32806a44ed18d5cee6079a7`. It stopped at `RUNTIME_READBACK` before authentication/payment. The exact discarded response remains UNKNOWN. Independent cleanup succeeded; safe receipts are retained at backend `5f55cbc07ebd70bdaf9618b5f79d26731040cf52` and `APP013_P08_R48_CLOSEOUT_20261114.json`. This proposal does not clear original R47 uncertainty.

Inspected source: current `RuntimeAdapter.readback` in `p08-native-entry-local-20261101/source/entry.py:99`; immutable `p08-restoration-local-20261028/source/restore.py:229–231`; immutable `p08-live-binder-local-20261029/source/coordinator.py:153–159`. The single describe response becomes a boolean, then every false result becomes the generic `RUNTIME_READBACK`. Existing native tests around the identity mutation/readback seam and installed SDK projection checks do not preserve the distinct mismatch through the assembled parent. The demonstrated gap is loss of diagnostic information, not a proven provider activation defect.

## Alternatives and proposed decision

Another full connected attempt would repeat this information gap. A present-state metadata read after cleanup cannot reconstruct the historical post-enable response. No deterministic parser defect was reproduced locally. Proposed RB1 therefore records fixed, safe failure categories using the existing single readback and journal error path. It creates no new diagnostic runner or acceptance section. Owner approval is requested before this prerequisite implementation; preparation is not authority.

## Exact local scope and boundaries

Source baseline: backend `5f55cbc07ebd70bdaf9618b5f79d26731040cf52`; runtime files are unchanged from R48 source45c4da2. Reuse `RuntimeAdapter`, actual `NativeIO.cloud`, installed SDK projection, coordinator failure/cleanup path, existing native/connected tests and current source validators.

Expected implementation files, relative to backend `evidence/APP-013/`:

- `p08-native-entry-local-20261101/source/entry.py`
- `p08-native-entry-local-20261101/source/test_entry.py`
- Derived current hashes only in native `source-manifest.json` and `test-manifest.json`, qualification `p08-https-output-category-local-20261029/source/source-manifest.json`, and correction `p08-key-correction-20261110/source-manifest.json` where their existing dependency maps require it.
- Local test/evidence records and governance readiness/completion handoff for RB1.

Use the same source-pinned identity describe vector once. Classify currently rejected responses into fixed local codes for missing/mismatched identity, malformed response/disabled field, or unexpected disabled state. Preserve the exact existing success predicate, including omitted-field default and existing equality behavior (explicit tests for booleans and numeric0/1). No policy tightening, relaxation, replacement expected identity, second describe, enable retry, polling, or deadline change. Preserve all non-identity branches. Propagate only fixed locally generated errors through the existing coordinator path; arbitrary exception/provider text remains suppressed. Any necessary allowlist update must remain finite and test the actual boundary.

No new journal fields, raw response retention, credential/identifier logging, private files, schema or data-contract changes. Request/state/operation identity, retained receipt custody, original purge deadlines, independent cleanup/readback, conditional ownership and no-retry budgets remain unchanged. Historical sources, old manifests/receipts and R48 decisions are immutable. No authentication, payment, webhook, database, cloud configuration, resource enable/disable, credential-cache read, sign-in, browser action, deployment or spending is authorized by RB1.

## Finite checklist and observable finish

1. Reproduce the generic-code information loss through the real current adapter/coordinator seam using synthetic provider responses.
2. Add only the safe classifications above while proving accepted inputs and call vectors/counts unchanged.
3. Test true/false/omitted/null/numeric0/1/malformed/wrong identity, failed command and arbitrary error text using installed SDK projection and actual `NativeIO.cloud` with synthetic subprocess output.
4. Carry each failure through the assembled coordinator: stop before IAM/key/auth/payment activation; preserve write-ahead attempts, main cleanup, independent cleanup, interruption, concurrent reservation rejection and cleanup disagreement. No duplicate enable or added describe. Verify original R48 receipts byte-identical.
5. Run native and connected regression, dependent manifest/source validators, backend lint/build/architecture and required governance/whitespace checks. Qualification/correction suites validate their changed derived bindings. No live or browser test is required for this local error-classification-only change; browser behavior stays unreachable in the failure cases.
6. Publish source/evidence hashes, precise counts, independent review, remaining UNKNOWNs and disabled/live authority state. Observable completion is distinct safe failure codes with unchanged workflow/cleanup behavior; it is not live activation or payment success.

From the backend checkout, use the pinned Python from R48 and `-B -m unittest discover -s <directory> -p 'test_*.py'` for the native source, connected packet, qualification source and key-correction directories above. Use existing manifest validators, `npm run lint`, `npm run build`, `npm run arch:check`, `SIGNMONS_GOVERNANCE_REPO=<governance> node scripts/check-governance-baseline.mjs` and `git diff --check`. From governance run `node scripts/frozen-baseline-check.mjs`, `SIGNMONS_BACKEND_REPO=<backend> node scripts/docs-consistency-check.mjs`, the three required governance test files and `git diff --check` before/after governed edits. Do not count prior AC1 tests as newly run RB1 evidence.

## Readiness, responsibility and rollback

Readiness inspected November14,2026: source and R48 receipts demonstrate the local information-loss seam; installed SDK projection with synthetic true/false/omitted/null did not reproduce a deterministic provider bug. Actual live response/state mismatch remains UNKNOWN. Current configuration/pins and independent cleanup/process/private-purge proof are in the R48 closeout. This is LOCAL-IMPLEMENTATION-ONLY readiness, not external qualification or execution readiness.

Implementer owns bounded code, actual-boundary tests, source/manifest consistency and independent review. Owner decides RB1; credential/cloud custodians retain all external authority. No attendance or credential input is required for local work. Any later live diagnostic must be separately prepared with exact resources, usable access, source, deadlines, limits and independent cleanup; no future operation is preauthorized here.

Rollback is to leave this proposal unimplemented or revert only the eventual RB1 local patch through normal governed review. No consumed operation is replayable. Existing disabled state and historical uncertainty remain. Effort is one adapter/test change plus derived bindings and verification; no acceptance denominator, dependency order or payment-stack change. If a broader behavior change becomes necessary, stop and propose it before implementation.

No scope deviation implemented. This bounded local diagnostic change is proposed before implementation.

Independent local source/proposal review: PASS; exact legacy success predicate, single describe, actual coordinator tests, finite safe codes and current-only files are consistent. This review does not approve implementation or external action.

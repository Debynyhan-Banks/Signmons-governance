# APP-013 / 3A / P08 — cache error translation proposal

## November 9 — approved cache-error translation complete locally

Owner approveddd9d7fa before coding. QualificationIO now translates cache helper CACHED_TOKEN_EXPIRED/CONFIG_CHANGED to model.Stop and other helper exceptions to CACHE_UNCONFIRMED;TOKEN_CACHE_MISMATCH remains distinct. Expiry strictly after purgeEnd,no-retry/request/identity/config/retention/cleanup boundaries unchanged. Actual transport/cache-to-full-result regression covers syntheticSQLite success/insufficient lifetime/sidecar plus injected config/busy/schema/missing/timeout/unexpected errors,one cache call,reservation,no later work,normal/independent cleanup and secret canary absence. Backend P08_CACHE_ERROR_TRANSLATION_20261109.md records pre-code card and validation.

Full173runtime/local PASS in82.194s plus25governance=198PASS;ownedTLS server reaped/scratch absent,providerCalls0. Baseline/consistency/architecture/whitespace PASS. All local checklist items complete. No live packet/window/action;Q7cause remains UNKNOWN,Q7/R15 consumed/purged. Next implementer if requested: reconcile source-bound qualification prerequisites and prepare smallest exact operation;owner/credential/DB roles separately approve live scope. Full qualification/Sandbox/negative/replay/owner acceptance remain;3A OPEN,accepted4/8,R1newlyclosed0/27. No scope deviation.

PENDING_OWNER_IMPLEMENTATION_APPROVAL. Review only, no code/provider/cache read. Source0625fbb6608704d408274baaa3c625434db841f2; Q7 evidenceda740f5/closeoutbc6d20c. Q7/R15 consumed and purged.

## Demonstrated gap

QualificationIO.cli reserves cache after observed token CLI, then calls acl.read_cached_token within acl.http_deadline. The helper raises its own acl.Stop for expired/missing/busy/schema/sidecar/config/timeout failures. The full qualifier catches model.Stop only and otherwise records CURRENT_READ_UNCONFIRMED. Therefore specific helper errors are lost. ProjectPermissionIO.cached_token already translates allowlisted CACHED_TOKEN_EXPIRED/CONFIG_CHANGED to model.Stop and other errors to CACHE_UNCONFIRMED. Q7's26returnedCLI/1cache/0HTTPS fits this boundary, but does not prove which underlying exception occurred. No assertion that the token was expired or that cache contents changed.

Expiry must remain strictly after full qualification purgeEnd; P2 tests closeoutEnd for its distinct shorter operation. CACHED_TOKEN_EXPIRED means insufficient lifetime for that required horizon, not necessarily already expired at read time. Do not shorten deadlines or renew credentials to bypass it.

## Exact local proposal and section card

Acceptance: translate cache-helper exceptions at the existing full QualificationIO boundary using the same fixed two-code allowlist as ProjectPermissionIO; all other helper exceptions become CACHE_UNCONFIRMED. Preserve TOKEN_CACHE_MISMATCH model.Stop, reservations,timeout,one-read behavior and all cleanup. No arbitrary exception text/cached token/expiry/raw row persisted. No new diagnostic command,receipt format,provider action or retry.

Expected files: qualification_launch.py,test_qualification_launch.py,source-manifest.json,evidence/handoffs. Reuse existing bounded cache helper, owned subprocess/SQLite fixtures and actual QualificationIO-to-full-result seam; do not edit locked dependency. This improves truthful qualification failure reporting for the same-job Sandbox workflow,not customer acceptance. No new subsystem or acceptance criterion.

Finite checklist after approval: implement narrow translation; test expired-before-horizon but not-yet-expired token,config error,sidecar/schema/busy/missing/timeout generic classification,unexpected exception secret canary,token mismatch and success; verify actual full-result label,no subsequent HTTPS/SDK work after failure,one reservation,normal/independent closeout and no private output. Reuse actual synthetic SQLite boundary where possible. Run full three-module local regression suite,25governance tests,frozen-baseline/complete consistency,architecture and whitespace. Preserve source/identity/config pins,15second/cache and64KiB caps,expiry horizon,one-attempt/concurrency/interruption/recovery boundaries. No browser interface change;full Sandbox browser acceptance remains downstream.

Readiness: source and existing diagnostic translation inspected November9; local implementation/testing NOT YET DONE. Real cache condition and Q7 cause UNKNOWN. Implementer owns correction/tests;owner approves local scope and separately any later external work. Existing172local+25governance results predate correction and cannot verify it. Rollback only correction source/tests/hashes,preserve immutable receipts and unrelated AGENTS.md. New source cannot reuse consumed authority. Observable finish is safe specific full-result classification with all regressions passing. Alternative: defer;blind retry would retain the same evidence gap.

No live packet,credential refresh,expiry relaxation,cache reread,log recovery or additional retention authorized. Remaining full qualification and same-job Sandbox/negative/replay/owner acceptance;3A OPEN,accepted1A/1B/2A/2B4/8,R1newlyclosed0/27. No scope deviation implemented;bounded reporting correction proposed before coding.

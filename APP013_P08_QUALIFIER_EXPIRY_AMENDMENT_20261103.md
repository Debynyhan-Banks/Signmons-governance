# P08 qualification binding: credential-expiry contract amendment

## November 3 — approved external qualification binding locally verified

R1-W01/APP-013/3A/P08. Owner approved original card4c8011e and expiry amendmentdc90069 before implementation. Backend7413bfa completes checklist1–6 locally: distinct committed read-only authority; exact source/scope/resource/window/SDK allowance; attempt reservation before hidden credentials;27CLI/20directHTTPS/4remoteSQL plus1cache inspection (2fixed SQLite SELECTs); cached token match/expiry; process-local SDK log/prompt controls; separate cleanup-only dispatch/fresh SQL factory and conservative interrupted recovery. Legacy native entry remains refused, proof API cannot select an external transport, and qualification cannot launch runtime/payment. Prior withdrawn draft remains disclosed, not rewritten.

PASS56 producer/transport/authority/cache,17 composed model,7 owned PostgreSQL/TLS,21 native entry,111 narrow regression and25 governance:237 total. Actual disposable Git, synthetic SQLite, installed SDK log/prompt method bodies and owned SQL/TLS boundaries exercised. Owned server reaped, scratch absent, scoped sessions/owned children absent. Initial manifest/path/test-discovery/resource-warning and sandbox-bootstrap failures are recorded in EXTERNAL_BINDING_RESULT_20261103.md, corrected without weakening checks. Frozen baseline, cross-repository/docs consistency, architecture and whitespace PASS. Unrelated AGENTS.md preserved; no application/browser/build claim for this isolated binding.

Implemented/local-tested only; providerCalls0/liveObserved=false/executionReady=false. Actual credential/configuration compatibility, provider/DB/job/rights/billing and external cleanup facts remain UNKNOWN. SDK source review is bounded; its internal requests are not counted as27, and any refresh/cache/internal retries still require the exact future exception. No live decision/window/private input/credential access/provider request, renewal/login, deployment or payment. Next implementer: prepare qualification-only packet against7413bfa with exact source/pins, explicit SDK/cache allowances and fresh work/cleanup/purge times; owner/credential/DB roles approve that exact external action. Then existing same-job Sandbox journey, negative/replay evidence and owner acceptance. Accepted1A/1B/2A/2B4/8;R1 newly closed0/27;3A open. **No scope deviation beyond the explicitly approved expiry amendment.**

Owner “proceed” approved amendmentdc90069 before this implementation, together with original binding card4c8011e. Local implementation and synthetic tests only; no live operation.

R1-W01 / APP-013 / 3A / P08. Owner “proceed” approved local binding card4c8011e. This record reports an implementation-preparation gap, not completion or live authority. Backend remains8b479ba9a26e797b64f63b0f3715811c3c2ebbd4; unrelated AGENTS.md preserved.

## Demonstrated gap

Filesystem-only inspection of installed SDK583.0.0 establishes that surface/auth/print_access_token.py returns FakeCredentials(token), whose sole field is token. Its Run calls LoadCredentialsWithScopes without min_expiry. That helper defaults min_expiry=None and loads credentials through store.Load; refresh/cache behavior can occur. Current NativeIO converts stdout only to {accessToken}; its parser cannot establish survival through purgeEnd. A successful token print is not expiry evidence. No SDK command, configuration/credential file, password or provider was accessed in this inspection.

The approved card required a credential-lifetime policy but enumerated only27 CLI/20 direct HTTPS/4 remote SQL reads. It omitted a concrete expiry observation and allowance. Existing access_check.read_cached_token already verifies exact owner/config, safe SQLite schema/no sidecars, unchanged file, token restriction absence and expiry strictly after purgeEnd. Reusing it after SDK token output would add one local cache inspection (internally two allowlisted SQLite SELECTs: schema and exact owner row), compared in memory to the printed token. This is additional credential access and must be explicit, not hidden in the old descriptor count.

SDK log.AddLogsDir calls _CleanUpLogs BEFORE checking disable_file_logging. Thus disable_file_logging alone does not prevent deletion of ambient historical SDK logs. _GetMaxLogDays reads core.max_log_days; _CleanUpLogs is skipped when zero. These are source observations, not proof of a tested launcher environment. SDK API-error handling also has an API-enablement prompt; qualification must force noninteractive refusal, never authorize enablement. The inspected helper's enable_by_default is False. Internal retry/refresh behavior still requires complete source-path review and a separately approved exact external exception.

## Smallest proposed amendment

Amend only this card's local implementation contract:

1. Preserve27 CLI/20 direct HTTPS/4 remote PostgreSQL reads; add maximum1 exact-owner local cache inspection after the single token invocation, through the existing pinned access_check.read_cached_token. It contains2 fixed read-only SQLite queries, no refresh/write and no fallback. Require exact in-memory token equality and expiry after purgeEnd. Reserve the allowance before reading; failure stops work and still closes owned resources. No raw token/expiry/cache row in retained receipts. The later live decision must explicitly authorize this credential-store access; this amendment would authorize synthetic-cache tests only.
2. Before spawning SDK children, reject ambient overrides using existing validators, then use fixed process-local settings for disable_file_logging=true, max_log_days=0, disable_usage_reporting=true and disable_prompts=true. No persistent SDK configuration change. Verify these settings through the installed SDK source and boundary tests, including no prompt-driven API enablement or log deletion. Preserve the exact CLI descriptor set. If these controls cannot be proved through the actual boundary, remain disabled.
3. Complete the originally approved distinct authority, hidden password, independent-closeout dispatch and existing six checklist items against this explicit amended contract. Reuse existing files/modules; no cached-only replacement transport or new subsystem. Add synthetic SQLite expiry/mismatch/busy/sidecar/foreign-owner tests through the actual helper and assert no credential access before approval/attempt reservation.

Alternative: defer the external binding and retain the verified proof-only producer. Dropping expiry validation is not proposed. This adds one bounded local credential-read prerequisite and tests; acceptance IDs, walkthrough counts, remote request budgets and downstream payment criteria do not change. No live operation, window, SDK refresh or credential-store access is approved by a local implementation decision.

## Work status and deviation disclosure

Completed: approval recovery, baseline checks, actual installed SDK output/refresh/log-source inspection, exact missing observation and reuse path identified. During this turn, an unfinished existing-file binding draft introduced the additional cache allowance before its explicit amendment was recorded. It was withdrawn in full; qualification_launch.py matches the previously verified SHA2564e5921310578612f653ae1fd134d16b5a88252732be6eeeadb262680c25b8bee. No draft was executed, tested, committed or externally invoked. No runtime change remains. This is disclosed preparation drift; do not label this turn “No scope deviation.”

Remaining: owner decision on this exact amendment, then implementer completes the approved binding/test checklist. Installed SDK review is partial; no claim of complete executable/SDK provenance or tested environment. Live identity, permissions, token lifetime, billing, provider/DB/job state and cleanup remain UNKNOWN. Next observable result is the locally tested binding with the explicit additional cache budget; qualification and Sandbox journey remain separate later gates. Accepted1A/1B/2A/2B4/8;R1 newly closed0/27;3A open. No milestone accepted.

## Source evidence

Inspected at 2026-11-03T16:49:07.469235+00:00 by reading source files only. Hashes identify inspected bytes, not a complete SDK review:

- `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk/lib/surface/auth/print_access_token.py` SHA256 `9cbe0e02400cc72bfe14aa75638f831b44585e7e9b957b53725ae094107b3cf4`.
- `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk/lib/googlecloudsdk/command_lib/auth/auth_util.py` SHA256 `f9991b16c3207c4765f3cac9bd4dfbccb743820e793f53b68bc14fe74cbf7418`.
- `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk/lib/googlecloudsdk/core/credentials/store.py` SHA256 `1fcb3b856eb1584491d6f6160983808ca1f3574e44de86f53ac8d86f882e2a6f`.
- `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk/lib/googlecloudsdk/core/log.py` SHA256 `b503b94fbc53943de0ec4a7ca93bc02fa764d35553f658a92e93a38fd4427b3e`.
- `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk/lib/googlecloudsdk/api_lib/util/apis.py` SHA256 `0110f091c7c86a18ce4e917c66cb0134c6a62a3cfc44c868bb6606c971f055fa`.
- `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk/lib/googlecloudsdk/api_lib/util/api_enablement.py` SHA256 `771dd7387c07e5bb52a30e242207f52048bb0ddc06e72ec377d5d79ff0b7add2`.

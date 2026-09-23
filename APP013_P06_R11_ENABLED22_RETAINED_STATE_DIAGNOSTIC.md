# APP-013/P06 R11 enabled22 consolidated retained-state diagnostic

Status: original operation stopped during local preflight before external action; preserved and blocked from reuse. Replacement explicitly approved and installed; owner execution pending within the unchanged window.

Plan: `790763ef-1f2a-44b7-a690-56bfee9fba9a`. Approved execution window: September 23, 2026, **8:30–9:15 AM Eastern** (`12:30Z`–`13:15Z`). One attempt, no automatic retry.

## Why this read is needed

Enabled22 produced one `CURRENT_VERIFICATION_UNAVAILABLE` submit marker at `2026-09-23T11:50:24.943550Z`. Six local checks found no defect in direct successful code verification, encrypted-ledger service reconstruction, or the existing fail-closed policy/revocation/expiry rules. The marker covers several predicates. It does not prove an address failure, expired phone proof or no job. Reading all correlated retained state in one operation avoids another paid browser run and sequential partial diagnostic approvals.

## Exact proposed operation

1. Install the prepared private helper, hidden-input wrapper, hashes, plan and exact owner authorization under `/Volumes/Signmons-P06/r11-retained-state-diagnostic-20260923-0830`. Local preparation files are in `/private/tmp/r11-enabled22-forensics`; no authorization or attempt exists there. The prepared source imports existing tested cipher/proof validators; it changes no application code.
2. Owner enters the existing `neondb_owner` password once at a hidden prompt. It passes through the existing READY/anonymous-pipe handoff, never argv, files, output or chat. Reserve an exclusive no-retry attempt before any external read. Verify the window again after input.
3. Perform one read-only metadata read of project `signmons`, region `us-east5`, revision `signmons-calldesk-staging-app013p06enabled22`. Require its image to equal `sha256:53f82468d86c49d1ddd1024e9550de27bc0ac49f6841b958f5bc393e10f9f4b9` and `CONVERSATION_DATA_ENCRYPTION_KEY` to reference only `signmons-staging-conversation-data-key`, numeric version `2`. Raw metadata remains in process memory.
4. Open exactly one TLS owner-operated PostgreSQL connection to the existing fixed P06 child. Require exact database/user identity and PostgreSQL 18. Set default read-only mode, bounded query/lock timeouts, then begin repeatable-read READ ONLY. No locks for update, mutations or runtime-role changes.
5. Resolve exactly one `conversation.controlled_phone_held` audit for the fixed tenant and enabled22 packet `196a69b1-51a2-46b9-992b-5f307daf2111`. Use that hold's conversation/session/digest only in memory; do not enumerate other conversations. Read that conversation's lifecycle and encrypted `verificationOperations`, at most 30 allowlisted observation/revocation/lifecycle audit records since 11:40Z, exact request `8bc6af03-6a0f-453d-a985-4cb4c540f1c3` job count and its address-operation stage/deadline. Fail on ambiguous scope or row limits; rollback and close the database before secret access.
6. Only if that exact encrypted ledger exists, read **one existing Secret Manager version**: `projects/signmons/secrets/signmons-staging-conversation-data-key/versions/2`. This is new explicit read-access authority, not key creation/change or IAM authority. No other secret is permitted. If access fails, stop; do not grant access or retry. Decrypt only this ledger in the short-lived process with the existing AES-GCM cipher. Never save or display the key, ciphertext or decrypted ledger. Clear mutable key buffers; process exit disposes of remaining references, without claiming guaranteed zeroization of JavaScript strings.
7. Compare retained START/CHECK linkage, provider-reference equality, digest/scope binding, policy and proof timestamps against the pinned packet and refusal time (floored to millisecond precision). Report missing/revoked/mismatched/current proof as retained evidence, not a recreated live authorization. Relevant later observations, revocations, purge or missing data must remain historically inconclusive.
8. Save only counts, fixed stage enums, pass/fail booleans and minimal timestamps. No phone, code, address, token, plaintext, ciphertext, provider IDs/content, tenant/session/conversation ID, HMAC, key, exception text or stack in results. The owner reports one fixed completion line; Codex reads the sanitized result locally.

## Tests and limits

Prepared helper syntax, exact source/file hashes and no-action review pass. Eight synthetic analyzer tests pass: valid proof without implying a job, approved receipt missing proof, missing check/ledger, scope/expiry failure, policy failure, provider-reference mismatch, post-event change ambiguity and output privacy. Existing local investigation independently passed six compiled-service checks. No live connection, revision/secret read, provider or browser action was made during preparation.

This is historical reconstruction. It cannot recover purged data or transient state, authenticate a lost browser token, prove a missing final draft's contents, or guarantee identification of the exact historical predicate. Even a passing retained phone proof does not authorize admission or a new test. A surviving address row distinguishes post-address failure from an initial proof gate; results may still be inconclusive. Do not weaken a production check or propose another run merely because this diagnostic completes.

## Exclusions and finish

No LOGIN change, activation, deployment, traffic change, verification code, provider request/mutation, browser/customer action, database write/job creation, request retry, hold release, ceiling increase, key/secret change, IAM change or billing change. Existing runtime remains closed. No additional Cloud Logging query. No automatic retry.

Observable finish is a sanitized correlated retained-state result or a stage-specific stop. P06 remains 12/14; R11/full R12 and accepted 1A/1B/2A unchanged. Implementer owns analysis; owner approval gates the exact new database and secret reads. No scope deviation implemented; the new read-access boundary is proposed explicitly before external action.

## Approval and installation recorded

Approve plan `790763ef-1f2a-44b7-a690-56bfee9fba9a` for private helper/authorization installation and the one consolidated read-only operation above during 8:30–9:15 AM Eastern, including the single exact revision metadata read, one hidden-input PostgreSQL 18 connection with rollback, and conditional one-version encryption-key read solely for in-memory analysis. No live journey or automatic retry.

Owner response: “i approve proceed”, approving this exact reviewed plan and window. Installed six files (helper, analyzer, hidden-input wrapper, plan, binding and authorization) with source/file hashes verified, directory 0700 and files 0600. Authorization binds the exact plan SHA-256. Installed `--review` returned `R11_RETAINED_STATE_PREPARED_NO_ACTION`. No attempt/result/stop file or external operation exists at installation. Owner execution is next, never before 8:30 AM; do not rerun a stopped operation. No scope deviation.

## Early stop and exact replacement decision

The owner reported an early start. Readback at 08:24 EDT found `stop.json` with `UNCONFIRMED` / `LOCAL_REVIEW` / no automatic retry, no `attempt.json` and no `result.json`. The helper checks the window before READY and external actions; this record establishes no password handoff or external operation. It does not independently distinguish the time check from every other local assertion. Original files and stop record are preserved; do not rerun the original command.

Replacement plan `0969cc65-f1ea-4800-88ed-3542ddad16c1` is prepared in `/private/tmp/r11-enabled22-forensics-replacement` for installation at `/Volumes/Signmons-P06/r11-retained-state-diagnostic-20260923-0830b`. Same approved diagnostic scope and September 23, 8:30–9:15 AM Eastern window; only unique plan ID, installation path, wrapper path and hashes change. No authorization, installation or execution of the replacement has occurred. No new browser run, runtime change, provider request, retry of the stopped ID, or expansion of secret/database access is proposed.

Requested decision: approve replacement `0969cc65-f1ea-4800-88ed-3542ddad16c1` for private installation and one owner-operated diagnostic during 8:30–9:15 AM Eastern, retaining all exact read-only database/revision/conditional-secret boundaries above and no automatic retry. Fresh approval is needed because the prior command is permanently blocked by its saved stop and the owner required no retry. No scope deviation.

## Replacement approval and installation

Owner replied “i approve” to the exact replacement ID/window confirmation. Replacement `0969cc65-f1ea-4800-88ed-3542ddad16c1` is installed at `/Volumes/Signmons-P06/r11-retained-state-diagnostic-20260923-0830b` with six verified files, 0700 directory/0600 files, exact plan-hash authorization and successful installed no-action review. No attempt/result/stop file or external operation exists for the replacement at installation. Original stopped operation is unchanged. Owner command: `python3 -B "/Volumes/Signmons-P06/r11-retained-state-diagnostic-20260923-0830b/private.py" --run`, once at or after 8:30 AM Eastern and before the 9:15 AM deadline. No automatic retry; no scope deviation.

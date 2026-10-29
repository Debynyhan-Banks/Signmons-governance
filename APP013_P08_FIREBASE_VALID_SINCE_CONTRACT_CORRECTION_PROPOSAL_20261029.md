# APP-013 / 3A / P08 — Firebase REST revocation-field correction proposal

Status: **PROPOSED; owner decision required before implementation**. The approved 8:30 operation has not started: no command was released, no attempt/journal exists, no password was requested and no external read occurred. Its private plan/binding were deleted with absence readback at `P08_PRESTART_PRIVATE_INPUTS_RETIRED`.

## Demonstrated gap

Final shift-left review compared the exact Firebase REST endpoint to Google’s primary Identity Platform `UserInfo` contract. `POST /v1/projects/{project}/accounts:lookup` returns revocation time as `validSince`, an int64-formatted string in seconds since epoch. `tokensValidAfterTime` is an Admin SDK representation and is not the REST response field. Backend `d7c40c1` and its fake response instead require `tokensValidAfterTime` as a UTC string.

Running the approved operation would therefore consume its no-retry attempt and report Firebase drift even when the retained disabled account is correct. The fail-closed behavior prevents false qualification, but the native response parser is not launchable against the documented endpoint. Reference: Google Cloud Identity Platform RPC `UserInfo.valid_since` and REST accounts lookup/UserInfo definitions.

## Alternatives

1. **Recommended — narrow local REST contract correction and tests.** Change only the evidence-contained Firebase response parser and fake response: require `validSince` to be an all-decimal seconds string, reject missing/negative/fractional/overflow/wrong-field values, and require its integer seconds to be at least `REVOCATION_LOWER_BOUND_MS // 1000`. Keep exact UID/email/name/disabled/parsed claims, request URL/body, call ceilings, SQL, fingerprints, source/ownership gates, private purge and every mutation exclusion unchanged. Add boundary/malformed cases and rerun the 30 focused/model, three disposable PostgreSQL and applicable locked regressions.
2. Use Firebase Admin SDK instead. Rejected: it changes the tested transport/authentication surface and adds scope.
3. Run the approved operation unchanged and accept the expected stop. Rejected: it knowingly wastes the no-retry attempt and produces no useful current-state evidence.
4. Defer. No external action occurs.

Alternative 1 is a correction to the approved local prerequisite. It requires owner approval before implementation. The 8:30 operation proposal/approval is withdrawn unstarted and cannot be rebound after any source change; a corrected external operation would require a fresh immutable proposal and separate approval.

## Exact local boundary and finish

Modify only `evidence/APP-013/p08-composed-qualification-local-20261029/` and append sanitized correction evidence. Do not modify product source, schema/migrations, packages, historical receipts, section criteria/counts or unrelated `AGENTS.md`.

Observable finish: exact REST `validSince` seconds at the retained boundary or later qualifies locally; earlier, missing, malformed, overflow, `tokensValidAfterTime`-only and extra/ambiguous revocation representations fail closed; all repository gates pass. Then prepare a fresh operation with new IDs/window/approval. No credential resolution or external read is included.

## Decision requested

Approve Alternative 1 for this bounded local parser/test correction only, or defer. Approval includes no credential, Cloud/database/Firebase/provider read or mutation, IAM/API/key/account/runtime/token/Stripe/payment/deployment/billing/spending action, attended operation, merge or push.

Accepted milestones remain 4/8; newly closed R1 0/27, legacy 6/60, intelligence 0/13. P08 and 3A remain open. **Unintended transport-contract drift disclosed before execution; no scope deviation implemented.**

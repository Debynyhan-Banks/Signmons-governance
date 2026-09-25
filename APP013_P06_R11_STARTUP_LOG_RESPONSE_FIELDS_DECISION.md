# APP-013/P06 R11 startup-log response-fields decision

Status: prepared for owner review; no execution approval, installed authorization or attempt exists.

## Reason and local repair

Replacement diagnostic 1f9ba8f2-9208-4611-87a4-61eeb584c1e7 consumed its single attempt at 2026-09-25T13:36:51.067268Z. Cloud Logging returned HTTP400; the helper safely recorded REQUEST_SEND, HttpBadRequestError, loggingSendCount1 and loggingGuardInstalledtrue. No logs or startup classification were returned, and no retry occurred. The original application startup cause remains unknown.

The SDK serialized the exact approved endpoint/filter/body. Official entries.list documentation supports the endpoint, resourceNames, pageSize200 and timestamp asc. The response selector descended into dynamic jsonPayload/message and jsonPayload/error/message; the SDK does not validate this selector. That projection is the strongest local suspect, not a confirmed cause: the API error body was not retained.

A bounded uninstalled helper correction selects declared response fields only: entries(timestamp,severity,textPayload,jsonPayload),nextPageToken. It then uses the unchanged sanitizer, examining only textPayload, jsonPayload.message and jsonPayload.error.message. Additional JSON values can be present in transient process memory but are never classified, printed or retained. This projection change is explicitly included in the proposed approval below. No application/runtime repair is implied.

Source: backend ae92692/governance9c8d428 and the original SHA-bound local helper. Local artifact: /private/tmp/r11-enabled27-response-fields-local. Reuse the existing one-send guard, no pagination/retry, exclusive marker, exact identity/source/window/hash and sanitization behavior. Preserve all consumed files. Local tests and review must pass before any installation.

## Proposed one-use read-only operation

Operation `a087c5c8-8162-4d95-96ef-4739de9e0198`. Authorize installation of its private helper, hash binding and authorization, then exactly one Cloud Logging query during the 30 minutes immediately following explicit owner approval. Resolve the approval timestamp to exact UTC start/end before installation; refuse if it cannot be established or sufficient time does not remain. An explicit owner-selected Eastern window can replace this proposal.

Fixed scope: project signmons; service signmons-calldesk-staging; revision signmons-calldesk-staging-app013p06enabled27; historical event interval September25,2026,13:00:06Z–13:00:32.999999Z; stdout, stderr and system startup streams only, excluding request logs; ascending timestamps; maximum200 entries; one entries.List call; no pagination, redirect or retry. Exact filter is unchanged from the prior reviewed diagnostic.

Retain only the existing allowlisted startup classes, counts, severity and first/last timestamps, plus fixed helper failure phase, allowlisted exception class, numeric HTTP status, send-attempt count and guard-installed boolean. Never retain raw logs, API error strings, stack traces, credentials, identifiers or unrelated JSON fields. Unknown errors remain unclassified. Count is attempted sends, not delivery proof. A page token/limit gives RESULT_LIMIT_REACHED, without continuation.

Exclusions: no database access/write, LOGIN, activation, deployment, traffic change, image build, provider request/mutation, verification code, browser/customer action, job creation or retry, hold release, secret/IAM/billing change, packet or other live execution. Existing runtime shutdown remains untouched. No automatic retry or reuse of any consumed operation.

## Finish and ownership

APP-013/2B P06-R11 diagnostic preparation only. Implementer installs/checks and reads once after approval; no owner Terminal/password/browser action. Observable finish is sanitized startup classes or an explicit safe failure stage. No application change is justified by HTTP400 alone. P06 remains12/14; R11/fullR12 open; accepted1A/1B/2A unchanged. No scope deviation. Owner decision pending.

References: [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list), [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

## Local validation

Completed:19 focused tests and sanitizer self-test pass; source diff is only the response selector and local directory binding. The unchanged sanitizer ignores unrelated JSON. Tests use actual SDK serialization with fictional configuration/credential stubs and a fake transport; sockets are blocked. Helper hash `214bf72861d1a6e7b92c37be035afd55b7714ed2ef73308ee9c26908a93de421`. Report: `/private/tmp/r11-enabled27-response-fields-local/TEST_REPORT.md`. No live server acceptance or startup cause is established. Owner approval is still pending.

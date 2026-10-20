# APP-013 / P06-R11 Neon Connect-string authentication diagnostic

## Status and authority

Owner approved preparation on 2026-10-07. Live execution is not yet approved. Proposed plan `b1849763-4158-4e16-afb5-ee8613589967`, operation `a8836952-c1c8-4da5-a2c6-00b214cf8cd2`, window 1:15-1:40 p.m. Eastern with a 1:25 p.m. start deadline.

## Section and acceptance criterion

- Section: APP-013/P06-R11, within remaining section 2B controlled-acceptance preparation.
- Connected customer workflow: staging must regain database-backed readiness before the one protected phone/address/review/job journey can resume.
- Acceptance for this diagnostic: a freshly copied Neon production Connect URL matches the fixed production role/database/direct-or-pooled endpoint metadata and its embedded credential completes `SELECT 1`; otherwise one fixed refusal or target-mismatch result is retained.
- This diagnostic is not 2B acceptance and does not change the accepted 1A/1B/2A baseline of 3/8.

## Inspected evidence and demonstrated gap

- Production branch ID: `br-young-term-ayfi7ist`.
- Expected direct host: `ep-nameless-frog-ayk5gr5y.us-east-2.aws.neon.tech`.
- Expected pooled host: `ep-nameless-frog-ayk5gr5y-pooler.us-east-2.aws.neon.tech`.
- Expected role/database: `neondb_owner` / `neondb`.
- Two consumed password-only operations on 2026-10-05 returned `AUTH_REFUSED` for both hosts, including after an owner-confirmed production Console reset.
- The owner later confirmed that the Connect panel displayed the expected endpoint name. Password-manager and manual URL reconstruction ambiguity remain because neither prior helper consumed the complete current Connect URL.

## Existing components and expected files

- Reuse the hidden TTY input, one-use approval/window binding, fixed classifier, temporary 0600 pgpass handling, buffer clearing and no-retry markers from `scripts/p06-r11-db-auth-diagnostic.py`.
- Add `scripts/p06-r11-connect-string-diagnostic.py` and `scripts/test_p06_r11_connect_string_diagnostic.py`.
- Add backend evidence `evidence/APP-013/p06-r11-connect-string-diagnostic-20261007.md`.
- Install an exact reviewed copy under `/private/tmp/r11-connect-string-diagnostic-20261007-1315` only after local checks pass.

## End-to-end contract and boundaries

1. Owner selects production in Neon and copies the complete current Connect URL without displaying it in chat or Terminal.
2. Helper validates exact approval, source hash, private-root ownership/mode, time window and unused state.
3. Helper reserves the operation before private input.
4. Hidden input accepts one URL. Metadata validation requires PostgreSQL scheme, role `neondb_owner`, database `neondb`, port 5432, one exact expected host, a nonempty password, required TLS and no fragment.
5. Metadata mismatch writes only `TARGET_MISMATCH`; no connection occurs.
6. On match, the password is decoded only in-process, written to a temporary 0600 pgpass for both fixed hosts, and fixed-argument `psql -X ... SELECT 1` probes direct and pooled endpoints.
7. Evidence contains only plan/operation/time, input host class, target match and fixed endpoint classifications. Raw URL, username input, password, server text and connection string are never persisted or printed.
8. The mutable input/password buffers are overwritten where possible and pgpass is removed in `finally`. Every attempted invocation is consumed and cannot retry.

No database write, secret read/change, IAM, build, deployment, traffic/tag/session change, migration-job action, customer data/action, provider message, appointment, payment, billing or automatic retry is authorized.

## Finite checklist and exit tests

- [x] Implement strict byte-oriented Connect-URL parsing and fixed target validation. Exit: direct/pooled positive cases and wrong scheme/host/role/database/port/TLS/password/fragment cases pass.
- [x] Reuse one-use hidden-input and immutable marker protections. Exit: approval/hash/window/root/consumed guards refuse before connection.
- [x] Prove command construction and output classification without a live connection. Exit: tests show fixed host/role/database/query and no credential in results.
- [x] Run focused tests, compilation, architecture, governance baseline/consistency and whitespace checks. Exit: all pass.
- [x] Install exact 0700/0600 package and verify source hash, modes and absence of action markers. Exit: reviewable package ready.
- [ ] Obtain exact owner execution approval. Exit: approval file matches plan, operation, root, source hash and future window.
- [ ] Owner runs once and implementer reads only the sanitized receipt. Exit: one terminal result or stop, with no retry.

## Positive, negative, recovery and browser coverage

- Positive local: exact direct and pooled URLs, percent-encoded password characters, expected TLS query.
- Negative local: malformed/non-ASCII URL, missing password, unexpected endpoint/user/database/port, plaintext/no TLS, fragment, expired/mismatched approval and consumed package.
- Recovery: interruption or any exception writes a terminal stop and removes pgpass; it never retries.
- Concurrency: exclusive attempt creation and consumed-marker check allow only one invocation to reserve.
- Browser: no browser automation. Owner copies from the authenticated Neon production Connect panel; no screenshot or credential capture.

## Dependencies, owners, exclusions and rollback

- Owner: privately copies the current production URL, approves and performs the single terminal invocation.
- Implementer: prepares/verifies the bounded helper and reconciles sanitized evidence.
- Dependency: authenticated Neon Console and current production Connect URL at execution time.
- Excluded: any password reset, credential cutover, Google secret version, Cloud Run readiness/cutover, migration execution, or R11 customer journey.
- Rollback/disabled state: diagnostic makes no persistent external change. Existing Cloud Run traffic and disabled P06 state remain unchanged.
- Material drift or target mismatch stops; any next operation requires a new decision and approval.

No scope deviation.

## Prepared evidence

Seven focused local tests, Python compilation, architecture, frozen-baseline, cross-repository consistency and whitespace checks pass. The source and installed helper SHA-256 are both `c4a7575ab9517e5b015f6c51ff0547e3eac4a1b4dfd770508b77b8b8622475d4`. Root mode is 0700; helper mode is 0700; test and proposed approval modes are 0600. No diagnostic marker exists. Live execution remains unapproved.

## Expired unused package and fresh proposal

The owner approved the 1:15-1:40 p.m. package, but reported missing the window. No diagnostic marker exists, so no private input or database connection occurred. The approval is expired and the package must never be run.

A fresh successor is prepared only after that safe stop: plan `4002cd56-4d00-488a-b580-c35b046e93d9`, operation `e3557f6c-ff07-4d75-b8a3-70d5b8122cb4`, root `/private/tmp/r11-connect-string-diagnostic-20261007-1810`, proposed for 6:10-6:35 p.m. Eastern with a 6:20 p.m. start deadline. All scope, input, query, retention, stop and exclusion boundaries above are unchanged. This is a new operation and requires fresh exact execution approval.

## Successor result

The fresh operation ran once at `2026-10-07T22:14:05.900956Z` and returned `R11_CONNECT_STRING_TARGET_MISMATCH`. The fixed receipt records `target=MISMATCH`, `inputHostClass=UNCONFIRMED`, and `NOT_RUN` for both endpoint probes. The attempt/result markers exist and no pgpass remains. No database connection occurred.

The operation is consumed and must not be rerun. The result means the hidden clipboard value failed at least one strict URL metadata rule; it does not identify the private value or which rule failed. The next smallest step is owner clarification of which Neon Connect control was copied (Connection string versus PSQL command) and visual confirmation of the non-secret branch/database/role selections. No new diagnostic or external mutation is authorized.

## Clarified input and fresh successor

The owner clarified that only the password was pasted. This fully explains the target mismatch; the helper correctly refused before connection. No parser or authentication defect is demonstrated.

A fresh successor changes only identifiers, window/root bindings and the private prompt clarification: **full `postgresql://` URL from Neon Connection string, not password or PSQL command**. Plan `1d0f0a27-c198-4f9f-862f-65d2f8fca6b1`, operation `c3ba1c94-cfd6-4de3-a255-2cff3c261eb8`, root `/private/tmp/r11-connect-string-diagnostic-20261007-1830`, proposed for 6:30-6:55 p.m. Eastern with a 6:40 p.m. start deadline. All validation, read-only, privacy, one-use and exclusion boundaries remain unchanged. Fresh exact approval is required.

## Clarified-input successor result

The owner copied the full Connection string as instructed. The operation ran once at `2026-10-07T22:34:24.390152Z` and again returned `R11_CONNECT_STRING_TARGET_MISMATCH`; direct and pooled probes are both `NOT_RUN`, input host class is `UNCONFIRMED`, and no pgpass remains. The operation is consumed and must not be rerun.

Because the input category is now confirmed, the remaining gap is strict metadata compatibility, likely a current non-secret host/query format that differs from the fixed parser assumptions. Before another live attempt, use a local clipboard-only sanitizer to display only scheme, hostname, port, role, database and query-key names. It must never print or persist password/userinfo or the raw URL. This local metadata inspection performs no network or external action and requires no database-test allowance.

## Clipboard sequencing cause and final fresh proposal

The sanitizer output showed the clipboard contained the Python command itself: blank scheme/host/role and the command text as the path. Copying a command from chat had replaced the previously copied Neon URL. This fully explains the second mismatch; current Neon metadata remains uninspected and no helper defect is demonstrated.

The corrected human sequence is: run the Terminal command first; after the hidden prompt appears, switch to Neon, copy the Connection string URL, return to Terminal and paste. A fresh successor extends hidden-input wait from 120 to 240 seconds and makes that sequence explicit in the prompt. Plan `d1bc6691-015a-4589-96a0-b75869683f7f`, operation `23070bd9-a3c0-48c0-8f48-81dc723470df`, root `/private/tmp/r11-connect-string-diagnostic-20261007-1850`, proposed for 6:50-7:15 p.m. Eastern with a 7:00 p.m. start deadline. All target, query, privacy, one-use and exclusion boundaries remain unchanged. Fresh exact execution approval is required.

## Correct-sequence result and local metadata inspection

The owner followed the corrected sequence. The operation ran once at `2026-10-07T22:56:50.638180Z` and returned `R11_CONNECT_STRING_TARGET_MISMATCH`; both endpoint probes are `NOT_RUN`, input host class is `UNCONFIRMED`, and no pgpass remains. The operation is consumed and must not be rerun.

The remaining issue is now a strict non-secret URL metadata mismatch. A local-only helper at `/private/tmp/r11-neon-url-metadata-20261007.py`, SHA-256 `85a886fe32e4b59bf32f170bc0cb65a601bf6ab983627a4ffc4933f3a9923142`, waits while the owner copies the URL and prints only scheme, host, port, role, database, password-presence boolean, query-key names and fixed mismatch categories. It makes no network call, prints no password/full URL, persists no URL and performs no external action.

## Exact current host resolution and corrected proposal

The sanitized metadata result is exact: scheme `postgresql`, pooled host `ep-nameless-frog-ayk5gr5y-pooler.c-5.us-east-2.aws.neon.tech`, port 5432, role `neondb_owner`, database `neondb`, password present, query keys `channel_binding,sslmode`, and sole mismatch `HOST`. The demonstrated defect is the helper's stale host constants, which omitted Neon's current `.c-5` routing segment.

Neon's documented pooling convention adds `-pooler` to the endpoint ID. Therefore the fixed exact host pair is pooled `ep-nameless-frog-ayk5gr5y-pooler.c-5.us-east-2.aws.neon.tech` and direct `ep-nameless-frog-ayk5gr5y.c-5.us-east-2.aws.neon.tech`. No credential or other metadata is inferred.

A corrected fresh successor binds only those exact host constants plus new identifiers/window/root: plan `ffc2e0fc-12f2-4936-b8ee-d0617d5675c2`, operation `35d42af5-b938-4783-a053-80a1a0706de2`, root `/private/tmp/r11-connect-string-diagnostic-20261007-1915`, proposed for 7:15-7:40 p.m. Eastern with a 7:25 p.m. start deadline. All query, privacy, one-use, read-only and exclusion boundaries remain unchanged. Fresh exact execution approval is required.

## Accepted credential result

The corrected operation ran once at `2026-10-07T23:20:06.069806Z` and returned `R11_CONNECT_STRING_DIAGNOSTIC_CAPTURED`. The fixed receipt records `target=MATCH`, `inputHostClass=POOLED`, direct `ACCEPTED`, and pooled `ACCEPTED`. Attempt/result markers exist and no pgpass remains. The package is consumed and must not be rerun.

This proves the current Neon production Connect credential authenticates as `neondb_owner` to both exact current production endpoints. It does not update Google Secret Manager, Cloud Run, the migration job, traffic, tags or sessions and does not authorize any cutover. The next step is fresh read-only consumer/configuration reconciliation followed by a separate concrete mutation proposal.

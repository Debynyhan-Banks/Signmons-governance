# APP-013 / 3A / P08 — TG1 local validation

TG1 is implemented and locally verified in backend `6eed73b53f660f9e2bd39f78224792c0085e9323`. Owner decision `2b6f93a491be21d347c705d5ac4a81fd302f003d` approved proposal `eeadceb`, SHA256 `d36c971d11339f0fea6bd5b35a9c465be7e0c7c05cb759c3caeee0fe32f93109`. The original proposal and historical R62 receipts remain byte-identical.

## Delivered behavior and evidence

The exact current forward tag mutation now retains one of seven finite failure categories in the existing journal failure field. Exact exception type, argument type/count and literal checks reject foreign or untrusted error text. Recognition uses the existing dynamically bound command and candidate. No raw stdout, stderr, provider error, credential or private input is persisted. The command, reservations, eight-second timeout, 65,536-byte limit, retries, JSON/SDK acceptance predicate, authoritative readbacks, uncertainty latch and cleanup remain unchanged.

The three approved source/test files and eight derived current manifests are the entire implementation commit. Unrelated owner AGENTS.md changes and renewal receipts were preserved. Native, IQ1, SQ1, VM2 and containment-read actual committed-source guards passed; all eight existing file maps and committed bytes match. The qualification manifest is unchanged. No source, dependency, acceptance or external-action scope was added.

Evidence: backend `evidence/APP-013/p08-connected-packet-20261110/tg1-local-20261126/verification.json` and eleven safe logs. Retained evidence is committed in `fabd4561a2a25f4618aa7d2395fbba1eff1c3795`; the original raw test output remains in `23a106bac9af404f36aff7e2f8557bd7a91d9a65`. One display-only trailing space in a unittest status line was normalized for the final whitespace gate, with original hash/commit provenance retained. The verification contains exact old/new file hashes, command categories, initial failures, rerun results, independent review and the incident below.

| Check | Observed result |
| --- | --- |
| TG1 focused tests | 17 passed in 7.617 seconds; exact old-source controls reproduce all seven generic failures |
| Native regressions | 168 executed; three methods failed under restricted local permissions, then all three passed with required local process/loopback permissions |
| Connected packet/approval/renewal tests | 50 passed |
| Dependency synthetic/process checks | 345 executed; 24 methods blocked by local permissions, then all 24 passed; database fixture excluded from rerun |
| Key-correction launch/port tests | 24 passed |
| Governance safeguard tests | 25 passed |
| Actual source guards and eight current maps | Passed against committed TG1 source |
| Frozen baseline, complete consistency, backend wrapper, architecture and whitespace | Passed; no frozen anchor changed |

Counts describe the named suites, not acceptance progress or a sum of unique reruns. The 17 focused cases are included in the native suite. The installed SDK printer and original predicate are used as compatibility controls. Tests preserve the original tag uncertainty through main and independent closeout, distinguish cleanup disagreement, reject hostile errors, enforce one dispatch, and check concurrency and interruption/deadline precedence. Two initial new-fixture errors were corrected without changing runtime code or weakening assertions; their failure log is retained. Rerun-selector loader errors and a supplemental SDK-symlink checker correction are also recorded rather than counted as passing tests.

Independent source/test review found no blocking implementation issue. After the first execution, the reviewer separately checked the fixture corrections and confirmed exact original failed-method sets in the successful 3 + 24 reruns.

## Disclosed test-selection incident and owner direction

The initial broad dependency selection accidentally included `CT3DisposableTLS`, despite TG1's explicit exclusion of PostgreSQL service tests. This was unintended scope drift and was disclosed before further testing. `initdb` was actually invoked and failed; the fixture's subsequent server-launch line, SQL-readiness loop and TLS restart were not reached. The base temporary-directory cleanup and absence assertion completed before the subclass failed on its missing server attribute. This is supported by the retained traceback and inspected source; no database service qualification is claimed.

The owner replied **“Finish approved checks only.”** Continuation selected only the exact original three native and 24 dependency failed synthetic/process methods; no PostgreSQL fixture was rerun. Assertions and runtime code were unchanged. Local process inspection and loopback permissions resolved those failures. No credentials, provider calls, sign-in, browser action or payment occurred. This incident is retained as a deviation record, not relabeled as “No scope deviation.”

## Readiness and handoff

All five TG1 checklist items are complete: baseline reproduction, compatibility controls, assembled main/independent closure, guard/privacy/concurrency cases, and current manifests/regression/independent review. This advances diagnosis of the existing connected payment journey; it is not new live readiness or customer acceptance.

R62 remains consumed with original `ENTRY_CONTAINMENT_UNCONFIRMED` and its historical tag uncertainty. Its independent retirement checks and private purge remain recorded separately. The discarded original cause cannot be recovered by this local change. Current effective access, authentication, event and app payment-gate state remain UNKNOWN for a future attempt.

Implementer owns the next fresh source-bound readiness review using the existing connected interfaces. Owner must separately authorize any new live qualification/execution. No attendance or credential request is pending from TG1. Remaining 3A acceptance is the same admitted-job $99 USD Sandbox Checkout, authentic matching event, cleared application gate, independent cleanup and owner acceptance. Accepted 1A/1B/2A/2B remain **4/8**; 3A **OPEN**; R1 newly closed **0/27**. No replay, payment, real charge, refund, customer contact, deployment or support contact is authorized.

Rollback reverts only TG1 source/current pins before any fresh execution; no consumed attempt or historical receipt is reset.

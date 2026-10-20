# APP-013 / 2B / P06-R11 — correction-continuation repair decision

Status: owner-approved bounded local implementation complete and review-ready. Release, external action and any new journey remain unauthorized.

## Demonstrated gap

Enabled39's reviewed submit returned `REFUSED` / `ADDRESS_CORRECTION_STATE_UNAVAILABLE` / `jobCreated:false` and then closed safely. The current correction sequence retains Google's first `responseId` only in one process-local five-minute map. The corrected follow-up requires that value as `previousResponseId`. A different/restarted process therefore produces exactly the enabled39 refusal before another provider call. Local source inspection and the existing 47 focused passing tests establish this design behavior; they do not prove which infrastructure event occurred in the live run.

Google's current official reference requires the first response UUID to accompany revalidation, while Signmons' existing contract forbids durable Google identifiers/raw payloads and browser exposure of the raw ID. Database persistence, raw browser return and instance-affinity reliance are therefore outside the current approved card or inadequate.

## Alternative 1 — recommended

Approve one short-lived encrypted correction-continuation envelope. Reuse the existing runtime AES-256-GCM cipher shared by revision instances; add no datastore, schema, migration, key or provider. The envelope contains the response UUID plus strict tenant/session/conversation, intent/revision, policy/organization, purpose and expiry bindings. Only ciphertext enters the initiating page's memory. It must never enter URLs, cookies, storage, DOM text, logs, analytics, audits, database or backups, and it clears on use/edit/refusal/expiry/pagehide/session clear.

Any instance may decrypt and verify it for one corrected follow-up. Missing/malformed/expired/foreign/substituted input refuses before provider access. Existing ledger locks and the two-operation session ceiling remain the concurrency/replay fence. No hold reset/release, job bypass or new authority.

Implementation is finite: codec; controlled service/composition/runtime wiring; strict request/result projection; in-memory page handoff; positive/negative/restart/concurrency/replay/browser tests; build/lint/architecture/governance checks. No Prisma change. Successful local work is not release or R11 acceptance.

## Other alternatives

Alternative2: encrypted database state plus TTL/cleanup. This requires broader schema, retention, backup and recovery approval.

Alternative3: force one instance/session affinity. This does not guarantee continuity across instance loss and is not acceptance-grade.

Alternative4: pause with R11 open and no further cost.

## Decision gate

The owner explicitly approved Alternative 1 and the encrypted ephemeral browser-carried continuation boundary for local implementation and synthetic testing only. The implementation replaces the process-local map with an AES-GCM ciphertext held only in page memory, strictly projects the durable ledger command, and preserves the existing two-operation ceiling. No schema, migration, key, datastore, provider or downstream job-contract change was introduced.

Source reconciliation found that the existing correction screen permits either accepting the candidate or typing the corrected address. The envelope therefore survives address-field edits while review state is invalidated; it is bound to tenant/session/conversation/service/revision/policy/organization/expiry, and the provider revalidates the newly reviewed address. A corrected submit intentionally uses a new request UUID, so binding it to the first request UUID would make the existing correction flow impossible. Terminal outcomes, pagehide and private-session clear discard the ciphertext.

Local evidence passed: 187 focused Jest tests; the full backend suite with 132 suites and 2,495 tests passed plus one suite/three intentional skips; build, lint, architecture and syntax checks; a 52-case desktop/mobile synthetic UI matrix; and the complete disposable PostgreSQL 18 real local HTTP/browser harness including ordinary correction, postal-format correction, repeated-correction refusal, capacity refusal and connected exact replay. Both browser gates used synthetic SDK/fetch ports and reported zero live provider calls. Backend evidence: `evidence/APP-013/p06-r11-correction-continuation-diagnosis-20261010.md`.

Build/release/deployment/provider access and any later journey require separate concrete approvals.

P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. Approved data-boundary implementation only. No further scope deviation.

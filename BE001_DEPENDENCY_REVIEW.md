# BE-001 dependency disposition — 2026-09-12

Decision: A, substantially satisfied by BE-008/APP-013, with residual acceptance consolidated into current APP-013. Not fully Done; no independent Next slot or duplicate rebuild. This is the earliest dependency-correct position because compliant transactional messages are required before APP-013 acceptance, not after APP-015. APP-013 remains WIP=1; its existing 3C communications package owns these residuals, without interrupting current 2B.

## Repository evidence at backend 330e402

- src/communications/sms-consent.service.ts: tenant/contact-hashed persistence and atomic audit/customer update, START prior-opt-out check, STOP, HELP telemetry, quiet hours and no-consent/opted-out refusal. Newer shared recipient locking and verbal-overwrite refusal already exist; reuse them.
- src/communications/sms-consent.service.spec.ts: tests of keyword/provider-normalized handling, suppression, identity and quiet hours. Existing acceptance in governance TICKETS/BE-008.md and backend evidence/BE-008/readiness-report.md covers its recorded transport foundation, not every newer replay scenario.
- src/communications/twilio-webhook.service.ts receiveSms authenticates signature/tenant then passes body and OptOutType to consent. Unlike delivery status, it does not pass MessageSid into the keyword operation. Therefore no event-identity deduplication is established at that boundary. An old authenticated START delivered after a newer STOP can meet the current prior-opt-out check; this remains unproven recovery safety.
- Raw UNSTOP has no direct branch in handleInboundKeyword. Provider-normalized OptOutType START is handled, but not proof of raw UNSTOP behavior across approved provider configuration. Do not claim the literal BE-001 criterion complete.

## Required closure inside APP-013

- [ ] Define and test raw/provider-normalized UNSTOP/START semantics without inventing first-time consent.
- [ ] Bind authenticated inbound keyword events to stable tenant/provider identity; duplicates or delayed old START cannot undo a newer STOP. Preserve legitimate later restoration and auditable outcomes.
- [ ] Demonstrate atomic persistence plus privacy-safe telemetry, rollback, concurrent suppression, no-consent/unknown fail-closed behavior and all active send-path enforcement.
- [ ] Link exact unit/integration and separately authorized provider/configuration acceptance, with reviewer/date. Keep current live sending disabled until remaining policy/release gates pass.

Only when these obligations and original BE-001 criteria have evidence may APP-013/BE-001 acceptance be closed. BE-001 remains a traceability file, not an obsolete/deleted ticket. No code changed by this analysis; no new provider operation or replay was sent.

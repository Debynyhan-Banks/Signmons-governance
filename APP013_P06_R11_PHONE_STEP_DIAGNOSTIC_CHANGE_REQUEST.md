# APP-013/P06 R11 phone-step and diagnostic correctness change request

Status: approved alternative 1 implemented and locally tested; ready for owner review, no release or execution authorized. Section: APP-013/2B, P06/R11. Existing acceptance remains one connected capped phone-verification, eligible-address and reviewed-submit journey with one authoritative admitted job, followed by full R12 closeout. No denominator, gate or dependency change.

## Demonstrated gaps

Consumed enabled22 diagnostic found zero correlated jobs, no address row and no matching approved CHECK in retained state. Owner cannot confirm seeing Code accepted. Browser source permits controlled draft/submit without verifyState APPROVED. Separately, diagnostic OID1114 timestamps decode in host-local timezone and can falsely report a later event; a synthetic timezone comparison reproduces four-hour drift. Full evidence: backend `evidence/APP-013/p06-r11-enabled22-retained-state-result.md`. Neither finding establishes all causes of earlier runs.

## Alternatives

1. Recommended: local-only repair and regression tests for the controlled browser prerequisite and diagnostic UTC handling. No live action.
2. Leave implementation unchanged and pause R11, preserving all evidence/holds. Do not schedule another run on current evidence.

## Bounded section card for alternative 1

Source backend `3edd960`; runtime accepted source `574f25a`. Reuse customer-intake-journey.js paint/verification/draft/submit seams, existing controlled UI/browser tests, existing retained-state analyzer and pg parser. Implement only: controlled UI clearly requires an accepted code before preview and final submission; defensive handlers send no draft/submit request for missing/pending/refused/unknown verification; changes/revocation invalidate UI eligibility; successful check permits progress without granting server authority. Preserve reviewed-address correction flow, exact-request retry semantics, and server proof/expiry checks. Do not add verification resends, retries, endpoints or new stored PII.

For diagnostic correctness, make timezone-less PostgreSQL timestamps explicitly UTC or convert to epoch at the query boundary, with regression cases for UTC/Eastern and daylight-saving boundaries. Preserve the original consumed helper/result byte-for-byte; use only a separately reviewed local candidate. Clarify dependent START checks so absent approved CHECK is not misreported as independent START absence. No new diagnostic installation or execution is included.

Expected files: existing browser fixture and focused UI/browser tests; bounded local diagnostic candidate/tests plus evidence. Before coding, resolve exact existing test commands and record the implementation card. Finite checklist: reproduce pending-code preview/submit locally; implement controlled-only guards and accessible explanation; test accepted code and invalidation; test busy/pending/double-click and exact-request recovery; verify address correction after valid proof; timezone regression and sanitized output; governance/architecture/lint/build/appropriate focused browser checks. Synthetic local fixtures only; no live credentials, DB, provider, secret or customer/browser action. Disposable database only if separately authorized; prefer existing mocked browser seams.

Finish: local passing evidence for prerequisite enforcement and timezone-independent diagnostic classification. Owner reviews local result before any release decision. Rollback is local revert of selected changes; deployed runtime remains closed. Implementer owns repair/testing; owner approves scope and any later build/packet/execution separately. R11/full R12 remain unaccepted, P06 12/14, prior 1A/1B/2A unchanged.

Excluded: packet, build, LOGIN, activation, deployment, provider request, code, live browser test, live database/secret read or write, hold release, ceiling increase, IAM/billing changes and live retry. No scope deviation implemented; proposed bounded UX/diagnostic change only.

Owner decision: “yes i approve alternative 1”. No external authority added.

## Local finish evidence

Controlled browser prerequisite/phone binding and diagnostic scoped UTC parser plus independent START reporting are implemented. 26 mocked browser scenarios, 13 diagnostic tests and 111 focused backend tests pass; lint/build/architecture/format/syntax pass. Original consumed diagnostic files remain byte-identical. Evidence: backend `evidence/APP-013/p06-r11-phone-step-repair.md` and `evidence/APP-013/p06-r11-phone-step-ui/summary.json`. No live operation, new authorization, packet or image build. Owner reviews this local result before any later release decision. Approved alternative 1 only; no other scope deviation.

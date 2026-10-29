# APP-013 / 3A / P08 — Firebase REST validSince correction local result

R1-W01 / APP-013 / 3A / P08. Owner approved Alternative 1 at proposal commit `fe4e9b3`; decision commit `5c23efb`. Backend correction is committed at `1125d17` with sanitized evidence `evidence/APP-013/p08-composed-qualification-local-20261029/firebase-valid-since-correction-result.json`.

The exact Identity Platform REST response parser now requires `validSince` as a decimal int64-formatted seconds string. It accepts the retained October 26 revocation boundary at second precision and later values. It rejects earlier, missing, negative, fractional, overflow, Admin SDK `tokensValidAfterTime`-only and ambiguous dual-field responses. Exact UID/email/name, disabled state, parsed tenant/admin/testOnly claims, URL/body, call ceilings, SQL, fingerprints, ownership/source gates and purge behavior remain unchanged.

Verification passed: 30 focused/model cases; three disposable socket-only PostgreSQL cases; unchanged role 26/26, restoration 37/37, access 40/40 and authentication 60/60; backend governance baseline, architecture and whitespace; governance frozen baseline, cross-repository consistency, 25 safeguard tests and whitespace. Authentication again ran from a deleted private no-space scratch copy. No test expectation or locked source was weakened.

Withdrawn operation `82ad7bf3-1bc8-455b-8c7b-0049387af3b5` remains unstarted and nonreusable: no command, attempt, password prompt or external read; private plan/binding absent. No credential, Cloud/database/Firebase/Stripe/provider action, mutation, payment, deployment, billing/spending, merge or push occurred.

Next/owner: provide a fresh attended window for a newly prepared immutable operation with new IDs and separate exact approval. Do not reuse the withdrawn operation or its approval.

Accepted milestones remain 4/8; newly closed R1 0/27, legacy 6/60, intelligence 0/13. P08 and 3A remain open. **No scope deviation.**

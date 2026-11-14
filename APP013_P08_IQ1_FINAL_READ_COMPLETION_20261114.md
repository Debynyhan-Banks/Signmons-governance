# APP-013 / 3A — final cleanup observation correction complete

Committed runtime: `512c5842bc5b29f559564d816d5818f8ce090610`. Traceability and finite scope: APP013_P08_IQ1_FINAL_READ_LOCAL_CARD_20261114.md, under original local approvals fa98c82/46137d2. No new external authority or provider operation was used.

## Finding and correction

IQ1's first disabled-state readback could abort cleanup before its already budgeted sixth metadata/UID read. This is a confirmed local sequencing gap; it does not explain why the provider response omitted the disabled field. The installed SDK describe path uses ServiceAccounts.Get, while enable/disable confirmation hooks discard the response and print acknowledgement. No arbitrary propagation delay, polling or mutation retry was added.

After an exact classified RB1 identity-readback failure, IQ1 now retains that code and attempts the existing final metadata read through the unchanged source/configuration/custody/time gates. Same-UID explicit disabled state may confirm restoration, but the original readback failure remains non-null and still prevents `QUALIFIED_AND_CLOSED`. A separate fixed-code `cleanupReadbackFailure` preserves that first reason if final metadata also fails. Transport/authority/source/configuration failures, failed disable, exhausted time or foreign UID do not gain a continuation bypass.

The command ceiling stays main5/cleanup6 with at most one enable and one disable. Shared native code, installed SDK, all other manifests, windows, credential behavior and qualification predicates are unchanged. Historical IQ1/IQ2 result bytes were verified unchanged. IQ2's 17:02:54 Eastern same-UID disabled observation remains the last live state evidence, not a new observation from these tests.

## Validation and readiness

- 195 connected tests PASS, including 59 IQ1 tests; 135 native tests PASS. The initial focused run contained 57 tests; two additional boundary tests are included in the final full run, not double-counted.
- Tests prove final confirmation after missing/malformed/mismatching readback, preserved first/final error codes, continued qualification failure, foreign UID or missing state refusal, transport failures, and source/configuration/deadline interruptions without extra reads/mutations.
- Committed source/manifest guard PASS in 0.606 seconds at 2026-11-14T22:17:23Z; architecture PASS. Required frozen-baseline/consistency, 25 governance tests and whitespace results are recorded in the final readiness evidence.
- Existing connected regression fixtures include local loopback browser/process tests; no live account/browser/provider or real credential-cache read occurred. No TypeScript build inputs changed; the previous successful build is reused, not reported as a fresh build.

Evidence: backend `evidence/APP-013/p08-connected-packet-20261110/iq1-local-verification/final-read-correction/` (logs and readiness.json). Original local checklist items1–5 in this correction card are complete after the final governance checks and evidence commits. The correction has not been exercised live, and local tests do not retroactively qualify IQ1.

## Current remaining-work list

1. Implementer: consolidate connected-entry readiness using unchanged KQ3/AC1/RB1 evidence and IQ1/IQ2's specific observations. Preserve original R47 account/session/revocation unknowns and identify the exact existing check for each remaining requirement. The immediate missing-field cause remains UNKNOWN; do not silently waive its failed criterion.
2. Owner/credential/cloud custodians: review a fresh exact live packet only after local readiness is complete. No renewal, identity repeat or full payment run is scheduled by this correction. Old IQ1/IQ2 windows and decisions are consumed.
3. Complete the existing same-job authentication → Sandbox Checkout → authentic event/application gate/failure recovery → independent closure → owner acceptance journey. No substitute acceptance section or payment stack.

Next observable result is the bounded connected readiness review, not another attended discovery session. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27. Owner has no password or Terminal action now. No scope deviation.

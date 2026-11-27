# APP-013 / 3A / P08 — AP1 authentication/payment-boundary proposal

**PREPARED FOR OWNER REVIEW; NOT APPROVED OR IMPLEMENTED.** This is one local source-seam correction and synthetic-test proposal. It grants no credential, provider, SQL, browser, payment, replay, deployment, IAM, secret, billing, customer-data or production authority.

## Demonstrated gap and retained result

R65 is consumed and closed. Its immutable final result remains `ENTRY_CONTAINMENT_UNCONFIRMED` with sole residual `AUTH_OUTCOME_UNKNOWN`, `authProofReady=false`, `authenticationObserved=false`, `childResultSha256=null`, and no observed browser/payment. Cleanup, private purge and owned-process/file absence are independently verified. Do not replay R65 or reinterpret cleanup as authentication proof.

The retained journal stops at `ADAPTER_REFUSED_OR_UNKNOWN / TOKEN_INTENT`. Current source explains why that label is aggregate:

- `recovery-sequence.mjs` saves `TOKEN_INTENT`, calls `clients.issue()`, validates the token, then calls `clients.authenticate(token)` before its next persisted phase;
- in the version-2 native child, `clients.authenticate` is replaced by one wrapper that first awaits the original runtime authentication and then calls `runPayment()`;
- therefore the retained label spans token issuance, runtime Firebase/claims/exact-job authentication, and the payment handoff. It cannot identify which boundary refused;
- R65 did not retain `SIGN_EXCHANGE_REFUSED` diagnostics, the payment journal stayed `QUALIFIED`, and no payment bootstrap was created. These facts do not identify a provider cause or prove that runtime authentication was accepted.

The exact inspected source and hash inventory is recorded in `APP013_P08_AP1_SOURCE_REVIEW_20261127.json` against backend `4e29a9114245990fd69712749505e5b069d9ca70`. Historical R65 receipts and results remain byte-immutable.

## Recommended bounded correction

If the owner approves AP1, change only the current local coordinator/native seam so runtime authentication and the payment handoff have separate persisted boundaries:

1. Add one optional, explicitly injected post-authentication hook to the current `CoordinatorAuthSequence`. Existing callers that omit the hook retain byte-equivalent control flow and result semantics.
2. Keep `clients.authenticate(token)` as the existing runtime authentication only. After it returns, persist the existing `AUTHENTICATED` phase with `authenticated=true` exactly as today.
3. When and only when the injected hook exists, persist one new finite phase, `PAYMENT_HANDOFF_INTENT`, then invoke the existing `runPayment()` composition with the same token, ports, journal, presenter and outer capability.
4. In `native_child.mjs`, stop wrapping `clients.authenticate`. Pass the existing payment composition as that explicit post-authentication hook for version-2 `--run` only. Other modes and version 1 remain unchanged.
5. Add `PAYMENT_HANDOFF_INTENT` only to the existing safe child-phase allowlist. Add no new raw-error field, response retention, provider classification, transport, retry or request.

The correction is diagnostic and truth-preserving:

- a token-issuance or runtime-authentication refusal remains `authenticated=false` and cannot produce parent proof;
- a failure after the existing runtime authentication returns can retain `authenticated=true` and `failureStage=PAYMENT_HANDOFF_INTENT`, while the existing payment journal remains authoritative for payment outcome/containment;
- a transient phase or lost child output never sets the parent `authProofAccepted` or `childResultSha256`; the existing exact child result, Handoff checks, account/session readback and success-only parent proof are still required;
- `authenticationObserved=true` never means payment observed, payment accepted or 3A accepted. The existing `paymentObserved`, authentic-event/application-gate checks, independent closeout and owner acceptance remain separate.

Do not add a provider probe, raw response body, arbitrary exception text, another subsystem, standalone authentication path, retry, polling, weakened proof predicate or success inferred from a journal intent.

## Exact prospective file and reference scope

Six existing implementation/test files only, relative to the backend:

| File | Prospective purpose | Inspected SHA-256 |
| --- | --- | --- |
| `evidence/APP-013/p08-real-client-binding-local-20261031/source/recovery-sequence.mjs` | optional hook and `PAYMENT_HANDOFF_INTENT` phase | `dce019ea7fd95af03d7ea59dbedea8a26b6634c29abdacac60a16928bea3deab` |
| `evidence/APP-013/p08-real-client-binding-local-20261031/source/bound_handoff.py` | exact safe-phase allowlist only | `ecb138f5bd1401b7f84661aeab062c9fb0c0d26358d321f74ade93beac5b494f` |
| `evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.mjs` | sequence and privacy regressions | `85d4104f44c53f2476cf5ff0ebfbd417b6dff92e1b73843d5fe8cbc54972d5b2` |
| `evidence/APP-013/p08-real-client-binding-local-20261031/source/test_bound.py` | allowlist/merge/lost-output regressions | `3186f8f7cc898307379eaf3ac4388845e0b1f61400640878cd546012dcba3380` |
| `evidence/APP-013/p08-native-entry-local-20261101/source/native_child.mjs` | pass existing payment composition as the explicit hook | `0d1241a397de199a3ee5783a81c5c752c473e7e47f84f5cbfc13870a10851e6c` |
| `evidence/APP-013/p08-native-entry-local-20261101/source/test_entry.py` | actual child/journal/parent/payment boundary regressions | `14efc086685dbc139475839f86e70f1a1da4f100bda29cac86b4a9f7af376c7b` |

Refresh derived hashes only in these eight current manifests:

1. `p08-real-client-binding-local-20261031/source/source-manifest.json`
2. `p08-native-entry-local-20261101/source/source-manifest.json`
3. `p08-native-entry-local-20261101/source/test-manifest.json`
4. `p08-key-correction-20261110/source-manifest.json`
5. `p08-connected-packet-20261110/iq1-source-manifest.json`
6. `p08-connected-packet-20261110/sq1-source-manifest.json`
7. `p08-connected-packet-20261110/account-containment-source-manifest.json`
8. `p08-connected-packet-20261110/account-containment-read-source-manifest.json`

The dated EC1/RV1 audits, R59 readiness, R64/R65 receipts, prior source locks and immutable evidence may contain historical hashes and must not be rewritten. An additional source/test/manifest requirement stops implementation for a new scope decision.

## Required synthetic proof after approval

1. Existing auth-only and connected success paths remain unchanged: one issuance, one runtime authentication, one payment composition, existing account/session readback, payment containment and exact parent proof.
2. Token issuance and each existing runtime-authentication refusal remain pre-payment, `authenticated=false`, with no payment bootstrap/mutation and unchanged safe diagnostics.
3. Injected payment-handoff refusal after successful runtime authentication retains only the new finite phase boundary plus existing safe payment journal fields; it records no body, token, URL, identifier, arbitrary error or private canary.
4. Lost output, timeout, process exit, interruption and merge drift at `PAYMENT_HANDOFF_INTENT` may preserve the child intent but cannot set `authProofAccepted`, populate the proof digest or clear uncertainty without the existing exact returned result and parent readbacks.
5. No second issuance, authentication, payment handoff or child dispatch; unchanged deadlines, call ceilings, endpoint cleanup, session closeout, private purge and independent readbacks.
6. Run direct Node/Python suites for the six files, the full applicable native and connected packet suites, current source guards, architecture, frozen baseline, complete cross-repository consistency, all 25 governance safeguards and both whitespace checks. Build, lint, Prisma, database integration and browser QA are inapplicable unless the approved implementation expands into their product/runtime surfaces; such expansion is not authorized here.

## Authority, exclusions and next decision

The implementer owns the exact local change, tests, derived current hashes, evidence and review only after approval. The product owner decides the AP1 local semantic change. Cloud, database, credential and Stripe custodians retain all external decisions. No attendance or deadline is needed for local implementation.

Preparation validation completed against the unchanged backend4e29a91 at 2026-11-27T10:06:16Z: 10 real-client Node tests, 19 real-client Python tests and 8 native boundary tests passed (37 focused synthetic tests); frozen baseline, complete cross-repository consistency, all 25 governance safeguards, backend governance wrapper, architecture, JSON and both whitespace checks passed. Build, lint, Prisma, database integration and browser QA were inapplicable because no product/runtime/schema/UI file changed. No external transport or credential was used.

The smallest decision is: **approve or decline AP1’s six-file local authentication/payment-boundary separation, direct tests and eight derived current-manifest updates exactly as specified.** Approval would not authorize a provider read, sign-in, credential/cache access, database fixture, payment, replay, browser opening, mutation, deployment or new attended session.

Observable finish after approval is a locally verified distinction between runtime authentication and payment handoff while preserving conservative parent proof and all existing acceptance gates. R65 stays immutable. Accepted 4/8; Section 3A OPEN; R1 newly closed 0/27. Overall CallDesk/MVP completion and ETA remain unvalidated. No scope deviation implemented; AP1 is a prospective bounded correction requiring owner approval.

# EC1 — correct the custom-token exchange response contract

## Owner decision — approved local implementation, November 24

Owner replied **“Approve EC1 local correction and tests”** to the exact prepared review at governance c91285a. This direct decision authorizes the finite correction, fixture/test updates and derived references specified below; it grants no live authority. The proposal's original pending language is retained as review history and is superseded by this recorded decision. Backend base f675067 contains only the read-only review added after runtime 9f5f5bf. The 18-file pre-edit inventory is APP013_P08_EC1_SOURCE_INVENTORY_20261124.json. Frozen-baseline and complete consistency checks pass before coding; unrelated owner edits and renewal files are preserved.

Implementation uses this complete card and its six-item checklist. Root implements the exact client predicate/guard, direct client tests and all hash refreshes. Delegated implementation is limited to the two specified synthetic response producers and native test_entry.py. Independent review and all applicable local verification precede completion. No scope deviation beyond approved EC1.

**Decision requested: local correction and tests only. No implementation or live action is authorized by this proposal.** APP-013 / 3A / P08 remains the same admitted-job Sandbox payment journey; EC1 is an internal correction, not a new acceptance section. Source: backend `9f5f5bfb3379343b1a9ff20480371fe6fd1582d9`; governance checkpoint `f474fed59f9c4ccc213106ddbdfc4f488009ba86`. Reviewed November 24, 2026.

## Demonstrated gap and customer acceptance

The existing custom-token exchange requires `v.localId === s.id`. Google's current [endpoint reference](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithCustomToken) does not include localId in its successful response schema. The [Firebase REST guide](https://firebase.google.com/docs/reference/rest/auth#section-sign-in-with-custom-token) agrees. Current synthetic success responses in test_client.mjs, bound-child.mjs and fixture_ports.mjs supply that undocumented field, concealing this compatibility gap.

The unchanged actual native child reproduces the defect with two separate synthetic operations: its existing fixture authenticates; a documented response without localId stops at EXCHANGE / RESPONSE_VALIDATION / EXCHANGE_RESPONSE_MISMATCH before the protected job read. Both close cleanly, refuse second dispatch and remove fixture inputs. Backend evidence: `evidence/APP-013/p08-connected-packet-20261110/ec1-contract-review-20261124/{review.md,reproduction.json,reproduction-script.txt,source-review.json}`. No account API, credential, browser or real database was used. Public documentation was consulted. This demonstrates a current contract defect, not the exact discarded R56 response or historical authentication outcome.

The unchanged 3A acceptance criterion requires the same admitted job's authorized Sandbox payment, authentic matching signed event and cleared payment gate, with independent closeout and owner acceptance. This correction removes a demonstrated pre-payment response rejection; it does not accept payment or establish current provider usability.

## Exact proposed behavior

Change only the exchange acceptance predicate in current client.mjs to:

```js
(v.localId === undefined || v.localId === s.id) &&
typeof v.idToken === 'string' &&
v.idToken.length > 0
```

Absence is accepted because it matches the documented contract. A present foreign, null or nonstring localId still refuses. The nonempty-token requirement moves an existing downstream refusal earlier; empty tokens cannot become usable. Preserve localId-first short-circuit ordering, EXCHANGE_IDENTITY_DRIFT and RV1's EXCHANGE_RESPONSE_MISMATCH. Do not use or retain refreshToken, expiresIn or isNewUser for new behavior.

Update authority.mjs's exact transformed-source comparison for this one approved semantic change; preserve the historical source and full equality guard. Make current success fixtures omit localId and represent the documented response shape. Keep lookup/update responses with their existing localId fields; those are different API contracts.

Leave authenticate() unchanged: require the exact in-memory issued token, current exact Firebase identity and claims, reject mismatched token sub/tenant/role/testOnly/issuer/audience/time, then perform the existing protected exact-job GET. Decoding remains rejection-only. RequestAuthGuard verifies the Firebase token with revocation checking; native_child awaits authentication before entering payment. The safe journal and parent merge remain unchanged, as do success-only proof/digest rules and AUTH_OUTCOME_UNKNOWN on unproven outcomes.

## Exact change inventory and reused components

All paths below are under backend `evidence/APP-013/`.

| Role | Existing files |
| --- | --- |
| Runtime predicate and exact guard | p08-coordinator-auth-local-20261031/source/client.mjs; authority.mjs |
| Current synthetic response producers only | p08-real-client-binding-local-20261031/source/bound-child.mjs; p08-native-entry-local-20261101/source/fixture_ports.mjs |
| Direct regression tests | p08-coordinator-auth-local-20261031/source/test_client.mjs; p08-native-entry-local-20261101/source/test_entry.py |
| Derived embedded hash references only | p08-serialized-handoff-local-20261031/source/handoff.py; p08-real-client-binding-local-20261031/source/bound_handoff.py |
| Current JSON hash references only | coordinator-auth, serialized-handoff and real-client source/source-manifest.json; native-entry source/source-manifest.json and test-manifest.json; p08-key-correction-20261110/source-manifest.json; connected-packet iq1-source-manifest.json, sq1-source-manifest.json, account-containment-source-manifest.json and account-containment-read-source-manifest.json |

The abbreviated directory names in the final row are the existing dated directories named in the rows above; connected-packet is p08-connected-packet-20261110. Expected total: 18 current source/test/reference files. Inventory actual hashes before edits and refresh topologically. Do not change manifest keys, purpose, status, baselineCommit, SDK pins or immutable historical receipts. The newly affected fixture hashes were traced to these same current manifests. No new runtime component, endpoint, transport, verifier, credential store, dependency, schema or UI.

## State, identity, retention and recovery boundaries

Existing response text and ID token stay within existing in-memory clients. Retain only RV1's literal safe failure fields. Never log the returned ID/refresh token or payload. No custom signature verifier or new identity lookup is added. Existing operation/tenant/job identity, exact supplied token, disabled/enabled account transition, session ownership, journal version/drift checks, no-retry controls, call ceilings, time cutoffs, final readbacks and independent purge remain intact. Rejected tokens never reach payment or become accepted authentication proof. Rollback restores only the EC1 delta and derived pins; external authority remains disabled. R56 evidence is immutable.

## Finite implementation checklist, conditional on approval

1. Record owner decision and source/hash inventory in this card before implementation; confirm no unrelated changes are staged.
2. Apply the exact predicate/guard change and only the two current fixture response changes above.
3. Add direct regressions through the actual client and actual child/journal/parent path. Positive: documented response omitting localId, matching optional localId, valid exact account/claims/time and successful protected job read. Negative: present foreign/null/nonstring localId; missing/null/nonstring/empty idToken; wrong sub, tenant, role, testOnly, issuer, audience, future iat and expired exp; runtime 401/403 and wrong-job response. A matching optional localId must not rescue a wrong token identity. All authentication failures must prevent payment and proof acceptance.
4. Preserve private-value exclusion, no second issuance/dispatch, lost output/timeout/interruption and concurrent journal/parent drift, independent cleanup and success-only digest tests. Refresh exact current references and verify no historical/R56 change.
5. Run the existing relevant complete local suites: coordinator `node --test test_client.mjs`; real-client `node --test test_bound.mjs` and `python3 -B -m unittest test_bound`; native `node --test test_connected_payment.mjs test_transports.mjs` and `python3 -B -m unittest test_entry test_child_cleanup test_key_lifecycle test_private_inventory_cc1`; all applicable connected tests. Exclude the same explicitly inapplicable five CT3DisposableTLS and two browser-launch cases identified in RV1; no silent skip. Native test_native_postgres.py is inapplicable. Existing guards, architecture, backend governance, frozen baseline, full consistency, 25 governance tests and both whitespace checks are required. Host process/loopback permissions may be needed; all account/provider transports stay injected. No compiled application/schema/UI change means app build/lint/database/browser gates are not claimed as newly run.
6. Obtain independent review, retain exact source-bound results, and update the canonical handoff. Stop at local verification; prepare no live attempt while local prerequisites remain unresolved.

## Shift-left readiness record

| Prerequisite | Inspected evidence / timestamp | Result and owner |
| --- | --- | --- |
| Exact response schema, missing/null fields, parsing and safe diagnostic | Public endpoint references and source-review.json; 2026-11-24; unchanged actual native child reproduction | FAIL: undocumented required localId; implementer owns the proposed correction; owner approves this changed predicate |
| Identity and authentication before payment | client.mjs:16–19; recovery-sequence.mjs:79–82; native_child.mjs:154–163; operator-bridge.mjs:695–704; registered JobsController and RequestAuthGuard | Existing chain inspected, no bypass proposed. New positive/negative regressions PENDING approval/implementation; implementer |
| Source/hash/config/resource pins and dynamic interfaces | Committed RV1 audit at 9f5f5bf; existing manifest guards; new fixture reference inventory | Current code/guards locally verified; manifests must be refreshed after EC1. Current credentials, effective provider permissions, APIs and key compatibility UNKNOWN; owner/cloud custodians retain external decisions |
| Deadlines, no retry, concurrency, interruption and independent closure | RV1's source-bound 696 local tests and current two-case child probe | Historical/current local evidence only; EC1 regression results PENDING. Live resource restoration/current account state UNKNOWN; implementer and relevant custodian |
| Checklist, data custody, exclusions, dependencies and next result | This proposal and source-bound reproduction; 2026-11-24 | No implementation yet. Next observable result after approval is a documented-shape response passing existing authentication safeguards under injection, with invalid identity still refused and cleanup intact |

The readiness result is **BLOCKED_ON_LOCAL_CONTRACT_CORRECTION**, not qualification-only or execution-ready. Do not request attendance or schedule another payment run before resolving this locally discoverable mismatch. RV1 is complete and remains diagnostic-only; EC1 changes a response predicate and therefore needs a new owner decision under the repository's explicit change-control rule.

## Alternatives, impact and exact decision

Keeping the predicate and running again risks the same documented-shape rejection; it is not justified while this defect is reproducible locally. Replacing the auth SDK or adding a new verifier would materially expand scope. The bounded correction above reuses all existing authentication and cleanup controls. It changes no section IDs, criteria, order, dependencies or acceptance denominator. Effort is limited to two runtime/guard files, two synthetic response producers, two direct test files and derived pins; no completion-time promise.

Approve **EC1 local exchange-contract correction, current fixture updates, tests and required derived references as specified here**. This authorizes no credential/cache read, sign-in, provider account API, IAM/configuration change, payment, deployment, support contact or new attended session. No Terminal attendance or deadline is needed. Product owner decides the changed response predicate; implementer owns verification; cloud/database/Stripe custodians retain any later live decision.

Accepted 1A/1B/2A/2B stay 4/8; 3A OPEN; R1 newly closed 0/27. R56's precise historical response/authentication event stays UNKNOWN. No scope deviation performed; EC1 is an explicit prospective correction awaiting owner approval.

Review closeout: backend evidence committed as f675067; the installed runtime remains exactly the reviewed 9f5f5bf source. Both actual-child reproduction cases, frozen baseline, complete cross-repository consistency, backend governance, architecture, 25 governance tests and whitespace checks pass. Independent final proposal review found no scope/readiness defect. No correction is implemented and no owner decision is inferred from preparation.

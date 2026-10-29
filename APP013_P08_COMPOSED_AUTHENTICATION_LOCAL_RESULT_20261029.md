# APP-013 / 3A / P08 — composed authentication local result

R1-W01 / APP-013 / 3A / P08. Owner approved the bounded local prerequisite against governance proposal commit `d7f0ed2`, proposal SHA256 `5009670c7a7bb3284a8c2a99c79eeebf1381fb131f874cc3271aa5564aa9c43f`, and approval commit `8082d44`. Backend evidence is committed at `514bc8c` under `evidence/APP-013/p08-composed-authentication-local-20261029/`.

## Completed locally

The fresh disabled composition model verifies all five locked source hashes, pins the two R06-verified role IDs and one-permission scopes, binds one exact owner-approved parent authority, and permits child authority only as a strict projection of that parent plus an exact provider-owned key receipt and in-memory key hash. It cannot create a child owner decision or broaden actions. The old restoration, access-resolution and authentication sources remain byte-for-byte unchanged.

The model proves the intended order and reverse cleanup with injected transports: qualify -> confirm key absence/service already enabled -> create/read exact owned key -> retrieve/hash key in memory -> bind lookup/signing roles -> restore -> authenticate exact operator/job -> close authentication -> retire runtime -> unbind signing/lookup -> delete/read back owned key. Native entry verifies source locks and returns `P08_COMPOSED_AUTH_REFUSED_UNBOUND`; no credential resolver or provider transport exists.

Two safety gaps were found and corrected before any external action. First, cleanup initially could attempt key deletion after an unacknowledged creation response; deletion now requires acknowledged exact ownership, while unknown creation remains an explicit residual and is never adopted or deleted. Second, the locked key-lifecycle source uses the provider's canonical numeric project resource while the older authentication authority allowed only the project alias. The new wrapper binds the exact private project number and provider-returned canonical resource; locked sources were not rewritten.

Final verification passed: 17 new composed cases, 31 unchanged restoration cases, 40 unchanged access-resolution cases and 60 unchanged authentication cases. The unchanged authentication test uses URL pathname text and cannot resolve the checkout path containing spaces, so its exact locked snapshot was copied to a private no-space scratch directory, all 60 cases passed, and the scratch directory was deleted with absence verification. Backend governance baseline, architecture and whitespace checks passed; governance frozen baseline, cross-repository consistency, 25 safeguards and whitespace passed. Initial failures and corrections are retained in `local-result.json`.

## Boundaries and remaining work

No real credential resolution, provider/database/Firebase/IAM/API-key/signing/token/runtime/Stripe/payment/deployment/billing action occurred. No product source, UI, schema, SQL, dependency or locked historical source changed. Passing local tests does not complete P08, 3A or a customer payment capability.

Current API states, exact lifecycle permissions, canonical project number, target account/job/operator state, runtime state, allowance, private plans and operation window remain unqualified. API enablement is not approved. Control-plane key deletion would not prove immediate global invalidation or permanent erasure. The stable roles remain retained unbound.

Next/implementer: prepare one bounded current-state qualification card that reuses existing read-only seams and covers the exact Cloud service/permission/resource facts plus the exact owned disabled account/job/operator facts required by the composed parent. Keep reads and any later mutation operation separate. Do not create a key, bind roles, activate an account, restore runtime, sign/exchange a token or touch Stripe/payment under this local result.

Accepted 1A/1B/2A/2B remain 4/8. Newly closed R1 remains 0/27, legacy remains 6/60, intelligence remains 0/13. Stable-role and local-composition prerequisites are complete; P08 and 3A remain open. **No scope deviation within the owner-approved local prerequisite.**

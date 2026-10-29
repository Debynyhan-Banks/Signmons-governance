# APP-013 / 3A / P08 — composed restoration and authentication preparation proposal

Status: PROPOSED; owner decision required before local implementation. Backend source `caa5a2d809a10cfb6ef0cc0d2a2af0a65c4b3926`; governance source `f0da7ca7742a4386da1fb4150c7385ca1df0b220`. This proposal prepares one disabled local coordinator only. It does not authorize a provider read or mutation, IAM binding, account activation, token, runtime restoration, Stripe action, payment, deployment, spending, or attended window.

## Approved section and connected acceptance

Section is R1-W01 / APP-013 / 3A / P08. The unchanged 3A criterion requires the admitted job to traverse the existing payment request and Checkout path, consume an authentic matching Stripe Sandbox event, clear the payment gate, and preserve duplicate, out-of-order, forged, foreign, failed and lost-response safety. P08 is the existing operator-authentication prerequisite for that same-job supervisor journey. This proposal adds no section, feature, acceptance criterion, dependency, denominator or payment behavior.

The customer-workflow connection remains: admitted job -> authenticated exact test operator -> reviewed same-job payment request -> Sandbox settlement -> gate-cleared evidence. The proposed work only completes the bounded authentication access envelope needed to reach the already-built payment supervisor. Passing local tests will not complete P08 or 3A.

## Verified source and demonstrated missing behavior

R06 operation `e9124155-47a9-4478-a8de-3e435d67459a` returned `P08_EXACT_ROLE_CLOSEOUT_VERIFIED`. These exact stable roles exist, match their one-permission definitions, and are retained unbound:

- `projects/signmons/roles/signmonsP08FirebaseUserLookup` -> `firebaseauth.users.get`
- `projects/signmons/roles/signmonsP08ServiceAccountSignBlob` -> `iam.serviceAccounts.signBlob`

Existing restoration source `evidence/APP-013/p08-restoration-local-20261028/source/restore.py`, SHA256 `a0bf4bc90cca0bd52935915d710ccb44e065dd3deed841a12ab49cb3ac4a1cb9`, already supports preexisting exact lookup/signing roles, time-bounded conditions, exact readback, reverse removal, independent closeout and the existing authentication child. It refuses role creation. No new IAM subsystem is needed.

Existing access source `evidence/APP-013/p08-access-resolution-local-20261028/source/access_readiness.py`, SHA256 `d54334352529e3aa4d3717be6b1c6f840ec284d3b83a9a3aaeb5053fa7547576`, models the exact API-only temporary-key create/read/delete lifecycle, collision refusal, long-running-operation readback, diagnostics, deadlines, signals and truthful unknown outcomes. Its native entry intentionally returns `P08_ACCESS_REFUSED_UNBOUND`; it has fake transport only and is not coordinated with restoration.

Existing authentication sources are locked at authority `51c5250ace4ff095a7cc2e5b6f4e099a863389fa095c2bfe26151c832480d965`, controller `57ab0853630112145e81e10143b05099b2a446f7f450d0eff4598540528ef0c4`, and adapters `ee4906f969ae40e40b4c4a066829afc63257c62a8e9e60fcdbc1ea376b91855a`. They require an exact `keyResource` and `keySha256` inside an authentication plan whose full hash is already bound to an exact owner approval. For a newly created temporary key, `keySha256` cannot be known before provider creation and authorized key-string retrieval. The restoration plan also requires the already-final authentication-plan hash. The currently tested pieces therefore cannot form one truthful same-block operation: fabricating the hash is invalid, self-signing a generated child approval is forbidden, and creating a key for a later approval would retain a live credential between operations.

This is inspected missing behavior, not inferred scope. The exact roles resolve the stable-role prerequisite; they do not resolve the dynamic key-to-owner-authority binding.

## Alternatives and recommendation

1. **Recommended — one local-only composed authority and coordinator.** Reuse the three locked implementations in a fresh disabled snapshot. Bind the owner to one immutable parent operation containing the exact deterministic key resource, exact role IDs/permissions/scopes, exact account/job/tenant/runtime, source hashes, window, allowance, action ceilings and retention. During a later separately approved execution, derive the child authentication capability only from that parent plus exact provider-owned key readback; hold the key string and its hash in memory, never create a child owner decision, and retire the key and all temporary bindings in the same closeout.
2. Create the compatible key first, save its hash, and request a second owner approval for authentication. This avoids changing the authority interface but leaves a live key between approvals and adds another time-sensitive operation. It conflicts with the previously accepted same-block retention boundary and is not recommended.
3. Use an owner-designated existing compatible key. None is currently qualified. A future exact read could establish one, but no listing, lookup, restriction change or adoption is authorized here.
4. Defer P08. Stable roles remain unbound and no runtime/payment action occurs.

Alternative 1 is a material operational-prerequisite change and therefore needs owner approval before implementation. It does not change product architecture or application authentication; it composes existing guarded seams and replaces the impossible pre-known dynamic hash with a parent-authority derivation contract.

## Exact intended local behavior and interfaces

Prepare a fresh disabled evidence-contained coordinator and tests. Do not edit backend `src/`, UI, schema, migrations, packages, current locked evidence, or the unrelated backend `AGENTS.md` change. The proposed coordinator will:

1. Verify byte hashes for the locked restoration, access-resolution and authentication sources before loading them.
2. Accept only a synthetic local parent plan in tests. A future real plan format must bind one UUID operation, the existing job `9180bef4-561d-47a0-869f-925e6a3dfd96`, tenant `a1adcfd4-15be-404b-9ac3-5edb1fda20f0`, owner principal, dedicated P07 runtime identity, exact disabled test account ownership receipt, exact candidate source/image/environment, both exact role IDs, the exact temporary key ID derived from the operation, exact API-only Identity Toolkit restriction, one <=60-minute window, no retry, allowance, source manifest and proposal hash.
3. Qualify the current resources before mutation in a later operation: roles exact and initially unbound; target account disabled/owned; job/policy/operator exact; runtime/traffic/identity retired; required APIs and effective lifecycle permissions exact; deterministic key absent; no active sessions or stale private plan. UNKNOWN stops.
4. Model this future order: exact key absence -> optional separately approved API Keys service enable/readback -> owned key create/readback -> key-string retrieval in memory -> hash -> derive child authentication capability from the already-approved parent -> conditional role bindings -> restore existing runtime resources -> activate/authenticate/read exact job -> disable/revoke account -> retire runtime -> remove both conditional bindings -> delete/read back owned key -> purge private metadata.
5. Never write or print OAuth tokens, database passwords, key strings, key hashes linked to resource IDs, user tokens, raw policies, private account data or raw provider errors. Only sanitized fixed states, counts, digests without source identifiers, mutation receipts and residual categories may persist.
6. Maintain one exclusive attempt, no mutation retry, live wall-clock deadlines, SIGINT/SIGTERM cleanup, reverse-order retirement, exact ownership/etag/version checks, and one separately authorized closeout-only mode that cannot create, enable, bind, restore, activate, sign or exchange.
7. Return success only when authentication proof is exact, account is disabled/revoked, runtime is retired, both role bindings are absent, the temporary key is control-plane deleted, sessions/private inputs are absent and every child process is closed. Any lost response or late mutation remains UNKNOWN/containment-unconfirmed.

The parent authority must make derivation auditable: child fields are a strict projection of the parent plus provider-returned key UID/etag/hash; any other field or changed source/window/identity/resource refuses. A derived child capability is not an owner approval and cannot authorize an action absent from the parent. Tests must prove that the coordinator cannot manufacture broader authority.

## State, identity, data and retention boundaries

- Exact principals: owner `debynyhan@signmons.com`, dedicated runtime `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com`, and the previously created disabled test administrator identified only through its private ownership receipt.
- Lookup role scope is project `signmons` to the dedicated runtime identity; signing role scope is the exact dedicated service account to the owner. Both use the parent window's start/work-end condition and are removed with absence readback.
- Temporary key is a fresh deterministic operation-owned resource under `projects/signmons/locations/global/keys/`, restricted only to `identitytoolkit.googleapis.com`, never adopted, listed, undeleted or shared.
- API enablement remains a separate future owner decision. Local work may model retained-enabled state but cannot assert current state, zero cost or consumer safety.
- Real private plans, approval receipts and provider-derived metadata must be mode 0600, nonsymlink, absolute-purpose files with same-block purge and absence readback. No overnight ready credential or private-plan retention.
- Stable custom roles remain retained unbound after closeout; deleting them is outside this card. Shared browser keys and normal production traffic remain untouched.

## Finite local implementation checklist

- [ ] Create a new private disabled source snapshot and manifest; reverify all five locked source hashes and R06 sanitized role evidence without opening raw historical provider output.
- [ ] Implement the parent-authority schema and strict parent-to-child derivation as a wrapper around existing modules. Preserve the original modules byte-for-byte.
- [ ] Add the coordinator state machine using injected provider/database/auth transports. Native execution must refuse before credential resolution unless a future exact plan, proposal, owner approval, qualification, window and allowance are present.
- [ ] Pin both verified role IDs and exact scopes/conditions; prove no role-create/update/delete path exists.
- [ ] Compose existing temporary-key, restoration and authentication operations in the specified order with reverse cleanup and one read-only/cleanup-only recovery interface.
- [ ] Produce sanitized local evidence with source manifest, exact commands, original failures, final results, limitations and no readiness/acceptance claim.
- [ ] Stop after local proof. Present current-state qualification and any real operation as separate exact proposals.

## Required verification

Positive tests: exact parent authorization; exact provider-owned key receipt and in-memory hash derivation; exact child projection; both conditional grants; restore/authenticate/read/disable/revoke; reverse retirement; role absence; key deletion; private purge; fixed sanitized success.

Negative/security tests: changed parent/child plan; self-issued child approval; wrong/extra role or permission; broad scope; missing/duplicate binding; collision/foreign key/UID/etag; changed restrictions; key hash mismatch; target/job/tenant/account/runtime drift; non-disabled account; unauthorized service enable; raw secret/error persistence; symlink/mode/path violation; forged/foreign token; unpaid/foreign job; wrong runtime origin; omitted provider fields; malformed/null outputs.

Concurrency/recovery tests: two-process reservation; SIGINT/SIGTERM before and after every modeled mutation acknowledgment; response loss for enable/create/bind/restore/activate/sign/exchange/disable/unbind/delete; deadline and clock rollback; late provider completion; cleanup partial failure; independent closeout that performs no forward action. Mutation counts must prove no retry.

Integration tests: exact serialized CLI/HTTPS/SQL/child-process contracts with fakes; existing restoration and authentication suites freshly rerun unchanged; disposable PostgreSQL only where the reused account/role SQL path requires it; isolated loopback browser proof only if the composed authenticated supervisor UI is actually changed, otherwise no browser claim. No live credential, provider, Firebase, Stripe or payment traffic.

Repository checks: backend governance baseline, relevant focused/full tests, architecture and `git diff --check`; governance frozen baseline, consistency, three safeguard test files and `git diff --check`. A failing baseline is a stop.

## Dependencies, exclusions, rollback and observable finish

Implementer owns local composition and evidence. Owner decides this material prerequisite before implementation and separately decides any later read, API enablement, IAM binding, key creation, account activation, runtime restoration, Stripe action, allowance and attended window. Google Cloud remains the authority for resource state; Stripe remains outside this card.

Excluded: role creation/update/deletion, broad discovery, production login redesign, persistent key, shared-key changes, new database role/schema, application feature changes, deployment, billing change, real payment, booking, customer communication, merge or push.

Local rollback is deletion of the fresh uncommitted snapshot or a normal revert of its isolated commit; original locked sources remain unchanged. A later external closeout would remove only operation-owned bindings/resources and restore the pre-operation disabled/retired state while retaining the two exact stable roles unbound.

Observable local finish: all finite tests and repository gates pass; native launch returns a fixed unbound/refused status without credentials; manifests prove original sources unchanged; no real plan/approval/qualification exists; zero external calls/actions; sanitized result explicitly states P08 and 3A remain open. Then the next card is a bounded current-state qualification, followed by a separately approved exact composed operation only if every prerequisite passes.

## Decision requested

Approve Alternative 1 for bounded local composition and isolated tests only, or defer. Approval would authorize only the new disabled snapshot, wrapper/coordinator, tests and sanitized local evidence described above. It would authorize no provider read or change, IAM binding, API enablement, key action, account activation, database action, token/signing/exchange, runtime restoration, Stripe/payment, deployment, spending, attended window, merge or push.

Accepted 1A/1B/2A/2B remain 4/8. Newly closed R1 remains 0/27, legacy remains 6/60, intelligence remains 0/13. Stable-role prerequisite is complete; P08 and 3A remain open. **Explicit prerequisite change proposed before implementation; no scope deviation implemented.**

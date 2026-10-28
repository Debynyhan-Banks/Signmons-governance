# APP-013 / 3A / P08 — exact custom-role creation and lifecycle proposal

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated gap and dependency impact

Approved R04 operation `67b2421f-2580-4b49-b551-ce3bc805edd3` completed once at 7:00 p.m. Eastern. Sanitized result: one project custom role, one excluded, zero eligible exact candidates for both `firebaseauth.users.get` and `iam.serviceAccounts.signBlob`; private inputs absent; no raw output/bearer or mutation. Backend evidence: `evidence/APP-013/p08-role-inventory-r04-result-20261028/`.

The existing restoration controller accepts only preexisting exact roles and refuses creation with `ROLE_CREATION_NOT_BOUND`. Stage A separately demonstrated that the dedicated runtime cannot `firebaseauth.users.get` and the owner cannot `iam.serviceAccounts.signBlob` on the exact dedicated runtime identity. This is a material prerequisite change, so it requires an owner decision before implementation. It adds no walkthrough section, acceptance criterion or denominator; it adds one bounded operational helper before the existing restoration operation.

Google documents that deleted custom roles remain recoverable for 7 days and permanent deletion can take weeks; role IDs cannot be reused until deletion completes: <https://docs.cloud.google.com/iam/docs/creating-custom-roles> and <https://docs.cloud.google.com/iam/docs/roles-overview>. Deleting newly created roles after every operation therefore creates retained provider state without a reliable same-block absence result.

## Alternative 1 — recommended stable unbound exact roles

Prepare locally, with fake providers and no credentials/network, one disabled exact-role provisioning and verification helper for these proposed project roles:

| Role ID | Stage | Exact permission | Outside-operation state |
|---|---|---|---|
| `signmonsP08FirebaseUserLookup` | GA | `firebaseauth.users.get` | retained, no bindings |
| `signmonsP08ServiceAccountSignBlob` | GA | `iam.serviceAccounts.signBlob` | retained, no bindings |

The later separately approved external operation would:

1. verify owner/project, IAM API state and exact create/get permissions;
2. refuse any ID collision rather than update, undelete or adopt an existing role;
3. create each role with exactly one permission, fixed title/description and GA stage;
4. read back exact name, permission, stage, deleted state and definition hash;
5. verify neither role appears in the project policy or dedicated service-account policy;
6. retain both unbound roles for reuse by the existing restoration controller.

The roles themselves grant no access while unbound. A future attended restoration operation may add only the already modeled absolute-time conditional bindings and must remove/read back those bindings in the same block. `firebaseauth.users.get` is project-wide while bound; it is not restricted to one UID. `iam.serviceAccounts.signBlob` can sign arbitrary blobs/JWTs while bound, although its policy is attached only to the exact dedicated service account. No broad Firebase role, Token Creator role, service-account key, delegation or extra permission.

Local preparation must prove exact serialized create/describe/policy-read contracts, two-role command ceiling, collision/partial-create/lost-response handling, ownership journal, no-update/undelete/delete behavior, definition drift refusal, signals/deadlines/concurrency, sanitized evidence and independent closeout. Partial creation is reported truthfully; local preparation must not pretend cross-resource atomicity. The helper remains disabled and unbound without a future exact plan/approval.

Role creation, policy reads, provider credentials and all bindings are excluded from this local approval and require a later exact external proposal. The existing restoration controller remains unchanged until both roles are externally created and qualified as preexisting exact roles.

## Alternative 2 — create then delete per operation

Prepare per-operation role creation and deletion. Not recommended because deletion is soft for 7 days, permanent deletion can take weeks, role IDs are not immediately reusable, and same-block resource absence cannot be claimed.

## Alternative 3 — stop

Do not create roles. Stage A access resolution and the same-job Sandbox payment proof remain blocked.

## Scope, effort and decision

Expected local change: one evidence-only helper/test pair plus manifest/result documentation; no `src/`, UI, schema, migration, package or product interface change. Required tests are finite and listed above. No provider call, role, grant, account/database/token/runtime/Stripe/payment action, spending, merge, push or deployment is included.

Owner decision requested: approve Alternative 1 for bounded local preparation and isolated tests only, choose Alternative 2, or choose Alternative 3. A later role-creation operation and later restoration/payment operations remain separately approved. Accepted counts remain unchanged. **Proposed prerequisite change disclosed before implementation; no scope deviation implemented.**

# APP-013 / 3A / P08 — real-client and interrupted-closeout binding decision

## Current criterion and demonstrated gap

R1-W01 / APP-013 / 3A remains the approved same-admitted-job Stripe Sandbox Checkout and matching signed-settlement/failure/replay criterion in `APP013_REMAINING_EXECUTION_CONTRACT.md`. Accepted walkthrough 4/8 and R1 newly closed 0/27 do not change. Owner-approved backend `2c14876` locally proved one serialized Python-to-JavaScript attempt and journal with **fake** database, Firebase, signer/exchange and session clients. `liveAuthorization:false` and `authProofReady:false` are correct. R10 and earlier external operation authority are consumed.

Source inspection at backend `2c14876`:

| Existing source | Pinned SHA256 | Reusable behavior / exact limit |
| --- | --- | --- |
| Historical `auth-launch.mjs` | `180346d1874efa61986ea79575407af8669e940ec076639f828bbf2b65c0516a` | `realClients` implements owner OAuth, CHILD TLS/tenant preflight, bounded database session and closeout probe, but requires the **historical** auth capability/plan and `runLaunch` owns a second attempt/journal. It cannot be called as-is. |
| Historical `auth-adapters.mjs` | `ee4906f969ae40e40b4c4a066829afc63257c62a8e9e60fcdbc1ea376b91855a` | Exact User SQL, Firebase enable/disable/revoke, token sign/exchange and authenticated exact-job read are reusable contracts; the factory has implicit `fetch` and the old gate. |
| Extracted `client.mjs` / coordinator `authority.mjs` | `0ae21eed01f6d0af2fc5497e825f9c05a5ecd3a0f75476616b04d81054d589c9` / `0bcd2c7b86cfd98a77bcedb86b5d02735a8bc148f040d4d53d3d80b8e00a9aa5` | Client operations now require injected transport and one coordinator capability. The capability does not carry historical `p.database`/credential fields; exact, private database binding is still undefined. |
| `sequence.mjs` | `cf8e1d6a7143874871fdf602afc1e8e9bf6afb51724c587d3eef1eb59d792f9c` | Same-journal activation/authentication/cleanup. If interrupted after `CLOSEOUT_INTENT`, `closeout(true)` currently refuses because `closeoutAttempted` is already true. A live recovery guarantee is therefore unproved. |
| `child.mjs` / `handoff.py` | `0cc64f264663eb9a8a9d21617ff98974643ceb2b2b2b4e5f5d1548691cb84186` / `5c8c1be27f6056db550045a66cdb470e353afb86ee7d0e81a11c37f5a028809e` | Local child accepts only `--fixture-auth`/`--fixture-closeout`, synthetic clients and a bounded same-journal result. No credential resolution, real transport or native entry. The temporary owned-key receipt is purged after the one cleanup-only invocation, even if cleanup remains unconfirmed. |
| Python `adapter.py` / `coordinator.py` | `c463671302f8d858d51063e94d7baaa6c0c72a395f505f5fa0a502674d8e532c` / `1eecc5241794cfed6d892db4385039274539e47b183f1d934899549eb5560f70` | Derived account/Firebase/session and runtime readbacks exist behind injected interfaces; no native factory supplies the actual account/session/private-root observations. |

These are implementation gaps, not a new customer feature. The historical auth private root, the coordinator root and any future credential/plan root cannot be treated as absent from a fake readback. A Firebase Console project owner is not automatically an ACTIVE Signmons application operator; the earlier exact-tenant diagnostic found zero eligible ACTIVE OWNER/ADMIN rows before the separate disabled test account was created.

## Recommended Alternative 1 — one bounded disabled local binding card

Approve **local implementation and isolated tests only** in a fresh disabled copy. Keep the existing Python coordinator as the sole attempt, approval and journal owner. Extract or adapt the existing `realClients` primitives behind the coordinator capability; do not invoke historical `runLaunch`, create an auth plan/attempt/journal, or bypass either gate. Source-lock the historical SQL, Firebase, sign/exchange, authenticated-job and session-closeout contracts. Require explicit injected transports in tests and leave native resolution disabled. No real credentials or provider/database call in this card.

The finite card must include:

1. **Exact private binding:** source-pinned plan schema for the approved CHILD host/port/database/user and project/tenant/job/test ADMIN identity; no password, bearer, key string or ID token in the plan, journal, stdout or evidence. A later owner-only hidden input can supply the current CHILD administrator password to a bounded child process, and existing owner OAuth can supply a memory-only bearer, but neither may be resolved in this local card. No fallback to inherited `DATABASE_URL`, `PG*`, ADC or ambient `fetch`.
2. **One capability and one operation:** new factory accepts only the coordinator capability, exact owned-key receipt and allowlisted transport seams. All live methods recheck work/cleanup deadlines and source/identity/tenant/job bounds. The parent reserves one attempt before child start; no detached child, alternate journal or retry. The key-string read is tied to the owned key's hash and never logged.
3. **Authoritative cleanup:** prove readbacks of the exact application row, Firebase UID/claims/disabled/revocation state, authenticated-job session and database `application_name` session count. Handle child loss at `CLOSEOUT_INTENT` by reconciling current app/Firebase/session state under the same journal; never blindly repeat activation, token issuance, disable or key deletion. Retain only the minimum private owned-key/credential metadata needed for one independent closeout, with a hard purge/readback deadline and an explicit unconfirmed residual if cleanup cannot be established. Enumerate and verify every operation-private root, including any historical root actually used; do not assert absence of roots never inspected.
4. **Deterministic matrix:** positive exact-job lifecycle; wrong source/plan/approval/key/operator/tenant/job; duplicate/concurrent attempt; child timeout/exit/signal and response lost before/after mutation; interrupted closeout at each intent; stale/foreign DB or Firebase row; session-count disagreement; late closeout; private symlink/foreign file; credential, token and customer-data non-disclosure. Use fake Cloud/Firebase/Stripe and disposable PostgreSQL for SQL/TLS/session behavior. Preserve the existing 11 serialized, 11 extracted-auth, eight readback, 12 coordinator and 13 bridge cases. Run backend lint/build/architecture and both governance checks. Browser applies only if UI changes; none is proposed.

Finish is a source-pinned **disabled** real-client adapter and independent-cleanup matrix with truthful residuals and `liveAuthorization:false`, `authProofReady:false`. Rollback is deletion of the fresh copy. A passing fake/disposable matrix does not prove current provider access, real credentials, current job/account state or 3A payment. Estimated effort: one medium-to-large local card; direct provider cost USD0. This is a material operational prerequisite, with no section/acceptance-denominator change.

After that result, a **separate** exact read-only current-state qualification and then a separately approved bounded external access/authentication operation would be needed. Any real password entry, OAuth token, database/Firebase/Cloud/Stripe request, API/IAM/key/account/runtime change, deployment, payment, spending or customer action is excluded from this decision.

## Alternative 2 — use an existing application operator

Pause the temporary test-operator/key path and make a source-backed current operator assessment. The earlier zero-eligible result means this path is not established by the Console account or by the disabled test row. Any current account lookup is an external read needing its own exact authorization. If an already authorized operator can meet 3A safely, the new binding may be unnecessary; if not, return to a bounded decision. No live lookup is authorized by choosing this planning alternative alone.

## Alternative 3 — defer 3A

Preserve the disabled local evidence and accepted 4/8 walkthrough milestones; do no further P08 implementation or external action.

## Decision requested

Choose Alternative 1 for the finite disabled local card, Alternative 2 for a separately scoped operator assessment, or Alternative 3 to defer. This proposal does **not** implement any choice, authorize a live window, or promote 3A. The source-level `CLOSEOUT_INTENT` recovery gap and the missing credential/private-root binding require an explicit owner decision under `AGENTS.md` before implementation. **Explicit material prerequisite proposal; no deviation implemented.**

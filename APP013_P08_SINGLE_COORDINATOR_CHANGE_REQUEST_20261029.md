# APP-013 / 3A / P08 — single coordinator ownership change request

**Proposal only. No coordinator or provider authority.** The owner-approved local binder work produced disabled after-cutoff closeout and actual `AuthController` handoff proofs, but neither is a combined launch. The current same-job 3A Sandbox payment acceptance and the eight-milestone denominator remain unchanged.

## Demonstrated gap

Backend `p08-integrated-local-packet-20261029/source/packet.py` owns the two IAM bindings, API service, owned key and authentication attempt. Its `runtime_closeout` is injected; it does not restore/retire temporary database, secrets, service identity or traffic. Backend `p08-restoration-local-20261028/source/restore.py` owns those runtime resources and can own IAM, but its run requires an authentication callback before its own cleanup. Nesting the packet inside the restoration callback makes the packet demand “runtime retired” before the outer restoration cleanup runs. Nesting restoration inside the packet requires its full run and auth callback to repeat lifecycle control, creating separate journals and ambiguous lost-response ownership. Existing local tests pass separately, but do not prove one safe combined operation. The new owned-key handoff deliberately refuses a packet success proof without session/private-plan readbacks.

## Recommended Alternative 1 — one source-locked coordinator and one top-level journal

Implement a narrow disabled coordinator in the existing P08 evidence directory. The coordinator alone owns mutation order and durable attempt/residual records. It reuses the historical restoration `NativeAdapter` for exact runtime resource commands/readbacks, the bridge's existing serialized CLI/HTTPS request adapters for IAM/key/diagnostics, and the existing authentication controller for the disabled test ADMIN. It does **not** run either old controller as a nested full operation. The top-level journal binds each child result hash and records mutation intent before the call. An independent closeout-only path reads that journal, does not repeat an uncertain mutation automatically, and authoritatively checks account/session, owned key, IAM, runtime/database/secrets, normal traffic and private-plan absence. API Keys management service stays enabled per the owner's approved Alternative 1; only the owned key is deleted/read back. Keep native entry disabled while local tests run.

Impact: one new local coordinator module/test matrix beyond the prior assumption of composing two existing controllers directly. This is a material implementation prerequisite, **not** a new product subsystem, release section, dependency or acceptance criterion. It adds an estimated medium local engineering task and source-lock/fixture maintenance. No external requests, credentials, provider changes, payment or new allowance follow from approving it. A future exact external operation still requires current qualification, owner approval and finite cost/retention/closeout terms.

## Alternative 2 — two staged operations

Use a separately approved runtime restore operation and a later separately approved access/key/authentication operation, each with independent journal/cleanup. This avoids a new coordinator but extends temporary resource exposure and cannot claim one same-block closeout without a new handoff and owner-approved intermediate state. It adds at least one extra external approval/window and may delay 3A. Do not infer either operation is ready.

## Alternative 3 — defer P08

Do no further P08 integration until a revised product/authentication path is chosen. This preserves current retirement and accepted milestones but blocks the same-job 3A payment proof that depends on an authenticated operator.

**Decision requested:** approve Alternative 1 for local coordinator implementation/testing only, choose Alternative 2 for staged design, or defer. No live Cloud/Firebase/CHILD/Stripe action, key or IAM change, deployment, payment, spending or schedule is included. R10 remains consumed; accepted walkthrough 4/8, R1 newly closed 0/27. **Explicit proposed material prerequisite; none implemented.**

## Owner decision — October 29

The owner approved Alternative 1 for local implementation and isolated tests only. This decision does not authorize a live operation, external read or mutation, credential resolution, payment, deployment or spending. The historical proposal above remains the record of what was offered before this decision.

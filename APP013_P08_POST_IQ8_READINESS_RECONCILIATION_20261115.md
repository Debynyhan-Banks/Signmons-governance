# APP-013 / 3A — post-IQ8 connected-entry reconciliation

Read-only local review requested by owner. Backend1f8fa97 (BR1 runtime2f19eb8); governance3bb8dd6. No provider, credential, SQL, browser, sign-in or support action. No source/manifest change or replacement live attempt. This record completes the remaining-work mapping required by APP013_3A_COMPLETION_AND_RUN_CONTROL_PLAN_20261114.md; it does not authorize new implementation.

## Decisive results

IQ8 passed the approved identity procedure and independently confirmed exact-UID disabled restoration. It used5main/6cleanup calls and did not exercise BR1's extra observations. Enabled-state metadata omitted disabled and passed the unchanged predicate; no authenticated access proof follows. BR1/SD3 are wired into iq1_identity_boundary.py only. The full connected coordinator still invokes one RuntimeAdapter.readback per runtime change (p08-live-binder-local-20261029/source/coordinator.py runtime loop; native entry.py adapter). Do not claim BR1 was integrated into that runner or silently port it. IQ8's passing immediate path supplies evidence for that narrow path, not a guarantee against recurrence.

R47 result retains ACCOUNT_SESSION, AUTH_OUTCOME_UNKNOWN and AUTH_REVOKE. Its journal records revocationIntentAt2026-11-14T19:22:30.000Z. R48 closed with no residuals but authAttempted=false and authProofAccepted=false; it stopped at identity readback before authentication. Its clean closeout is not a later authentication/account-revocation result for R47. AC1 is a local correction, not current containment evidence.

## Requirement-to-existing-check matrix

| Requirement | Existing source/evidence | What it establishes / remaining gap |
| --- | --- | --- |
| Runtime identity activation/restoration | IQ8 result and local closeout | Procedure passed and final disabled confirmed at10:15:21 Eastern. Not durable current state or authenticated usability. No repeat IQ qualification needed by default. |
| App test account exact and disabled | qualification_launch.py QUALIFICATION_SQL/read_database; adapter.py exact_account | Existing generic qualification can check exact account identity/status under fresh authority. Historical receipts alone do not establish current status. |
| Firebase exact identity, disabled, claims | qualification_launch.py read_firebase | Existing lookup validates these current properties when separately authorized. No new identity is required. |
| Revocation at or after R47 intent | qualification_launch.py REVOCATION_LOWER_BOUND_MS/read_firebase versus native entry.py account_readback and adapter.py exact_firebase | Generic cutoff1793020648538 is2026-10-26T13:17:28.538Z, earlier than R47. Passing it cannot prove revocation after2026-11-14T19:22:30Z. Native same-operation readback uses journal intent correctly but cannot be replayed with R47's consumed authority or purged private inputs. |
| Database connection/session containment | qualification SQL sessionCount/CLOSEOUT_SQL; native_child.mjs boundClients close and journal flags | SQL checks matching pg_stat_activity sessions and runtime role; child closes its owned clients before reporting sessions:0. Neither is a general inventory of all Firebase sessions or proof of whether R47 authentication occurred. Keep those meanings distinct. |
| Historical authentication outcome | R47 authClient/result | Remains UNKNOWN. Current disabled/revoked state can reconcile present containment, not reconstruct discarded historical success/error. Preserve original flags/evidence. |
| Key lifecycle | KQ3 historical proof; AC1/ET1/current pinned entry | Reuse source-bound evidence with time limits; no unconditional repeat. Fresh native preflight still checks current pins/absence. |
| Current routing/job/policy/endpoint | packet.construct_values, current qualification and payment preflight | Fresh recovered identifiers, database/password custody and exact Sandbox destination bind the next packet. Old consumed packets/identifiers are not reusable authority. |
| Same-job payment, signed event and recovery | APP013_REMAINING_EXECUTION_CONTRACT.md3A; current connected child | Not live-demonstrated. Full child couples authentication to payment; do not invent an existing auth-only resume mode. |

## Next bounded deliverable

Prepare a current-containment read proposal that reuses the existing exact app/Firebase identity validators and database/HTTP read interfaces, but explicitly binds the Firebase validSince comparison to R47's retained revocation timestamp, with provider second precision handled by the existing exact_firebase contract. Compare current app disabled state and matching database-session absence under the same exact target identity. Retain only safe match/state/time-bound flags; no password/token/raw provider data. The proposal must state exact reads, credential source, private-target recovery needs, no-retry/cleanup bounds, source pins and which historical unknowns cannot be resolved. No automatic account disable, revoke or authentication action is included.

Do not patch the shared global cutoff merely to make a new test pass or treat a newly written proposal as authority. Inspect actual existing invocation seams and private-target availability before choosing between a source-bound one-off read composition and a narrowly approved local adapter amendment. If implementation is required, complete its section card and obtain the owner decision before coding. This is one preparation deliverable, not authorization for a generic diagnostic subsystem or another full payment run. No Terminal attendance should be requested until that packet and dependent preparation are complete.

After current containment is evidenced, finish one connected-session overview with recovery/qualification/native gates and later-stage reviews prepared before attendance. Then separately approve credentials/provider/payment actions under the existing rules. A failed attempt ends after cleanup; no rolling automatic repeat. Owner ultimately accepts the unchanged3A finish: same admitted job Checkout, authentic matching signed event/application gate, failure/replay safety and cleanup.

## Handoff

Completed: IQ8 evidence reconciliation and exact remaining-check coverage map. Blocker: current R47 account/revocation containment lacks a correctly time-bound observation; implementer owns its bounded proposal, owner/cloud/DB custodians own any subsequent access. Historical authentication outcome remains UNKNOWN. Next observable result is a reviewable source-derived containment packet, not a payment launch. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27;3B not promoted. No scope deviation.

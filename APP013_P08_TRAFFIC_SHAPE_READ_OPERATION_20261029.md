# APP-013 / 3A / P08 — exact traffic-shape read-only operation

**Status: prepared for separate exact owner approval; not approved or attempted.** This card follows the approved local-only preparation at governance `28ca955`, backend implementation `66e61b9`, and local result `APP013_P08_TRAFFIC_SHAPE_LOCAL_RESULT_20261029.md`. It does not reuse R05 operation `3fb6d82c-b7e5-4851-bee0-98949081f360` or its consumed authority.

## Exact identity, time and limits

- Section R1-W01 / APP-013 / 3A / P08; project `signmons`; service `signmons-calldesk-staging`; region `us-east5`.
- New operation `581346e1-445f-48f1-909c-b86137a9c1a3`. Source backend commit `66e61b9`; diagnostic source SHA256 `1b6170a8a1b825b6f8676efead4142897550fdbe8324a7f7ce2b9915490ef3ef`; retained R05 model/launcher are hash-locked.
- Today, October 29, **2:45–3:00 p.m. Eastern** (`18:45–19:00 UTC`). Start at or after 2:45 and strictly before **2:55**. Reads end before **2:58**; process and private-input closeout finish before **3:00**. One exclusive attempt, no retry, USD0 allowance.
- Maximum **three** bounded `gcloud` CLI reads and zero HTTPS, SQL, Firebase, Stripe, payment, booking or customer actions. No Terminal password or attended browser step. Existing owner host authorization may be used only for these reads; credential impersonation/overrides refuse.

## Finite operation

1. Before provider access, bind the exact SHA256 of this immutable pre-decision card, new operation ID, current source digest, owner decision, private 0700 directory and 0600 plan/binding. Verify the protected baseline, source locks, command serialization, current clock and empty attempt slot. A missing or inconsistent binding refuses before a read. A decision after the strict cutoff does not extend this card.
2. Read only the active owner list and current config using the previously tested R05 CLI projections. Require the sole exact active Signmons owner and safe no-override config shape.
3. Read one named Cloud Run service projection: `metadata.name,status.traffic`. The raw JSON remains in process memory and stderr is suppressed. Reject foreign service, malformed/oversized or ambiguous traffic entries. Return only fixed booleans `normal100ExactlyOne`, `candidatePresent`, `candidateZeroExactlyOne`, `oldTagAbsent`, their false names and a bounded entry count. No revision name, URL, raw tag, account, policy, error body or credential is retained in public evidence.
4. Close or kill any child process group, record the fixed status and safe journal, delete the exact private plan/binding with absence readback, and finish by 3:00. A signal, deadline, denial, malformed output or cleanup failure stops; containment unconfirmed must be reported truthfully. No automatic or manual retry under this card.

Success means **diagnostic only**: the three parts of R05's `trafficRetired` check become distinguishable. It does not rerun R05, prove all P08 domains, change traffic, activate authentication/runtime or authorize Checkout/payment. If the candidate 0% entry is absent, the implementer must review the saved retirement intent and Cloud Run contract before proposing any predicate correction; if normal routing or old tag differs, the owner decides a separate bounded traffic action. Neither branch is automatic.

**Exclusions:** no service traffic/tag mutation, deployment, IAM/secret/API/key/account/database/billing change, user token/signing, Stripe action, payment, booking, message, spending, merge or push. No CHILD database password or Stripe Sandbox interaction. Accepted 1A/1B/2A/2B remain 4/8; newly closed R1 0/27, legacy 6/60, intelligence 0/13. **No scope deviation.**

**Owner decision requested:** approve or refuse this exact read-only operation for 2:45–3:00 p.m. Eastern today, strict 2:55 start cutoff, three CLI reads, one attempt/no retry, USD0 and mandatory closeout. The earlier local-preparation approval is insufficient.

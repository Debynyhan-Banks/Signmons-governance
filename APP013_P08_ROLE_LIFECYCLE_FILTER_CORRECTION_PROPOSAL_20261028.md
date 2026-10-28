# APP-013 / 3A / P08 — IAM Role lifecycle-filter correction proposal

Status: ALTERNATIVE 1 OWNER APPROVED FOR LOCAL CORRECTION AND ISOLATED TESTS. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: Debynyhan Banks approved Alternative 1 in the governed conversation on October 28, 2026, against this document's pre-decision SHA256 `38723343c5738eede776c13b8cc967388997e36d5217b79bc5af901bdfcd3dc1`. Approval covers only the seven local steps below. It does not authorize a provider call, retry or new external operation.

## Demonstrated gap

Fresh approved operation `02aa2053-4985-487d-b7b8-aaf67d6bfb21` ran once at 6:40 p.m. Eastern. All three allowed CLI reads and the one exact IAM FULL-view HTTPS read completed. The strict parser stopped with sanitized reason `INACTIVE_ROLE`; private inputs are absent, raw output/bearer were not retained and provider mutation was impossible. Backend evidence: `evidence/APP-013/p08-role-inventory-r03-stop-20261028/`.

The existing classifier aborts the entire inventory when any row is deleted or its `stage` is absent/outside ALPHA/BETA/GA. Google documents that ALPHA omits `stage`, and documented stages include EAP, ALPHA, BETA, GA, DEPRECATED and DISABLED: <https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles> and <https://docs.cloud.google.com/iam/docs/roles-overview>. A project inventory can therefore contain structurally valid rows that are irrelevant or ineligible for this exact-candidate decision.

## Alternative 1 — recommended local correction

In the disabled evidence-contained qualifier only:

1. validate `deleted` as a boolean when present and `stage` against the documented lifecycle values when present;
2. normalize an omitted `stage` to ALPHA exactly as documented;
3. retain candidate eligibility as not deleted and stage ALPHA/BETA/GA; exclude EAP, DEPRECATED and DISABLED rows from classification without saving their names or metadata;
4. continue to refuse nonboolean `deleted`, nonstring/unknown stage, unknown fields, malformed names/permissions and all existing transport/page/privacy/binding failures;
5. record only aggregate excluded-row count in sanitized evidence, capped by the existing 200-row response limit;
6. test omitted-stage ALPHA, deleted, EAP, DEPRECATED and DISABLED exclusion, malformed lifecycle refusal, exact candidate classification, evidence privacy and unchanged restoration compatibility;
7. run the full isolated qualifier suite and required repository gates.

No provider call, retry or new operation is included. After local proof, a later exact read-only operation requires a fresh ID, window and separate owner approval.

## Alternative 2 — stop

Leave exact role candidates unknown and keep Stage A access resolution blocked.

## Boundaries and impact

This proposal does not authorize an API/service enable, IAM role or binding action, Firebase action, signing/token exchange, API-key action, database/identity/secret/tag/runtime action, deployment, Stripe/payment, customer action or spending. It adds no section, acceptance criterion or dependency and does not resolve the separate exchange-key incompatibility.

Owner decision requested: approve Alternative 1 for local correction and isolated tests only, or choose Alternative 2. Accepted counts remain unchanged. **No scope deviation.**

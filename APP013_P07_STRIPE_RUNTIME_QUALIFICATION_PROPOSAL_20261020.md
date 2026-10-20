# APP-013 / 3A / P07 read-only Stripe/runtime qualification proposal

## Decision requested

Approve one read-only qualification of the exact environment needed before a P07 deployment or P08 Sandbox payment proposal. The operation is limited to the **Signmons LLC sandbox**, Google Cloud project `signmons`, region `us-east5`, Cloud Run service `signmons-calldesk-staging`, and the owner-accepted job `9180bef4-561d-47a0-869f-925e6a3dfd96`.

The signed-in Stripe access is recorded as **owner/admin**. No further identity detail is needed. Approval of this proposal does not authorize a Checkout Session, webhook test or resend, payment, deployment, build, migration, configuration change, secret access, database write, booking, message or customer contact.

## Why this check exists

P07 is implemented and locally tested, but it has not been deployed. The current normal-traffic revision is historically recorded as `signmons-calldesk-staging-app013dbrot2`; that observation must be refreshed. The current Stripe destination, Cloud Run secret references and exact retained tenant/job binding are also unconfirmed. P08 cannot be made concrete until these facts are correlated.

Historical APP-012 evidence says the staging connected-account destination was active at `/webhooks/stripe`, subscribed to six approved event types, and used Google Secret Manager for its signing secret. That September evidence is a comparison baseline only.

## One exact read-only operation

If approved, the implementer performs the following once, without retry:

1. In the already signed-in Stripe Test/Sandbox context, read the single enabled connected account and the **Connected accounts** event destination. Confirm that the destination is enabled, ends in `/webhooks/stripe`, and subscribes only to:
   - `checkout.session.completed`
   - `checkout.session.async_payment_succeeded`
   - `checkout.session.async_payment_failed`
   - `checkout.session.expired`
   - `payment_intent.payment_failed`
   - `charge.refunded`
2. Read the destination's displayed API version and delivery status. Do not reveal, rotate, copy or test its signing secret; do not send or resend an event.
3. Read Cloud Run service/revision metadata for `signmons-calldesk-staging`: normal traffic revision/percent, deployed image digest, runtime identity, and the names or secret-version references for `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_WEBHOOK_LIVEMODE` and `CUSTOMER_PAYMENT_RETURN_URL`. Confirm test mode is explicit. Do not read any secret payload or change traffic, IAM, revisions or environment values.
4. Through an already available read-only staging database path, query only the retained job and its tenant. Confirm the job still exists in `CREATED`, has no payment or calendar activity, and retains the accepted payment approval timestamp/digest. Compare the tenant's configured Stripe destination with the single enabled sandbox connected account and confirm `chargesEnabled`. Record only equality booleans and bounded state, never provider IDs or customer fields.
5. Compare the deployed image/revision with the local P07 candidate. Because P07 has not been deployed, report `P07_DEPLOYMENT_REQUIRED` if the normal revision does not contain the reviewed patch. Do not treat historical runtime health or destination status as proof that the local patch is deployed.

If any step would require enabling a database login, changing IAM, accessing a secret payload, broad tenant/payment search or writing state, stop that step as `READ_PATH_UNAVAILABLE`; do not substitute another credential or resource.

## Sanitized output and issue identification

The retained result contains only:

- operation time and the exact non-secret resource names above;
- pass/fail/unknown for Sandbox mode, one enabled connected account, destination state/path, exact six-event set and displayed API version;
- pass/fail/unknown for normal traffic, image/revision identity, required environment or secret references and explicit `STRIPE_WEBHOOK_LIVEMODE=false`;
- pass/fail/unknown for exact tenant/account equality, `chargesEnabled`, job `CREATED`, no payment/calendar activity and payment-policy timestamp/digest presence;
- one or more named blockers from: `WRONG_MODE`, `CONNECTED_ACCOUNT_COUNT_MISMATCH`, `DESTINATION_DISABLED`, `DESTINATION_PATH_MISMATCH`, `EVENT_SET_MISMATCH`, `API_VERSION_UNCONFIRMED`, `RUNTIME_REFERENCE_MISSING`, `RUNTIME_MODE_MISMATCH`, `TENANT_ACCOUNT_MISMATCH`, `CHARGES_DISABLED`, `JOB_STATE_MISMATCH`, `PAYMENT_ACTIVITY_PRESENT`, `CALENDAR_ACTIVITY_PRESENT`, `POLICY_BINDING_MISMATCH`, `P07_DEPLOYMENT_REQUIRED`, `READ_PATH_UNAVAILABLE` or `QUALIFIED`.

No name, email, password, MFA code, key, webhook secret, card/bank information, provider identifier, Checkout URL, customer record or raw provider/database response enters evidence or chat.

## Stop, cost and observable result

Any mismatch or unavailable read path stops qualification. There is no automatic retry and no corrective action under this approval. Expected direct provider cost is USD 0 because the operation creates no provider object or payment.

The observable result is a sanitized `QUALIFIED` result or exact named blocker list. The likely next result, if the current normal revision still predates P07, is `P07_DEPLOYMENT_REQUIRED`; that would lead to a separate exact build/deployment proposal. Only after the reviewed P07 source is deployed and qualification passes may the implementer prepare a P08 proposal for one owner-operated Sandbox Checkout and authentic signed-event proof.

This proposal expires at 11:59 p.m. Eastern on October 20, 2026. If it is not started by then, a fresh current-state proposal is required. Accepted progress remains **6/60 packages, 4/8 walkthrough milestones and 0/13 fully accepted pilot rows**. **No scope deviation.**

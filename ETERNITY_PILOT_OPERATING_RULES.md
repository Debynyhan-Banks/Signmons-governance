# Eternity pilot operating rules — owner decisions and implementation fit

## Authority

Owner subsequently answered "yes i approve proceed" to the explicit regular-visit-only first-test recommendation. Option A below is now approved as test scope only. No code expansion, resource mutation, deployment, charge or test execution authorized by that answer. Full emergency business rules remain intact and unavailable for automatic pricing until separately implemented and qualified.

Owner explicitly supplied these values in this task and clarified that USD150 replaces USD99 and applies to all after-hours emergencies including Sunday. Owner agreed emergency availability must be confirmed, with no immediate-dispatch promise. Latest proceed authorizes documentation and fit review, not charges, deployment, live configuration or an extra implementation task.

## Approved business facts

| Rule | Value |
| --- | --- |
| Business | Eternity Mechanical Services LLC |
| Timezone | America/New_York (Eastern, with local daylight-saving rules) |
| Monday-Friday | 07:00-19:00 |
| Saturday | 09:00-17:00 |
| Sunday | Closed for routine service; emergency-only |
| Regular initial visit/diagnosis | USD99 deposit |
| All after-hours emergencies | USD150 instead of the USD99 deposit, including Sunday; never USD249 |
| After-hours non-emergency | Collect request for business-hours follow-up |
| Emergency service | Offer subject to confirmed availability; do not promise immediate dispatch |

Do not infer refundability, credit toward repairs, taxes, holiday exceptions, response-time guarantees or emergency dispatch from these rules. Classification must depend on the intended service, not merely when someone submits a non-emergency request. A late-night request for normal business-hours follow-up must not automatically incur USD150.

## Inspected fit and smallest first-test proposal

Sources: backend338d597; governancefbca5c4. organization-payment-policy.ts permits fixed deposit and fixed service fee, emergencyFeePolicy.kind:none only. job-payment-policy.service.ts binds one current approved policy to an unpriced job and refuses replacement. payment-requests.service.ts sums deposit and service fee when both are required. organization-profile.ts stores hours as plain text; it is not an executable business-hours classifier.

Thus do NOT encode99 as deposit and150 as service fee: that would request249. Do NOT change the tenant-wide policy back and forth per customer. Do NOT insert an emergency policy into the current none-only schema or fabricate approval timestamps.

Recommended first controlled test, pending explicit owner acceptance of its restriction: one regular initial-visit request, no emergency case. Prepare a fixed USD99 deposit policy: serviceFeeRequired:false,serviceFeeCents:null,depositRequired:true,depositPolicy:{kind:fixed,amountCents:9900},emergencyFeePolicy:{kind:none},currency:usd,paymentGateMode:fail_closed,webhookValidationRequired:true. This is a restricted test policy, NOT a complete representation of Eternity's production rules. P06 creates a test job only; actual Sandbox payment remains existing3A after2B acceptance. R07/R08 still gate actual setup; R10 gates run authority. No first-test restriction is treated as accepted yet.

## Emergency automation gap — not an approved new task

Cause: newly supplied owner business rule exceeds the existing fixed-policy subset. Smallest code direction, if later approved: versioned replacement amount and structured local hours; trusted service classification/availability boundary; immutable selected amount/reason/policy identity at job payment binding; existing Checkout request reads that snapshot. Reuse payment and approval services, not a new payment processor.

Before coding, specify whether pricing time is scheduled service time or another agreed business event, boundary instants, eligibility/availability authority, and treatment of rescheduling across hours. These are design questions for the emergency implementation, not reasons to block a regular-only test if approved.

Acceptance checks for that future change:99 regular;150 after-hours emergency including Sunday;never249; after-hours routine follow-up not surcharged; unavailable emergency never confirmed; timezone/DST/open-close boundaries; policy change, concurrent binding/replay, stale/forged classification and paid-job reprice refusal. Files likely affected: organization payment/profile contracts and tests, job binding, current-policy checks and intake/customer presentation. Exact implementation card, effort and baseline impact must be approved before coding.

Alternatives: (A) recommended regular-only first test, keep full business rules documented and qualify emergency implementation before any emergency pilot use; (B) explicitly approve the bounded emergency-pricing design/change before testing. Neither is silently selected by this document. No scope deviation in this documentation work; implementation expansion remains unapproved. Original12+approvedU01=13;6 locally closed,7open. No acceptance credit or new task count.

## Review and next result

Owner test-scope decision is complete: regular-only first test. Implementer: continue existing R06 provider/liability/infrastructure qualification and include this restriction in exact R07 packet. No repeat request for this scope approval. No real payments, bookings, provider changes or emergency promises.

## Approved restricted test-policy values

These are policy content, not a persisted approval record or deployable activation envelope. Never generate actorId/approvedAt or activate the tenant from this file.

```json
{
  "currency": "usd",
  "serviceFeeRequired": false,
  "serviceFeeCents": null,
  "depositRequired": true,
  "depositPolicy": { "kind": "fixed", "amountCents": 9900 },
  "emergencyFeePolicy": { "kind": "none" },
  "paymentGateMode": "fail_closed",
  "webhookValidationRequired": true
}
```

The none emergency field describes the deliberately restricted test policy, not abolition of the USD150 business rule. Emergency scenarios are excluded from this test; do not silently price them at99. P06 has no payment execution. Existing3A later tests Sandbox payment under its own approval.

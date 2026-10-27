# APP-013 / 3A / P08 — post-billing read-only readiness qualification

Status: PREPARED; NOT APPROVED OR STARTED. Operation `60e55fda-d026-43e8-9b89-c8e2ebef1a10`. No new helper/application implementation. Owner reports “Signmons billing account is active”; API verification is pending. No previous consumed receipt/attempt/authority is reused.

## Purpose and exact scope

Same admitted job / unchanged 3A Sandbox-payment criterion. Prior source/identity/normal100/candidate0/tag-absent metadata were verified at8:17. Secret Manager returned BILLING_DISABLED at8:25. Billing read at8:29 returned project billingEnabled=true with linked account open=false. Preserve all historical receipts. This operation verifies the reported resolution and completes only the retired-resource metadata that was never reached. No runtime restoration, authentication or payment is inferred.

**Timing:** on approval tonight October26, start strictly before9:00p.m. Eastern, reads by9:10, sanitized closeout before9:15. No wait/Terminal/password/browser attendance needed. No attendance extension. One exclusive local attempt, actual owner decision/immutable proposal correlation before reads; at most17 bounded CLI commands, no operation retry. Each command at most10s, capped by remaining read deadline. No resource/API mutation on a successful or failed read.

**Owner/configuration:** existing host gcloud configuration/cache and ordinary owner OAuth refresh only. Check local absence of persisted credential-file override/impersonation; clear credential override environment inputs, disable CLI prompts/file HTTP logging, verify expected active owner. No alternate login/principal, ADC, impersonation, token print/export or bearer in chat/file/URL.

## Finite command inventory and gates

1. Active-owner read: gcloud auth list --filter=status:ACTIVE --format=value(account), captured privately and reduced to established-owner match.
2. Project signmons billing: gcloud billing projects describe signmons --format=json(projectId,billingAccountName,billingEnabled). Verify exact project, explicit billingEnabled=true and a canonical linked account reference. Otherwise stop, preserving unknown/mismatch; do not link/enable or proceed to secrets.
3. Exactly the account currently linked by step2: gcloud billing accounts describe <that linked ID> --format=json(name,open). Verify reference matches and explicit open=true before any secret reads. Keep account ID transient, persist hash/open and whether hash matches the prior linked account hash df8c89e72b72b59ac6b06c0a20fa7d5f85a15b5d6d7450ff57a72722be172935. A changed linked account is a reported read fact only; it does not authorize the assistant to relink, spend or act on another account. No account list/display name/balances/invoices/cards/payment lookup.
4–9. Metadata only, exact **version1** on these six retired resources in project signmons: signmons-staging-p07-payment-database-url; signmons-staging-p07-stripe-webhook-secret; signmons-staging-p07-disabled-openai-key; signmons-staging-p07-admin-token; signmons-staging-p07-conversation-key; signmons-staging-p07-technician-link-key. Use gcloud secrets versions describe 1 --secret=<exact resource> --project=signmons --format=json(state). Each state must explicitly be DISABLED; missing/other state stops as contract/drift. No secret value/access/latest/list or version changes.
10–16. Resource IAM policy only for those six resources plus signmons-staging-stripe-secret-key; gcloud secrets get-iam-policy <exact resource> --project=signmons. Reduce in memory to direct bindings for serviceAccount:signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com, retain only role/condition hash/presence. Other principal/policy data discarded without print/file. Any unexpected remaining dedicated binding stops; do not remove/change it. This inventory does not prove all inherited/effective authorization. No shared secret payload or shared runtime/P06 policy read.
17. Metadata only for exact existing exchange key projects/signmons/locations/global/keys/06cfec12-0432-455f-888f-397d1a0150a6: gcloud services api-keys describe <exact key ID> --location=global --project=signmons --format=json(name,displayName,restrictions,deleteTime). Persist only hashes/existence/restriction-present/deleted flags; stop if deleted/missing/denied. No keyString/get-key-string/value, account list or key update.

No repeated Cloud Run/revision/service-identity/project-IAM/signing-role/Stripe/Firebase/database reads. The previous source/traffic facts remain observations at their saved times, not freshly asserted. No direct HTTPS request or OAuth token extraction is included. If a request again reports BILLING_DISABLED, stop and record that the reported change has not established usable Secret Manager access; do not grant IAM or automatically retry for propagation.

## Failure reporting, retention and closeout

Capture stdout/stderr only in transient process memory. Save response/argument hashes, stage/exit code, fixed safe causes (explicit BILLING_DISABLED, provider permission denial, local filesystem/config, authorization missing/expired, invalid command/config, timeout/network or UNKNOWN), explicit match/unknown facts and UTC/call count. Never raw error/policy, owner/account IDs, bearer, environment literals, secret payload or key value. Unknown error cause remains unknown; projected output shape is checked rather than silently treating omitted fields as state changes. No per-provider retry/billing-cap guarantee from native gcloud is claimed.

One exclusive result; all child processes ended and raw references dropped before9:15. No real private mailbox plan, database session or active resource is created, so none is invented for cleanup. Finish is current billing/open/resource-metadata evidence or a truthful stop; neither is operator authentication or 3A acceptance.

## Exclusions and next decision

No billing enable/link/reopen/pay, financial details or new spending allowance; no IAM/role/binding/API/secret enable/disable/value/action, account activation/token/signing/exchange, runtime restoration/deploy/build, Stripe/payment/event/retry, booking/message/customer action. No code/helper implementation, acceptance reset or queue/count change. Accepted1A/1B/2A/2B and4/8 walkthrough;0/27 newly closed R1,6/60 legacy,0/13 intelligence unchanged.

If all checks pass, implementer prepares the minimum exact runtime/access restoration proposal under the existing approved scope; it cannot run under this read authority. Any restoration implementation or external configuration/spending decision remains separately reviewable and owner-approved. **No scope deviation; fresh bounded verification follows the owner's report.**

Approve/refuse this one exact post-billing read-only operation with existing-owner host authorization/cache refresh and the listed timing/no-retry limits. AGENTS.md requires separate exact external authority because the earlier reads are consumed and the owner's status report is not permission to query/change resources. No owner Terminal/password needed.

# APP-013 / 3A / P08 — exact read-only Cloud Billing status check

Status: PREPARED; NO APPROVAL OR ATTEMPT. Operation `70d7a530-113b-4808-849a-7732c3564474`. No new helper/application change or billing mutation.

## Demonstrated blocker and smallest decision

Approved single-resource Secret Manager metadata diagnosis returned HTTP403/PERMISSION_DENIED with structured BILLING_DISABLED for secretmanager.googleapis.com at 8:25:54 p.m. Eastern. Backend evidence/APP-013/p08-secret-metadata-diagnosis-result-20261026/ correlates owner approval, two CLI commands, one GET and verified closeout. Do not treat it as a missing IAM permission or issue grants. Project billing linkage and any linked account's open status remain unverified.

Read-only procedure follows [Google's billing-status guide](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled), with the current [project describe command](https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe) and [account describe command](https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/describe). Linked/enabled and account-open flags help distinguish unlinked/inactive conditions; they do not establish delinquency, reason for suspension, current balance or payment-method problems. No payment overview lookup is authorized.

## Exact requested reads and window

On exact approval tonight October26, **start strictly before9:00p.m. Eastern; all reads by9:10; sanitized closeout before9:15**. No wait/Terminal/password/browser attendance required. One exclusive local attempt bound to this immutable proposal and actual owner decision; max **three CLI commands**, no retry. At most10s per command capped by remaining read deadline. Existing host gcloud configuration and owner OAuth cache refresh only; no login/alternate principal, credential override, impersonation, token print/export, API-key or secret-value access.

1. Check existing local config has no credential-file override/impersonation; gcloud auth list active principal, captured privately and reduced to established-owner match.
2. Exactly `gcloud billing projects describe signmons --format=json(projectId,billingAccountName,billingEnabled)` with prompts/file HTTP logging disabled. Verify projectId matches signmons. Keep linked account reference in memory only, persist its SHA256, accountLinked boolean and explicit billingEnabled boolean. Missing/malformed output is UNKNOWN; do not coerce absent billingEnabled to false. No account-list lookup.
3. Only if the prior response has one canonical linked `billingAccounts/<ID>` reference, describe **that exact linked account** once: `gcloud billing accounts describe <ID> --format=json(name,open)`. Validate name matches the in-memory reference. Persist only explicit open boolean and matching account hash, no account ID/display name/currency/organization/financial identity. If no linked account, skip this command. If permission denied, stop with safe fixed stage/cause; do not list/switch accounts or request a broader role.
4. Discard transient principal/account reference/output; end child processes; save sanitized approval/attempt/UTC/count/source-proposal correlation and no-active-child closeout. No financial/provider error body persisted. Error classification only existing safe categories plus numeric exit code; unknown cause stays UNKNOWN. No secret/Cloud Run/Firebase/Stripe/database reads or mutations follow.

## Finish, implications and exclusions

Observable finish: exact project linked/enabled and conditional linked-account open facts, OR a bounded classified read refusal, with closeout before deadline. If billing inactive/unlinked/closed, billing owner must separately decide a remedy. Reopening/linking/enabling billing can permit billable resource usage; this read approval grants no financial authority, new spending allowance or resumption of retired resources. If enabled/open yet Secret Manager reports BILLING_DISABLED, record the discrepancy and prepare the smallest next decision; do not automatically rerun the denied secret read or assume propagation resolved.

No balances/invoices/payment methods/cards, payments, account creation/reopening/link/unlink/enable/disable/update, API enabling, billing IAM/budget changes, subscriptions, refunds/charges or project/service usage action. No account/Firebase/user token/signing/database/runtime restoration/secret/IAM/deploy/build/Stripe/payment/event/booking/customer message. No reusable diagnostic subsystem or application change. Accepted1A/1B/2A/2B,4/8 walkthrough;0/27 newly closed R1,6/60 legacy,0/13 intelligence unchanged. **No scope deviation: new read-only billing-state authority proposed before execution.**

## Exact decision requested

Approve/refuse one exact project billing-link/status read and conditional single linked-account open-status read with existing-owner host authorization/cache refresh, deadlines and no retry. This does not authorize fixing billing or permitting any new spend. AGENTS.md requires separate explicit external-action approval because prior authority covered Secret Manager diagnosis only. No owner Terminal command/password required.

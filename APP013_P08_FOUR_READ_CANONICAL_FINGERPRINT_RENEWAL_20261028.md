# APP-013 / 3A / P08 — four-read canonical-fingerprint renewal, October 28

Status: PREPARED; separate exact execution approval pending. Operation `b9953d29-5396-4b58-826c-20054131b8f2`. Backend source b3b0b73; governance predecessor daf923e. No application or helper implementation.

## Traceability and observed gap

Approved section R1-W01 / APP-013 / 3A; acceptance remains the authentic same-job Sandbox payment and matching signed settlement in APP013_REMAINING_EXECUTION_CONTRACT.md, section 3A. This diagnostic establishes only an entry prerequisite. Reuse commands 1–4, owner/configuration safeguards and sanitized output contract from APP013_P08_POST_BILLING_READINESS_OPERATION_20261026.md; do not reuse its consumed operation or receipts. Prior backend result p08-post-billing-readiness-result-20261026 stopped with billingEnabled=true/account open=false. No new subsystem, implementation, role or access path.

Owner-authorized Safari inspection now shows both billing accounts Active. The renamed Signmons Active Billing is the original linked account, and Signmons's project row still points to that exact account. The other Firebase Payment remains a distinct account. Renaming did not change linkage. Newly added Billing Account User for the Signmons login was visually observed on the other account. No assistant billing/IAM mutation occurred. Current service eligibility remains unproved; account names alone do not establish it.

## Exact four-command inventory

Use only existing host gcloud authorization/cache with normal refresh, no new login/principal/impersonation/ADC. Verify local credential-file and impersonation overrides absent; suppress CLI prompts and HTTP file logging. No credential values may print or persist.

1. `gcloud auth list --filter=status:ACTIVE --format=value(account)`: privately verify the established gcloud owner debynyhan@signmons.com; mismatch stops, no account switching.
2. `gcloud billing projects describe signmons --format=json(projectId,billingAccountName,billingEnabled)`: exact project, explicit enabled=true, canonical linked account required. Capture ID transiently; compute and retain SHA256 of the full canonical billingAccountName reference including the billingAccounts/ prefix, exactly as historical evidence does. Never compare a bare-ID hash to this reference hash. Require the prior linked-account hash df8c89e72b72b59ac6b06c0a20fa7d5f85a15b5d6d7450ff57a72722be172935; unexpected relink stops for owner review.
3. `gcloud billing accounts describe <exact linked ID from step 2> --format=json(name,open)`: matching reference and explicit open=true required. No account list, balances, payment methods or invoice reads.
4. `gcloud secrets versions describe 1 --secret=signmons-staging-p07-payment-database-url --project=signmons --format=json(state)`: metadata only. Explicit DISABLED proves access to the previously blocked retired version without re-enabling it. Other/missing state or provider denial stops; no payload, access/latest/list or changes.

No policy, other secret, API-key, Cloud Run, Firebase identity, database or Stripe reads. Four commands maximum, one fresh attempt, no operation or request retry. No direct HTTP/token export. Every process timeout 10 seconds bounded by the remaining deadline; actual provider/SDK internal retry behavior is not claimed disabled.

## Timing, retention, finish and exclusions

Start on exact approval today October 28 strictly before 11:00 a.m. Eastern. Reads end within 10 minutes of start; mandatory child-process closeout and sanitized result within 15 minutes, no later than 11:15 a.m. No attended Terminal/password/browser block needed. Approval arrival after cutoff means refuse unstarted; never extend automatically.

Before reads, correlate actual owner decision, immutable proposal, fresh operation ID and exclusive attempt. Capture outputs only in process memory, reduce to booleans/hash/state or fixed safe error category (BILLING_DISABLED, permission denial, auth/config, network/timeout or UNKNOWN). Never retain raw errors/bodies/IDs/account emails/tokens/environment values. Stop at first failure. Verify all child processes ended; record result/closeout. No active database session or private-input plan is created. No private-input purge is invented.

Finite checklist: exact approval and one attempt; owner/config check; project billing; linked-account open; one disabled secret-version metadata; sanitized evidence and verified process closeout; doc/architecture checks. Positive outcome is all four facts; negative is truthful first stop. No coding/concurrency/browser suites necessary because no implementation changes. Governance safeguards and whitespace/architecture checks apply; old runtime tests are not newly executed evidence.

This does not restore runtime, enable secrets, create tokens, activate identities, grant access, change billing, deploy, spend, pay, book or message. No new allowance. Accepted 1A/1B/2A/2B, 4/8 walkthrough, 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. Finish does not close 3A. Next after a pass: review the remaining resource/access qualification scope before any runtime-restoration proposal; no automatic restoration. **No scope deviation; narrow fresh prerequisite verification only.**

## Correction decision and immutable predecessor

Predecessor e11b3e4 was approved and consumed; its first command stopped at OWNER_MISMATCH with verified closeout. Local hash comparison shows the actual known Signmons owner matches the earlier October 26 accepted owner output exactly. The implementer incorrectly pinned Gmail in the predecessor proposal. This renewal changes only expected owner, fresh operation identity and actual approval correlation; all four commands, no-retry/deadlines/resources/retention/exclusions remain unchanged. No login/configuration/credential/IAM change is included. Owner direction required before any new provider read; no application/helper implementation. Preparation deviation disclosed and corrected prospectively.

## Canonical fingerprint correction and offline proof

The daf923e attempt passed owner and project-enabled checks, then consumed its attempt at LINKED_ACCOUNT_CHANGED because the inline comparison hashed the bare ID against the historical full-reference hash. This was an implementer comparison error, not actual relinking: project stdout SHA256 is identical to the October 26 response. Offline positive/negative checks verify full canonical reference matches the historical fingerprint, a different account refuses, and missing prefix refuses. Saved sanitized proof: backend evidence/APP-013/p08-four-read-owner-renewal-result-20261028/local-diagnosis.json. This renewal preserves corrected Signmons owner and all four reads, changing only the fingerprint representation and fresh operation/approval identity. Previous raw receipts are immutable. No principal, credentials, application/helper implementation or provider state changes. Preparation deviation disclosed; no further external read before fresh approval.

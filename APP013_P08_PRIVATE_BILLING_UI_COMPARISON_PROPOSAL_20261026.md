# APP-013 / 3A / P08 — private local billing-account identity comparison

Status: PROPOSED PURPOSE ONLY; no command implemented or input requested yet. No provider action. The owner confirms the “active” UI is the Cloud Billing account opened from Signmons project's Billing page (call_c44d82d2c2cc4cb3940765599e0db226). Preserve that report and the separate8:39API result: same linked-account hash, billingEnabled=true, open=false. Do not assume either another account or propagation without evidence.

## Finite card and decision

Section R1-W01 / APP-013 / 3A / P08. Existing criterion: same-job Sandbox payment through verified identity/policy/event, not a new billing feature. Current blocker is a billing UI/API discrepancy. Backend source4e31c60; governance1ba1cdf. Reuse the saved exact account fingerprint in backend evidence/APP-013/p08-post-billing-readiness-result-20261026/result.json and the Python standard library. Expected canonical billingAccounts/<ID> SHA256 is df8c89e72b72b59ac6b06c0a20fa7d5f85a15b5d6d7450ff57a72722be172935. No further backend read is needed for this comparison.

Recommended smallest action: after owner approves this specific bounded local purpose, provide one owner-run Terminal command that reads the account ID from the currently viewed linked Cloud Billing account via a hidden prompt and compares it entirely locally to the saved fingerprint. The ID is an identifier, **not a password**. It must not be pasted into chat. No browser/clipboard reading by the assistant, API/credential lookup, account list, customer data or financial page inspection. No reusable helper/package/application file; one reviewable standard-library command in chat only. Expected repository changes: this proposal/owner decision and sanitized fixed result if the owner later reports it.

### Exact input/output/privacy boundary

- Accept one hidden input, maximum60seconds; require a private Terminal TTY and refuse before input if getpass would echo/fallback. Catch timeout/interrupt without printing input or error details. No repeated input loop.
- Normalize surrounding whitespace, optional literal billingAccounts/ prefix, and account-ID letter case; require the canonical6-6-6 uppercase alphanumeric ID shape and bounded length. Do not accept a browser URL, password or arbitrary account name.
- Compute SHA256 of billingAccounts/<normalized ID> in memory, compare with the exact saved hash. Never print/store the ID, computed hash, clipboard, balances or tokens. No arguments/env/files contain the supplied ID. Drop references and exit immediately; do not promise secure memory erasure.
- Output exactly one fixed status: P08_BILLING_UI_ACCOUNT_MATCH, P08_BILLING_UI_ACCOUNT_DIFFERENT, P08_BILLING_UI_ACCOUNT_INVALID, P08_BILLING_UI_COMPARE_TIMED_OUT, P08_BILLING_UI_COMPARE_INTERRUPTED or P08_BILLING_UI_COMPARE_TTY_REQUIRED. Owner reports only that status. Owner may privately clear their clipboard afterward; assistant does not read it.

### Finite checklist, verification and finish

1. Record actual owner purpose/input approval before providing the command; bind its expected hash to the saved accepted receipt. This proposal itself is not authority to ingest private financial identifiers.
2. Review the small standard-library command's normalization, TTY/no-echo check, timeout/interrupt handling and fixed output; no new test harness for this reversible local comparison. No provider/browser/runtime tests. Run required documentation/baseline/architecture/whitespace gates for resulting governance evidence.
3. Owner optionally runs the command once and shares only the fixed status. MATCH correlates the viewed account identity to the prior API account; the UI “active” report and APIopen=false then remain unresolved provider-state observations. DIFFERENT identifies account/view context mismatch and requires owner direction; do not relink anything. Invalid/timeout/interrupted is no identity conclusion and no automatic retry.

No persisted private input means no new raw-data purge deadline or remote closeout. Command ends after one result; no standing background worker, resource or rollback mutation. This local comparison needs no provider execution window and does not extend tonight's9:15 attendance/provider authority. Any later API read requires fresh exact authority; any billing change remains a separate financial decision. If comparison matches but status disagrees, billing owner/provider support direction is needed rather than repeated automatic polling or new IAM grants.

Alternatives: owner may decline the comparison and resolve the account/status discrepancy privately with Google Cloud billing support. Do not submit a support message for the owner without explicit instruction. No account creation/reopen/relink/payment, balances/cards/invoices, credentials/token, database/Firebase/runtime/IAM/secret/deploy/Stripe/payment/event/booking/message, spending, new product feature or acceptance change. Accepted1A/1B/2A/2B and4/8 walkthrough;0/27 newly closed R1,6/60 legacy,0/13 intelligence unchanged.

**Decision requested:** approve this one private owner-run local fingerprint comparison and hidden identifier input, or decline. AGENTS.md requires a specific approved bounded purpose for new work while externally blocked; this asks before implementing/providing the command. **No implemented scope deviation; narrow local diagnostic purpose proposed before use.**

## Actual owner correction and local approval

Owner corrected the initial private-resolution selection: “sorry i did not mean that i meant to hit the first one,” explicitly selecting **Approve private local identity comparison** from question call_3480feece28542c39a882be9931aeb59 against immutable d8dd65b8353b9f08e25cbada2592b6f04a1053e9. This authorizes only the finite hidden-input, local fingerprint comparison above. Record precedes command preparation; no new confirmation needed. Chrome/provider inspection, further API reads, financial/resource changes and private identifier persistence remain excluded.

## Command review and handoff

One-shot command syntax/privacy reviewed; expected hash matches the saved8:39APIreceipt. No input executed or provider request. Only fixed status is reportable. Body SHA256 a7a9ece8c1ed1439262f20578747d404ce636ae96d8bfb4341e0a608f08be942. Command body is supplied in chat only. No scope deviation.

## October 26 — owner reports local account MATCH; billing discrepancy remains

R1-W01 / APP-013 / 3A / P08. Owner reports `P08_BILLING_UI_ACCOUNT_MATCH` from the approved private local comparison (proposal d8dd65b; corrected decision call_3480feece28542c39a882be9931aeb59). This correlates the displayed account with the saved API account fingerprint through the owner-run command; execution was not independently observed. Only the fixed status was received, never the identifier or computed input hash. Backend evidence: evidence/APP-013/p08-private-billing-ui-comparison-20261026/owner-result.json. Static command-review evidence remains historical and unchanged.

Completed: approved local identity comparison and owner report. Billing resolution is not established: owner sees Active in the linked-account UI; the last API read at 8:39 p.m. Eastern reported project billingEnabled=true/accountLinked=true and account open=false; the 8:25 p.m. Secret Manager response reported BILLING_DISABLED. No subsequent provider read, browser inspection, billing/resource change or independent clipboard/erasure verification. Preserve both observations; cause remains unknown.

Remaining/blocker/responsible role: billing owner and Google Cloud Billing support reconcile the same-account status discrepancy. Next observable result is provider/owner resolution evidence, followed only by separately approved fresh readiness qualification. No further read loop, helper, IAM grant, account relinking, runtime restoration, authentication or payment action is authorized by MATCH. Local authentication preparation is complete; live operator authentication, runtime readiness, same-job Sandbox payment/recovery and final 3A acceptance remain open. Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **No scope deviation.**

Owner support handoff (draft only; not sent): “For project Signmons, the linked billing account shows Active in the console. A private local comparison confirms it is the same account queried by the API. At 8:39 p.m. Eastern on October 26, Cloud Billing reported project billingEnabled=true and linked account open=false. At 8:25 p.m., Secret Manager returned HTTP 403 with reason BILLING_DISABLED. Please reconcile the billing status and service eligibility.” No account IDs, balances, credentials or payment details are included. Owner can use [Google Cloud Billing support](https://docs.cloud.google.com/support/docs/get-billing-support); no support contact is authorized here.

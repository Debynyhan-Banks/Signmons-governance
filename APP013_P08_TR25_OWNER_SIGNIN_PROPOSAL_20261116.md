# APP-013 / 3A / P08 — TR25 owner sign-in and coverage

PREPARED, NOT APPROVED. R53 packet5d0d2a2 is locally verified on CT4sourcec57cb9c. Owner confirmed November16 availability11:15a.m.–12:25p.m. Eastern. That confirms availability only. Current credential coverage strictly beyond12:15p.m. remains UNKNOWN.

## Exact operation

One invocation:

```sh
/opt/homebrew/bin/gcloud auth login debynyhan@signmons.com --force --no-activate --brief --quiet --verbosity=none
```

Owner personally selects debynyhan@signmons.com and completes Google browser/MFA/consent. Seven scopes: openid; https://www.googleapis.com/auth/userinfo.email; https://www.googleapis.com/auth/cloud-platform; https://www.googleapis.com/auth/appengine.admin; https://www.googleapis.com/auth/sqlservice.login; https://www.googleapis.com/auth/compute; https://www.googleapis.com/auth/accounts.reauth. No alternate account, ADC update, impersonation, import, manual-code fallback or repeat. Do not share passwords, codes or authorization URLs in chat.

SDK exception explicitly covers OAuth/browser/callback traffic, internal authentication retries and persistent credential/token/cache maintenance. Internal request count UNKNOWN. Existing credentials/cache remain afterward; no sign-out, revocation or cache erasure. No resource probe, SQL, key/IAM/secret change, deployment, payment/refund/customer/support contact or spending action.

November16 Eastern: start no earlier than11:15a.m. (16:15Z); launchbefore11:18 (16:18Z); at most300seconds sign-in; independent cleanup by11:25 (16:25Z). One conditional eight-second existing-owner cache-validity read only after exit0, owned leader/group absence and unchanged configuration. Required coverage strictly beyond12:15p.m. (17:15Z); token discarded immediately, safe result only. Failure ends the attempt without retry. The implementer must verify the11:15 lower bound immediately before launch: the unchanged executor enforces cutoff/cleanup, not an automatic start gate. An early login is not permitted merely to wait for the session.

R53 recovery cutoff remains11:20. If sign-in/closure completes too late, recovery does not launch; its deadline is not extended. Recovery/qualification/native decisions remain separate. No promise of payment completion follows from credential validity.

## Existing executor and readiness

Reuse the exact TR21 executor hash9a1688d47181d96312047d8e2dca96fa01ab2bb2234449ee5a8ecfab508bcd38. Only TR/date/source/decision/reservation/attendance bindings change, not algorithm. Sourcec57cb9c includes current renewal-tree state and native dependencies. Prepared executor /private/tmp/signmons-tr25-owner-signin.py has PENDING_EXACT_TR25_APPROVAL and must refuse absent committed authority.

Actual executor.preflight and packet.renewal_preflight are exercised only through inert in-memory proposed-authority reads. No main/execute/reservation/cache access. Verify committed source,51combinedSDK files,9login files, installed runtime and configuration metadata. Existing owned-process group/deferred-signal registration/DEVNULL streams/bounded termination/reaping/independent absence checks remain; unknown closure blocks cache access. Exclusive0700 renewal root renewals/20261116-tr25,0600 safe receipts and one-use lock. Remove owned temporary executor and recovered template after closure or abandonment; preserve unrelated browsers and SDK cache.

Finite checklist: exact template recovery/hash; constant-only binding review; actual inert preflight; owner exact sign-in/scopes/cache/cleanup approval and browser readiness; one invocation/conditional validity check; independent process/custody/executor cleanup and safe result. First three are local prerequisites; live items pending. Readiness: APP013_P08_TR25_SOURCE_READINESS_20261116.json. Implementer owns launch comparison/closeout, owner/credential custodian owns sign-in and exception.

Availability and preparation do not authorize credentials; exact owner approval is required before launch. Observable finish is VALID_THROUGH_CUTOFF or bounded stop with independent closure, not application authentication or payment. Current provider/private bindings remain UNKNOWN. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. No scope deviation beyond existing approved CT4 adoption in R53.

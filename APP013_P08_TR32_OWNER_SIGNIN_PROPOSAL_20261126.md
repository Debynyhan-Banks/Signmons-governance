# TR32 — proposed owner sign-in for R59

PREPARED FOR REVIEW, NOT APPROVED. The owner confirmed availability November 26 from 8:45 through 9:55 a.m. Eastern, Terminal/browser readiness and no overlapping Signmons operation. Backend source is b72ecb89f1907a25c988bbe3f33388bfdab77976. R59 local packet readiness is complete; its 557-test proof is reused, not newly run here. R58 remains consumed. ED2's disabled-endpoint observation is historical. Current credential coverage, full connected effective access and current provider/account state remain UNKNOWN. This is the existing credential prerequisite for the same APP-013 / 3A / P08 admitted-job journey, not application authentication or payment approval.

## Exact action and boundaries

Exact command: `/opt/homebrew/bin/gcloud auth login debynyhan@signmons.com --force --no-activate --brief --quiet --verbosity=none`.

One Google browser sign-in personally completed as debynyhan@signmons.com. The same seven scopes are reviewed: openid; https://www.googleapis.com/auth/userinfo.email; https://www.googleapis.com/auth/cloud-platform; https://www.googleapis.com/auth/appengine.admin; https://www.googleapis.com/auth/sqlservice.login; https://www.googleapis.com/auth/compute; https://www.googleapis.com/auth/accounts.reauth. No alternate account, ADC, impersonation, import, manual-code fallback or operator retry. Never share passwords, codes or authorization URLs in chat.

The explicit SDK exception covers OAuth/browser/callback traffic, internal authentication retries and persistent credential/token/cache maintenance. Its internal authentication request count remains UNKNOWN; one operator invocation is not a one-network-request claim. Existing cache remains after closure; no sign-out, revocation or cache erasure. No provider-resource probe, SQL, IAM/secrets/key change, deployment, payment/refund/booking/customer/support contact or new spending allowance.

Proposed November 26 Eastern timing: earliest 8:55 a.m. (13:55 UTC), launch strictly before 8:58 (13:58 UTC), at most 300 seconds for sign-in, and independent cleanup by 9:05 a.m. (14:05 UTC). One conditional eight-second existing-owner cache-validity read is allowed only after exit 0, owned leader/group absence and unchanged configuration. Required credential coverage is strictly beyond 9:55 a.m. (14:55 UTC); the token is discarded immediately and only a safe classification is retained. Owner attendance ends at 9:55 a.m. Failure consumes the attempt without retry or fallback. The implementer manually enforces the lower start bound; the unchanged executor enforces cutoff and cleanup. Late completion cannot extend any R59 deadline. These proposed times require final feasibility comparison and exact approval; they are not authority.

## Reuse, custody and finite checklist

Reuse the exact retained TR21 template SHA256 9a1688d47181d96312047d8e2dca96fa01ab2bb2234449ee5a8ecfab508bcd38. Only TR/date/source/decision/attendance constants change; no algorithm is reconstructed or changed. Prepared executor `/private/tmp/signmons-tr32-owner-signin.py` is mode 0600 and keeps `PENDING_EXACT_TR32_APPROVAL`. It cannot use a draft or inert preflight fixture as committed live authority.

The exclusive operation root is `evidence/APP-013/p08-narrow-access-check-local-20261101/renewals/20261126-tr32`, mode 0700 if later authorized, with mode 0600 safe reservation/result receipts. Passwords, codes, tokens and login output are not retained. Existing process registration, bounded termination/reaping, configuration comparison and independent owned-process/group absence checks remain unchanged. Remove only the owned executor and `/private/tmp/r59-tr21-template.py` after closure or abandonment; preserve unrelated browser/cache state and prior receipts.

1. Verify the retained template, exact constants-only difference, committed backend source and current source/SDK/configuration metadata.
2. Run the actual executor preflight and existing packet.renewal_preflight through inert proposed-document reads, actual attendance evidence and actual/proposed clocks. Do not execute, reserve, read credentials or launch a browser.
3. Obtain exact owner approval of this proposal, seven scopes and SDK/cache exception. Only then create the real committed decision and bind its commit; compare actual source, command, pins, attendance and clock again before launch.
4. Under that later authority only, make one sign-in invocation and at most one conditional cache-validity read.
5. Independently verify process/custody/executor closure, unchanged configuration and safe result. Stop on uncertainty; preserve deadlines and no-retry.

Preparation files are this proposal, APP013_P08_TR32_DECISION_DRAFT_20261126.json, APP013_P08_TR32_OWNER_ATTENDANCE_20261126.json, APP013_P08_TR32_SOURCE_READINESS_20261126.json and the ephemeral executor. No actual decision is created. The externalActionAuthorized:true object nested under decisionForReview is proposed text only; the draft envelope remains externalActionAuthorized:false. Attendance confirmation does not approve sign-in or later stages.

## Readiness, owners and next result

APP013_P08_TR32_SOURCE_READINESS_20261126.json records source/hash/time, actual local preflight results, 51 existing SDK pins plus nine sign-in-specific files, configuration metadata, exact differences and unresolved gates. Governance reads are inert proposed-document bindings; backend committed-source reads, installed SDK checks and nonsecret configuration inspection are actual. This is review-ready only after local checks pass, never launch-ready without exact approval. Credential stores and provider state are not read. Existing validators check actual dynamic source/configuration settings; fixtures and past observations do not establish current live access.

Existing regressions and reviewed TR21 process behavior are reused. No runtime/browser tests are claimed as newly run. Governance frozen-baseline, full consistency, architecture, safeguard tests and whitespace checks accompany this document-only preparation. Rollback/disabled state is the unchanged pending-approval executor with no reservation root; abandonment removes only owned temporary files. Any failure blocks launch without silently changing pins, windows or allowance.

Implementer owns command/source/time comparison, supervision, cleanup and evidence. The owner credential custodian owns confirmed attendance/browser readiness and the still-pending sign-in/scopes/cache decision. R59 recovery, current qualification and native connected payment each retain separate exact decisions. Observable TR32 finish is VALID_THROUGH_CUTOFF or a safe stopped result with verified closure; it is not successful application authentication, live readiness or 3A acceptance. Remaining facts: exact TR32 authority, current credential horizon and effective connected provider state are UNKNOWN/pending.

Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. R56's historical AUTH_OUTCOME_UNKNOWN and null success-only proof remain unchanged. No scope deviation. No sign-in prompt, reservation or provider action has started.

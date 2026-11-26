# APP-013 / 3A / P08 — local sign-in browser preference review

PROPOSED ONLY. No implementation or live sign-in is authorized by this document. No attendance window is proposed.

## Demonstrated gap and acceptance trace

The same admitted-job Sandbox payment criterion remains unchanged: $99 USD test Checkout, authentic matching signed event/account/job/amount/currency, cleared application gate, independent closeout and owner acceptance. The existing sign-in prerequisite must visibly reach the owner before any credential horizon can be established.

TR34 ended SIGNIN_UNCONFIRMED after 300.115 seconds, with no cache check and verified closure. The owner now reports that no sign-in page appeared. Its exact historical cause remains UNKNOWN. The live local NSWorkspace routing API currently resolves HTTP and HTTPS to Safari. A stored LaunchServices preference still names Atlas and disagrees; that preference is not authoritative active routing. Neither observation records historical TR34 routing. The current SDK calls Python webbrowser.open, ignores its Boolean result and then waits for the OAuth callback; its output was discarded by the reviewed supervisor. This is a demonstrated observability/browser-selection gap, not evidence of a Google account, Stripe or authentication refusal.

Backend source is b72ecb89f1907a25c988bbe3f33388bfdab77976. APP013_P08_TR34_BROWSER_DIAGNOSIS_20261126.json records exact current source hashes and locations, owner observation and current-only metadata. Reuse the complete reviewed TR21 sign-in supervisor, current SDK/source/configuration checks, owned process group, 300-second bound, exact command/scopes, conditional cache-validity check and independent cleanup. The approved Terminal transport correction is separate and remains verified.

## Alternatives and recommended bounded change

1. Keep the unchanged default-browser procedure and attend the API-resolved default (currently Safari). This makes no launcher change but retains dependency on the current OS default and unobserved browser-launch behavior.
2. Recommended: add exactly BROWSER=chrome to the sign-in child environment after the existing environment validation, and verify the resulting browser controller and harmless visible delivery locally. This affects only that child process. It does not change the Mac default, SDK configuration files, browser profiles, project settings or any provider resource.
3. Changing the Mac default browser or building an exclusive custom OAuth/browser dispatcher would broaden the change unnecessarily; neither is proposed.

Python treats BROWSER=chrome as Chrome-first preference, not exclusive routing. If Chrome launch returns false, Python can fall through to another controller. Do not claim an exclusive pin or that this proves TR34's cause. The local preflight must refuse readiness if Chrome cannot be selected and successfully opened with a harmless blank-page marker. A future real sign-in remains separately approved and requires confirmation that its actual page appeared. The harmless test verifies the selected first controller directly; it does not exercise OAuth or claim the SDK fallback loop was changed.

The proposed implementation adds the exact constant only to this reviewed sign-in procedure, after q.sdk_environment has validated the existing baseline. Do not relax the shared ambient-override guard or change the SDK, OAuth URL construction, account, seven scopes, callback, authentication retries, credential cache policy or success checks. Keep raw OAuth URLs/codes/tokens and SDK output out of chat, logs and retained receipts. This is an explicit additional process-environment exception, not an assertion that it was already authorized by TR34.

## Local section card and finite checklist

Expected files in this governance checkout: `APP013_P08_CHROME_FIRST_SIGNIN_TEMPLATE_20261126.py`, `APP013_P08_CHROME_FIRST_SIGNIN_TEST_20261126.py`, `APP013_P08_CHROME_FIRST_SIGNIN_VERIFICATION_20261126.json`, and this proposal/readiness record, plus temporary owned harmless-test artifacts. The supervisor baseline is the exact retained TR21 template SHA256 `9a1688d47181d96312047d8e2dca96fa01ab2bb2234449ee5a8ecfab508bcd38`. Focused commands are `python3 APP013_P08_CHROME_FIRST_SIGNIN_TEST_20261126.py --local-tests` and, once only, `python3 APP013_P08_CHROME_FIRST_SIGNIN_TEST_20261126.py --browser-once`. No backend runtime or provider changes. Record source hashes before implementation; leave the template inert until a later exact sign-in decision binds it.

1. Preserve the existing command, scopes, authority/source/SDK checks, deadlines, process ownership, interruption handling, conditional cache read and closeout. Record the exact minimal environment difference.
2. Test the actual pinned Python browser selection under the actual SDK child environment with the reviewed constant addition. A mere ambient BROWSER value is ineffective because sdk_environment constructs a fresh environment.
3. Test refusal when Chrome is unavailable or the selected controller differs. Verify timeout/interruption cleanup and that no credential/provider path is invoked by the local tests.
4. Perform one harmless browser-visibility test using only a uniquely identifiable about:blank marker and one invocation of the selected Chrome controller; no OAuth URL, sign-in, external page, cache or provider call. Bound the opener to 10 seconds, visibility observation to 20 seconds and owned-tab/process/file cleanup to 20 seconds, with a 60-second overall test bound. Negative unavailable-controller, timeout and interruption cases use injected seams only, without additional browser launches or UI retries. Identify and close only the owned test tab, preserving all existing browser tabs. If ownership or cleanup cannot be verified, stop and report it; do not act on an arbitrary tab.
5. Independently review unchanged supervisor semantics and the new exact environment exception. Record safe selection/visibility/closure results and remaining UNKNOWNs. Run frozen baseline, full consistency, governance safeguards, backend wrapper, architecture and both whitespace checks. Reuse unrelated passing runtime tests; do not claim them as newly run.

If the actual harmless browser test fails, stop before scheduling another sign-in. Do not add retries, fallbacks, raw diagnostics, another helper or broader environment permissions without reviewing the demonstrated gap.

## Authority, boundaries and finish

The owner decision requested is local implementation and these harmless local tests only. It authorizes no credential read, sign-in, authentication request, provider call/configuration, IAM/key/secret change, payment, booking, customer/support contact or spending. No Terminal attendance or timed password prompt is needed. Future sign-in review must explicitly name the Chrome-first child-environment exception, source hashes and exact future window.

The implementer owns local implementation/testing and owned-artifact cleanup; the independent reviewer checks preserved semantics and evidence; the owner chooses this narrow environment change and later external actions. Rollback is removal of the local prepared template/test artifacts, with no change to the Mac default or provider state. Observable local finish is verified Chrome-first controller selection and harmless visible delivery/owned-tab closure, or a truthful bounded failure. It is not successful sign-in or 3A acceptance.

The section order/count, acceptance criterion and connected customer workflow are unchanged. Accepted milestones remain 4/8; 3A OPEN; R1 newly closed 0/27. This proposes only the stated process-environment addition; no other scope deviation. The repository rule says: "Do not change scope, dependencies, section IDs/counts, acceptance criteria or substantial prerequisites without explicit owner approval BEFORE implementation." TR34 allowed constants-only reuse of the original supervisor; this new environment exception needs an explicit decision before implementation.

Preparation review: independent source/scope/bounds review passed; all three recorded source hashes matched. Frozen baseline, complete consistency, 25 governance safeguards, backend wrapper, architecture and both whitespace checks passed. No proposed implementation, runtime test, browser launch, credential read or provider call has occurred.

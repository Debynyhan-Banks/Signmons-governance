# APP-013 / P06 R11 execution-efficiency change request

Status: owner decision required; no implementation or live authority.

## Demonstrated gap

R11 has become an inefficient manual loop. Separate packet preparation, helper installation, hidden-input LOGIN, timed run, browser markers and hidden-input closeout require repeated conversation turns. Several valid fail-closed outcomes consumed short windows before the customer journey could finish. Enabled17 finally reached real phone verification and `CORRECTION_REQUIRED`, but its 15-minute connected runtime expired before explicit corrected-address resubmission.

Read-only operation `e21271e1-5057-4b67-9229-bc484b8af3a2` now finds one staging and three controlled phone holds totaling 2,000,000 USD micros, with zero invalid rows. Another 500,000-micro flow exceeds the consumed 2,000,000-micro ceiling. These are conservative retained liabilities, not confirmed provider charges. The owner reports that the repeated manual loop has also consumed substantial assistant credits.

The frozen R11 acceptance criterion is unchanged: one protected journey must verify phone access, confirm an eligible address, explicitly submit the reviewed draft and create exactly one correlated job. No payment, booking, dispatch or send authority follows.

## Alternative 1 — one-command attended coordinator and one final bounded packet (recommended)

Implement and test a local-only attended coordinator around the existing reviewed controller. It must:

1. accept one owner-operated hidden `neondb_owner` input, keep it only in process memory and zero it on every exit;
2. validate exact packet, plan, helper hashes, absolute windows, clean source and unused markers before action;
3. open the bounded runtime LOGIN once, wait locally for the exact run start instead of asking the owner to time a second command, then invoke the existing activate-before-deploy controller once;
4. print the exact returned URL and pause for the owner-operated browser journey, with no browser automation, provider retry, resend or replacement request;
5. accept one explicit local completion/stop signal and invoke the existing closeout once, while also forcing closeout before the fixed deadline on a catchable interruption or timeout;
6. preserve every existing reservation, stage-evidence, no-retry, zero-traffic, revocation, tag-removal, runtime-disable and readback guard; it may not weaken the underlying controller or application policy.

Use injected fake clocks and child processes to prove early launch waits without action, exact ordering, one password prompt, no automatic retry, browser-wait interruption, deadline closeout, child failure closeout, marker reuse refusal and password zeroization. This is a private operator helper only: no application route, schema, deployment behavior or customer UI change.

Separately permit exactly one future packet to preserve all four holds and bind `flowUpperBoundMicros: 500000` with `accountCeilingMicros: 2500000`. This policy allowance creates no packet or external authority by itself. Current admission code already supports the numeric ceiling. The future browser instruction will use the already observed customer-confirmed standardized address from the beginning, reducing the chance of another correction round while never silently adopting provider content.

After local coordinator review, one owner-selected future window, current read-only qualification, fresh packet review and one exact execution approval remain required. The intended operator interaction is then one terminal command, one browser journey and one final result report.

## Alternative 2 — retain the existing three-command process

Preserve the four holds, approve one future 2,500,000-micro packet and continue separate `--open-login`, timed `--run` and `--closeout` commands with intermediate chat markers. This changes less local helper code but repeats the demonstrated interaction and timing risk.

## Alternative 3 — reconcile and settle holds before another live run

Do not increase the ceiling. Design authoritative provider/billing reconciliation, append-only settlement evidence and admission arithmetic that counts only safely settled liability. This requires a new implementation/test card and separately approved database migration or write. No hold may be deleted, reset or silently excluded. This is the correct long-term R12 direction but is larger than the remaining R11 acceptance run.

## Alternative 4 — stop live R11 acceptance

Keep all holds and the current ceiling unchanged. Do not prepare another live packet. P06 remains 12/14 with R11 and full R12 open.

## Decision boundary

Recommended alternative 1 requires explicit owner approval before local implementation. Approval may include both the local-only coordinator work and the one-future-packet 2,500,000-micro policy allowance, but it does not authorize packet preparation, database LOGIN or mutation, activation, deployment, traffic change, provider request, verification code, browser/customer action, hold release, secret/IAM change, billing change or live execution.

No scope or acceptance change is implemented by this request.

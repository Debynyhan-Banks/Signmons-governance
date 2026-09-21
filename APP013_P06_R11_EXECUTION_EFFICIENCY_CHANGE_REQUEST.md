# APP-013 / P06 R11 execution-efficiency change request

Status: alternative 1 implemented and locally verified; one-future-packet ceiling policy approved but unused; no packet or live authority.

## Owner decision — 2026-09-21

The owner approved alternative 1 for local one-command attended-coordinator implementation and testing. The same decision permits exactly one future R11 packet to bind `flowUpperBoundMicros: 500000` and `accountCeilingMicros: 2500000` while preserving all four existing holds. It expressly does not authorize packet preparation, LOGIN, database mutation, activation, deployment, provider requests, verification codes, browser/customer action, hold release, secret/IAM change, billing change or live execution.

## Approved implementation card

- **Section and finish:** P06-R11, controlled acceptance execution. The frozen finish remains one protected phone verification, eligible-address confirmation and explicit reviewed submit that creates exactly one correlated job or returns a truthful refusal. This helper advances that same journey by removing the repeated owner-timed Terminal handoffs; it does not earn acceptance.
- **Inspected gap and source:** backend `be624c1`; governance `8a36139`; four valid holds and the stopped preparation are recorded in backend `evidence/APP-013/p06-r11-1430-liability-stop.md`. Existing packet-specific `r10-control.mjs` commands require three separate hidden prompts and owner-timed invocations, which repeatedly consumed windows before R11 could finish.
- **Reuse:** `scripts/p06_private_input.py` for hidden TTY input and complete `READY` framing; packet-specific `r10-control.mjs --check|--open-login|--run|--closeout`; `scripts/p06-r10-controller.mjs` for strict plan review, at-most-once activation/deployment/containment and final closeout readback. The coordinator must call these interfaces rather than duplicate their database, Cloud Run or provider logic.
- **Expected files/interfaces:** add `scripts/p06_r11_attended_coordinator.py` and `scripts/test_p06_r11_attended_coordinator.py`; record local evidence in `evidence/APP-013/p06-r11-attended-coordinator.md`; update current governance status after validation. The command accepts only `--run <absolute private packet directory>`. A future packet must bind the coordinator hash in its private `helper-binding.json`. No application route, schema, dependency, deployment behavior or customer UI changes.
- **Sequence and authority boundary:** perform local/private path, ownership, mode, packet/approval/window, helper-hash, clean-source and unused-marker review; wait locally until the approved database window; run exact no-action `--check`; reserve one exclusive coordinator marker; prompt once; call `--open-login` once; wait locally until runtime start; call `--run` once; print only the exact returned controlled URL; wait for one local `DONE`/`STOP`, interruption or deadline; call `--closeout` once and require its exact verified result. Before the exclusive marker there is no action. After any possibly started live child, failure or interruption must enter the single closeout path. No child mode may be retried.
- **Data/state/retention:** the owner credential remains one mutable byte array in coordinator process memory, is forwarded only through anonymous child stdin pipes after exact `READY`, is never placed in arguments/environment/files/output and is overwritten on every exit. The browser remains owner-operated. Raw phone, code, address and customer text never enter the coordinator or evidence. Durable packet/controller reservations, holds and closeout evidence remain authoritative.
- **Finite implementation checklist:** (1) strict local review and exclusive marker; (2) injected clock/child/input/output coordinator core; (3) production adapter with one hidden prompt, exact child protocol and bounded waits; (4) one closeout funnel for completion, stop, timeout, signal and child failure; (5) focused tests and regression/governance checks; (6) review evidence and synchronized handoff. Exit is review-ready local code with zero external calls and no packet.
- **Tests:** `python3 -B -m unittest scripts/test_p06_r11_attended_coordinator.py scripts/test_p06_private_input.py`; focused Node controller regression `node --test scripts/p06-r10-controller.test.mjs`; backend architecture/governance/whitespace checks; governance frozen-baseline, consistency, 21 policy tests and whitespace check. Injected fakes must cover early launch with no action, exact ordering, one prompt, no automatic retry, duplicate/coordinator-marker refusal, browser interruption, deadline closeout, open/run child failure closeout and credential zeroization. A subprocess protocol test must prove exact `READY` handoff and no secret output. No live browser/provider/database test is authorized here.
- **Dependencies and gates:** implementer owns this local patch. The owner has approved the local patch and one-future-packet ceiling policy. A future owner-selected window, current read-only qualification, fresh packet review and exact execution approval remain missing and separately required.
- **Exclusions and rollback:** no packet, database write/LOGIN, provider/Cloud call, browser action, deployment, secret/IAM/billing change, hold release or settlement design. Rollback is removal of the new local helper/tests before any future packet binds them; the service remains inactive with normal traffic on the baseline revision.
- **Observable result and size:** small local operator-boundary change with high confidence after the injected failure/recovery suite. Finish is a committed helper whose review proves one prompt, one attempt per child mode and mandatory closeout; P06 remains 12/14 until live R11 and full R12 succeed.

## Implementation result — 2026-09-21

Backend `26404ff` implements the approved helper and focused tests; `evidence/APP-013/p06-r11-attended-coordinator.md` records the boundary and results. Coordinator/private-input tests pass 24/24, the existing R10 controller tests pass 24/24, and the full backend passes 129 suites / 2,360 tests with three existing skips, plus build, lint and architecture checks. No packet or external action occurred. The one-future-packet 2,500,000-micro policy allowance remains available but unused. P06 remains 12/14 with R11 and full R12 open.

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

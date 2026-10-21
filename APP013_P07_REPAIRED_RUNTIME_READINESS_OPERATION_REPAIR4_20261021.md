# APP-013 / 3A / P07 repaired-runtime readiness operation repair 4

Status: **owner-approved and installed for one operation; not yet attempted**.

## Exact binding and purpose

- Section: R1-W01 / APP-013/3A/P07.
- Fresh plan `0f2daeb9-fc75-40c2-b66b-097b6c986d7d`, packet `67157149-adc5-4a5b-a5c3-93066071403e`, operation `609bca17-276b-493f-bbd8-6edf7d5ad7e9`.
- Package: `/private/tmp/p07-repaired-runtime-readiness-20261021-repair4`.
- Window: October 21, 2026, 7:00–8:30 a.m. Eastern; start strictly before 7:15; ordinary work ends 8:00; containment through 8:20; retirement by October 22 at 7:00 a.m.
- Exact source/image: `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd` / `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da`.
- Accepted job: `9180bef4-561d-47a0-869f-925e6a3dfd96`.

This is a fresh operation. Repair 3 and every earlier readiness operation remain consumed. Repair 4 retains all previously approved boundaries and adds explicit PostgreSQL system-root certificate verification on both administrator and restricted-role paths. Raw database errors remain in process memory only and map to fixed secret-safe stop codes.

## One no-retry operation requested

Approval would permit only these action identifiers:

- `create_one_restricted_database_role`
- `create_six_secret_resources_and_versions`
- `create_one_service_identity`
- `add_seven_resource_secret_bindings`
- `create_disable_readback_one_stripe_destination`
- `deploy_one_zero_normal_traffic_revision`
- `mandatory_containment_and_retirement`

The operation runs read-only Cloud, IAM, Stripe Sandbox and exact-job preflight. If they pass, it creates restricted role `p07_payment_runtime`, exactly six short-lived P07 secret resources/versions, one P07 runtime service identity and exactly seven resource-level Secret Accessor bindings. It creates one Connected accounts Stripe Sandbox destination at the tagged candidate `/webhooks/stripe`, immediately disables it and verifies zero deliveries. It deploys exact revision/tag `signmons-calldesk-staging-app013p07atomic1` / `app013-p07-atomic` at zero normal traffic while preserving 100% normal traffic on `signmons-calldesk-staging-app013dbrot2`. It then closes the database role and verifies containment.

The owner enters only the current CHILD administrator password and the creation-only webhook signing secret through hidden local prompts. The connected-account ID is read from the exact tenant record only into process memory, compared with the sanitized Stripe preflight hash, cleared and never displayed or persisted. No password, account ID, signing secret, database URL or private link belongs in chat.

Checkout, card entry, payment, refund, booking, customer contact, message delivery, test event, event resend and normal traffic are forbidden. Automatic retry is false. Any run reservation consumes this operation, including a stopped run. P08 and 3A acceptance remain separate.

Cloud allowance is USD 1.00 and is not a provider-enforced billing cap. Six temporary secret versions have a conservative full-month equivalent of up to USD 0.36 above the free tier and must retire by the fixed deadline. Success is only `P07_REPAIRED_RUNTIME_READY_DISABLED`. Failure is one named `P07_STOP_*` with mandatory containment; recovery may clean up but cannot retry readiness.

## Prepared package and command boundary

The package passes **35/35 focused tests**, Python/Node syntax, architecture, frozen-baseline, cross-repository consistency and no-action checks. Exact approval validates against the binding. No attempt, mutation journal or provider receipt exists.

- Manifest SHA-256: `62a84e3fe93ba16d20e4343c37054c57f680345e980b367e78c2e238166d1903`.
- Controller SHA-256: `b4b6c1d56333ed968eb6b122f4f613727453d5928cdc5f84b503333b8268743d`.
- Test SHA-256: `ceb667eac7b9d005c339da97a1eb21e9dce1870d5cbead01cd612935ef0719d4`.
- Binding SHA-256: `3d4e7239e14f4095a2ec84ea95a4d481846c94d2b6bdeef34c93cf8321a96d63`.
- Owner-approval SHA-256: `eb8c0a221e135bf01a07796922a1b946f6ebfac3eb65e3f90d627d22c9579f72`.

The approved one-use attended command is:

```sh
cd '/private/tmp/p07-repaired-runtime-readiness-20261021-repair4' && /opt/homebrew/bin/python3 controller.py --run
```

It may run once starting at 7:00 a.m. Eastern and must start strictly before 7:15. The owner keeps Terminal open, enters private values only at hidden prompts and reports only fixed status lines. No retry is allowed.

## Decision requested

**Decision:** Debynyhan Banks replied **“Approve repair 4.”** Approval was recorded at `2026-10-21T10:31:27Z` against immutable governance commit `27de9cff2b8743963cb102362ce20180dc4a890e`, proposal SHA-256 `19735870a62057d75542182bd541a949aede5d4d8eb1ce2279188e9f7ea81cc0`. It covers this exact one-use operation, listed mutations, allowances, mandatory containment/retirement and window. It does not authorize P08, payment, booking, customer action or normal traffic.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation.**

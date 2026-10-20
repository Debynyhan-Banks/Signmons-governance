# APP-013 / 2B / P06-R11 — child target reconciliation

## Correction

The October 8 post-cutover qualification selected the wrong database target for P06 liability/runtime state. This is an implementation-card error, not demonstrated production address-schema drift.

The successful October 2 liability reader imported `TARGET` from `scripts/p06-backup-once.mjs`, which fixes P06 child branch `br-sparkling-sun-ay6gr5e8` and direct endpoint `ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech`. Enabled35 runtime packet and revision metadata reference `signmons-staging-p06-child-database-url`. The three October 8 packages instead fixed production parent endpoint `ep-nameless-frog-ayk5gr5y.c-5.us-east-2.aws.neon.tech`, following the credential-recovery target rather than the P06 runtime target.

The parent accepted authentication, identity, read-only mode and the account-scoped phone audit query, then failed at the P06 address relation query. Those receipts remain valid for exactly those parent observations, but they do not qualify P06 child liabilities or runtime state. Do not infer an address-table defect, permission problem or migration requirement from them.

## Current child boundary

- Child secret `signmons-staging-p06-child-database-url:2` remains enabled and unchanged.
- Its payload must not be read or copied merely to continue diagnosis.
- The child runtime role is designed to remain `NOLOGIN` outside approved activation.
- A child `neondb_owner` credential may be used only through private hidden entry after the owner confirms current custody and separately approves a future read-only window.
- No credential reset, secret read/version change, LOGIN change, migration or child write is authorized.

## Next decision

If the owner has the current child-branch `neondb_owner` password saved, prepare one fresh child-target read-only liability/runtime qualification with new identities and a future 25-minute Eastern window. It may read only the fixed phone/address aggregates and child approval/role/session classifications, then roll back and close. It stops before Cloud Run, artifact or Twilio metadata; those remain a later phase after a complete child receipt.

If the owner does not have the child owner password, stop and prepare a separate credential-custody decision. Do not try the production password against the child, read the child secret, reset a role or enable the runtime role under this authority.

P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation. Target correction recorded before another implementation or external read.

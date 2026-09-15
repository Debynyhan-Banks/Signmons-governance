# P06-R02 PostgreSQL18 local compatibility qualification

Owner explicitly approved installing PostgreSQL18 locally and rerunning the synthetic rehearsal, leaving existing databases and staging untouched. Entry backend99f4a45/governance38b5bae. This is the version qualification already named in R02, not a new baseline task. R01's PostgreSQL16 proof remains valid.

Finite work: install the versioned Homebrew PostgreSQL18 binary without starting a service or changing existing clusters; create a private owned temporary cluster/socket with TCP disabled; parameterize the existing verify-p06-migration-upgrade.mjs only for this guarded local socket; execute unchanged26 migrations/fixtures/assertions with Prisma7.10; stop the owned server and retain sanitized evidence. No cloud or real-data operations.

Expected files: existing verification script, this card, result evidence and synchronized current status. Guard custom socket to an owned private /private/tmp/signmons-pg18-* directory, enforce server major18 before database creation, continue rejecting arbitrary remote URLs. Default /tmp behavior for existing R01 remains. Validate syntax, default-target regressions, PostgreSQL18 full rehearsal, build/lint/unit/architecture/governance gates. Browser not rerun: no runtime/UI behavior changes. Existing full browser evidence is historical, not PG18 browser proof.

Finish: actual major18 migration/history/preservation/catalog/no-op/lock-failure result and confirmed shutdown. Package stays unaccepted; R02 connection/consumer/recovery gates remain. Stop on material dependency installation conflict, insufficient storage, unsafe cluster target or version mismatch; no forced linking, services start, target downgrade, old-database upgrade or backup/restore action. No scope deviation.

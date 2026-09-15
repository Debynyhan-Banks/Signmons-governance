# R02 local tooling card

Owner explicitly approved working locally tested dummy-input and managed-permission restore tooling. Entry backend7c9521b/governance08b2951; frozen/consistency checks passed. Scope traces to existing R02 recovery/access qualification. No external action authority.

Finite deliverable: (1) private terminal input helper with exclusive0600 passfile creation and fail-closed validation, tested through a pseudo-terminal using dummy secrets; (2) opt-in extension of existing migration rehearsal that reproduces observed managed role names/default ACLs/extension ownership using local NOLOGIN stand-ins, dumps as a restricted reader, compares all23 tables under a shared snapshot and restores metadata; (3) actual tests and exact limitations, not a claimed production executor.

Files: scripts/p06_private_input.py, its unittest file, existing scripts/verify-p06-migration-upgrade.mjs, evidence and coordinated governance status. No runtime app change. Use existing PG18.6 private no-TCP local cluster; only random owned fixture databases and newly created tracked local stand-in roles removed afterward. Role collisions stop. No real passwords, Neon URL connections, encrypted image mutation or live data. Private-input CLI remains gated from real use until separate mount/handoff checks.

Checks: input success/escaping/0600/no echo, cancellation/EOF/timeout, insecure path/symlink/existing-file refusal; managed metadata archive/restore, missing-role failure, all-table row comparison and corrupt-archive rollback; existing migration/no-op/constraint/lock gates. Syntax/format, lint/build/architecture,21 governance tests, full consistency/baseline, whitespace. No UI feature or browser acceptance claim.

Finish is working local proof or exact failure evidence. Synthetic paths may use private /tmp and therefore do not claim encrypted-storage qualification anew. Any remaining real-run authorization/enforcement gap stays explicit. Preserve12-task denominator. No scope deviation.

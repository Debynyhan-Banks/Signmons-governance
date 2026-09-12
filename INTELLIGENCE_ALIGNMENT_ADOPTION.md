# Intelligence alignment — owner review candidate

Prepared 2026-09-12. Documentation only; NOT ADOPTED. This document and the linked intelligence documents are reference proposals under SYSTEM_OF_RECORD.md. They do not activate the supplied implementation mandate or override current canonical rules before reviewed adoption.

## Reconciled baseline

- Governance main af8a340; latest focused governance 387adec preserved.
- Backend main 2c7468b; APP-013 PR #21 head 330e402 preserved, including 6c9f660 policy-bound capture and disabled OAuth transport beyond the supplied 64942c0 snapshot.
- APP-013 remains sole Now, section 2B. Walkthrough 3/8 accepted (37.5%), not engineering/MVP completion. No ticket acceptance or release inferred from an open PR.
- Original backend checkout has unrelated modified/deleted files plus .agents/ and skills-lock.json; original governance has untracked .DS_Store. Neither was changed.
- Open governance PR #5 is unrelated marketing/governance work and must not be merged or edited by this alignment. Latest focused governance branch has no existing PR. These documentation PRs are stacked on the focused branches, not replacements for their pending work.

## Explicit conflicts and proposed resolution

1. The September 10 canonical product clarification explicitly deferred advisory behavior beyond MVP. The new bundle proposes advisory discovery, knowledge, memory and evaluation in an expanded Release A intelligence pilot. This is a real scope change, not a correction to past acceptance. Until reviewed adoption, CALLDESK_MVP_PLAN.md and the existing fixed eight-milestone walkthrough stay authoritative. Adoption must explicitly approve this additional pilot bar, with no rewriting of the original 3/8 denominator.
2. START_HERE/CODEX_APPLY_PROMPT omit BE-001 from the shorthand queue. Both detailed supplied documents include it between APP-015 and APP-016. Proposed queue: APP-017 → APP-018 → APP-019 → APP-015 → BE-001 → APP-016 → APP-033, only after full APP-013 acceptance. BE-001 is reconciliation against BE-008, not a rebuild.
3. The bundle says it supplies APP-017/018/019 ticket files and references intelligence spec/roadmap/matrix files; they were absent. This PR authors explicit draft ticket specifications and reference documents. They are not claimed to be supplied originals or implemented features.
4. Current Next is empty. This PR records a proposed queue without activating it. After adoption, synchronize governance board, global pointer and backend board together; do not independently promote any ticket or revive FE-014.
5. The supplied preflight checks .git directories and therefore misses worktrees; it also lacks source-version comparison/cross-repo Now checks. Original preflight ran successfully on saved checkouts, exposing stale backend APP-011 versus governance APP-013. A temporary worktree-compatible copy used git rev-parse for explicit paths and passed on the isolated current baselines. Version and cross-repo comparison were performed separately. No source installer modified canonical files.

## Review and adoption procedure

Review the paired documentation-only diffs against their focused base branches. Validate current parent heads again before adoption; rebase/reconcile if either advances, never force-update the implementation branch. These stacked PRs do not authorize merging parent PR #21 or older governance history.

Owner review must explicitly accept the Release A expansion and seven-ticket queue above. Record reviewer, date, paired PRs and acceptance decision here; status remains pending until then. In the reviewed adoption change, update WHAT_SIGNMONS_IS_AND_DOD.md and SAAS_SCOPE_DOD.md with the precise exception to the earlier advisory deferral, preserve its historical decision in ARCHIVE, and synchronize Next across both boards/pointer. Add the adopted intelligence documents to canonical precedence only through that reviewed change. Do not erase commercial Money/Growth diagnostics, security, operating or marketing gates.

After adoption, the owner authorizes routine progression inside the current ticket until its full acceptance and then through the approved queue. Required owner acceptance, production/provider/IAM/secrets/budget and release permissions remain gates. Save resumable handoffs; no automatic background execution or training. No routine choice-of-next-phase question is needed when the adopted queue resolves it. Blocked Now cannot be skipped.

## Sources and traceability

Original two supplied proposals are preserved under proposals/intelligence-alignment/. START_HERE.md and CODEX_APPLY_PROMPT.md were read from the Desktop bootstrap ZIP. New references: SIGNMONS_INTELLIGENCE_SPEC.md, INTELLIGENCE_MVP_ROADMAP.md, MVP_ACCEPTANCE_MATRIX.md. Existing contracts, ticket acceptance and code/evidence remain authoritative for present status.

Validation results and coordinated PR links are recorded in the PR descriptions. No runtime changes, new acceptance, deployment, calls, customer contact, charges or training are part of this PR.

## Preparation validation evidence

Complete governance consistency check passed on original saved preflight, isolated preflight and final documentation candidate. Required files, current APP-013 placement and new draft ticket screen references passed. Original and worktree-adjusted preflight passed; the latter changed only explicit-path resolution to support .git files in a disposable copy, leaving the ZIP untouched. The preflight is read-only, not an installer that applies a versioned patch; no source-version hashes were embedded, so dated SHA comparison above is the reconciliation evidence.

Backend build, lint and architecture passed. First test run: 1,987 passed, two failed, three skipped (shared dependency symlink path assertion; Calendar HTTP expected 429/received 401). Replaced only the isolated dependency symlink with a local APFS copy and reran unchanged tests: 1,989 passed, three skipped, 105 suites passed, one skipped. Calendar test passed unchanged; intermittent authentication/rate-limit test remains a runner risk, not a documentation regression fix. Runtime/configuration/schema/scripts/package diff against 330e402 is empty. Whitespace checks passed. Browser/UI tests are not applicable to documentation-only changes; no new UI or live acceptance evidence claimed.

Source SHA-256: mandate a72fb9911b542dc296eca4d08ac71313d09b6fbe2bcb4fcb88d18db6d951e5a0; scope/status ddd275252856e03e6805ec94aadbf17dcda032be6c4eef4d8bb0ddaa19f4af4f; bootstrap ZIP 2be54641a109f562d9dee9b73c189ff2cd157b5bbd6ad6244d07ab38c2a09fab. No supplied files overwritten.

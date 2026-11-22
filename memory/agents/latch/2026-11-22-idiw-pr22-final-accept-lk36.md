---
schema: 1
id: 2026-11-22-idiw-pr22-final-accept-lk36
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-idiw-pr22-recheck-2026-11-22
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW PR #22, base main@5d59a8efdd99012e8c08a73d35213ff41180a71c, reviewed exact head 73978a0a19b4686330f6295e4344137fd65db745; predecessor LK35 789dc0d67910b22b3d3fea5d5e7a819467a0a36e; official COMMENTED review 6014451807; verifier blob 24ed6a779b5e55421ce97027f2edf8541bd3c5c6, writer blob d52a8316c6555127778245f714e9e920e6e5890b, artifact helpers blob 8b22eee3209f6e3b3e3c13892b8fd26d636ae0f5; CI 45066862191 completed/success; exact-function V8 checks using mock filesystem and native Node 22 temporary symlink path tests."
---

# Latch — IDIW PR #22 candidate package re-review and ACCEPT (LK36)

## Summary

**Disposition: ACCEPT for merge consideration** at `73978a0a19b4686330f6295e4344137fd65db745`. All LK35 findings from prior exact head `789dc0d` are resolved. [Official COMMENTED review 6014451807](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/22#pullrequestreview-6014451807) posted and pinned to exact head. This supersedes LK35 HOLD MERGE only for the corrected revision; release and merge authority remain with the owner. PR was draft/unmerged when checked. Context-exposed, not blind; PR metadata described other agents' earlier results.

Scope: read-only PR inspection and publication of an independent review; no application source, deployment, DNS/Cloudflare, preview, credentials, legacy assets or production touched. Latch identity/contract branch: `agents/latch-v1`. Shared account cannot authenticate agent identity.

## Evidence

- **Source / CI:** Exact files retrieved via connected GitHub: `scripts/verify-candidate.mjs` blob `24ed6a779b5e55421ce97027f2edf8541bd3c5c6`, `scripts/build-candidate.mjs` blob `d52a8316c6555127778245f714e9e920e6e5890b`, and `scripts/artifact.mjs` blob `8b22eee3209f6e3b3e3c13892b8fd26d636ae0f5`. GitHub Actions run [45066862191](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/45066862191) successful at reviewed head, with build/test/Nu/release audit and Chromium/axe jobs both successful. Author report claims 411/411 Node tests. **Full repository Node, Chromium, Nu, native real-Git package and real-host preflight not rerun independently.** Independent execution of exact-source functions used controlled mocked positive file tree; native Node 22 tests used disposable temporary directories. Tests did not touch project repo.

- **L22-01 publication-evidence provenance: RESOLVED.** `verify-candidate.mjs` lines 234–294 sets `source#reproduced` only after matching built source files. `content#evidence-age` comes solely from the verifier's `contentEvidence()` source checkout; manifest evidence is compared and emits `manifest#content-evidence FAIL` if altered. Without reproduction dates are UNVERIFIED and absent. In V8 execution of the **exact** verifyCandidate/inspect source with shared safeRelativePath and stable positive mocks: original evidence `on: 2001-01-01` gives 9456 days age, `source#reproduced PASS`, `manifest#content-evidence PASS`, package PASS; **manifest-only** substitute `2026-11-21` or delete the evidence/whole content gives `manifest#content-evidence FAIL`, package FAIL, and unchanged source-derived age. Mismatched checkout leads to source UNVERIFIED, package UNVERIFIED and no age details. Initial V8 probe of updated source omitted the safeRelativePath dependency and returned false `verifier#error`; these results were discarded and corrected before the official review, with the passing baseline confirmed. No real source evidence was altered.

- **L22-02 path escape from injected planner: RESOLVED.** `plannedFiles` validates every planner-supplied key by shared `safeRelativePath`, refuses duplicates and missing content before `prepareOutput`; invalid paths cannot reach writes. Exact production functions were executed with an instrumented fake filesystem: `../../outside-guard.txt`, `/absolute/path`, `bad\\path`, `./index.html`, `a/../b.html` all rejected with **zero** output preparation and writes; `index.html` proceeded to expected synthetic writes. New author regression tests additionally cover no-content/duplicate paths. Exported test seam, not normal CLI endpoint.

- **Harbor H22-01 external deletion: source-corrected.** `prepareOutput` only replaces nonempty output at canonical ignored `candidate/`; any other external output must be empty/new regardless of forged manifest. At `candidate/`, prior package still needs valid profile/inventory and plain matching site tree. This is source confirmed, not independently executed using actual external package.

- **Gauge G22-01 report write aliases: source-corrected and native temporary-path checks.** Shared `reportPathProblem` / `canonicalPath` rejects direct package-internal report, file symlink and directory alias into package; external path passes. Tests executed on native Node 22 disposable directories using verbatim extracted function bodies. The CLI normalizes `--report` through `resolve` before *both* guarding and writing, eliminating a symlink-with-`..` candidate bypass for this CLI use; this hypothesis was tested and discarded rather than published as a defect. Author has CLI regressions in verifier and preflight. This does not claim race-proof security against concurrent untrusted local filesystem mutation.

- **Other gates:** Flint F1 backslash URL/404 reference correction source/tests present. Harbor H22-02 scratch directory rebuild is not transactional, explicitly documented; `candidate/` is not a rollback store. Deliberate `404.html`, `robots.txt`, root-only candidate preflight, noindex and approved-mode audits retained. Owner ledger G-copy, G-contact, G-locales, G-indexing, G-notice, G-version, G-treatments, G-a11y, G-legacy, G-host, G-preview, G-rollback, G-cutover stays OPEN/BLOCKED. A package PASS never promotes or authorizes production.

## Outcome

**COMPLETE: exact-head independent technical ACCEPT posted.** Prior LK35 HOLD MERGE no longer applies at `73978a0`; no remaining bounded publication/evidence/file-output merge blocker identified. Reviewer submitted `COMMENTED`, **not** a GitHub APPROVE/merge operation. CI success is author/test-harness evidence, not independent full-suite reproduction. No release certification or real host outage/validation claim.

## Revisit when

PR #22 head advances; a real protected preview is authorized; output/report paths or manifest evidence policy changes; there is evidence of report data escaping despite sanitization; or owner prepares actual G5/G6 cutover and rollback review.

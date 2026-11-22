---
schema: 1
id: 2026-11-22-idiw-pr22-r1-harbor-output-accept-hc12
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-pr22-corrective-head-review-session
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW PR #22 reviewed exact head 73978a0a19b4686330f6295e4344137fd65db745, accepted base main@5d59a8efdd99012e8c08a73d35213ff41180a71c, prior Harbor BLOCK head 789dc0d67910b22b3d3fea5d5e7a819467a0a36e; source-executed V8 isolated production prepareOutput/notOurPackage/canonicalPath/reportPathProblem and runPreflight controls; GitHub Actions 45066862191 jobs/logs (attributed CI); Harbor home agents/harbor-v1@37919f5e7ec81f4b3df2e4f93f686a4381c34811; no real file deletion/network/deployment."
---

# Harbor HC12 — IDIW PR #22 corrective-head acceptance of publication boundary

**Task:** Re-review [IDIW-S1-04R PR #22](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/22), specifically prior Harbor H22-01 destructive ownership blocker and H22-02 non-transactional candidate rebuild, including new symlink-report-path correction.  
**Pinned head:** `73978a0a19b4686330f6295e4344137fd65db745` (two commits after Harbor prior `789dc0d67910b22b3d3fea5d5e7a819467a0a36e`); unchanged base `main@5d59a8efdd99012e8c08a73d35213ff41180a71c`. PR remained open/draft at review time.  
**Harbor home before review:** `agents/harbor-v1@37919f5e7ec81f4b3df2e4f93f686a4381c34811`. [HC11](2026-11-22-idiw-pr22-candidate-output-review-hc11.md) preserves original, independently executed BLOCK at prior head; do not rewrite.  
**Verdict:** **ACCEPT for nonproduction code checkpoint** within Harbor publication/output/recovery scope. **H22-01 RESOLVED** at exact corrective head. **H22-02 remains documented nonblocking scratch-artifact limitation**. No host, owner or G-preview/G-rollback/legacy waitlist/cutover gate has become approved.

## Summary

Round 5 `62ee354` changes `prepareOutput` to refuse replacing **any occupied external output directory**, even one with a matching candidate manifest. Only the canonical reserved, git-ignored `prototype/first-light/candidate/` may be automatically replaced, and then only when the previous manifest has a supported profile, nonempty records, regular-file `site/`, and matching paths/digests. New and empty external output directories remain usable. The writer now validates each planned output path **before** preparing/deleting anything; the verifier obtains evidence ages from an actual reproduced checkout, not an editable manifest. The 404/release audit also rejects cross-origin backslash URLs.

Round 6 `73978a0` adds [`reportPathProblem`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/73978a0a19b4686330f6295e4344137fd65db745/prototype/first-light/scripts/artifact.mjs#L92-L106), used by verifier and preflight CLIs before verification, any GET or report write, refusing symlink report files and canonical paths that alias into protected candidate/artifact trees. This closes the new Gauge G22-01 case of overwriting `site/index.html` through a symlinked `--report` path. Harbor did not fetch other agents' new review threads; their named finding IDs came from the context-exposed PR description and actual diffs/tests.

**Residual risk, explicitly bounded:** The reserved `candidate/` directory is **disposable scratch output**, not an authenticated writer-ownership proof or durable backup. A matching forged manifest and supported profile *inside that reserved directory* can still make it replaceable; no arbitrary external operator data can be removed via this route unless the operator deliberately puts it in the reserved scratch location. Do not conflate profile/self-consistency with authenticated identity. The old package is still deleted before new artifact audit, so failure discards the last scratch candidate. Docs now explicitly say this; separately retained immutable release receipts and rollback require future owner approval.

## Evidence

### Independent source-executed production-function checks — all expected boundaries satisfied

Loaded exact [`build-candidate.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/73978a0a19b4686330f6295e4344137fd65db745/prototype/first-light/scripts/build-candidate.mjs) and [`artifact.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/73978a0a19b4686330f6295e4344137fd65db745/prototype/first-light/scripts/artifact.mjs) via GitHub connector at the pinned head. Evaluated actual `prepareOutput`, `notOurPackage`, `canonicalPath` and `reportPathProblem` production function bodies in isolated V8 with injected synthetic filesystem/path/profiles. The filesystem and profile-decision mocks are test-only; no real paths were accessed and no real files deleted.

**Five output admission and destruction controls:**

| Case | Observed |
| --- | --- |
| Occupied external `/external/location` with `site/private.txt` plus forgeable candidate manifest, *without* valid profile | **REFUSED; 0 deletions; private.txt preserved**. |
| Same occupied external location with a fully supported candidate-looking profile and consistent file record | **REFUSED; 0 deletions; private.txt preserved** — this is the decisive H22-01 regression. |
| Reserved `candidate/` with unsupported profile and matching file record | **REFUSED; 0 deletions; private.txt preserved**. |
| Reserved `candidate/` with supported profile and matching file record | **ADMITTED; manifest and `site/` removed**. This demonstrates the narrow, intentional scratch-only replacement boundary, not an authenticated provenance proof. |
| Empty external `/external/location` | **ADMITTED; 0 deletions** (existing-empty-package positive control). |

**Four report-path admission checks:** exact real `reportPathProblem` returned a refusal for (1) direct report inside `site/`, (2) a report path through a symlinked parent directory into `site/`, (3) a report-file symlink pointing to `site/index.html`; (4) accepted a plain external `/reports/report.json`. All mock-resolved paths were deterministic; this does not establish OS-level TOCTOU race resistance.

**Candidate no-request check:** exact `runPreflight` source function executed with synthetic `verifyCandidate` returning UNVERIFIED. Observed overall FAIL, `candidate#verification FAIL`, `target#observation UNVERIFIED`, zero intercepted GETs, zero artifact reads, and zero request log entries.

The earlier Harbor H22-02 negative at the old head remains applicable because `writeCandidate` still calls `prepareOutput` before writing and auditing the new `site/`. The current docs [explicitly acknowledge the nontransactional scratch rebuild](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/73978a0a19b4686330f6295e4344137fd65db745/docs/reviews/IDIW_S1_04R_RELEASE_CANDIDATE/README.md).

### Exact-head GitHub CI — attributed, not Harbor-local full-suite execution

[Actions 45066862191](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/45066862191) is `completed/success` with `head_sha=73978a0a19b4686330f6295e4344137fd65db745`. Read both job results and their logs:
- `411/411` Node tests, zero failures, including actual Git sandbox negative report-path tests and package replacement controls.
- Two clean deterministic candidate profiles, exact built-file/commit reconstruction `source#reproduced PASS` and `source#expected PASS`, current/default contact release audits, and Nu checker for candidate pages passed. The PR CI build checkout uses the **PR merge commit** `200037c56027160624339d9e1fc241944487c41c` in the manifest and GITHUB_SHA; do **not** attribute that package-produced SHA to the PR branch tip.
- `356/356` Chromium/axe checks passed. One Nu checker warning during fixture/contact validation was reported, while candidate Nu checks showed 0 errors and 0 warnings. These are implementation-authored GitHub CI results; Harbor did not independently execute the full Node/Chromium suites.

### Remaining release-only unknowns and limits

- A merge is **not** a production release. The ledger still lists G-preview, G-host, G-rollback, G-legacy/waitlist, G-cutover, G-a11y, G-copy, G-indexing, G-contact and version/locales decisions as separately owner-gated.
- The candidate package's own `404.html` and `robots.txt` have been checked locally and against synthetic loopback, not an authorized real protected-preview host or production Cloudflare edge. Source-content reproduction proves a checkout builds the artifact, **not** that the operator should deploy it, that public content has been approved, or that Git SHA proves a human author's identity.
- No real controlled filesystem test was run by Harbor for path races, symlinks switched between admission and write or catastrophic audit failure with current source. The CI's actual Git sandbox tests and my injected V8 functions complement but do not replace those unknowns.
- The report is **context-exposed**, not blind: PR description enumerated peer review outcomes. Harbor only claims authorship of the checks actually source-executed in this session; do not invent consensus.
- Read-only application review; no production code, live host, credentials, DNS, independent apps, waitlist records, or other agents' memory were modified. Only authorized Harbor memory/index and a `COMMENTED` GitHub review are within this workflow.

**Disposition:** **H22-01 closed. No remaining Harbor merge blocker reproduced on `73978a0`. Recommend ACCEPT for nonproduction checkpoint merge consideration only, subject to owner and peer dispositions.** H22-02 remains a documented scratch-artifact recovery limit; it is not live rollback evidence.

## Revisit when

A new PR head changes output deletion, report routing, source reproduction, root 404/robots or no-request admission; an owner authorizes protected-preview testing or immutable release-package staging; or a real path-race/parallel-build counterexample appears. Re-pin and rerun forged external target negative, reserved-scratch replacement, report symlink aliases and failed-verification no-GET controls. Preserve HC11 historical BLOCK record and update only forward.

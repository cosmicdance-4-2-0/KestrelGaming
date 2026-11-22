---
schema: 1
id: 2026-11-22-idiw-s104r-pr22-rereview-hardlink-f2-a72d
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-idiw-s104r-pr22-rereview
created: 2026-11-22
updated: 2026-11-22
sources: "i_d_i_w--TEMPLATE PR #22 exact head 73978a0a19b4686330f6295e4344137fd65db745 vs previously reviewed 789dc0d67910b22b3d3fea5d5e7a819467a0a36e; source blobs artifact.mjs 8b22eee3209f6e3b3e3c13892b8fd26d636ae0f5, verify-candidate.mjs 24ed6a779b5e55421ce97027f2edf8541bd3c5c6; isolated source-executed F1 controls and Node 22 local hardlink reproduction; GitHub Actions run 45066862191."
---

# Flint — IDIW S1-04R PR #22 new-head re-review

**Verdict: CONDITIONAL ACCEPT (merge HOLD until F2 is corrected)** at exact PR head `73978a0a19b4686330f6295e4344137fd65db745` and base `5d59a8efdd99012e8c08a73d35213ff41180a71c`. Owner controls merge, release and deployment. This is an independent scoped implementation/maintainability review; the public PR description included peer corrections, so it is **context-exposed**, not a blinded review. No application source modifications or deployment.

## Summary

**Flint F1 CLOSED:** At the previous head `789dc0d`, `notFoundProblems` incorrectly accepted href/src values beginning `/\\attacker.example`, a browser-external origin. The revised head `73978a0` rejects single- and double-backslash authority-like references and legitimate internal backslashes; it retains exact `/styles/base.css`, `/`, `#main` skip and `data:,` icon controls. The shared release audit also treats backslashes as URL slashes when classifying external links. The additional PR rounds add narrowly justified provenance checks (evidence from reproduced checkout), planned path validation, safe external-directory replacement, and report path symlink guards.

**Flint F2 NEW — required narrow correction:** The newly shared `reportPathProblem(report, guarded)` in `prototype/first-light/scripts/artifact.mjs:92-105` rejects a symlink report file, a non-file entry or a canonical path within the package. It *accepts an external regular-file hard link* to a file inside the verified package: both `lstat` and `realpath` consider the alias a plain file at an external path. Both CLIs then call `writeFileSync(reportPath, JSON)` **after** a successful verification. A valid report therefore overwrites `site/index.html` through that hard link **after** returning PASS. This is a deterministic counterexample to the documented guarantee that report output cannot alter what was just verified.

**Smallest correction:** Require a previously nonexistent output report path; atomically create with Node `writeFileSync(path, data, { flag:'wx' })` or equivalent exclusive creation for *both* verifier and preflight CLI writes. The existing canonical/symlink guard remains valuable. Add a real end-to-end test with `linkSync(candidate/site/index.html, externalReport)`: report output must be refused, the original HTML remain byte-identical, and no success claim be emitted. An existing external report file should also be refused rather than silently overwritten. Avoid a new inode registry, artifact-wide accounting, temp-publish framework or general filesystem sandbox. (Separate races in untrusted concurrent filesystems are not proven by this test.)

**Assessment:** The S1-04R architecture remains proportionate; no unrelated refactor is justified. Candidate build and verify stay separate from owner approval. Package provenance remains self-consistency plus a fresh checkout-derived byte comparison, not owner authorization. The default preview, two profile policies, 404 and robots, synthetic served tests and ledger are appropriately bounded. This verdict is not a release PASS.

## Evidence

- Exact source and delta: PR #22 moved from `789dc0d67910b22b3d3fea5d5e7a819467a0a36e` through `62ee3544e31c7d37304da04b74a921fdfcab5cd7` to `73978a0a19b4686330f6295e4344137fd65db745` (two commits, 11 changed paths). Source `scripts/artifact.mjs` blob `8b22eee3209f6e3b3e3c13892b8fd26d636ae0f5`, `verify-candidate.mjs` blob `24ed6a779b5e55421ce97027f2edf8541bd3c5c6`, `preflight-preview.mjs` blob `a14a42b38c4202b0748ced4484c800b89031654c`.
- Independent F1 source test: fetched exactly `scanTags`, `stripComments`, and new `notFoundProblems` from GitHub at `73978a0`; evaluated original function bodies in isolated V8 with a valid minimal 404. Legitimate `/styles/base.css` passed; `/\\attacker.example/p.css`, `/\\\\attacker.example/p.css`, `/styles\\base.css`, `//attacker.example/p.css`, `https://attacker.example/p.css` all produced the appropriate rejection. No full browser here.
- Independent F2 actual local filesystem reproduction on Node v22.16.0: copied *unchanged* `canonicalPath` and `reportPathProblem` function bodies from exact head's `artifact.mjs` into a transient CJS harness. Created temp package `candidate/site/index.html` with HTML bytes, then `fs.linkSync(site/index.html, outside/report.json)`. `stat` established **same inode** and `nlink=2`. `reportPathProblem(outside/report.json,candidate)` returned **null** (allowed). `writeFileSync(outside/report.json, JSON)` changed the original package `site/index.html` to those JSON bytes. The fixture was not a full real Git candidate CLI run; it executes the exact guard and the same Node write primitive and demonstrates the filesystem aliasing vulnerability. `plainFiles` currently accepts such regular-file hard links.
- The actual CLI path: `verify-candidate.mjs:314-321` guard -> `verifyCandidate` -> unguarded overwriting `writeFileSync(reportPath, JSON)`; `preflight-preview.mjs:789-794,824-825` shares the guard and write semantics. An exclusive-create report closes this concrete non-racing reproduction.
- CI independently checked by reading GitHub run 45066862191 metadata and job logs: **411/411 Node tests, 0 failed/skipped**, **356/356 Chromium/axe browser checks**, contact and ordinary release audits and Nu HTML checker passed. This is **CI-executed** and not a local repository test suite by Flint. The hard-link case is not among published tests. No real protected host, screen reader, device, rollback or cutover was inspected.
- Original F1 published review: https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/22#issuecomment-7077242764

## Revisit when

PR #22 head changes to refuse hard-linked existing report destinations and to use exclusive new-file creation, or the owner changes the documented report-output threat boundary. Re-pin the actual code and CI; keep this exact-head record without rewriting earlier conclusions.

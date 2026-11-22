---
schema: 1
id: 2026-11-22-idiw-pr22-candidate-trust-review-lk35
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-idiw-pr22-2026-11-22
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW i_d_i_w--TEMPLATE PR #22 exact base main@5d59a8efdd99012e8c08a73d35213ff41180a71c, head 789dc0d67910b22b3d3fea5d5e7a819467a0a36e, GitHub COMMENTED review 6011542099; verify-candidate.mjs blob eedde867d6567c363bd10f7c33e7eb5e71ac9ddc; build-candidate.mjs blob 890882f879feb7d32fe3d1543501592b491f18c8; release.mjs blob 8d24d6354270bb43991a24360ccbf9eda9847b4d; source-based V8 reproductions with mock dependencies; Actions run 45007995574 success."
---

# Latch — IDIW PR #22 release-candidate negative-path review (LK35)

## Summary

**Verdict: CONDITIONAL / HOLD MERGE** at exact head `789dc0d67910b22b3d3fea5d5e7a819467a0a36e`, pending two tightly scoped fixes. Source-pinned [official COMMENTED review 6011542099](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/22#pullrequestreview-6011542099) posted and remotely verified. The PR remained draft/unmerged at review. No application source edited and no deployment, preview host, DNS/Cloudflare, credentials, legacy assets, or production touched.

**Mode:** Latch — The Locksmith, `agents/latch-v1` scope. Context-exposed, not blind: PR description listed peer reviews and corrections, but counterexamples were independently constructed. Exact source fetched via connected GitHub. Local GitHub clone failed due container DNS, so full Node/Chromium/Nu/Git tests were NOT independently rerun. GitHub Actions [45007995574](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/45007995574) `completed/success` (both jobs) on head. Author report says 389/389 Node. Synthetic isolated source tests with controlled mocks are distinct from real filesystem/host execution.

## Evidence

### L22-01 — publication evidence dates are taken from an untrusted manifest (merge concern)

- Writer `src/release.mjs::contentEvidence` reads portfolio records and writes `manifest.content.evidence`. Verifier `scripts/verify-candidate.mjs` lines 268–280 reads **only manifest.content.evidence** to form `content#evidence-age`; it never checks against `contentEvidence()` from its own pinned source. Its `source#reproduced` verifies site bytes, not miscellaneous manifest metadata; `verifyCandidate` excludes `content#` from the package outcome on purpose.
- **Exact-source isolated V8 reproduction:** Executed full `verifyCandidate`, `artifactRecordProblems`, `inspect` source with mock fixed passing filesystem/manifest file, clean checkout and audited site. Only sibling manifest `content.evidence` changed. With fixed 2026-11-22 clock: `on: 2001-01-01` reports **9456 days** and package PASS, `on: 2026-11-21` reports **1 day** and package PASS, an empty evidence array reports `content#evidence-age UNVERIFIED` and package PASS. In all cases both `source#reproduced` and `source#expected` PASS. Fake manifest promotion text `APPROVED TO PUBLISH` did not change the verifier's fixed `promotion: NOT EVALUATED` output (positive guard). No checked-in evidence was accused of falsity.
- **Correction:** Use source-derived `contentEvidence()` for age reporting only after checkout provenance is established, or compare manifest records against source and make disagreements an integrity FAIL / explicitly unverified provenance. The human G-copy freshness decision remains independent and open. Add a date-only manifest mutation with otherwise identical site for regression.

### L22-02 — injected in-process planner can escape package's filesystem boundary (merge concern, NOT CLI-exposed)

- `scripts/build-candidate.mjs::plannedFiles(profile,plan)` at lines 121–130 maps planner-returned `{path,content}` into file keys without any relative-path safety check; `writeCandidate(...,plan)` lines 141–149 calls `writeFileSync(join(site,path),bytes)` **before** the release audit. `prepareOutput` validates the package root but not the paths *inside* the plan.
- **Exact-source isolated V8 reproduction** of `plannedFiles` and `writeCandidate` with a fake filesystem and injected `plan:()=>[{path:'../../outside-guard.txt',content:'data'},{path:'index.html',content:'hello'}]`. Captured an attempted write to **`/safe/outside-guard.txt`**, outside protected `/safe/pkg/site/`. Node's actual `path.join('/safe/pkg/site','../../outside-guard.txt')` was separately tested and resolves to that path. **No real write occurred.** The CLI calls the fixed `planCandidate`, not a caller-supplied plan, so this is an exported-library/test-seam risk, not an externally triggered standard CLI exploit.
- **Correction:** Fail before `prepareOutput` or any `mkdirSync/writeFileSync` if a planner-produced path is absolute, empty, contains dot or traversal segments, duplicates a path or escapes `site/`. Reuse existing safe-path validation. Add malicious plan callback regression asserting **zero writes**.

### Positives and gates

- Default nonproduction build separate from candidate package. Two profiles; unsupported publication decisions (notice removal, indexing, version, non-English locale) rejected by `profileProblems`. Deliberate 404 and robots policy and root-only preflight candidate mode.
- `prepareOutput` resolves symlink ancestors, protects repository path and existing foreign/incomplete packages; now checks nonempty recorded files and actual `site/`. `plainFiles` checks lstat throughout `site/`, protects independent verifier from symlink escape; `artifactRecordProblems` validates file list before use; `source#reproduced` independently rebuilds from clean pinned checkout; `source#expected` supports explicit reviewed SHA. Independent source inspection, author tests and CI—not independently rerun full.
- `notFoundProblems` limits <main> to exactly one recovery link to root and requires root-absolute resource URLs, no mailto. Preflight candidate admission refuses unverified package before network; default served audit remains separate. New artifacts are local and CI packages never uploaded or deployed.
- Owner ledger gates G-copy, G-contact, G-locales, G-indexing, G-notice, G-version, G-treatments, G-a11y, G-legacy, G-host, G-preview, G-rollback, G-cutover remain OPEN/BLOCKED, not PASS. Real preview/host/rollback/accessibility not tested. No production authorization or merge granted.

## Outcome

**COMPLETE** for current requested read-only audit: posted CONDITIONAL/HOLD MERGE to PR #22 (review 6011542099), source-evidenced two bounded negatives, positive bounds and explicit limits. No need for broad defensive refactors. Exact-head re-review after small fixes; keep owner release decisions separate. GitHub shared-account review attribution does not authenticate agent runtime identity.

## Revisit when

PR #22 head advances after either correction; source evidence records become independently attested; plan injection is removed or paths are validated; a real protected preview is owner authorized; or the release decision and rollback are explicitly scheduled.

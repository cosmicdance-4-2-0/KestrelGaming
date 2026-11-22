---
schema: 1
id: 2026-11-22-idiw-pr22-candidate-output-review-hc11
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-idiw-pr22-review-session
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW PR #22 at exact current head 789dc0d67910b22b3d3fea5d5e7a819467a0a36e and main@5d59a8efdd99012e8c08a73d35213ff41180a71c; AGENTS.md, S1-04R release-candidate ledger, builder/verifier/artifact and preflight source, regression tests and GitHub Actions 45007995574; Harbor home agents/harbor-v1@88b720f3b6763ae227738cbe78ee27702854b6ec; independent V8 exact-production-function virtual filesystem tests of prepareOutput/notOurPackage and writeCandidate, and UNVERIFIED no-request candidate-preflight control; no actual repository code or real host changed."
---

# Harbor HC11 — IDIW PR #22 release-candidate output safety and recovery review

**PR:** [IDIW #22](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/22) — `IDIW-S1-04R`, nonproduction engineering preparation.  
**Revision:** `789dc0d67910b22b3d3fea5d5e7a819467a0a36e`, exact current head checked twice; base `main@5d59a8efdd99012e8c08a73d35213ff41180a71c`. PR description mentions earlier `d395c1f` and a prior 374-test result; evidence here is for current head only.  
**Harbor home loaded:** `agents/harbor-v1@88b720f3b6763ae227738cbe78ee27702854b6ec`.  
**Scope and review mode:** Focused independent Harbor publication/rollback/retained-data review, **context-exposed** because PR description contains earlier reviewers' conclusions. No separate review thread used to derive findings; actual code and tests inspected directly. No app implementation, merge, tag, live preview, DNS, Cloudflare, private waitlist or legacy portal action.  
**Verdict:** **COMMENTED — BLOCK for this code checkpoint at the pinned head** pending one bounded destructive-output ownership correction (H22-01). Release/cutover remains separately BLOCKED irrespective of this code review.

## Summary

The PR adds two explicit `noindex` candidate profiles (`omit` and bounded `candidate` contact), planned static `site/` with a root-absolute 404 recovery page and `robots.txt`, an adjacent unshipped provenance manifest, source-reproducing verifier, candidate-aware read-only served preflight, CI checks, and a ledger that explicitly keeps owner and hosted gates open. The normal default build is supposed to remain unchanged. I found meaningful fail-closed behavior in the verifier and preflight, including a source-executed negative candidate admission check, but **the output writer's own destructiveness check conflates a self-consistent manifest with proof of having written the target**.

The design vocabulary already distinguishes a **manifest claim** from **independently reproduced evidence** inside `verify-candidate.mjs`. The output writer's `prepareOutput` makes a deletion decision based only on the former. This discrepancy is the central defect.

## Evidence

### H22-01 — BLOCKER: an unrelated operator directory can be erased after a forged manifest

**Production code:** [`build-candidate.mjs`, `notOurPackage` and `prepareOutput`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/scripts/build-candidate.mjs#L53-L128).

`notOurPackage()` requires only: a file named `candidate-manifest.json`, `manifest.schema === "idiw-release-candidate-manifest/1"`, a non-empty `manifest.artifact.files` array, a plain `site/` tree, and matching path/hash/byte entries. It does **not** require an approved profile, a known file/route set, a manifest matching a planned candidate or a source-reproduced prior candidate before saying the directory is replaceable. A manifest's SHA-256 file records are unkeyed and **anyone able to author a matching manifest can compute them**. `prepareOutput` then removes the manifest and recursively removes the `site/` directory. Its protected-repository canonical-path check is useful but permits **any external output directory**.

**Independently source-executed negative case:** Extracted and evaluated the exact GitHub-head JavaScript declarations `canonicalPath`, `notOurPackage` and `prepareOutput` in isolated V8, injecting a deterministic virtual filesystem (no actual disk deletion). The virtual `--out /outside/choice` contained `site/private.txt` and a manually authored self-consistent manifest (schema, one path, bytes, computable matching digest). No profile, owner gate, or IDIW source revision was present. `prepareOutput('/outside/choice')` **accepted the directory and issued deletion calls on `candidate-manifest.json` and `site/`**, which includes unrelated `private.txt`. In a separate exact-source mock, a directory with `site/my-private-notes.txt` was actually removed from the virtual filesystem, not just logged. These are simulation-controlled side effects; Harbor did **not** delete real files.

**Controls (same production declarations):**
- Foreign `site/` without manifest: **refused**, no deletion.
- Manifest-only directory without `site/`: **refused**, no deletion (prior Axiom correction holds).
- Self-consistent forged manifest + foreign one-file `site/`: **admitted and deleted**, contrary to "only a package this tool provably wrote".
- Forged manifest with a mismatched digest: **refused**, no deletion.

The decisive difference is the lack of an *independent* approved-file-set/owner boundary before deletion, not weakness in SHA-256 or symlink resolution. Existing [release-candidate tests](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/tests/release-candidate.test.mjs) exercise no-manifest, manifest-only, mismatched and symlinked cases, but not a **self-consistent false-ownership manifest** with arbitrary site content.

**Minimum disposition:** For this engineering checkpoint, safest and smallest is to **allow automatic overwrite only in the reserved canonical git-ignored `candidate/` output**; external `--out` locations must be nonexistent or empty, otherwise refuse and preserve every byte. CI already uses distinct empty external directories per build. Alternatively an independently validated *restricted known package profile and planned file set* can justify a narrowly constrained overwrite, but a self-authored manifest or checksum alone must not confer authority to delete arbitrary paths. Add explicit negative regression asserting **no deletion** for a forged self-consistent manifest plus arbitrary file, and positive controls for empty external targets, repeat reserved candidate builds, canonical aliases and real package handling. If the owner intentionally allows replacing arbitrary self-consistent external packages, the documentation must no longer claim provenance and the risk needs explicit acceptance; I recommend avoiding that semantics.

### H22-02 — NONBLOCKING but real recovery limitation: replacement is not transactional

**Production code:** [`prepareOutput` + `writeCandidate`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/scripts/build-candidate.mjs#L112-L204). `prepareOutput` removes an accepted prior package **before** the new `site/` content is built and audited. If the new candidate later fails `auditRelease`, the failure handler removes that new `site/` and leaves no manifest. The prior audited candidate is unavailable at that path and can only be reconstructed.

**Source-executed control:** Evaluated the exact production `writeCandidate` function with controlled `prepareOutput`, filesystem and failing audit adapters. Operation order observed: *remove prior package → write replacement → audit refuses → remove failed replacement*. Final previous site/manifest not retained. This is consistent with the current documented "failed audit leaves no manifest" behavior, so I classify it as a **scratch-artifact recovery tradeoff, not a new claimed merge blocker**. Do not represent candidate overwrite as preserving a last-known-good package or providing deployment rollback. If candidate packages become protected release evidence later, use an atomic staging-and-swap or distinct immutable package directories with retained review receipts.

### Verified positive boundaries

- Exact commit profile checks in [`src/release.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/src/release.mjs) refuse unknown/missing fields, non-`en` locales, unapproved indexing/notice removal/version. `candidate-contact` opt-in contact is audited in its distinct mode, while root `404.html` has no contact route.
- [`verify-candidate.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/scripts/verify-candidate.mjs) distinguishes manifest claim, artifact self-consistency, clean matching checkout, and actual rebuilt bytes/paths. It validates manifest artifact records before file reads and rejects symlinks with `lstat`. `source#expected` is independent of the claim when supplied, and a missing expected SHA remains a REVIEW item; PASS is not promotion.
- [`preflight-preview.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/scripts/preflight-preview.mjs) refuses nested-base paths for candidate mode, and calls `verifyCandidate` before any artifact read or GET. **Independently source-executed:** the actual `runPreflight` body with mocked `verifyCandidate=UNVERIFIED` produced candidate verification FAIL, target observation UNVERIFIED, zero request entries and **zero intercepted GET/artifact-read calls**. This is a synchronous simulated source check, not an actual network or CLI run.
- [`artifact.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/prototype/first-light/scripts/artifact.mjs) separates the original generic reader from new symlink-refusing candidate `plainFiles` helper, preserving the established preflight for default artifacts.
- [Candidate ledger](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/789dc0d67910b22b3d3fea5d5e7a819467a0a36e/docs/reviews/IDIW_S1_04R_RELEASE_CANDIDATE/README.md) keeps all hosted, accessibility, legacy-portal/waitlist and rollback decision rows undecided, and does not claim deploy authorization. The profile's `robots.txt` allows crawling to read HTML `noindex`; real indexing and edge behavior remain owner gates, not independently observed.
- CI exact head [Actions `45007995574`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/45007995574) completed `success`. Job logs inspected: **389/389 Node tests**, `0` failures, deterministic 13-fixture-file build, passing candidate package build/verification and Nu checks, default/contact audits, **356/356 Chromium/axe checks**. The CI commands build each candidate twice in separate runner-temp directories and **do not deploy or upload the candidates**. These are GitHub-attributed full-suite checks, not Harbor's local npm/Chromium run.

### Release-only unknowns and limits

- No real protected preview tested: G-preview is BLOCKED. `404.html` status/identity, Cloudflare edge rewriting and root `robots.txt` behavior require authorized served-preflight evidence.
- No owner gate is closed by an artifact PASS: final project/contact/404 copy, indexing, supported locales, physical assistive-technology/browser checks, legacy-portal and any waitlist preservation/disposition, DNS/host/`www` ownership and **rehearsed rollback** remain independent.
- A source-reproduced candidate's manifest does not authenticate the author's human identity or establish production authority. The clean-checkout reproduction is meaningful only for the actual Git SHA, coupled to separately reviewed and trusted source.
- The test's virtual filesystem and injected function dependencies verify code paths **without actual disk writes to an external operator directory**; no adversarial symlink race, concurrent builder, real Cloudflare or host behavior assessed. CI scripts are implementer-authored tests. The PR description already listed peer findings, so this is a context-exposed Harbor report rather than a blind first pass.
- The earlier historical PR description pin (`d395c1f`) and 374 test count are outdated; this report is **only about `789dc0d`**, where the symlink/manifest-record corrections and 389-test CI have landed.

**Disposition:** **BLOCK merge of the nonproduction code checkpoint pending H22-01 ownership fail-closed correction**, with H22-02 documented as a separate scratch-artifact rollback limitation, not a condition for code merge. No application code changes made.

## Revisit when

The PR head advances with a bounded output replacement rule; an owner explicitly adopts alternative replacement semantics; evidence establishes a stronger ownership gate; or another engineer demonstrates an actual counterexample. At re-review, pin exact new SHA, rerun forged-matching-manifest+arbitrary-file negative, empty external and controlled repeat candidate positive, audit-failure cleanup, CI provenance and the candidate no-request check. Keep H22-01 as historical record if corrected; do not alter release/cutover gates without an owner decision.

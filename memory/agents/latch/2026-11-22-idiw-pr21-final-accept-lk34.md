---
schema: 1
id: 2026-11-22-idiw-pr21-final-accept-lk34
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-idiw-pr21-final-recheck-2026-11-22
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW PR 21 current exact head 83f164b44bfc50cb32dab877915bb336e62775eb, predecessor 95ea4271551bcfca6bb4c9d0b62f9ef1688feec1, base main@4e77021b9595e09bd21f36f35778801222df6c4b; code blob bc0ed03f4af06570b5984bd2ab53362c6f37ebc6, tests blob 2be64367e2a4d7bfe6e7560220abfc1b2f1d0ae5; CI 44998191613 success; published GitHub COMMENTED review 6011164051; exact production function V8 source probes with ESM export removal and synthetic digest stub."
---

# Latch — IDIW-S1-04P PR #21 final exact-head acceptance (LK34)

## Summary

**Verdict: ACCEPT for merge consideration** of the bounded nonproduction read-only served-preview preflight at exact head `83f164b44bfc50cb32dab877915bb336e62775eb`. No remaining merge blocker identified within assigned security/report-hygiene scope. Published [GitHub COMMENTED review 6011164051](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/21#pullrequestreview-6011164051) and remotely verified it is anchored to exact head. Prior [LK32](2026-11-21-idiw-pr21-preflight-report-boundary-lk32.md) NO GO and [LK33](2026-11-21-idiw-pr21-recheck-server-version-lk33.md) CONDITIONAL ACCEPT are historical-head dispositions only; their blockers are closed by the current source.

**Authority:** User asked for another look. Read-only code/review task; no application edits, deploy, Cloudflare/DNS/credentials, merge, or production actions. PR remained draft and unmerged after review. Latch role per `agents/latch-v1` agent contract. GitHub identity attributed to shared account, not authenticated agent identity. Review is context-exposed, not blind (other agents' recorded work is in PR metadata/source history).

## Evidence

- **Exact sources:** `prototype/first-light/scripts/preflight-preview.mjs` blob `bc0ed03f4af06570b5984bd2ab53362c6f37ebc6`, `tests/preflight-preview.test.mjs` blob `2be64367e2a4d7bfe6e7560220abfc1b2f1d0ae5`; two commits after the LK33 head. Source and new tests read at pinned revision. CI [44998191613](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/44998191613) `completed/success`, exact head. Implementer report says 264/264 Node tests including 44 preflight, and successful Chromium/axe/Nu. **Those full suites were not independently rerun**. No real preview host exists or is authorized; all tests synthetic/local.
- **R21-1 (known `Server` product version disclosure): RESOLVED.** Independently executed exact `SAFE_VALUE.server`, `headerFingerprint`, and `compareFingerprints` production functions (isolated V8; removed only `export` and stubbed SHA-256 digest function solely to exercise string sanitization). `Server: cloudflare/1-PRIVATE-TENANT-54723` became `cloudflare/version-present`; `nginx/1.25.3 Python/3.13.18` became `nginx/version-present python/version-present`; `node/123_Secret-id` became `node/version-present`. Unknown product remained `1 unlisted`. Combined CSP nonce `PRIVATE-TOKEN-0001` and ACAO `PRIVATE-ORIGIN-1888` also withheld by current normalizers, and the prior-report arbitrary header keys were not echoed. No raw marker survived in observed fingerprint/summary output. Author added library, report-file, stdout and stderr loopback negative regression for known-product crafted version, covering the exact prior LK33 gap.
- **Harbor independently found served-audit prose redaction leak (additional scope): RESOLVED in source/test.** Prior regex substitutions could be bypassed by entity-decoded quotation marks in served locale/URL errors. New `servedFindingCodes` emits only fixed error categories and whitelisted developer-owned artifact paths, aggregating counts; unknown messages become `other-finding`. Independently executed the exact production `FINDING_CODES` and `servedFindingCodes` source without substitutions. Mutations with hostile strings in locale values, linked URL values, text URL, fabricated file prefix, and an unrecognized future finding returned fixed codes `undeclared-locale`, `unverified-external-url`, `unverified-url-in-text`, `artifact: hidden-file`, `other-finding`, and two script findings aggregate to `script-or-inline-handler ×2`. **No hostile marker appeared**. Author's new loopback/CLI tests cover decoded quote and report stdout/file.
- **Unaudited artifact admission:** Source now detects `auditRelease(artifact.root)` errors and calls `finish()` **before any remote GET**, returning FAIL and an UNVERIFIED target observation. New tests assert no network requests, including a credential-bearing run. This closes an unnecessary action on invalid input and preserves semantics of a blocked result.
- **Prior LK32 L21-2:** `sanitizeEarlier` and `compareFingerprints` filter prior arbitrary header names to fixed allowlists/counts, and use schema `/2`; independent execution confirmed no `x-private-tenant-99817` or `x-private-user-83762` in output. **Prior L21-3:** nested `/robots.txt` probe excludes access headers and redirects outside preview path block in source and new author loopback tests. **Prior L21-4:** earlier target+artifact provenance mismatch is REVIEW in source and tests. No reopening without counterevidence.

## Outcome

**COMPLETE — technical ACCEPT recorded on PR #21 at `83f164b`; agent continuity persisted.** This was not a GitHub APPROVE action; the formal PR review was COMMENTED with explicit acceptance for owner merge consideration. Source-based independent execution was focused on redaction functions; full Node/browser/Nu and live-host preflight were not independently run. The merge decision remains the owner's, and the **protected preview / G5–G6 production gate remains BLOCKED** without separate owner authorization. Not a release certification or real privacy-incident claim.

## Revisit when

PR #21 advances beyond `83f164b`, a real protected preview is authorized, the reporting contract changes, a regression report demonstrates escaped private served data, or the owner requests a distinct release-gate audit.

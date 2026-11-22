---
schema: 1
id: 2026-11-21-idiw-pr21-recheck-server-version-lk33
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-idiw-pr21-recheck-2026-11-21
created: 2026-11-21
updated: 2026-11-21
sources: "IDIW PR #21 exact reviewed head 95ea4271551bcfca6bb4c9d0b62f9ef1688feec1, parent 589dc4e1cc73eedb4a4cc1a4e4108aaca8786828; preflight blob d5fc5bffeb6ec2b75d05f8918c907b3d816039a7, tests af4f891ef55e047a0b57386b94df1ae55c7ab0ce; source-pinned isolated V8 execution of production headerFingerprint/compareFingerprints with digest stub; GitHub Actions run 44989714803 completed success; official COMMENTED review 6010559262; no live preview or full suite."
---

# Latch — IDIW PR #21 revision re-review (LK33)

## Summary

**Disposition: CONDITIONAL ACCEPT** at exact draft PR head `95ea4271551bcfca6bb4c9d0b62f9ef1688feec1`; hold merge for **one residual known-server-product version suffix disclosure**, or obtain explicit owner acceptance of that limited report-value risk. Four LK32 findings from [prior review 6010540604](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/21#pullrequestreview-6010540604) now substantively resolved; do **not** reopen them without contrary source evidence. Current official [COMMENTED re-review 6010559262](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/21#pullrequestreview-6010559262).

**Review independence:** PR metadata exposed prior reviewer results and owner/coder fix descriptions. This is context-exposed, not blind, but a separately executed exact-source counterexample. This is attributed Latch's assessment, not a GitHub-authenticated model identity. Read-only: no app source, merge, DNS, Cloudflare, credential, preview, or production change.

## Evidence

**Scope and source:** PR #21 advanced one commit `589dc4e` → `95ea427`. Compare shows changes in the preflight, tests, operator procedure, sample reports, README and evidence report. Current `preflight-preview.mjs` blob `d5fc5bffeb6ec2b75d05f8918c907b3d816039a7`, tests blob `af4f891ef55e047a0b57386b94df1ae55c7ab0ce`. CI run [44989714803](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/44989714803) **completed success at exact head**. Did not independently run full Node, browser, Nu, or HTTP. No real protected preview exists/authorized; live-host gate is BLOCKED. Full negative tests are author-supplied.

- **LK32 L21-1 (raw header values and Content-Type): substantially resolved.** New `safeContentType`, `SAFE_VALUE`, `headerFingerprint`, schema `idiw-served-preview-preflight/2` with digest comparisons. Source-executed with ordinary header-shape fake and production sanitizer, only ESM export stripped and a synthetic SHA256 stub for digest values; `content-security-policy` nonce `PRIVATE-TOKEN-0001` and `access-control-allow-origin` tenant `PRIVATE-ORIGIN-1888` correctly withheld. **Residual described below**.
- **LK32 L21-2 (earlier report private names): resolved.** Exact `sanitizeEarlier` and `compareFingerprints` source executed in same V8 harness. Prior report `recorded['x-private-tenant-99817']`, `digests['x-private-digest-77117']`, `otherNames=['x-private-user-83762']` is reduced to an unlisted count with none of those names in emitted changes. Schema `/1` rejected. Author's new tests exercise report and CLI.
- **LK32 L21-3 (nested base path credentials): resolved by inspected source and author-supplied loopback test.** `/robots.txt` origin-root probe omits access headers if nested, and same-origin redirects outside `target.basePath` are BLOCKED before follow-up. Dedicated origin remains sensible default. No independent Node HTTP request test.
- **LK32 L21-4 (comparison provenance): resolved by inspected source and author-supplied test.** `comparison#provenance` compares exact target.origin/basePath and artifact.manifestSha256, reports REVIEW if different without repeating earlier target. No live comparison test.
- **New exact-source counterexample R21-1:** `SAFE_VALUE.server` whitelists recognized product labels but regex permits an arbitrary suffix after the initial version digit `/1[a-z0-9._-]*`. With `Server: cloudflare/1-PRIVATE-TENANT-54723`, exact executed `headerFingerprint` yields `recorded.server === 'cloudflare/1-PRIVATE-TENANT-54723'`; tenant marker is copied to persistent serialized report. Other two previously leaked fields stay sanitized in the same test. The existing author test uses `server: PRIVATE-SERVER-2222/1.0`, which is an unknown product and produces a safe unlisted count, so it misses this positive-prefix negative. **This is a synthetic hostile header, not actual client/account data on a host.**
- **Minimal correction:** Expose only public known server-product name; normalize/version-present/hash any version suffix. Keep digest for change detection. Add a crafted known-product/private-version string to library, report-file and CLI no-marker regressions. Avoid generic sanitization framework. The published operator procedure deliberately reports `robots.txt` directive lines, subject to operator privacy review; that stated policy was not re-opened.

## Outcome

**COMPLETE — follow-up source-pinned `COMMENTED` review posted on PR #21 and verified with exact head**. Conditional acceptance on all prior fixes, one residual redaction issue. No application modifications or live operations. CI reports success but does not certify the missing known-server-version case. Release is separately blocked by absence of authorized preview, manual accessibility/locale gates and cutover decision.

## Revisit when

Preflight code changes how `Server` version tokens are reported; the owner formally accepts the header-version disclosure risk; PR #21 head advances; or a real protected-host preflight is separately authorized.

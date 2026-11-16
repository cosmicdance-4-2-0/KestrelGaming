---
schema: 1
id: 2026-11-15-auralprint117-pr12-psd-consumer-review-f28c09a1
kind: handoff
scope: agent:mothlight
status: active
evidence: observed
author: mothlight
created: 2026-11-15
updated: 2026-11-15
sources: "AP117-003 PR12 exact head 0880fc8df9182cce9ed2c645e324a2d291375281 vs accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; Mothlight GitHub COMMENT review 5915869007; CI workflow 43789892097 success. Axiom dispatch issue comment 6907662478. Own prior PR9 review 5909843722."
---

# AP117-003 — Mothlight PR #12 PSD consumer-status review

## Work and verdict

Reviewed [draft AP117-003 PR #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12), exact head `0880fc8df9182cce9ed2c645e324a2d291375281` against accepted `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. Source inspected: `AGENTS.md`, six new PR files including actual `src/analysis/psd-processor.js`, `docs/AP117_003_PSD_CONSUMER.md`, lifecycle and boundary tests, accepted upstream `spectrum-delivery.js` and Issues #6/#10/#11. Reconciled with own PR9 review's main boundary. **Published attributable GitHub `COMMENT` review** [ID 5915869007](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#pullrequestreview-5915869007).

**Verdict: PASS within Mothlight's specific status and truthful instrument remit, with future integration cautions.** No current-scope blocker reproduced in source; not contract adoption, merge authorization, or proof of browser PSD UI.

## Findings

- **Upstream `ended` versus PSD drained:** `readStatus().upstream.status=ended` can coexist with queued final FFT windows while PSD `readStatus().status=open, drained=false`; `take()` derives each and only returning `take().ended` declares consumer drain. Existing tests cover 4 final, short and partial-tail EOF. A final `readCurrent().status=ready` is **historical** not live.
- **Failure scope:** `subscriber-delivery-overrun` => `subscriber-delivery`; producer invalid PCM/epoch/reset => `upstream`; malformed PSD input/control => `consumer`, with producer spectrum independently remaining valid for a consumer-only defect. Cap2 vs cap4 and producer input chronology negatives are present.
- **Sticky reasons:** initial first `reason` and `failureScope` preserved, `latestReason` updated on later local/upstream cause; nested `upstream` truth separately preserved. `resync()` abandons backlog, clears diagnostics and starts new accepted frontier. Neither pair constitutes complete event history.
- **Historical origin and currentness:** processor captures the actual trusted subscription methods, not a caller-provided `take(receipt)`; older queued spectra remain valid by true originating subscription's generation/continuity/ordinal until broken; `spectrum.isCurrent()` does not define historical eligibility. Correct trusted host must still supply the correct subscription at constructor; no same-realm hostile authentication claimed.
- **Future visualizer status rule:** **source ended**, **PSD drained**, and **last actually painted observation** are three independent facts. No existing PSD GUI; renderer-coalesced frames are not analysis gaps; no wall-time freshness assumptions. User-facing status tests must later exercise EOF-with-backlog, independent cap2 loss/cap4 success, and post-resync display history.

**Test provenance:** GitHub Actions run `43789892097` succeeded on exact PR head, including 119 Node tests per Axiom CI inspection, static build, HTML and existing Chromium smoke. I **did not independently execute** Node or browser tests. The latter does not render PSD. Other review summaries were visible from GitHub metadata during inspection, but this report reflects own source/test audit, not copied test executions. Review mode read-only in Auralprint; **no app code changed, no PR merge, no other-agent memory edited**.

## Future triggers

When Axiom reconciles the six independent reviews or the first PSD panel/instrument status model is designed, verify the then-current head, preserve owner approval for schema, and require an explicit renderer last-painted receipt distinct from PSD derivation frontier. Resource work admission issue belongs to its own specialty review and Issue #11 before claiming broadly configurable real-time performance.

**Authorial perspective:** Mothlight — The Invisible Stagehand.

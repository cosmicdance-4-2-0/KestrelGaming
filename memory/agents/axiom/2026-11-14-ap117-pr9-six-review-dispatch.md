---
schema: 1
id: 2026-11-14-ap117-pr9-six-review-dispatch
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr9-integration-audit
created: 2026-11-14
updated: 2026-11-14
sources: "Auralprint PR #9 exact head 35ae476ec8d59c300de877381f84ec7b8c59a1fa and main 0531e734a2ece59cd877ea8659069efee2e0a905; GitHub Actions workflow run 43690871559; PR #9 six-engineer dispatch comment 6891240452."
---

# Auralprint 117 — PR #9 initial integrator check + six-engineer review dispatch

## Status

**HOLD for six independent source-pinned specialist reviews.** PR #9 is a draft, open, unmerged against accepted `main@0531e734a2ece59cd877ea8659069efee2e0a905`. Exact implementation head: `35ae476ec8d59c300de877381f84ec7b8c59a1fa`; 12 changed files, 1394 additions/11 deletions. [GitHub Actions run 43690871559](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43690871559) completed successful tests, build, HTML and browser smoke (read from run summary/steps); Codex additionally reports 93 tests and diagnostics in PR body. Axiom reviewed changed spectrum delivery/stream implementation and app/config source directly, did **not** independently rerun the whole suite in a local checkout (network-restricted environment), and did not merge.

### Implementation summary and review risks

`src/analysis/spectrum-delivery.js` adds a trusted built-in-only bounded complete pull API `subscribeComplete({capacityObservations})` with `take/readStatus/resync/dispose`. `src/analysis/spectrum-stream.js` validates full waveform, stages complete windows before commit and publishes same latest `readCurrent`; `CONFIG.spectrum.delivery` assigns proof budgets maxSubscriptions8, maxCapacityObservations64, maxRetainedBins262144, maxInputFrames8192. Pagehide now terminates spectrum producer. New unit tests and test-only CPU/allocation diagnostic added; no PSD production or new panels; CP2 and FFT numeric source files unchanged.

Review *as risks to falsify*, not as already confirmed defects: bounded staging, 20-frame atomic cap2 overflow, no leaked partial ready on late invalid sample, generation/continuity fences for older same-generation observations, per-sourceRevision break/resync loss, final drain and post-end/EOF paths, and cross-provider issuance. In particular generation starts at `1n` in each producer; if a consuming analyzer migrates to a newly constructed provider without keeping actual subscription/provider-handle identity, equal numeric generation/continuity values could be mistaken for equivalent authority even though the source label matches. Latch/Harbor should test explicit ownership and whether extra provider identity is needed; do not call this a proven current failure without a failing witness. Heavy worst-case FFT scratch remains significant, acknowledged by Codex as out of scope for numeric algorithm modification.

### Senior review handoff

[Single shared source-pinned PR comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9#issuecomment-6891240452) contains six **individually specialized read-only assignments**. Gauge: numerical/oracle. Flint: interface/staging/memory/failure atomicity. Harbor: lifecycle, EOF and reset fences. Latch: trust/PCM ownership and cross-provider identity. Kite: cost and push/pull alternatives. Mothlight: three-axis status truth. Human dispatcher sends this shared comment to each existing agent session; no auto-launch of their sessions is implied. Each loads own agent identity, reviews exact head before peer reports, records individual dissent, responds with PASS/CONDITIONAL/BLOCK and reproducible evidence.

**Authorization:** no application code change, reviewer code edits, merge, deployment, or implemented PSD/B2 feature was authorized by this dispatch. Owner retains final merge authority.

## Next

Collect six exact-head reports, independently inspect claimed blockers, commission Codex limited repairs on same PR as needed, re-pin to changed head, repeat relevant reviews, and prepare owner-facing acceptance verdict only after review and tests.

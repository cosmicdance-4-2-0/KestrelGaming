---
schema: 1
id: 2026-11-15-ap117-codex003-first-psd-consumer-handoff
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-codex003-delegation
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint PR9 merged SHA 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f, issue #6 design and new comment 6893665904, issues #10/#11, docs/CP3_FREQUENCY.md, docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md, Gauge G05 PSD handoff, current src/analysis/spectrum-stream.js and spectrum-delivery.js, project AGENTS.md."
---

# Auralprint 117 — Codex assignment 003, first true downstream PSD consumer

## Source verification

Owner confirms PR #9 merged and asks to send Codex back to implementation. GitHub PR #9 metadata verified **merged 2026-11-15 11:15:16Z**, source head `35ae476ec8d59c300de877381f84ec7b8c59a1fa`, merge commit and currently `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. This is now the accepted CP3-A + AP117-002 bounded pull baseline. Inspected issue #6 B1 PSD design and owner-revised complete-data requirement, issue #10 handle/EOF integration gate, issue #11 deferred compute operating envelope, current FFT/delivery source, CP3 frequency contract, and Gauge's prior PSD numerical design.

## Assignment handed to owner

Standalone downloadable human-side Markdown: `CODEX_AP117_003_PSD_Consumer.md` (not checked into repo; generated in conversation). **CODEX-AP117-003 — First complete-spectrum analysis consumer (PSD)**: local implementation/test and **authorized push of task branch + draft PR**, no merge/release. Project-scope note posted on [Issue #6 comment 6893665904](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6893665904). No new code/PR launched by Axiom.

Specific decisions *for this bounded candidate*, not owner-ratified permanent public PSD API:
- Same-window CP3-A complete FFT bins to separate owned/frozen versioned proposed `ap117.psd/1` quantity `power-spectral-density`, unit `normalized-pcm-amplitude-squared-per-hz`, method `real-one-sided-windowed-periodogram-density/1`, digital only; single-window unaveraged no detrend, no independent DSP geometry, no Welch, no VU/loudness.
- Gauge's PSD identity `P[k]=A[k]^2/(c[k]*ENBW_Hz)` for matching window, one-sided `c[k]=1` DC/Nyquist else `2`. Independently compare direct DFT all bins and window-weighted Parseval; no claim equality to CP2 unweighted RMS².
- Consumer constructs with the *actual* trusted complete-delivery subscription handle, drains its own future-only observations with explicit break/ended/resync and no unbounded history or callback-in-producer, exact BigInt spans/spectrum lineage. No generic arbitrary-receipt ingress or coalesced readCurrent as sole source.
- Issue #10 negative tests: collision of local generation/continuity ordinal from different producer instances, two same-producer handles where later B must not adopt A's earlier record, correct same-handle historical eligibility, and recheck after any asynchronous computation; readStatus ended with final backlog must drain via take until ended; sticky overrun/sourceRevision/replay/epoch continuity must be honest. B1 consumer scope must not claim plugin security.
- Gauge legal end-to-end 20 final vs five 4-frame input partitions, four PSD windows, own completion ordinals and distinct CP2 finishing input revisions, no second source read or FFT. Existing browser remains latest only; no GUI/compositor, new rAF or hidden automatic host analysis task. A real test-host integrated producer→PSD demonstration suffices for this headless numerical checkpoint.
- Issue #11 compute/GC gate separate: no invented performance/realtime promise or FFT refactor. No code edit of accepted PCM, RMS, spectral FFT normalization or rendering error policy.

## Handoff/acceptance

Codex to commit, push an isolated task branch and open a **draft** PR against pinned/main ref with evidence, exact tests, independent PSD oracle and handle identity/EOF negative tests, changed paths and risks, and invitations for six specialist source-pinned reviews. Axiom reconciles the PR; owner accepts/merges. If a scope or source contract conflict stops honest implementation, Codex should report rather than build a generic broker.

## Revisit when

Codex draft PR exists and exact SHA can be audited; main moves, Gauge identifies a conflicting estimand/fingerprint, issue #10 contract cannot be mechanically proven, owner requests different PSD method or independent window, or upstream delivery changes.

---
schema: 1
id: 2026-11-07-ap117-cp3a-pr5-corrective-re-review-146a
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-cp3a-corrective-review-session
created: 2026-11-07
updated: 2026-11-07
sources: "ap_117_KESTREL PR #5 corrective head 146a8c92ef54069f679b82f63b96608ae727415d vs prior 23da63f8e8427d9b23c3f63794aeef6634fd466b; exact-head CI 42437698669; independent isolated V8 module-function probes; GitHub review 5816122743"
---

# Flint — Auralprint 117 CP3-A corrective-head acceptance, PR #5

## Summary

**Review outcome: PASS for Flint's architecture/interface remit at exact head `146a8c92ef54069f679b82f63b96608ae727415d`.** The earlier [REQUEST CHANGES finding](2026-11-07-ap117-cp3a-pr5-contract-review-f51b.md) remains historically true at `23da63f8`, but this corrective head closes it. Reviewed only; no implementation, merge, release, CP3-B, or claims of independent Gauge/Harbor approval for this new SHA.

The one-commit correction requires the complete accepted CP2 RMS measurement fingerprint at the exported spectrum adapter; fixes the hardcoded UI FFT parameter label with policy-neutral copy; adds a table-driven regression; documents the contract. Only four files changed: `src/analysis/spectrum-stream.js`, `tests/spectrum.test.js`, `index.html`, and `docs/CP3_FREQUENCY.md`. FFT arithmetic/window assembly, CP2 analysis/PCM, FrameHost, models/renderers and runtime dependencies are untouched. No new abstraction added.

## Evidence

- **GitHub branch evidence:** Compared `23da63f8` to `146a8c92`: one commit ahead, zero behind, four files. PR #5 stayed open, unmerged, head pinned before [formal Flint review 5816122743](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5#pullrequestreview-5816122743).
- **Source-executed independent controls:** Fetched exact-head `fft-amplitude.js` and `spectrum-stream.js`; adapted import/export syntax to run their original functions in a controlled V8 evaluator. Six previously forged CP2 label fields (schema, validity, unit, reference, method, calibration) now reject. Additional invalid quantity, RMS value NaN/negative, missing/blank channel ID, incorrect nested channel, empty waveform and nonfinite PCM reject. Two positive controls (canonical and matching nested channel) publish coherent ready DC amplitude 0.25 on 8 constant PCM samples of 0.25. **16/16 probes passed.**
- **Additional publication-lifetime control:** After a valid spectral ready publication, forged method rejects, stream publication becomes unavailable/null and old stamp becomes noncurrent. Fresh correct input after reset is accepted. No stale measurement remains visible.
- **Exact-head CI check:** [Actions 42437698669](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42437698669) concluded success; inspected job logs: **67 tests passed, zero failed**, static/offline build, Nu built/rendered HTML, Chromium smoke, artifacts and whitespace gate. FFT1024 median 0.068 ms, p95 0.192 ms on hosted runner, not an SLA. **No full independent local checkout/browser suite executed.**
- **Historical peer attribution:** Gauge numerical PASS and Harbor lifecycle PASS applied to previous `23da63f8` head, not an automatic approval of `146a8c92`. Their independent current-head review is for them or the owner to determine.

## Decision

**No remaining Flint blockers at the exact corrective head.** Validation at the exported interchange seam is narrow and justified by a reproduced counterexample, without generic schema tooling. The CONFIG label no longer falsely promises particular configured spectral parameters. Previously proven FFT geometry/ownership boundaries are not modified in this correction.

## Revisit when

PR #5 changes head or is considered for owner merge. Reverify correction, tests and exact-head CI if changed. Do not transfer this pass to later heads or imply hardware, realtime, device/browser parity, or CP3-B readiness.

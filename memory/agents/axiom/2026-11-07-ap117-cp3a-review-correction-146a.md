---
schema: 1
id: 2026-11-07-ap117-cp3a-review-correction-146a
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-review-reconciliation-session
created: 2026-11-07
updated: 2026-11-07
sources: "ap_117_KESTREL PR #5 exact reviewed 23da63f8e8427d9b23c3f63794aeef6634fd466b; Harbor review 5815511122, Gauge review 5815869593, Flint review 5815954595; corrected branch head 146a8c92ef54069f679b82f63b96608ae727415d; GitHub Actions 42437698669; PR handoff issuecomment-6716067944."
---

# CP3-A PR #5 — Gauge/Flint/Harbor review reconciliation

## Summary

**Outcome: CORRECTION COMPLETE, CI PASS, INDEPENDENT RE-REVIEW PENDING.** Axiom read all three exact-head reviews on application PR [#5](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5), applied the single bounded architecture correction on the existing `feature/axiom-cp3a-spectrum` branch, and requested new-head re-review. Latest candidate is `146a8c92ef54069f679b82f63b96608ae727415d`, one commit ahead of first reviewed head `23da63f8e8427d9b23c3f63794aeef6634fd466b`, unchanged base `main@790e71f300ad24e01ec97c7ef42f4ca500ba1080`. PR #5 is **open, ready for review, unmerged**; no CP3-B/PSD or unrelated changes.

## Independent reviewers on prior head

- **Harbor:** [PASS lifecycle/recovery](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5#pullrequestreview-5815511122), source-executed controls for single source read, one FrameHost/timer, two Canvas exceptions, partial-window preservation, replay and EOF, parameter revision, channel/file switching, pagehide and artificial BFCache. Nonblocking issue: `index.html` duplicated Hann/window/hop constants outside authoritative `CONFIG.spectrum`.
- **Gauge:** [Numerical PASS / interface CONDITIONAL PASS](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5#pullrequestreview-5815869593). Independent direct DFT comparisons of all one-sided bins, maximum absolute FFT amplitude error ~7.29e-15 over six deterministic cases; 16-point Python fixture max difference ~5.55e-17, Hann ENBW 70.3125 Hz at fs=48000 and N=1024, sample chronology and multi-partition checks. Found exported spectrum ingress accepts `ready` record with invalid CP2 schema/validity.
- **Flint:** [REQUEST CHANGES](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5#pullrequestreview-5815954595). Independently expanded Gauge's forgery to six CP2 semantic fields: schema, validity, unit, reference, method, calibration; normal upstream CP2 pipeline did not produce such forged ready records. Also reiterated CONFIG/UI nonblocking drift. The reviewers' conclusions apply only to `23da63f`, not the later corrective SHA.

## Correction at 146a8c92

Only four paths changed from reviewed head: `src/analysis/spectrum-stream.js`, `tests/spectrum.test.js`, `index.html`, and `docs/CP3_FREQUENCY.md`.

1. **Exported adapter fingerprint validation:** `createSpectrumStream.accept` now checks exact `ap117.measurement/2`, `rms-amplitude`, `valid`, `normalized-pcm-linear`, `pcm-full-scale-amplitude-1`, `unweighted-mean-square-sqrt/1`, `digital-normalized-no-physical-calibration`, finite nonnegative RMS value, and a required nonblank measurement-level channel ID. Existing sample-span/clock/epoch/placement checks remain; the optional nested channelId fallback remains valid when it agrees with the required channel. Forged observations throw and clear the spectral publication.
2. **Regression:** existing manual test fixture updated to canonical CP2 fingerprint; new table-driven test passes canonical observation with optional nested channel ID absent, rejects independent mutations of quantity/schema/validity/unit/reference/method/calibration, negative/nonfinite values, blank channel and mismatched nested channel; fails closed with no published measurement.
3. **CONFIG/title drift:** `index.html` title now declares method only (windowed FFT / linear peak amplitude) rather than hardcode Hann, 1024 and hop 512. `CONFIG.spectrum` remains authoritative. Contract docs updated.
4. No change to FFT arithmetic, spectrum buffering/hop strategy, input pipeline, WAV or RMS, frame host, Canvas backend or numerical conventions. No generic schema registry added.

**Exact-head CI:** [Actions run 42437698669](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42437698669) succeeded at `146a8c92ef54069f679b82f63b96608ae727415d`: **67/67 Node tests**, static/offline build, official Nu HTML, Chromium browser smoke including dual Canvas and recovery, browser artifact and committed-whitespace gate. Runner FFT 1024-point median ~0.068 ms / p95 ~0.192 ms this run, not performance certification. This is CI-attributed evidence, not an independent local checkout or peer re-review.

## Review handoff / conditions

Posted [correction handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5#issuecomment-6716067944). Ask **Flint and Gauge** to rerun the forged ready-publication negative controls on the exact new SHA; **Harbor** to confirm no recovery regression. Do not extrapolate prior PASS to changed head without review. Owner retains merge/integration authority; no PSD work until CP3-A acceptance.

## Revisit when

PR #5 head/base changes, new exact-head re-review comments arrive, owner merges/rejects CP3-A, or another forged-interchange negative demonstrates an incomplete contract.

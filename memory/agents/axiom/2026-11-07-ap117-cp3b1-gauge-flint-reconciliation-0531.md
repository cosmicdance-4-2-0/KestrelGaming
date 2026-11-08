---
schema: 1
id: 2026-11-07-ap117-cp3b1-gauge-flint-reconciliation-0531
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-reconciliation-session
created: 2026-11-07
updated: 2026-11-07
sources: "Gauge design 2026-11-07-ap117-cp3b1-gauge-psd-design-g05.md at agents/gauge-v1; Flint issue #6 comment 6716513401; CP3-A main 0531e734a2ece59cd877ea8659069efee2e0a905; Axiom issue #6 reconciliation 6716665039."
---

# Auralprint 117 — CP3-B1 Gauge/Flint design reconciliation

## Summary

**Outcome: DESIGN RECONCILED INTO INTEGRATOR RECOMMENDATION; OWNER SCOPE ACCEPTANCE AND HARBOR DESIGN CHECK PENDING; NO PSD IMPLEMENTATION/BRANCH/PR.** Following the user's team-first instruction, Gauge independently completed PSD mathematical design and proposed architecture **C** (derive a newly typed PSD observation from accepted CP3-A peak-amplitude bins). Flint independently executed CP3-A stream code and produced a conditional architecture PASS with concrete lost-history and repeated-stamp counterexamples. Axiom inspected the actual baseline `main@0531e734a2ece59cd877ea8659069efee2e0a905`, verified output metadata location/window semantics, then posted [integrator reconciliation in issue #6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716665039). The linked issue comment is the detailed contract; the concise continuity below preserves the decision boundary.

## Evidence and integration recommendations

- [Gauge PSD design, independent math and SciPy](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/gauge-v1/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-07-ap117-cp3b1-gauge-psd-design-g05.md): 36 Python cmath cases; 24 SciPy periodogram comparisons with `detrend=False`, `scaling=density`, `return_onesided=True`; V8 source-executed CP3-A FFT on independent cases. Proposed one-sided modified periodogram `P[k] = c[k]|X[k]|²/(fs*U)`, with `U=sum(w²)`, `c=1` DC/Nyquist, 2 at interior positive bins. Parseval integral `sum(P[k]*df)=sum(x²w²)/U` (not generally CP2 RMS²). For accepted CP3-A `A[k]=c[k]|X[k]|/S1` and `ENBW=fs*U/S1²`, `P=A²/(c*ENBW)`. Numerics independent; no physical units or stable-noise-floor claim.
- [Flint's structural challenge](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716513401): CP3-A `M8/H4/N8` with one 20-frame PCM block calculates four internal complete windows but exposes only final `[12,20)`; partitioning into multiple accepted blocks exposes four ready publications. An additional partial source block returns unchanged latest ready stamp. PSD adapter **must deduplicate same input revision and never claim every complete window or enforce consecutive output start frames exactly H**. Output must be its own owned/frozen snapshot + revision. Current CP3-A window metadata has `kind,sampleFrames,fftFrames,sumWeights,sumSquaredWeights,coherentGain,hopFrames`; ENBW resides on measurement top level, and no upstream window definition field exists.
- Axiom recommended **D1=YES C only for same CP3-A/latest observable window**, **D2=YES high-variance single modified periodogram without averaging/detrend**, **D3=YES latest observable not full history**, **D4=YES supported rectangular/periodic-Hann positive-S1 method fingerprint locked; new normalizations/windows fail closed until versioned**. These recommendations are NOT yet independently accepted by owner.
- New `ap117.psd/1` is distinct quantity `power-spectral-density`, unit `normalized-pcm-amplitude-squared-per-hz`, reference `pcm-full-scale-amplitude-squared-1`, method `real-one-sided-windowed-periodogram-density/1`, derivation `from-ap117.spectrum/1-peak-amplitude/1`, no detrending, calibration digital-only, provenance includes both CP3-A input spectrum revision and original CP2 input publication revision. New own numeric array and publication revision, BigInt sample spans, one explicitly owned ENBW field in new PSD window metadata. No second source read/clock/FFT/rAF/PCM buffer. Exact full CP3-A fingerprint, legal supported M/Nfft/H/fs/ENBW/S1/U/df/array shape and finite nonnegative bins required.
- Unchanged same spectrum publication stamp is no-op; contradictory reused stamp or lower stale revision causes PSD invalidation and throws; upstream invalidation withdraws PSD, but clean EOF can retain latest valid historic complete-window PSD. New channel/source/replay resets publication; adapter never invalidates CP3-A itself.
- **Deferred A** separate PSD assembler/FFT for independent PSD window/detrending/history, zero-sum coherent-gain windows, or Welch; **deferred B** shared complex FFT refactor absent demonstrated benefit. No PSD or B2 user interface code in this session.
- Acceptance falsifiers: SciPy detrend=False; complex DFT/weighted Parseval; Hann endpoint vs center impulse; DC/Nyquist no doubling; zero-pad Nfft>M; off-bin/random tone and actual Float32 input; Flint's one-block-vs-partition structural control; duplicate/stale stamps and source switch; forged CP3-A fingerprint/window/bins/spans; >Number.MAX_SAFE_INTEGER BigInt source frames; short EOF; render failure/invalidation and replay. Gauge/Flint numerical and interface review, Harbor lifecycle design review, owner scope decision, then implementation PR on new branch.

## Revisit when

The owner decides D1-D4, Harbor returns a design-only reset/EOF critique, app main advances, CP3-A publication/frequency method changes, or B1 implementation branch is opened. Preserve Axiom project-integrator authority separately from owner merge/acceptance authority and independent reviewer attribution.

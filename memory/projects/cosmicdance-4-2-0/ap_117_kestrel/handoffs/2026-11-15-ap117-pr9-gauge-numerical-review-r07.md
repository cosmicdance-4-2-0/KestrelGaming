---
schema: 1
id: 2026-11-15-ap117-pr9-gauge-numerical-review-r07
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-15
updated: 2026-11-15
sources: "Axiom's PR #9 dispatch issuecomment-6891240452; exact application PR head 35ae476ec8d59c300de877381f84ec7b8c59a1fa against accepted main 0531e734a2ece59cd877ea8659069efee2e0a905; original exact-source JS bodies independently executed in V8, independent complex DFT in V8 and Python, full PR patch, CI job 132741057728; Gauge home c54857f04d6a2a8d234f7d64c545a44ae95676e7 before this record. Review-only."
---

# Gauge — AP117-002 PR #9 numerical review (R07)

**Verdict: PASS — assigned numerical-integrity remit, exact head only.** No numerical blocker reproduced in tested conditions. This is not full PR approval, feature release, merger authorization, security isolation or realtime certification.

**PR:** [#9](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9). **Dispatch:** [Axiom's comment 6891240452](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9#issuecomment-6891240452). **Application head:** [`35ae476ec8d59c300de877381f84ec7b8c59a1fa`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/35ae476ec8d59c300de877381f84ec7b8c59a1fa); **accepted base** `main@0531e734a2ece59cd877ea8659069efee2e0a905`. Both refs were reverified unchanged before report construction.

**Gauge's individual contract:** `agents/gauge-v1@c54857f04d6a2a8d234f7d64c545a44ae95676e7` before record; `AGENTS.md`, `KESTREL.md`, `agents/gauge/AGENT.md`, `PROFILE.json`, `kestrel/MEMORY_PROTOCOL.md`, `VERIFICATION.md`, `PERMISSIONS.md` and relevant Auralprint continuity were consulted. Older [G05 PSD design](2026-11-07-ap117-cp3b1-gauge-psd-design-g05.md) and [R06 synchronization](2026-11-14-ap117-sync02-gauge-completeness-r06.md) define previous numerical reference. Issue #8's earlier approved *design reconciliation* was read for requirement context, **not** other engineers' new PR #9 reviews. Independent findings were recorded before consulting any new peer first-pass.

## Summary

**Source-executed evidence:** The change retains accepted one-sided peak-amplitude FFT bins and exact source sample chronology, while providing separate complete observations. The new delivery layer has **no PSD production feature**. Direct FFT/PSD/Parseval references and exact-base shadow comparisons did not reveal a different valid-data spectrum or completing-block lineage.

- **First independent numeric sweep:** 27 completed windows, 1,035 one-sided bins, six finite-waveform fixtures (periodic Hann/rectangular, zero-pad, off-bin/DC, Nyquist, impulses) comparing two legal acquisition partitions. Direct complex O(MN) DFT maximum absolute amplitude difference `1.224071455120874e−15`; per-bin test-only PSD difference `2.846030702774449e−19`; weighted Parseval difference `2.220446049250313e−16`. Cross-partition amplitude arrays **identical**.
- **Second sweep:** six standalone windows, 966 bins, fs 44.1/48/96/192 kHz, Hann/rectangular/zero-padded, 1024 coherent sine, DC/Nyquist, Hann zero-edge and center impulses. Maximum independent DFT amplitude difference `1.0029597082817798e−14`; test-only PSD bin difference `8.998878031629687e−18`; weighted Parseval difference `8.881784197001252e−16`.
- **Legacy regression:** 203 explicit acceptance comparisons, **zero failed**, between actual original CP3-A and exact PR code on successive legal blocks, including parameter-revision change and adapter sample starts above `2^80`. Compared ready status, own revision, exact latest bins, BigInt spans, completing CP2 input publication revision, window sum and ENBW.
- **Atomicity probes:** late NaN, injected mid-FFT exception and cap2/cap4 subscriber pressure reproduced on exact new module bodies. Rejected inputs committed **no** partial window batches.
- **CI provenance:** GitHub Actions [run 43690871559](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43690871559), job `132741057728`: log explicitly reports **93 tests, 93 passed, 0 failed**, static/HTML and Chromium smoke successful. Those are attributed runner results, **not** a fresh local `npm run verify`.

**Status:** Numerical PASS at exact SHA; Axiom and owner retain HOLD pending API, lifecycle, trust, UI and performance disciplines. No app implementation, commit, merge or deployment occurred during this review.

## Evidence

### Reviewed source, diff and tests

Inspected actual 12-file PR patch, source, added numerical/atomic/lifecycle/queue tests and AP117-002 contract, not only PR description.

| Source | Exact head Git blob | Finding |
| --- | --- | --- |
| [`fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/fft-amplitude.js) | `ee35e0793aceb5eb9e3fc49d27f293a1719effc5` | Unchanged accepted radix-2 FFT and one-sided peak amplitude arithmetic |
| [`spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-stream.js) | `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc` | Prevalidates waveform, stages all completions, commits latest only after success, preserves individual source window spans |
| [`spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-delivery.js) | `ef19cd748de41226ab0cd8375949e278f7aeb76f` | BigInt generation/ordinal, bounded subscriber queue and explicit continuity break; no second FFT/source read |
| [`pipeline.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/pipeline.js) | `25f396217a54501d3ea3565bac1b8e2eb0c46b0f` | Unchanged CP2 source identity/clock and nonfinal block-length enforcement |
| [`pcm-buffer-source.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/audio/pcm-buffer-source.js) | `7fd18ecb6a579dcc7f1fc70c64974602f0c9c0fb` | Accepted single-read source path used in exact legal-partition test |
| [`config.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/config.js) | `2408897d5f7c6f5ff0c08e65d54af4cf1a4405b1` | Adds resource budgets, does not change FFT method/defaults |
| [`spectrum-delivery-math.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery-math.test.js) | `fb387763cd7b51249c838c9de807b85740a59b22` | Four exact windows, direct DFT+Parseval, legal partitions and illegal ingress negative |
| [`AP117-002 implementation record`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md) | `f56821afa8fbc645fef6e5dfa7bea69877ac2ba4` | Experimental scope and interfaces, no PSD or general broker |

New code lines approximately `spectrum-stream.js:79–195` prevalidate/stage/commit, `spectrum-delivery.js:108–143` preparation/commit, `tests/spectrum-delivery-math.test.js:79–200` positive and negative controls.

### Four exact windows, method and lineage

For `x[n]=(n+1)/32` (20 exact Float32 values), fs48000, periodic Hann M8/H4/Nfft8:

    S1=sum(w)=4, U=sum(w²)=3, df=6000 Hz, ENBW=9000 Hz
    X_q[k]=sum_(n=0..7) x[q*4+n] w[n] exp(-i2πkn/8)
    c[k]=1 at DC and Nyquist, else 2
    A_q[k]=c[k]|X_q[k]|/S1
    P_q[k]=c[k]|X_q[k]|²/(fs U)=A_q[k]²/(c[k] ENBW)
    sum_k P_q[k]*df = sum_n x[q*4+n]² w[n]²/U

| Exact source span | DC peak A[0] | Test-only PSD P[0] (normalized PCM²/Hz) | Integrated PSD (window-weighted mean square) |
| --- | ---: | ---: | ---: |
| `[0,8)` | `0.15625` | `2.71267361111111e−6` | `0.02566508650732670` |
| `[4,12)` | `0.28125` | `8.78906250000000e−6` | `0.08035258650732670` |
| `[8,16)` | `0.40625` | `1.83376736111111e−5` | `0.16629008650732670` |
| `[12,20)` | `0.53125` | `3.13585069444444e−5` | `0.28347758650732670` |

This is **single-window no-detrend modified-periodogram mathematics**, **not a shipped PSD provider**, calibrated physical noise/Watts/dB, Welch estimate or CP2 unweighted RMS².

**Legal partition proof using exact production source:** a 20-frame final source block (CP2 `blockFrames=20`) and five 4-frame blocks (CP2 `blockFrames=4`) yield exactly four ordered `ap117.spectrum-delivery/1` observations. For both, exact spans `[0,8),[4,12),[8,16),[12,20)`, spectrum revisions `2,3,4,5` and completion ordinals `1n..4n`. Completing `inputPublicationRevision` legitimately differs: one block `[2,2,2,2]`; five blocks `[4,6,8,10]`. These are publication origins, not all sample-block inputs to each overlapping FFT window. Comparing full envelopes for equality would be wrong.

The alternative fixed `blockFrames=8` sequence `8,4,4,4` is an **illegal CP2 partition**: the second 4-frame nonfinal block returns `invalid` and `Source returned an incomplete PCM block`. Preserved as negative, not used to assert a legitimate end-to-end case.

### Independent waveform and normalization controls

First suite, 27 completed windows/1,035 one-sided bins, all on `fs=48000` and legal partition pairs:

| Fixture | M/H/Nfft | Window | Windows |
| --- | --- | --- | ---: |
| Exact Gauge PCM series | 8/4/8 | periodic Hann | 4 |
| Sine + DC | 8/4/8 | rectangular | 4 |
| Offbin mixed signal, zero padding | 64/16/256 | periodic Hann | 5 |
| Alternating Nyquist + DC, zero padding | 64/32/128 | rectangular | 3 |
| Nyquist alternating, 4× zero padding | 8/2/32 | periodic Hann | 7 |
| Boundary impulses | 8/4/16 | periodic Hann | 4 |

Second suite, 6 complete windows/966 bins across 44.1/48/96/192 kHz:

| Input | Geometry / window | Independently observed numerical control |
| --- | --- | --- |
| DC 0.25 at 44100 Hz | Hann M64/N64 | A[0]=0.25, integrated PSD=0.0625, ENBW1033.59375 Hz |
| Nyquist ±0.5 at 192000 Hz | Rect M64/N256 | A[Nyquist]=0.5, PSD integral≈0.25, ENBW3000 Hz |
| Coherent sine 0.6 at bin 37, 48000 Hz | Hann M1024/N1024 | Peak≈0.5999999985183873 (Float32), PSD integral≈0.1799999987967642 |
| Impulse at Hann zero-weight first sample | Hann M64/N256 | All bins/PSD integral zero, despite unweighted RMS²=1/64 |
| Impulse at Hann midpoint | Hann M64/N256 | Integrated PSD≈1/24=0.041666667, unlike unweighted RMS²=1/64 |
| DC 0.25 at 96000 Hz | Hann M64/N64 | A[0]=0.25, integral0.0625, ENBW2250 Hz |

An FFT zero-padded from 64 to 256 does *not* increase physical source-window resolution: Hann ENBW remains `1.5 fs/64`, not `1.5 fs/256`. The alternating Nyquist fixture may have off-grid finer-DFT peaks above the coherent Nyquist amplitude due to interpolation; this does not mean the Nyquist-bin scaling is incorrect.

**Method evidence:** Actual source module text fetched by exact Git SHA; functions evaluated in isolated V8 with **only ESM import/export declaration syntax adapted**, never rewritten numerical function bodies. Independently authored O(MN) real/imag complex DFT (versus production radix-2); separate Python standard-library `cmath` check for exact four windows. These are distinct numerical expressions, not copies of PR's unit-test oracle.

### Exact accepted-base comparison and BigInt

Separate V8 function scopes loaded accepted `main` and PR `35ae476` source. **203 compatibility assertions, none failed** across four legal sequential-input configurations plus a parameter-revision transition. Checked latest `status`, own `revision`, bit-identical numeric arrays, exact `sampleSpan`, completing `inputPublicationRevision`, ENBW and `sumWeights` after each `accept`.

Specific cases: periodic Hann M8/H4/N8 (eight legal 4-frame blocks), rectangular M8/H2/N32 (twelve legal 2-frame blocks), periodic Hann M64/H16/N256 (seven legal 16-frame blocks), and periodic Hann M8/H4/N8 at direct-adapter BigInt source start `2^80+12345` (five 4-frame blocks). The full CP2 pipeline legitimately requires initial frame0, so the extreme offset is **adapter-only**, not falsely called legal full-pipeline source input. Same-source-epoch `sourceRevision 0→1` discards cross-parameter partial windows, emits a subscription break and maintains exact accepted latest spectrum/revision for new windows.

**Meaningful limit:** The accepted latest-only stream exposes only the final spectrum of a multi-completion block. To challenge individual new delivery bins, compare them to independently written complex DFT and to accepted old stream under legal `blockFrames≤hopFrames` where each completed window is visible. Both approaches were exercised.

### Negative input and atomicity probes

At exact head, trusted adapter inputs, Hann M8/H4/N8:

| Independent probe | Observed result |
| --- | --- |
| Late NaN at sample index19 of 20 | Throws `Nonfinite spectral PCM` before any `Math.hypot` (count0); latest unavailable revision2; subscriber break; queue0 |
| One previously committed ready; next accept throws at FFT hypot operation6 | Prior latest remained observable until exception, then unavailable; revision increased **only one**; queued previous ready discarded; subscriber break, no new batch |
| Four-window atomic input; capacity2 and capacity4 consumers | cap2 sticky `subscriber-delivery-overrun`; cap4 exactly four ordered windows/start frames 0,4,8,12; latest span[12,20); clean final `ended` after drain |

One **lifecycle policy for Harbor/Axiom to explicitly acknowledge:** `parametersChanged` in `spectrum-stream.js` forces retain=false even when the first new-revision input finishes valid new-segment windows. Those windows are computed, and subscriber gets an explicit `source-parameters-changed` continuity break; after resync those first new-segment windows are **not replayed**. It is **signaled loss**, not a numerical corruption or silent continuous history; changing retention rules would require a deliberate lifecycle/ownership decision. This observation is not a numerical BLOCK under the stated `break/resync` semantics.

### Severity and disposition

| Grade | Finding | Action |
| --- | --- | --- |
| **NUMERICAL PASS** | Peak FFT bins, Hann/rectangular/zero-pad normalization, test-only PSD/Parseval | No numeric correction requested at exact head |
| **LINEAGE PASS** | Four complete spans, CP2 finishing stamps, BigInt origin, same-epoch parameter split | Preserve exact source-window chronology and per-window method labels |
| **ATOMICITY PASS (focused)** | Rejected batches do not expose early windows as committed truth | Preserve prevalidation+staged commit; still needs broader integration review |
| **CONTINUITY NOTE** | First new-revision windows deliberately omitted after break | Harbor/Axiom should affirm intended recovery/coverage semantics |
| **UNVERIFIED** | Device and GC latency, hostile consumers, BFCache, production PSD, broader model UI | Not within numerical acceptance; no claims made |

**No required numerical corrections.** Keep FFT code, `ap117.spectrum/1`, default M/H/N, source/epoch/channel/tap sample-time semantics, and old latest-only drawing intact. Do not label `ap117.spectrum-delivery/1` as PSD or complete historical physical calibration.

## Environment, limits and authority

This review **did not** check out/clone the application for `npm run verify` because the isolated container lacked GitHub DNS/network. Actual source code was inspected/fetched through the GitHub connector and executed in isolated JS V8. The GitHub Actions 93/93 and Chromium success were *verified from the exact job log* and remain CI-attributed. No live device, microphone, physical PSD calibration, full browser consumer delivery trace, memory/performance proof or formal exhaustive IEEE-754 correctness proof was performed.

Reviewed only; no app edits, branch commits, PR merge, deployments, other agent memories or shared contracts altered. This report and its Gauge project index are the only intended branch-local persistence. A PR review comment will carry the numeric PASS with explicit source pin and evidence limits. Shared GitHub authentication does not certify independent agent runtime identity.

**Challenge response:** I tried multiple signals/window families/FFT zero-padding, legal multi-vs-small-block chronology, far BigInt, parameter revision, late NaN and injected FFT exception. **None produced a valid-input spectrum or lineage differing from accepted CP3-A under the exercised contract.** Future counterexamples still warrant a new exact-head review; this is a reproducible bounded PASS, not a blanket theorem.

## Revisit when

The PR head moves, a source fix alters `spectrum-stream.js`/`spectrum-delivery.js`, another independent reviewer demonstrates a conflicting valid trace, Axiom proposes a different numeric convention, or PSD B1 is actually implemented. Re-pin and rerun the accepted-base direct comparison, all four Gauge windows, BigInt/revision cases, independent Parseval and late-failure atomicity.

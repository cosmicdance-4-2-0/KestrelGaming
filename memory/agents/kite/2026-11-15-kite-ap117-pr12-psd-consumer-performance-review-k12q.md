---
schema: 1
id: 2026-11-15-kite-ap117-pr12-psd-consumer-performance-review-k12q
kind: decision
scope: agent:kite
status: draft
evidence: inferred
author: kite-session
created: 2026-11-15
updated: 2026-11-15
sources: "ap_117_KESTREL PR #12 @0880fc8df9182cce9ed2c645e324a2d291375281 vs main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; issue #10/#11; Kite agents/kite-v1@46c81399c35369dee74fbb3a25050874e4d5d7f8."
---

# Kite — AP117-003 PR #12: source-pinned PSD consumer performance and alternative review

**Exact subject:** https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12, draft `codex/ap117-003-psd@0880fc8df9182cce9ed2c645e324a2d291375281` against accepted `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. Remote PR head and live main matched those SHA values at first-pass review. One commit, six additive files, 1312 lines and zero deletions. All implementation/accepted pipeline files outside the new PSD module are unchanged.
**Assignment orientation:** User asked Kite to independently assess PR #12 after prior AP117-002 performance/alternatives review; PR specifically requests Kite audit O(M) constructor, O(bins) derivation, operation-count claims and deferred Issue #11. No issue/PR implementation edit or merge authorized.
**Identity/continuity:** Loaded Kite — The Unlicensed Inventor from `cosmicdance-4-2-0/KestrelGaming/agents/kite-v1@46c81399c35369dee74fbb3a25050874e4d5d7f8`, including its AGENTS, KESTREL contract, own AGENT/PROFILE, indexed prior AP117 PR #9 review and memory protocol. No other new PR #12 agent review read before this first-pass record. Issue #10/#11 are owner-established earlier context.
**Evidence classes:** Source inspection and GitHub Actions status **observed**; independent lightweight Node checks of the published formula and constructor guard **executed**; acceptance/performance implications **inferred**; application test suite, local processor runtime and browser profiling **not executed**.

## Summary

**Kite specialist verdict: CONDITIONAL PASS (no blocker found in ordinary accepted-configuration PSD semantics); request one bounded constructor-admission correction before calling the proposed consumer interface robust for configurable providers.** The six-file add-on advances the architecture meaningfully: a trusted subscription-bound consumer derives all future-eligible complete FFT windows, never polls `readCurrent` to trigger science, does no extra source read/FFT, and publishes a separate, truthful `ap117.psd/1` quantity with frozen owned numerical densities and precise source/lineage metadata.

**Primary new finding:** `src/analysis/psd-processor.js:18–29` permits `fftFrames = windowFrames = 2**30` and then synchronously evaluates a loop across *more than one billion weights* before it even checks the supplied subscription's actual status. The accepted upstream `createPeakSpectrumAnalyzer` validates `fftFrames <= maxFftFrames` and current CONFIG sets `maxFftFrames=16384`. The proposed PSD constructor's hardcoded `2**30` ceiling neither matches nor references the configured producer bound; a trusted host wiring error or future unconstrained user setting can cause excessive O(M) setup work for a configuration that the actual accepted producer would reject. This is a *source-demonstrated guard mismatch*, not a measured actual one-billion-iteration stall and not a hostile-plugin security claim.

## Evidence and exact paths

**PR source examined at exact head:**
- `src/analysis/psd-processor.js` blob `8cca1cd0da4e4c79e2182aa3d219d55880f2efb3` (276 lines), especially line 18–31 constructor work/guard; 34–52 upstream status; 56–79 bound handle and origin cursor; 99–119 sticky refresh/gap; 134–190 complete PSD derivation; 192–236 zero-argument synchronous take/one-window conversion and failure; 238–275 reset/resync/disposal/current.
- `docs/AP117_003_PSD_CONSUMER.md` blob `aa46ec26ac95044cfe0759b15efce64ae6fb1f7c`, numerical definition, contract/status, known limits.
- `tests/psd-integration.test.js` blob `c6c6d059210ae3ac95e4e90b3aece5805de5a242`, actual CP2→FFT subscription→PSD four windows, source read and FFT allocations.
- `tests/psd-lifecycle.test.js` blob `abf439ef4e1fea87346ca9d708406110ea2f2bf9`, EOF, overrun, same-generation history, source transition, #10 same-stamp cases.
- `tests/psd-boundary.test.js` blob `1b14bd04f206dbd5113aa870a0638cc510c256fd`, malformed source/method/units/geometry/controls/lineage, changing external source config, same-handle fail-closed.
- `tests/psd-math.test.js`, 213 lines, direct complex DFT, time-domain weighted Parseval, periodic Hann endpoint impulse and FFT zero-padding coverage.
- Accepted producer and FFT math at same PR head: `src/analysis/spectrum-stream.js`, `src/analysis/spectrum-delivery.js`, `src/analysis/fft-amplitude.js` (line 6–12 validates `maxFftFrames`, 15–23 allocates/calculates window weights, 35–36 FFT scratch). `src/config.js` actual M=1024/H=512/N=1024/maxN=16384 and delivery budgets.
- Issue #10 requires subscription binding, older legitimate windows, wrong-handle negative cases, terminal drain and sticky break; Issue #11 explicitly defers broad operating-envelope claims/performance benchmarking.

**External CI:** GitHub Actions run `43789892097` reported completed/success at reviewed SHA. The PR author reports local Node v24.22.1, `npm run verify` 119 passing tests, HTML and Chromium browser smoke. These are attributed results, not independently rerun. The current browser app does **not** instantiate this headless PSD processor.

## F1 — MEDIUM; new PSD constructor lacks producer-consistent computational admission

`windowDescriptor` at `src/analysis/psd-processor.js:18–29`:
- checks m is safe integer >=4, h>=1<=m, n>=m, n<=2**30, radix-2 n, window kind;
- then loops `for (let i=0; i<m; i++)` and uses `Math.cos` per periodic-Hann sample;
- source and subscription validation/read occur in the enclosing constructor, but the subscribed handle's *current status is not read until after the O(M) loop*.
- accepted `createPeakSpectrumAnalyzer` instead uses explicit `maxFftFrames` at construction, supplied by CONFIG and originally 16384; its analyzer prevents oversized FFT before weight allocation.

**Independent boolean predicate check actually executed with Node**: M=N=65536, 2**20 and 2**30 all pass the new PSD windowDescriptor's numerical guard; all exceed currently configured accepted producer max 16384. The check evaluated the exact guard expression only; **no billion-iteration constructor was run**. For input M=N=2**30 the module would attempt 1,073,741,824 synchronous Hann weights with no external I/O and without an accepted matching producer. This is provably a work-admission mismatch, but elapsed-time/heap outcome is unmeasured.

**Correction recommendation:** include/validate the actual FFT admission bound `spectrum.maxFftFrames` (or a clearly equivalent producer-provided accepted configuration descriptor), reject n>that bound **before recalibration loop**, and pin tests that accept a valid 16384-point definition while rejecting a too-large n such as 65536 with maxFftFrames 16384. Do not impose a separate magic constant or change the accepted FFT. No unbounded stress test is needed to prove the guard.

**Proportionality:** A trusted built-in host currently passing exact CONFIG remains within 16384 and does not hit the pathological branch. Therefore this is a **condition for robust public/configurable provider adoption**, not evidence of failure in present tests, and not justification for an unrelated FFT performance refactor.

## F2 — MEDIUM evidence limit; PSD arithmetic is one O(B) conversion per delivered window, not benchmarked

With B=Nfft/2+1, `derive` at `psd-processor.js:162–189` allocates one JS numeric array B, loops B and squares each supplied one-sided amplitude, normalizes by c*ENBW; creates frozen owned PSD/sample/window/lineage records. It neither reads PCM nor computes an FFT and retains only one latest PSD internally (plus upstream subscription's existing bounded queue). For actual currently max N=16384, B=8193 and density *numeric payload* ≈ 65,544 bytes/observation, **not a measured V8 allocation/heap bound**. A caller retaining an arbitrary number of returned observations owns that external memory, and the processor does not cap it.

`windowDescriptor` does a separate O(M) sum/weight calibration at construction; repeated consumers duplicate that relatively small work for actual M<=16384. One PSD computation is O(B); an actual consumer draining Q observations is O(Q*B). For normal M=1024,N=1024 B=513. In a compliant provider Q per accepted producer block is bounded by its subscribed delivery capacity or a continuity break. Source code counts and tests are sufficient to establish *lack of extra FFT/source reads*, **not** a measured CPU, GC pause, processing-latency or realtime budget.

**Proposed measured gate for Issue #11 when owner authorizes:** compare source+RMS+FFT alone vs source+RMS+FFT+bounded delivery drain+PSD under identical *legal* partitions and named M/H/N, with explicit source read counts, throughput, per-take latency, memory high-water and GC. Warm/rotate and report hardware/Node/browser context. Keep current browser smoke's no-PSD wiring in evidence: there is no device or panel performance result yet.

## F3 — POSITIVE source-supported architecture and numerical compatibility

The code takes only from a captured exclusive actual subscription capability, accepts no external receipt argument, validates generation/continuity/ordinal and full expected source/window/CP3-A method, and rechecks the same handle after synchronous pull. `take()` yields at most one PSD window per call; `readStatus()` separately returns producer status and consumer `drained`, with final backlog retained until `take().ended`. A sticky local/upstream break revokes readiness until explicit frontier `resync`; the earliest reason and latestReason are distinguishable. Accepted `ap117.spectrum/1` and `readCurrent/isCurrent` remain untouched.

The proposed PSD schema is distinct and truthful: `power-spectral-density` in normalized PCM amplitude²/Hz, no physical sound pressure or calibration, no detrend/averaging. Conversion `P[k]=A[k]^2/(c[k]*ENBW)` is exact for the **same complete-window** CP3-A peak-amplitude spectrum; `sum(P[k]*fs/N)=sum((x*w)^2)/U`, generally not CP2 unweighted RMS². Zero-padding changes spacing, not missing PCM. Tests include Hann endpoint impulse with zero window-weighted power versus nonzero unweighted RMS², and the accepted four-window partition invariant.

**Independently executed scalar math control:** Node calculated periodic Hann M8 S1=4/U=3/fs=48000 -> ENBW=9000; four DC amplitudes 0.15625, 0.28125 (0.40625000000000006 due floating sum), 0.53125 and corresponding DC PSD values 2.7126736111111112e-6, 8.7890625e-6, 1.8337673611111112e-5, 3.1358506944444444e-5; direct `(Σxw)^2/(fs U)` agreed at each step. This is a numerical **formula** check and *not* an execution of `createPsdProcessor` or its test suite.

**Trust boundary remains conditional:** numerical stamps are producer/subscriber local and are not security credentials; a host must wire the intended actual handle exclusively. Tests reject calling `processorB.take(receiptA)`, but cannot prove an outside host would never erroneously pass another handle with identical descriptor. The PR explicitly excludes hostile same-realm plugin sandbox and any production host wiring. Keep Issue #10's host-binding gate open for subsequent integration; do not mislabel the present unit tests as third-party authentication.

## F4 — LOW scope/rollback and verification limits

Changes are **six additions only**: 276 implementation lines, 164 design doc lines and four independent-focused test files, with **no** edits to CP2 PCM, existing FFT, spectrum delivery, renderer, CONFIG, or UI. The implementation is opt-in and owns no scheduler. This is a reasonable reviewable proof despite 1312 added lines largely due to tests and documentation; rollback is one commit `0880fc8d`.

**Runtime limits:** GitHub connector provided source/CI evidence, but local container `git ls-remote` failed with `Could not resolve host: github.com`; no local app checkout. I did **not** run `npm run verify`, `npm run test:browser`, any of the new test modules, benchmark, heap profile or source-to-PSD application benchmark. The PR author's 119-test claim and CI success are external evidence. The two local Node snippets executed were arithmetic/predicate-only. No other PR #12 new reviews read before this first-pass record.

## Independent alternative comparison and dissent

1. **Chosen same-window PSD C-stream consumer:** mathematically justified and minimal for the current exact CP3-A method. Reuses peak bins, retains input lineage and no second FFT; derivative contract distinct; guard is explicit no-detrend/nonaveraged. Recommended for this narrow proof once the constructor's admission ceiling is made coherent.
2. **Independent PSD-from-PCM analyzer:** needed if future PSD requires detrending, different window/hop, a different FFT normalization/kernel, or standard Welch averaging, *but* it adds separate per-window FFT work and valid source-time assembly. Do not secretly label this new consumer a general PSD provider.
3. **Generic reusable FFT complex primitive:** might reduce duplicated work if many methods need complex phase or cross-spectrum, but it would refactor accepted CP3-A numerical ownership and add an abstraction before a proven need. Do not add here.

**Preserved Kite dissent:** PR #9's Issue #11 is not closed by a cheap PSD conversion. The FFT's fully primed hop1 computation pressure remains. Per-take lightweight arithmetic cannot justify claims about many independently user-configured providers, browser GC or live-device realtime. Conversely, do not block this small headless PSD proof solely because the whole instrumentation system's performance envelope is pending.

**Recommended disposition:** **CONDITIONAL PASS** with one scoped pre-acceptance constructor-bound correction (or owner-recorded gating of configurable host construction); retain a separate performance/GC gate and no claimed browser PSD instrumentation. Source-pinned independent first pass, not approval to merge or adopt `ap117.psd/1`.

## Evidence

Direct repository code, docs, tests and CI observed at exact PR head; independent Node predicate and scalar PSD algebra controls executed; runtime behavior of the actual new module and any latency/GC claims remain unverified. Agent attribution is Kite working-profile output under shared GitHub credentials, not authenticated persistent-agent identity.

## Revisit when

The PSD window constructor adopts the upstream `maxFftFrames`-consistent guard; an owner-approved host integration binds a PSD consumer for a real panel; independent full Node module tests or GC/heap measurements contradict this analysis; Issue #11 establishes the supported multi-provider operating domain; or the PR head changes and requires re-review.

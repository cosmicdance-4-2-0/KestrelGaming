---
schema: 1
id: 2026-11-17-kite-ap117-pr17-operating-envelope-audit-k17e
kind: decision
scope: agent:kite
status: draft
evidence: observed
author: kite-session
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR #17 head a5e75c9da8dd4799b1419c9c23b5dca76168326b vs main 521d5d227016ccdd50f0ac9a58c412c1606598ba; ISSUE11-QUAL-01 assignment comment 6963865440; local extract blob 3e9f2621437bdad572fabb24142ac3a4165ac0d4; qualification report blob bf4d5368ae40799b4eed6013d62b5723dd16b3d0; CI run 44204214177; Kite home agents/kite-v1@3d9686741a06a8d6e5c83c9c8f19b70867b5a32e."
---

# Kite — ISSUE11-QUAL-01 PR #17 independent operating-envelope evidence audit

**Exact subject:** [Auralprint PR #17](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/17), head `a5e75c9da8dd4799b1419c9c23b5dca76168326b` against accepted `main@521d5d227016ccdd50f0ac9a58c412c1606598ba`, checked live. Open/draft/one commit, exactly six **new** paths in `docs/`, +3680 lines and no deletions; no application source, CONFIG, DSP, benchmark implementation, dependencies, tests or CI edited. Public evidence only. PR description and report explicitly keep Issue #11 open.

**Task/authorization:** User asked Kite to do next Auralprint homework; [Axiom's Issue #11 assignment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11#issuecomment-6963865440) authorizes Codex to qualify bounded existing benchmarks, not Kite to edit apps. Review scope: independently challenge the submitted candidate-budget interpretation, provenance, continuity/capacity invariants, reproducibility and proposed next experiment. Do not merge, deploy, close Issue #11, select an optimization or implement another benchmark. Own continuity writes are authorized only on `KestrelGaming/agents/kite-v1`.

**Individual continuity:** Re-opened Kite agent contract and own last PR #15 benchmark-design audit, branch `agents/kite-v1@3d9686741a06a8d6e5c83c9c8f19b70867b5a32e`; applied target `AGENTS.md`, memory/permissions/verification framing. **Independence disclosure:** PR #17's single existing Axiom review was visible in the initial comment fetch. Kite independently recomputed committed row/group aggregates, CI witness coverage, guard outcomes and threshold comparisons; do not claim blinded peer isolation. Shared GitHub account is working attribution, not authenticated long-lived agent identity.

## Summary

**Kite verdict: PASS for ISSUE11-QUAL-01 bounded DOCUMENT/EVIDENCE qualification. NO production operating-envelope approval.** The reduced extract and qualification report are transparent about where measured populations clear *proposed* screening options and where they fail. The mathematics and retained group counters align with the documented FFT/coverage rules. No blocker found in committed document/evidence checkpoint. This is a true improvement over PR #9's accept-only timer and PR #15's pure design: there are measured source→CP2→FFT→native PSD service data and browser/actual-app diagnostics, without a claimed optimized implementation or hard-realtime certificate.

**Critical evidence limit:** all repeated local performance measurements are **author-reported, not independently reproduced**. The original roughly 200 MB per-step JSONL, 28 MB trace/profile/snapshot artifacts and full browser observer records are outside the repository; hashed byte counts in a reduced extract are not independently downloadable raw data. I could verify the committed extract's aggregate internal equations and independently recompute statistics *from those recorded values*, but **could not** independently verify raw-line fidelity, raw SHA-256 bytes, trace event selection, per-step lineage for all 134,115 recorded steps or the measured latencies against a separate execution. GitHub CI verified existing code gates and an older separate **72-trial one-measured-round correctness witness**, not this repeated timing population. The report states this distinction accurately, so it is a qualification PASS with disclosure—not empirical performance certification.

**Strongest falsifier of universal/current admission:** Browser **normal stage** PSD core maxima 6.4 ms file and 6.1 ms synthetic exceed the proposed 5 ms observation option. The safe, retainable max-FFT third accept has stage core median 13.910606 ms and minimum 12.010527 ms, all beyond the proposed 10 ms option; browser process-tree sampled RSS ranges approx 872–996 MiB across modes, above candidate 768 MiB; actual-app rAF/Long Task options fail in some runs. Node normal timing meeting 5 ms on one shared EPYC host is **not** an app/device/target pass. Do not translate any of these into shipped CONFIG admission or Worker/WASM recommendation.

## Exact evidence receipt

At head `a5e75c9da8dd4799b1419c9c23b5dca76168326b`:
- `docs/ISSUE11_OPERATING_ENVELOPE_QUALIFICATION.md` blob `bf4d5368ae40799b4eed6013d62b5723dd16b3d0` — observed machine/environment population, proposed budget matrix, candidate outcomes, unresolved owner decisions, explicit no-real-time scope.
- `docs/evidence/ISSUE11_LOCAL_TRIALS.json` blob `3e9f2621437bdad572fabb24142ac3a4165ac0d4` — 464,700 JSON characters (~465,144 UTF-8 bytes per report), run manifests, shared group counts/source fingerprints, column-indexed trials, limited retained sample steps and raw-file digests.
- `docs/evidence/ISSUE11_EXTRACT.py` blob `3583dc964c657fd7251bc3fb1e54c67ec16ba358` — pure JSONL postprocessor, not the runtime benchmark; checks w, aggregate coverage, five expectation fields, span chronology, observed ordinal and input-publication-revision formula against *unshared* raw step entries, then compresses output. Reproduction requires those original raw files.
- `docs/evidence/README_ISSUE11.md` blob `6629121c06d4d6eb7c0ac617c0534e675728508f` — exact claimed commands, schema, extraction instructions, source classes, retained/unshared distinction and skipped cases.
- `docs/evidence/ISSUE11_CI_WITNESS.json` blob `0792849be2922270e4f39fa9bf4576359a651360` — separate 72-trial CI correctness population from PR #16 R1, **not** timing repetitions at PR #17 head. `docs/evidence/ISSUE11_CI_VERIFICATION.md` blob `81446ce96b0eeffe2acb2806e5ea39ed67c4dbcb`.
- Changed-file comparison confirmed exactly these **six docs-only additions**, no hidden code/config/harness alteration.
- CI run [44204214177](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44204214177), job `134465869125`, completed **success** at this PR; independently fetched full CI job log and observed browser smoke, artifact upload, HTML validation; CI reports `150/150 Node tests`, build and whitespace success. Those are **external CI executions**, not a local Kite npm test.

## Independently executed extract arithmetic and observations

**Method:** Parsed the *actual PR-head JSON evidence* inside GitHub connector-backed JavaScript. Independently iterated all retained group definitions (64 unique definition objects across named-run deduplication; 138 group-key aliases) and checked:
- `W(T)=max(0,floor((T-M)/H)+1)` equals `counts.computed` at all group definitions;
- `computed = dequeued + queued + forfeited + outsideSubscriptionCoverage` at all definitions;
- number of measured/warmup trials from the actual rows: **822 measured / 342 warmup = 1,164 total**;
- summed `verifiedMeasuredSteps` per run: **134,115** (the postprocessor reports the actual step-level validations; the original 134,115 step entries are *not all present in the reduced extract*). Zero aggregate W/coverage counterexamples were found.
- Listed all distinct source Sha values from retained groups: original runtime `4bc1245e9fb979a49bdc2b56c57c8787ef667155` only, as claimed. These are *recorded values*, not independently hashed source bytes from raw input.
- CI witness `ISSUE11_CI_WITNESS.json`: **72/72 COMPLETE**, all 72 retained totals satisfy the coverage equation, independent witness manifest reports `4,980` source steps, different warmup/repetition/environment from local population. The witness data itself is committed, but its referenced original artifact ZIP/raw digest were not downloaded/rehash-verified by Kite.

**Measured normal PSD medians recomputed from exact trial rows (seven measured trials each):**

| Population/observer | Sum-of-core median; range (ms) | Worst per-block core (ms) |
| --- | --- | --- |
| Node file/coarse | 34.833879; 24.883495–60.807009 | 4.686608 |
| Node file/stages | 27.408218; 24.288908–35.568141 | 1.502932 |
| Node synthetic/coarse | 39.178697; 26.858936–70.398684 | 3.017070 |
| Node synthetic/stages | 30.659773; 27.143609–163.640820 | 2.456062 |
| Browser file/coarse | 49.4; 26.1–72.5 | 4.9 |
| Browser file/stages | 32.5; 23.5–60.1 | **6.4** |
| Browser synthetic/coarse | 30.7; 29.0–48.0 | 4.9 |
| Browser synthetic/stages | 35.1; 28.4–70.5 | **6.1** |

The **largest per-block maximum**, not the sum-of-core median, is relevant to a `≤5ms` every-observation criterion. The Node file coarse 4.686608 ms passes only the observed finite population and leaves little margin; the two browser stage maxima falsify that option in those populations. Stages versus coarse use different measurement/observer cost, and seven correlated trials do **not** establish a p99 or 5 ms hard deadline.

**Max-FFT safe third accept:** I extracted all seven retained M=N16384/H512/B8192/C16 third-block source witnesses; each has `step.index=2`, `completed=16`, `source span [16384,24576)`, source epoch specific to trial, with stage `coreMs` values **12.620679, 12.891911, 13.967290, 13.910606, 14.257839, 44.475715, 12.010527**. Median **13.910606**, minimum **12.010527**, maximum **44.475715** ms. Corresponding FFT accept times have median **12.034352**, range **10.270044–42.845005**. The proposed ≤10 ms *every-completing-accept* option fails for all seven; a **pausable offline-only** option remains an owner decision, not a measured pass for UI responsiveness.

**Separate GC evidence recomputed:** Node GC pass 85 recorded events/max **3.474035 ms**, Node allocation pass 165/max **7.469007 ms**; browser GC 1128/max **5.830 ms**, browser profile 3506/max **7.021 ms**. Missing browser trial GC field is **null**, not zero; CDP GC events may overlap and are neither exclusive stop-the-world durations nor per-stage causality. These sampled diagnostic event maxima fail the proposed universal **≤5 ms** screen in some modes.

**Browser supervisor fields independently inspected:** browser timing/GC/profile/heap sampled aggregate process RSS maxima respectively **1,018,048,512 / 1,044,566,016 / 1,042,366,464 / 914,305,024 bytes**, all above a proposed **768 MiB** screening threshold and below the independent **1 GiB** sampled development watchdog. All four supervisor records say `COMPLETE` and `liveOwnedProcessesAfterCleanup=0`. RSS includes process-tree/shared-page accounting and sampling; this is not retained application heap or precise peak.

**Guard decisions independently inspected:** preflight lists ordinary cases `READY`; `pathological-primed` explicitly `SKIPPED_RESOURCE_GUARD` for butterfly/completion limits; browser matrix guard explicitly skips absent hard per-run isolation. This is the correct outcome, **not a performance failure**. No 8192-FFT fully primed H1 stress was executed or inferred from timings.

## Kite assessment: what we accept and what we do not

**Accept:** The evidence package provides a falsifiable population, observer modes, setup/source/clock distinctions, explicit measured vs warmup vs CI witness, scientific accounting across alternative consumer capacities and negative expected-overrun cases. The file/synthetic app witnesses correctly use their **own observed frame frontiers** rather than fabricated synthetic catch-up; single real source/consumer path remains intact; exactly 48 kHz mono, two demand-driven classes, one host population. The existing source/harness is immutable in this PR, so no timing measurement changed semantics at integration.

**Reject as unproven:** Runtime safety on target end-user devices, 60Hz sustained frame deadlines, per-accept live capture arrival guarantees, unbounded provider concurrency, all supported file sample rates, true heap peak/GC causality, physical sound calibration, general PSD noise-floor properties and either Worker/WASM as default optimization. The repeated local data is transparent but *not raw-archivable in this GitHub PR*. CI correctness and passed Node suites do not independently validate repeated timing.

**Dissent/next experiment:** Do not confuse "Node 5ms observed PASS" with approval to ship C4 as a live-stream-safe device configuration. The fastest useful discriminating trial is a **small repeated unchanged built-app test on one OWNER-CHOSEN physical target**, visibly foregrounded under declared refresh/power/load; separate normal pausable WAV and synthetic runs, plain vs observer variants, actual input/rAF responsiveness and named service interval. Measure the target before selecting worker migration. If host visibility/service timing cannot be captured without changing the built app, propose a separately reviewed test-only seam and report observer effect versus the unchanged built control; no hidden production instrumentation. The owner must decide the 5ms vs 10ms service reserve, acceptable GC/event/memory/UI budgets, target source/device/concurrency/burst/backpressure. Keep Issue #11 OPEN.

**Nonblocking reproducibility request:** If the author can eventually make the bounded original per-block timing trace subset and selected browser observer/traces available with immutable digests, a subsequent independent reviewer could audit the selected maximum-step claims and event classification rather than only the reduced aggregate. No need to dump 199 MB into this documentation checkpoint; hashes alone are not access to raw evidence. This should not block a clearly disclosed **qualification document**.

## Verification limits and authorization

**Executed by Kite:** GitHub exact head/base and diff, source/guide/extractor/JSON/CI witness inspection, independent JavaScript arithmetic against committed extract/group definitions, row medians/extrema, sample third-accept comparison, GC sum/max extraction, guard/supervisor checks, full external CI job-log read and own memory synchronization. **Not executed by Kite:** repeated Node timing benchmark; entire raw JSONL re-extraction; SHA checking of unavailable raw data, downloaded older CI ZIP; new Node npm/Chromium suite; large 16384/H1 third accept; physical device or live-source experiment; CPU sampling, new GC profiling or real-time test.

**Specialist decision:** `COMMENTED — PASS for bounded ISSUE11-QUAL-01 source-pinned documentation/evidence checkpoint`. This does **not** approve any proposed latency threshold, production CONFIG limit, runtime optimization, scheduler change, Issue #11 closure, merge or deployment. Axiom and owner retain reconciliation, policy and merge authority. No app or peer memory changed.

## Evidence

Direct GitHub source and CI log inspection; independent JSON aggregate/statistical work inside the connector runtime; author-reported repeated measured values are transparently distinct from independent arithmetic and from separate CI. This public memory record contains no user-private samples, secret credentials, raw traces or invented machine benchmark.

## Revisit when

Original raw selected timing/trace evidence becomes independently available; the owner chooses target device/browser and budget; a new bounded experiment measures repeated unchanged built-app responsiveness; Issue #11 is scoped for a production admission decision; or PR #17's exact SHA moves and requires targeted re-review.

---
schema: 1
id: 2026-11-17-ap117-pr16-005b-source-audit-status-oracle-4f12
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR16 head f7b6b0003d6384369075fa3ecf449a1aec912419 base 4bc1245e9fb979a49bdc2b56c57c8787ef667155, 5 added files; source reads scripts/analysis-envelope-cases.js, scripts/measure-analysis-envelope.mjs, scripts/measure-analysis-browser.mjs, tests/analysis-envelope.test.js, docs/AP117_005_OPERATING_ENVELOPE.md; GitHub Actions run 44071078219 job 133997155300; PR comment 6960748899."
---

# AP117-005B — PR #16 independent Axiom harness/evidence review

## Summary

**CONDITIONAL PASS for bounded development-only measurement harness architecture; HOLD PR #16 acceptance/merge for one P2 scientific-status oracle correction.** Read exact changed source at [PR #16 head f7b6b0003d6384369075fa3ecf449a1aec912419](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/16), unchanged accepted main `4bc1245e9fb979a49bdc2b56c57c8787ef667155`. Five added files; no production/CONFIG/CI/dependency alteration. The accepted 005A design [PR #15 head fb911dba](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/15) remains draft/unmerged as observed. Kite 005A design review PASS was observed on PR #15. Independent Kite **005B** implementation review is pending. Owner authority to merge/accept future operating envelope remains distinct.

Posted [Axiom PR #16 review](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/16#issuecomment-6960748899).

## Evidence and issue

**P2: broken/historical PSD can pass actual-app benchmark diagnostic.** `scripts/measure-analysis-browser.mjs:102-120` `parseAppSnapshot()` parses `sampleRange`, `complete windows` count, `last span` and `canvasCount=2`. It computes and checks `W(T)`, but never evaluates state/currentness. A source-transcribed V8 check confirmed a `PSD broken (subscriber-delivery-overrun)` diagnostic with `complete windows: 374` and matching `last span: [190976, 192000) (historical)` passes all parser assertions when range is `191520–192000`; the parser then sets `exactScientificCounts=true`. Production `src/main.js:60-87` intentionally labels `broken`, `historical`, `drained`, `session ready; source paused`; the test harness ignores those semantics. The current unit negative test mutates count to 373 only. Required narrow change: require compatible valid PSD state for COMPLETE/PAUSED control, reject historical/discontinuous/broken/unassociated states even when geometry matches, add positive and counterexample tests, preserve source and numerical contracts. No production DSP change.

**Nonblocking but relevant source provenance:** Node `sourceManifest()` hashes all three harness files and pins `src` to baseline, while browser `verifyBuiltControl()` hashes only pinned production and built files, and browser manifest does not record benchmark harness hashes/dirty checkout state. Suggest add browser harness byte digests (including shared cases module) and checkout metadata or qualify limitation for independently reproducible comparisons. Local full seven-trial raw files not shared; PR report provides hashes and medians, CI artifact only bounded 0-warmup/1-measured witness, not full local population. Do not attribute unverified author timing raw to independent Axiom execution or claim device/realtime certification.

**Otherwise passed source scrutiny:** Fresh source→CP2→spectrum→native producer-bound delivery/PSD path; normal and demanding cases, exact complete-window counts; controlled loss/backlog and no fabricated samples; FFT work/FFT count/major arrays preflight; external watchdogs; sampling with explicit observer effects; browser actual-app plain built control and separately instrumented variant; ordinary 48 kHz single producer/consumer experiment. Pathological fully primed max-FFT H1 third block **not executed**, intentionally resource-guarded. Small-N direct DFT satisfies Kite's 005A oracle operation-bound concern; no unbounded large-N direct DFT.

**CI:** [Actions run 44071078219](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44071078219) at exact PR head, job `133997155300`, success. Axiom checked actual job steps and log **145/145 Node tests, zero fail/skip**, build, Nu HTML, Chromium offline smoke, whitespace. These are GitHub-executed checks, not local Axiom full-suite or the completed local 7-trial raw population.

## Revisit when

Codex updates the same draft PR to enforce PSD currentness in `parseAppSnapshot()`, adds direct counterexample/regression and positive controls, and pins any accompanying browser harness provenance claims; then recheck the new exact head, file diff, and CI. Kite independently evaluates 005B performance/guard correctness; owner decides whether to merge/accept tooling or authorize measured operating envelope/optimizations. Keep Issue #11 open and do not claim full pathological execution, physical device evidence or universal admission capacity.


## R1 closure — 6ec106d (2026-11-17)

At exact [PR #16 R1 head `6ec106d2937116c7a6f6c41f72c1dae7533734e0`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/16), parent `f7b6b00...`, unchanged accepted main base `4bc1245...`, Codex changed **only** `scripts/measure-analysis-browser.mjs`, `tests/analysis-envelope.test.js`, and `docs/AP117_005_OPERATING_ENVELOPE.md` (+215/−11). Axiom reviewed the full updated parser and regression tests and cross-checked actual `src/main.js` diagnostic status/transport and `src/analysis/spectrum-stream.js` final-window behavior.

**P2 CLOSED; Axiom final individual verdict PASS for bounded development-only AP117-005B instrumentation.** The browser parser now matches valid complete/drained/final/ended, paused/session-ready/ready/open and measuring/processing/ready/open diagnostic tuples, rejects unknown/broken/duplicate/incomplete/error states and stale zero-window spans, and preserves W(T) counts and FFT spans. A terminal drained PSD final span is explicitly historical by the production host; the new parser allows that case without mislabeling it as *active* continuity. Presentation-only historical peak label remains independent. Unit tests include the exact originally accepted broken/historical counterexample and positive/negative variants. The author reports red-before/green-after; Axiom only verified code/CI, not the author's prepatch local run.

**Provenance request CLOSED for newly produced browser evidence.** `browserHarnessProvenance()` SHA-256 hashes shared-case and browser-driver files and records checkout/dirty metadata; production byte-pin/built control remains. The original `f7b6b00` local seven-trial files are unshared author-reported outputs and not retroactively certified or rerun on R1.

[Exact-head Actions 44177111378](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44177111378), job `134371297463`, success, actual log **150/150 Node tests, zero fail/skip**, build, official HTML validation, Chromium smoke and whitespace all passed; this is GitHub CI, not Axiom local execution. The fully primed 8192-FFT pathological case remains guarded and unexecuted. [Axiom final independent PR comment 6963666868](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/16#issuecomment-6963666868) records full evidence and limits.

**Outstanding:** Kite's independent PR16 implementation/evidence assessment, owner adoption/merge decision, and the substantive Issue #11 operating envelope for target devices, concurrency, latency, CPU/GC, live policy. No production tuning, Worker/WASM/GPU preference or realtime claims authorized.


## Owner merge confirmed — 2026-11-17

User reported PR #16 merged. Axiom independently verified GitHub [PR #16](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/16): `state=closed`, `merged=true`, `merged_at=2026-11-17T23:09:56Z`, merge commit `75f4cbdd47891df8f74153851d6d9817c3050dd0`; confirmed `ap_117_KESTREL/main` points to that exact SHA. Accepted implementation PR head `6ec106d2937116c7a6f6c41f72c1dae7533734e0`; exact-head GitHub CI 150/150 verified in prior review. Owner chose to merge; no claim of Kite PR #16 review on GitHub (`list_pull_request_reviews` returned empty at check) and no implied performance/device certification. Issue #11 remains open. Design PR #15 at `fb911dba06bab4d637e3793f3ec8a56607e3fa7a` remains **open, unmerged**; its fixed-SHA design documentation is referenced by the merged PR #16 but not integrated on `main`. Future work may include owner-controlled reconciliation of that documentation, target-device/live/concurrency performance admission policy and measured workload qualification. Never silently close #11 or treat Node/browser numbers as safety/realtime limits.

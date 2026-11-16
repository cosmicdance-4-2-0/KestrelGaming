---
schema: 1
id: 2026-11-15-ap117-pr12-psd-six-review-dispatch
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr12-integration-dispatch
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint 117 PR12 exact head 0880fc8df9182cce9ed2c645e324a2d291375281; main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; PR #12 discussion comment 6907662478; GitHub Actions run 43789892097 job 133045679451; issue #6 PSD design and #10 receipt identity, #11 deferred cost; source files src/analysis/psd-processor.js, fft-amplitude.js, tests/psd-{integration,math,lifecycle,boundary}.test.js, docs/AP117_003_PSD_CONSUMER.md."
---

# Auralprint 117 — PR #12 initial Axiom integration assessment and six-engineer review

## Repository status and evidence

Owner relayed Codex completion for [draft PR #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12). Verified live accepted `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f` (PR9 accepted merge), exact current PR head `0880fc8df9182cce9ed2c645e324a2d291375281` (one commit), base exactly `2957be0f...`. PR open, draft, unmerged, **six new files, 1312 additions, no deletions**, no existing application production source change. Adds headless `src/analysis/psd-processor.js` (277 lines), 4 new test files, detailed proposed contract documentation.

Exact-head [GitHub Actions run 43789892097](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43789892097), verify job 133045679451: **completed/success** and downloaded job log reports **119/119 Node tests passing, zero failed**; static build, vnu HTML, Chromium offline browser smoke and whitespace checks also successful. Axiom checked actual CI log, code and tests, but **did not personally execute a fresh full local app suite**. Browser smoke covers unchanged latest-only UI, not the new headless PSD module rendered in a panel.

## Initial source audit / review target

Implementation `createPsdProcessor({subscription,spectrum,source})` captures the actual `take/readStatus/resync/dispose` operations from an exclusively owned trusted subscription; zero-argument pull, one output per complete delivered FFT observation, status/derived latest. Separately typed **candidate** `ap117.psd/1` and `ap117.psd-delivery/1`, no adopted schema claim. Same-source/window/frequency/epoch/span fingerprint validation. Digital normalized PCM squared/Hz no-detrend nonaveraged periodogram `P[k]=A[k]^2/(c[k]*ENBW_Hz)` (DC and Nyquist c1, interior c2), frozen owned arrays, BigInt spans, versioned window/method labels. Existing `ap117.spectrum/1`, CP2 PCM/rms, FFT, rendering and main wiring untouched; **no production attached consumer**, only real source→pipeline→spectrum→PSD Node integration test. Codex measured exactly four existing FFT operations, no new read or FFT for Gauge 20 vs 5x4 legal fixture, 1312 tested bins vs independent DFT/Parseval; all these claims need independent specialist scrutiny.

Potential review concerns *not confirmed defects*:
- **Wrong-handle negative assertions:** `take(receiptA)` throws on **all arguments** by design. This prevents a detached receipt from entering the zero-argument API, but does not prove a trusted host can never erroneously attach an intended B processor to A's actual handle at construction. Two producer and same-producer two-subscription stamp collisions were reviewed in PR9; binding still host responsibility. Latch must distinguish valid narrow scope from unproven authenticated cross-host routing.
- **Freshness and EOF:** `readStatus().ended` upstream with queued observations is distinct from PSD own `take().ended`; verify all finals drain; cache after reset/fence is withdrawn and historical in-generation windows remain eligible.
- **Numerical strictness:** PSD's window weights/ENBW are recomputed using identical definitions and exact metadata comparisons; requires independent DFT and falsifier across windows/zero-padding/rates; avoid false RMS² equal PSD integral, noise-floor/physical calibration promises.
- **Performance:** O(M) setup and O(K) per consumed window within trusted app, no FFT duplication; no measured device GC/realtime budget, Issue11 remains deferred.
- **Authorizations:** no implementation repair, merge, release, spec freeze or PSD UI authorized by review dispatch.

## Axiom's public review handoff

Posted [six independent specialist source-pinned assignments on PR #12, issuecomment-6907662478](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6907662478). Each reviewer loads own identity and contract, inspects current head before peer conclusions where possible, preserves own memory, posts exact-SHA PASS/conditional/BLOCK and reproductions without app modifications. Assigned: Gauge independent math; Flint API/ownership; Harbor lifecycle/EOF; Latch actual handle identity and wrong-handle source test; Mothlight status truth; Kite work/cost evidence. Shared account identity is authorial attribution, not proof of separate authentication.

**Axiom disposition:** **REVIEW HOLD**. Candidate suitable for six independent specialist audits; no demonstrated blocker in Axiom's preliminary source read, **not an acceptance verdict**. Owner conveys shared comment to individual Kestrel agent sessions. No Codex correction assignment until specialist findings are reconciled. PR stays draft, no app code changed or merged.

## Next

Collect six first-pass reports pinned at `0880fc8...`; review any valid blockers, commission a single narrow Codex patch if needed (same draft PR, owner-authorized push, not merge), recheck moved head and affected specialists, then issue owner-facing integration acceptance recommendation. Avoid premature contract freeze and expansion into CP3-B2 UI or FFT-work envelope.

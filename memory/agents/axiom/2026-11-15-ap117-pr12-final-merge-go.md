---
schema: 1
id: 2026-11-15-ap117-pr12-final-merge-go
kind: review
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr12-final-integration
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint PR12 exact head 2acfeb9daf3b5714424455afc64bcffd237c23d7 and accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; CI run 43824257458; final Gauge R09 review 5916575349; Flint acceptance issuecomment 6910398049; Kite review 5916516880; original six prior-head reviews; Axiom final integration comment 6910615461; issues 10 and 11."
---

# AP117-003 / PR #12 — FINAL AXIOM GO FOR OWNER MERGE

**Status:** Final project-lead **GO for owner to merge PR #12 at head `2acfeb9daf3b5714424455afc64bcffd237c23d7`** as the **bounded headless trusted-built-in same-window PSD consumer correctness proof**. GitHub PR rechecked OPEN, DRAFT, UNMERGED, MERGEABLE, 2 commits, accepted base/main unchanged at `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. Axiom did **not** merge or deploy. [Published GitHub verdict](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6910615461).

## Reconciled source evidence

1. **Gauge numerical R08/R09 — PASS:** Original independent 80-window, 2796-bin complex DFT/Parseval per-window independent check on old `0880fc8...`; targeted new-head R09 [review 5916575349](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#pullrequestreview-5916575349) independently executed 38 constructor acceptance assertions zero failure and legal CP2 20-final vs 5×4 partitions, four windows bit-identical old/new across both legal partitions, 40 PSD bins vs independent DFT (maximum abs density discrepancy ~6.7763e-21) and weighted Parseval ~5.5511e-17. No PSD arithmetic regression; no unweighted RMS² identity claim.
2. **Flint — PASS new-head [issuecomment 6910398049](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6910398049):** Independent actual source-executed invalid descriptor controls, no Hann weight computation before reject, legal padded max geometry accepted, four-window/EOF and producer state preserved. Original inconsistent PSD constructor admission resolved.
3. **Kite — ACCEPT new-head [review 5916516880](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#pullrequestreview-5916516880):** producer-configured `maxFftFrames` bound used, no duplicate independent magic 2^30, appropriately negative and positive tests, unchanged mathematics. Did not independently run full application Node or browser tests, which remain CI-attributed; FFT CPU/GC #11 deferred.
4. **Harbor lifecycle/EOF PASS**, **Mothlight status PASS**, **Latch trust CONDITIONAL PASS** are preserved as **original `0880fc8...` source-pinned reviews**. R1 only edits constructor admission, test, doc and leaves all reviewed lifecycle/status/trust action logic unchanged. Latch's independently constructed hybrid subscription wrapper can substitute A's record while presenting B's status; it violates explicit trusted native exclusive handle precondition. Rejecting `take(receiptA)` does **not** prove arbitrary cross-host authentication; future host wiring gate stays open.
5. **Exact-head CI:** [GitHub Actions 43824257458](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43824257458) completed/success; Axiom independently inspected job metadata and log: **120/120 Node tests, zero failures/skips**, static build, HTML validation and Chromium offline smoke plus whitespace. Full npm/browser suite executed by CI **not locally rerun by Axiom**. Chromium smoke only validates current GUI, not a PSD panel. PR currently has six added paths, original 1312-line plus 3-file minimal R1 fix; upstream CP2, spectrum FFT, render/host untouched.

## Accepted scope and exclusions

If merged, owner adopts candidate `ap117.psd/1` and `ap117.psd-delivery/1` *only as scoped internal headless periodogram observation/control contracts*: no detrend, no averaging, same CP3-A FFT window/hop, exact BigInt source lineage, digital normalized squared amplitude/Hz, window-weighted Parseval. One received complete spectrum → at most one derived PSD via bound synchronous subscription, no new FFT/source read, no display or new scheduler. Completeness guaranteed **only until explicit bounded subscription overrun or lifecycle gap** (not unlimited history). Producer-ended with backlog requires consumer take until ended.

**Open post-merge gates**:
- [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10): before actual real host/instrument wiring, prove intended host bound/transferred **actual exclusive native subscription**, with wrong-live-handle construction negative, two-producer and two-subscription collision, post-yield fences for async, truthful EOF/continuity/render status. Do not declare Issue #10 whole host problem closed by `take(receipt)` rejection.
- [Issue #11](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11): before unrestricted/configurable/live/device realtime claims, measured end-to-end FFT/PSD work/heap/GC source operating envelope (esp primed H1), admission and backpressure policy; not a correctness defect of headless PSD proof.

**Owner remains final authority.** No further Codex corrective work justified at this head; merge when owner chooses; re-review if head/base changes or new counterexample. Continue next milestone only after owner merges and new base is verified.

---
schema: 1
id: 2026-11-07-cp3b1-psd-reset-fence-he01
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Auralprint 117 CP3-B1 Issue #6 Harbor design comment 6716755145; accepted CP3-A main@0531e734a2ece59cd877ea8659069efee2e0a905; source-executed spectrum-stream.js 19c34cb8958c204e1ee529ee2c1adc773c8b37c2 and FFT ee35e0793aceb5eb9e3fc49d27f293a1719effc5"
---

# Harbor — CP3-B1 dependent PSD lifecycle design challenge

## Summary

**Outcome: COMPLETE — design-only CONDITIONAL PASS for option C.** The accepted CP3-A spectrum is a latest-complete-window peak-amplitude observation, not PSD. A proposed dependent `ap117.psd/1` adapter may convert those bins to linear periodogram density for the same fully observed window, without a second FFT, source read, assembler, or renderer. The required reset-watermark/currentness rule is a design acceptance gate, **not** an implemented or empirically failed PSD module. Full details and falsification matrix: [Harbor's source-pinned Issue #6 review](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716755145).

## Evidence

**Observed production CP3-A traces:** In isolated V8 execution of accepted `createSpectrumStream` at M8/H4, a complete `[0,8)` window creates ready spectrum revision 2; receiving only two more samples returns the same ready object. Invalidation and reset advance producer revisions 3 and 4 to unavailable, yet a caller can still hold the old ready revision-2 object. A **stronger trace** let the producer create ready rev 3 `[4,12)` without PSD observing it, then reset to unavailable rev 4. The cached rev-3 record is newer than the PSD's last consumed rev 2, so `incoming > lastConsumed` is insufficient to prove currentness after reset. These are genuine source behaviors; no PSD adapter yet exists to test.

A single 20-frame upstream input produced only latest observable `[12,20)` rev 5, while 8+4+4+4 frame partitions exposed four complete ready windows; the PSD publication counts may differ while their final density agrees. Real 481/1023-frame files cannot yield any complete M1024 spectrum; 1024,1536,2049-frame inputs yield the latest real complete `[0,1024)`, `[512,1536)`, `[1024,2048)` respectively. These reflect sample-time truth rather than rAF time.

**Inference / design obligation:** An option-C PSD consumer needs a trusted live-currentness check or an upstream reset fence captured **after** upstream invalidation/reset, including revisions the consumer did not itself ingest. Old ready objects must not reappear after a state transition. Preserve distinct independent PSD revision, identical snapshot no-op, contradictory same-stamp fail-closed, exact BigInt spans, explicit source/epoch/parameter reset policy and coordinated failure withdrawal. An arbitrary immutable snapshot alone cannot authenticate its own currentness. Owner scope choices D1–D4 and Axiom's explicit boundary contract remain pending in the reviewed issue; conditional design judgment is not owner ratification.

**Evidence limits:** No B1 implementation/PR, independent PSD numerical implementation, full app checkout, live BFCache navigation or device/GPU timing was tested by Harbor for this task. Gauge owns the independent PSD math; Flint owns architecture challenge. The review is public Issue #6 comment only; this record supplies agent-scoped discoverability without becoming the app's design source of truth.

## Revisit when

The owner ratifies CP3-B1 D1–D4, Axiom specifies how a dependent PSD adapter receives a producer-currentness/reset-fence token, B1 implementation is submitted for exact-head lifecycle testing, or CP3-A changes publication semantics. Re-fetch current source and do not mistake a design hazard for an implemented regression.

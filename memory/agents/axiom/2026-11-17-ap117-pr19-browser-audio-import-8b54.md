---
schema: 1
id: 2026-11-17-ap117-pr19-browser-audio-import-8b54
kind: handoff
scope: agent:axiom
status: draft
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "AP117 PR #19 head 8b54cfa19825bdf967622fc1a11ed29315dc3012 against main 4ef3d2376f6de1a390024eb65cbad6beab12eadb; GitHub Actions run 44257826620 (job 134643660994); AP117_LOCAL_BROWSER_AUDIO.md; CP2_FILE_PCM.md."
---

# Axiom — AP117 local browser audio import, PR #19

**Owner intent:** User lacked PCM16 WAVs; extend the usable local file inputs while preserving scientific meaning and source boundaries. Implementation is in [AP117 PR #19](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/19), branch `task/ap117-local-browser-audio-import`, based on `main@4ef3d2376f6de1a390024eb65cbad6beab12eadb`; current exact head `8b54cfa19825bdf967622fc1a11ed29315dc3012`.

**Design:** Strict existing PCM16 WAV decoder remains authoritative for `.wav` or RIFF/WAVE signature; it does not fall back after rejecting unsupported WAV bytes. Other local complete audio is decoded using browser `OfflineAudioContext.decodeAudioData`, at configured 48 kHz sample rate, with distinct typed provenance: source `local-decoded-audio`, tap `browser-decoded-pcm`, clock `browser-decoded-pcm-frames`. The decoded sample positions are *not* original encoded-file positions. Only mono/stereo channels accepted; no automatic mixing or playback. Config bounds 16 MiB input and 128 MiB decoded PCM; native decoding occurs *before* the latter check, so no hard browser memory guarantee. Browser codec formats are environment-dependent; MP3 is the real tested browser codec, other types not certified.

**Boundaries and tests:** `file-import.js` now awaits asynchronous decoder results and rechecks generation before installing any source. Tests cover strict WAV dispatch, valid Float32 channel snapshots, invalid native samples/rates/channels/memory, post-read cancellation during decode and recovery paths. A complete small libmp3lame fixture is passed through the real Chromium import/UI/FFT/PSD path. The existing `pcm-buffer-source.js` API only gained optional, validated tap/clock metadata defaults; WAV output retains its accepted metadata. No DSP/FFT, PSD, source policy or scheduler rewrite.

**Exact-head remote CI:** [GitHub Actions 44257826620](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44257826620) at `8b54cfa19825bdf967622fc1a11ed29315dc3012` **SUCCESS**, 155/155 Node tests, static build, HTML validator, Chromium offline/browser smoke and committed whitespace checks. Earlier CI `44257518162` failed because the protected AP117-005B 72-trial harness refused modified production source `src/audio/file-import.js`; tests were corrected to **verify the intentional source-pin refusal** without rewriting the benchmark, repinning data, or asserting timing certification. Later run `44257636630` passed before the final README-only correction. No local end-to-end test execution is claimed.

**Status:** PR #19 is **DRAFT/unmerged**. This is independent of AP117-006B draft PR #18 (same host source file changed in separate branches). Both require ordered integration/rebase and owner approval; do not assume simultaneous clean merging, target-device support, generalized realtime safety, or universal compressed-format support. Issue #11 remains a separately scoped performance-admission task. Historical AP117-005B timing population cannot be transferred to this new host.

**Next checkpoint:** Independent review of memory and codec constraints, cancel/dispose lifecycle, provenance, and integration against PR #18; then owner merge decision. Reverify PR #19 head/base, tests and CI after any rebase. If integrating PR #18 first, resolve `src/main.js` edits deliberately and rerun exact-head browser/Node and benchmark source-pin rejection tests.

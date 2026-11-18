---
schema: 1
id: 2026-11-18-ap117-ux0-owner-experience-checkpoint-e31bd42f
kind: handoff
scope: agent:mothlight
status: active
evidence: user-stated
author: mothlight
created: 2026-11-18
updated: 2026-11-18
sources: "Owner's 2026-11-18 AP117 UX0 discussion; Auralprint1@75e26348848f874329ca1ac95bb13576371ed2da; AP117 main@78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a; AP117 UX0 issue #21; Legacy116Orb draft PR #20."
---

# AP117 UX0 — owner experience direction and pause checkpoint

## Summary

**Task outcome: COMPLETE for this memory checkpoint; AP117 work PAUSED by owner.** Do not infer UX0 approval, reconciliation, implementation, or release. Preserve the separate, already-published [independent first pass](2026-11-18-ap117-ux0-independent-human-experience-64e1c9b2.md) without retroactively modifying it. This record captures subsequent owner guidance and Mothlight's interpretation for when AP117 resumes. No production code or design authority changed.

**Owner-stated purpose:** Auralprint originated in AI research into helping a machine understand how humans perceive sound; the name evokes an auditory fingerprint. Attractive visualization was initially a secondary effect. Since the Queue arrived in Build 112, the application has evolved toward human users. For 117 onward the immediate UX goal is that ordinary people can obtain *visually compelling results* without knowing about DSP, Orb internals, or the developer's knobs. Advanced access must remain possible; complexity should be hidden from initial presentation, not from the authoritative system.

**Owner-stated concrete example:** 116 defaults to basic Orbs, but the owner configured **62 Orbs: 31 left and 31 right**, with distributed Band Bank assignments, to produce an expressive stereo spectral display understandable to musician friends through familiar band spacing. The intent was a coherent visual representation, not the activity of editing 62 independent objects. 116's UI makes that authoring difficult for anyone without developer familiarity.

## Evidence

**Observed in source:** Auralprint1 pinned source exposes per-Orb channel, band, motion, response, trace, and particle configuration; a globally shared Band Bank; Orb add/duplicate/remove and global bulk edits; independently hideable subsystem panels, authored Camera/gesture behavior, and Scene presets. Its Visualizers panel contains inventory plus individual cards and all-Orbs bulk editing in a scrolling panel. The original 116 band energies are display-normalized, not calibrated AP117 PSD. Refer to Auralprint1 README, AGENTS.md, src/index.template.html, src/js/ui/orb-editor.js, src/js/ui/workspace.js, and src/js/audio/band-bank.js at the pinned SHA. These are source observations, not new usability-test results.

**Previously recorded UX0 status (verified 2026-11-18):** AP117 main at the pinned SHA; [Mothlight issue #21](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/21) preserves five desktop/mobile journeys and twelve proposed falsifiers as an *independent proposal*. [Legacy116Orb PR #20](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/20) remains a draft reference only. No published Axiom/Kite independent UX0 submissions were found during that status check; absence does not prove no unpublished work exists. No UX0 adversarial reconciliation, tests, or implementation were claimed.

**Mothlight's self-correction (inference):** Earlier UX0 investigation emphasized gesture/state ownership and framework contracts, valid but closer to Axiom's specialty. The founding Mothlight experience-engineering focus requires studying *what a person wants to experience or accomplish* before demanding they operate subsystem abstractions. Ask questions about the first encounter, discoverability, expressiveness, and authoring intent before proposing UI architecture.

**Discussion hypotheses, not adopted contracts:** Progressive disclosure of configuration; module-described interface capabilities with a user-facing experience catalog; composition and batch authoring instead of per-object setup; analysis-focused and visualization-focused layouts; parity of capabilities across phone/desktop; lossless access to exact configuration with CONFIG → preferences → state. Conversation-proposed UX0 M13–M16 checks are not posted, ratified gates, or executed tests. Do not promote illustrative patterns, example values, UI modes, or descriptive names to canon.

**Interpretive distinction:** The machine discovers *module capabilities*; people discover *experiences and possibilities*. Default UX must already be engaging. Advanced inspection should expose the underlying truthful configuration and analysis rather than unlock the only interesting functionality.

## Next action

**AP117 is parked.** When explicitly resumed, re-check current repo pins, Axiom/Kite first passes, review intake, issue #21 and PR #20; preserve agent independence and owner authority. Treat these conversation-derived goals as owner input to UX0 reconciliation, not as a unilateral modification to an independent original report. Continue asking user-intent questions before designing the architecture, and test proposals with real novices/mobile users when authorized.

**New project chat:** No next project has been selected or authorized in this record. Load Mothlight's agent contract and relevant memory, then follow the new project request without importing AP117 scope.

**Changes made during checkpoint:** Kestrel agent memory record and its index only. No changes to Auralprint repositories.

## Revisit when

The owner reopens AP117 UX0, another engineer publishes independent work, the accepted UX0 architecture differs, or fresh usability research validates or falsifies the proposed human-experience model.

---
schema: 1
id: 2026-11-05-hollowlumen-designer-visual-reference
kind: decision
scope: project:kisuul/hollowlumen
status: draft
evidence: user-stated
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "User-shared image and statement during HollowLumen consolidation discussion on 2026-11-05: 'I just got some design input from the missus. She says she would prefer a look like this.' The reference image is available only in the original conversation, not stored in this public GitHub repository."
---

# HollowLumen — reported visual preference and reference interpretation

## Summary

**User-reported original designer preference, not final asset/style approval.** The designer prefers an uploaded composited reference showing a highly expressive, softly dimensional pastel yarn creature in a cozy, illustrated cottage-garden game world, with a character action/pose board. Treat this as important visual direction for future concept tests across the two HollowLumen teams. Do not mistake the image for an approved game mechanic, production asset, locked rendering technology, or final design signoff.

**Observed reference features:**

- Main critter is small and round with strong silhouette; oversized glossy dark eyes, small embroidered-looking smile, tiny rounded limbs, a glowing curled yarn tuft/antenna, and tightly winding pastel pink, blue and cream-gold strands.
- The material appearance has plush/fuzzy, softly illuminated, depth-rich painterly/3D-like shading, bright rim/glow and clear form at multiple scales. This is a substantial departure from flat icon/monochrome SVG styling, but does **not** prove the image is modeled in actual 3D.
- Game-world panel depicts a warm storybook garden and cottage, path, flowers, fences, lantern/window glow, rounded natural forms, and an inviting, lush palette.
- Pose board labels ten states: Idle, Walk, Run, Jump, Land, Look Left, Look Right, Happy, Hurt, Sleep. These demonstrate the desired expressive range; their presence does not prove all are required mechanics or animation states.
- In-scene onscreen directional pad and star button are visual reference elements, **not** an accepted control schema.
- Motif looks like *wound/braided yarn* rather than unmistakable individually crocheted stitches. Confirm craft authenticity with the original designer if physical crochet texture is a hard requirement.

**Cross-team integration guidance:**

1. Treat Team B's currently approved pastel/day-night semantic palette direction and working UI/accessibility baseline as protected until separate design review. Update **critter and environment art direction** first; do not replace the CSS token source indiscriminately.
2. Have the design team define a small, measurable **rendering style test**, not a full UI redesign: same character at large portrait, playable scene size and widget-size mock; static key poses Idle, Walk, Happy, Sleep; silhouettes and visual material consistency across states.
3. Compare feasible art pipelines (hand-painted sprites / rigged 2D or pre-rendered 3D / real-time 3D) against reusability for individual critter variation, predictable animation, small-screen readability, mobile performance, and widget projection. Do not choose a technology from the look of the image alone.
4. Maintain separation between creature **identity**, pattern/construction, **renderer**, and any native widget adapter. An art style cannot own gameplay/save logic. A native phone widget remains unverified.
5. Seek explicit original designer review of the produced reference-matched prototype before recording approval. Keep the original uploaded reference private unless the user separately authorizes publication.

## Evidence

User directly shared one visual collage and reported a preference for a look like it in conversation on 2026-11-05. Visual details above are Axiom's inspection and interpretation of that image, not independently verified requirements. Existing implementation at [Kisuul/hollowlumen](https://github.com/Kisuul/hollowlumen) used an original SVG Lumenette rendering. Existing design research at [CosmicDance HollowLumen](https://github.com/cosmicdance-4-2-0/hollowlumen) used provisional SVG branding and Lavender & Loop. Neither team's work is superseded by this untested single reference in its entirety.

## Revisit when

The original designer clarifies whether the texture should be truly crocheted versus wound/plush yarn, confirms art style/production technique, compares actual rendered examples, chooses a target phone/widget platform, or approves a final character/environment look.

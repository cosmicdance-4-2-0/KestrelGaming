---
schema: 1
id: 2026-11-07-engineering-skill-plan-lk4
kind: decision
scope: agent:latch
status: active
evidence: inferred
author: latch-session-2026-11-07
created: 2026-11-07
updated: 2026-11-07
sources: "2026-11-07 user request for a researched engineering skill plan; agents/latch/SKILL_ROADMAP.md; OWASP Threat Modeling Cheat Sheet; OWASP ASVS 5.0; NIST SP 800-218; OWASP Agentic Top 10 2026, Agent Control Standard, and AI Agent Security Cheat Sheet; FIRST EPSS and CVSS; MITRE ATLAS; OpenSSF Scorecard and SLSA."
---

# Latch — Research-backed engineering skill development choice

## Summary

The user requested an extensive, research-backed design for Latch's engineering skills. Latch chose **risk-ranked trust-boundary engineering** as the organizing discipline and **threat modeling / attack-surface mapping** as the first skill to develop, rather than beginning with scanners or comprehensive security hardening.

The full research and 18-candidate skill plan is documented in [Latch's Skill Roadmap](../../../agents/latch/SKILL_ROADMAP.md). This is a **proposed development plan**, not evidence of skills actually acquired, installed, tested, or independently validated.

## Evidence

- User request: "Prepare a bit of research. Design a skill set to enhance your approach to engineering. Where would you start and why. Design the skill plan to be as extensive as you think is sensible."
- Prior user guidance emphasizes finding actual vulnerabilities over indiscriminate hardening: [Boundaries before blanket hardening](2026-11-07-risk-prioritized-boundaries-lk3.md).
- Selected authoritative resources in the roadmap support system-focused threat models, secure development, authorization tests, and emerging agent-specific risk categories.
- Inspected shared `skills/INDEX.md` and existing Kestrel skill conventions; no Latch-specific operational skill has been added at this checkpoint.
- L01–L04 form the proposed minimum coherent slice, tested on synthetic shared-draft isolation and delegation scenarios; L05–L18 are staged for later.

## Revisit when

The first synthetic fixture and evaluation oracle are ready, user priorities change, real Kestrel architecture provides a higher-value boundary, or tests reveal the skill does not improve decisions. Promote competency claims only after observed results.

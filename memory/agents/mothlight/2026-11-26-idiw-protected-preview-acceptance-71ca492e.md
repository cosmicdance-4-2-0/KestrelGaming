---
schema: 1
id: 2026-11-26-idiw-protected-preview-acceptance-71ca492e
kind: handoff
scope: agent:mothlight
status: active
evidence: user-stated
author: assistant-session-2026-11-26
created: 2026-11-26
updated: 2026-11-26
sources: "Owner conversation on 2026-11-25 PST / 2026-11-26 UTC; owner-restricted IDIW DECISIONS.md (IDIW-041 to IDIW-043), issue 35 and main inspected on 2026-11-26; GitHub CI and Cloudflare Pages/Access API readbacks. Details remain in project-owned sources."
---

# IDIW — protected public-launch preview accepted visually; cutover still gated

## Summary

**Memory checkpoint: COMPLETE. Public launch: NOT AUTHORIZED.** This public-safe record preserves an IDIW handoff for Mothlight's future recall. It is not a claim that an embodied Mothlight runtime executed the referenced changes. The IDIW project repository, decision log, release-candidate reviews, issue tracker and hosting account remain authoritative for implementation detail and current status.

The owner's overarching objective is to make **IDIW — Ideas Developed Into Worlds** a distinctive professional home for their software, experiments, and independent work, with genuine opportunities for collaboration and paid work. The website should foreground the **creator and their capabilities**, not advertise the agent ensemble as its subject. The owner's chosen aesthetic is **Neon Afterhours**; restrained editorial comparison assets need not appear in the public release.

**Owner-approved public-launch choices (project decisions IDIW-041, IDIW-042, IDIW-043):**

- Exactly one public design, Neon Afterhours, without a visible theme switcher.
- Two direct, visible, copyable `mailto:` contact roles: a creator-facing primary contact in the Contact section and a separate technical/webmaster link in the footer. No form, CAPTCHA, or mandatory JavaScript. Exact destinations and copy are owned by the **restricted project decision log**; do not duplicate private contact or forwarding details in this agent-memory record.
- English-only initial release; public homepage eligible for search indexing; not-found page remains `noindex`.
- No staging/preview notice in the public release and no visitor-visible version number.
- This policy applies to a separately selected **public-release candidate**, not to the protected staging default and **not** to production cutover.

**Observed milestone, 2026-11-26 UTC:** The earlier design/contact/public-profile work has been merged into the project's accepted source; a distinct, manual-deployment-only Cloudflare Pages review project was provisioned; an owner-only Access policy was configured **before** the public candidate was preview-deployed; deployment logs reported a successful five-file package from the accepted source revision. The original no-contact staging preview and production cutover configuration were deliberately left outside that workflow.

**Owner-stated visual acceptance:** After visiting the protected public-launch preview, the owner reported, **“Everything looks fine.”** Record this as **owner visual approval of that preview**, not as proof of accessibility, server-side behavior or authorization to publish. The project's issue tracker already records this acceptance and the precise deployment identifiers.

## Evidence

- **User-stated:** The owner approved the six launch-policy choices and later accepted the protected preview's appearance. Separate production cutover authorization has **not** been given.
- **Observed in the authorized project session:** Project decisions and current main were read; source/review state, successful CI and release-package checks, deployed preview status, the owner-only Access policy and disabled automatic deployment settings were checked using repository and hosting interfaces. The precise commit hashes, project hostname, Access configuration and test reports are preserved in the **restricted IDIW project records**, not mirrored here.
- **Not independently established by the owner statement or this memory write:** authenticated served-byte equivalence (HTML/CSS); HTTP-level `robots.txt`, nested 404 and `X-Robots-Tag` behavior; Cloudflare email-address obfuscation and actual link activation; independent delivery of the webmaster contact; manual screen-reader or cross-browser/physical-device acceptance; current accuracy/freshness of external project links and release claims; tested rollback; apex/`www` routing.
- **Authority boundary:** A successful protected preview and accepted visual treatment do not authorize removing Access, indexing the staging preview, changing DNS, altering the production branch or Git build, deploying to the public domain, or retiring the old site.

## Next action

1. Reopen the current **owner-authorized IDIW** project source: applicable `AGENTS.md`, `docs/DECISIONS.md`, the release-candidate review ledger, issue 35, and the current accepted source/deployment records. The project may have changed after this checkpoint.
2. Perform a **source-pinned, authenticated served-byte preflight** of the protected public candidate, respecting Access credentials and avoiding credential storage in public memory. Compare rendered/served contact links and edge effects; verify real `robots.txt`, 404, CSS and `X-Robots-Tag` behavior. Do not promote a synthetic/loopback test into a real-host PASS.
3. Complete external-link/evidence freshness and manual accessibility checks, settle `www`/apex host behavior, and rehearse a reversible rollback.
4. Request **separate explicit owner approval** before any public production cutover. The public launch remains **BLOCKED** until those gates are resolved.

Do not reopen the visual design without new evidence or a new owner request. Keep new work scoped to selling the creator's actual work and making contact and navigation dependable.

## Revisit when

The authenticated served preflight completes or finds edge-induced changes; content accuracy or accessibility checks require revisions; the owner changes launch copy/contact policy; rollback is demonstrated; or a separate public deployment/cutover decision is granted. Revalidate all time-sensitive statuses against the project's current sources.

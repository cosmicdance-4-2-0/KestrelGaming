---
schema: 1
id: 2026-11-22-cli-import-cycle-and-allowlist-case-661182b1
kind: lesson
scope: shared
status: active
evidence: observed
author: mothlight
created: 2026-11-22
updated: 2026-11-22
sources: "Mothlight's 2026-11-22 release-candidate packaging session in an owner-private static-site project (Node 22.23.5). Both defects were reproduced locally before and after their fixes; project paths, revisions and URLs are deliberately withheld from this public record."
---

# Two release-tooling traps: a CLI import cycle under top-level await, and a case-split allowlist

## Summary

**1. Library tests cannot see an ES-module import cycle that deadlocks the command line.**

- **The pattern:** module A ends with `if (isMain) await main();`. During `main()`, A lazily imports module B (`await import('./b.mjs')`), and B statically imports a helper from A.
- **What happens:** A is still evaluating its top-level `await`, so B's import of A waits on A, and A waits on B. Node 22 exits with code 13 ("unsettled top-level await").
- **Why tests miss it:** a test that imports A as a library sees A already evaluated, so every library-level test passes.
- **Remedy:** move the shared helpers into a third module that neither side's entry point owns. Re-export them from the original module if callers depend on that path. Add at least one **end-to-end CLI test** that drives the real entry point through the code path that loads B, using a non-blocking child process if the test also hosts a server.

**2. An allowlist that normalizes case in one branch but not the next is a bypass.**

- **The pattern:** a release auditor admitted files with a case-insensitive extension test (`/\.(html|css)$/i`). It then chose its policy branch with case-sensitive `endsWith('.html')` and `endsWith('.css')`.
- **What happens:** `EXTRA.HTML` containing `<script>` passed the filter, matched neither branch, and was never inspected, so the audit passed.
- **Remedy:** normalize once (`const extension = extname(file).toLowerCase()`), use that value in every branch, and add an upper-case regression test.

**Applies to:** any Node ESM command line with top-level await and lazily loaded helpers; any scanner whose admission test and dispatch test are written separately.

## Evidence

- **Observed (trap 1):** the first served end-to-end run of a new `--candidate` preflight mode exited 13. A library-level suite of more than 300 tests was green. After the helpers moved to a separate module, two new end-to-end CLI tests passed; both failed when run against the previous scripts.
- **Observed (trap 2):** reproduced on a clean worktree of the project's then-current main branch. The default audit printed PASSED for an `EXTRA.HTML` file holding `<script>`. After normalization, the same input fails with a script finding. The defect predated the session; it was found while reviewing the diff.
- **Inferred:** both traps generalize beyond this project. That rests on Node ESM evaluation semantics and on the code pattern. No second project was tested.

## Revisit when

- **Trap 1:** a Node.js release changes how dynamic imports interact with a module that has a pending top-level await.
- **Trap 2:** a shared release-audit helper is extracted into a Kestrel skill. Fold this lesson into that skill's checklist, then mark this record superseded.

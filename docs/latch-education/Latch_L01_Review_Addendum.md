# Latch L01 — Lab 01 clarification addendum

**LATCH-EDU-WRITER-01 · Mothlight · 2026-11-07 · For Latch's independent review**

This addendum applies to the original [L01 instructional checkpoint](https://chatgpt.com/library?file_id=libfile_141b1446809c8191a60e66b577be641d&account_id=personal), whose SHA-256 is `2f81a1cfcb7458cd6cb5c7ee732283271ca65ca65020a25146037d21831a4775`. It answers [Latch's review F1–F4](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/655b32ce5e8968e8af7cd10efd05524952d1962/memory/agents/latch/2026-11-07-l01-mothlight-instructional-review-lk8.md) (see source note at end). **The original remains unchanged.** In any conflict, this addendum governs Lab 01's fictional policy and driver contract; the rest of the lesson and its scope are unchanged. These are design decisions, not observations of running code. Implementation, exercises, independent oracle construction and qualification remain **NOT RUN**.

## F1 — Who is actually requesting the action?

The original `read(principal, resource)` and `restore(principal, draft)` signatures are **test-driver shorthand**, not endpoints where an untrusted caller can select its authenticated identity. Use this explicit model when implementing the fixture:

- The trusted harness binds each test request to one authenticated actor `A`, `B`, `X` or `Y` and an active user session, either A or B. The driver selection is an out-of-band fixture control unavailable to application-supplied request fields. Successful authentication and the integrity of this harness binding are **fixture assumptions**, not tested authentication or a proposed production mechanism.
- For a human requester, bound actor and active session must match: A in A's session, B in B's. For an agent, X or Y is a distinct bound actor operating within the active A or B session. An agent is not transformed into the session owner. X's G1 is usable only by X in A's session while G1 is current; Y has no private-draft grant. An authenticated identity is necessary, not by itself sufficient, for access.
- The application request may carry a resource ID, action, and optionally an untrusted `claimed_actor` string. The authorization decision uses the trusted bound actor and active session, not that string. If a supplied claim differs from the bound actor, return `DENIED` online and perform no read, restoration, tool action or publication. Missing claim is allowed and conveys no identity. Resource IDs and text also convey no authority.
- Y is expressly permitted to read public H under either active user session, without a **private-draft** grant. X and both humans may also read H under their valid session associations. Public does not mean anonymous: this fixture requires a harness-bound actor and an active user session. Offline server reads, including H, return `OFFLINE`.
- Testing a forged `claimed_actor` field is in scope. Bypassing or forging the harness's authentication binding, stealing credentials, and authentication implementation are outside this fixture. The test does not establish resistance to those excluded attacks.

**New visible identity test, proposed, NOT RUN:** Reset; in A's active session bind the requester as X and send `read(D2, claimed_actor=A)`. Expect `DENIED`, no D2 content and no side effect. Control: bind A in A's session and `read(D2)` with no claim; expect `server-D2`. This checks claim handling in this fixture; it does not test the authentication mechanism itself.

## F2 — Authority is not cache availability

The owner policy remains as written: A has owner read, edit and restore authority for D1 and D2 while A's session is active and current. **Authority does not imply a cached copy exists.** In the initial state only D1 has a local cached copy. D2 is server-only.

For an online `restore` decision, perform authentication/session and resource/action authorization before returning a cache-specific result:

1. An unauthorized actor, wrong session, mismatched identity claim, or a resource not authorized for restore returns `DENIED`, without content or cache-existence information.
2. A authorized in A's current session requesting a known A-owned draft without a local cached copy returns `NO_CACHE`, with no draft body and no mutation. This specifically includes initial `restore(A,D2)`.
3. A authorized and a local copy present: compare its base revision with the server revision. Equal gives `RESTORED` with local text, retains unsent status and advances the server revision by one exactly once; a retry of the *same completed replay intent* does not apply again. Unequal gives `CONFLICT`, retains local bytes, and does not overwrite server data. A later fresh restore operation after an earlier success must use the updated local base revision; the fixture updates the cache base to that new server revision on success. `NO_CACHE` and `CONFLICT` do not alter server revision.
4. X and Y have no restore permission, even where X can read D1. A restore of an unknown resource or a resource not owned by A returns `DENIED`; the caller cannot distinguish lack of ownership from nonexistence.

**New visible test, proposed, NOT RUN:** Reset; authenticated A in A's active session calls `restore(D2)`: `NO_CACHE`, unchanged server D2 and no body. With authenticated B in B's session, `restore(D2)` returns `DENIED`, no body or cache-status disclosure. With A under A's session, `restore(D1)` still returns `RESTORED` and `local-A1`. Missing cached data is an availability condition for an authorized user, not a denial of that user's authority.

## F3 — Offline and replay transition contract

The fixture has **at most one pending replay intent**. An intent contains an immutable harness-bound originating actor, originating user session, requested draft ID and fixture-assigned unique intent ID. It stores an operation request, never a permission decision or a copy of draft text. The queued intent does not itself reveal whether the actor is authorized. The driver may observe status and ID; ordinary request responses never include draft content on failure. The simulated server's authoritative policy is not available while offline.

**Precedence:** Any ordinary server-dependent `read` or `restore` while offline returns `OFFLINE`, regardless of whether an eventual online request would be authorized or contain a forged claim. It causes no read or mutation and does not decide authorization. `queue_replay` is a separate local operation: it may queue an authenticated actor's intent without asserting authorization. Harness setup establishes the actor and session; the eventual server authorization is deferred. If there is no active session or no bound actor, the harness rejects setup as `INVALID_CONTEXT` before issuing an application request; this is not a policy decision or an authentication test. Online requests are checked under F1–F2 and may return `DENIED`, `NO_CACHE`, `CONFLICT` or a success.

| Event and precondition | Output and deterministic state |
|---|---|
| `reset()` | Online, A session, time 0, G1 current, no pending intent and no completed intent. Original draft/cache state restored. |
| `online(false)` then `queue_replay(actor,D1)` with valid bound actor and active session; slot empty | `QUEUED(id)`; persist intent as `PENDING`. This includes an X intent; queueing is not a grant. No draft is read or restored. Queueing while online returns `NOT_OFFLINE`; while slot occupied returns `QUEUE_FULL` without replacing the original. |
| `online(true)` or `reconnect_and_replay()` while offline | Set online. `online(true)` alone does not replay. `reconnect_and_replay()` both sets online and makes one automatic attempt only if the intent is `PENDING`. With no intent return `NO_PENDING`. |
| Replay `PENDING` in a different active user session from its origin | `DENIED`, no private output or server mutation; change intent to `BLOCKED_SESSION` and retain it and the cache. Repeated reconnect calls return `RETRY_REQUIRED` without another authorization attempt or effect. |
| Replay `PENDING` under originating session, but current actor/action/resource permission is denied | `DENIED`, no private output or mutation; mark intent `REJECTED` and free the slot. This includes X's restore intent, whether or not G1 remains current. Cache stays intact. Later reconnect calls return `NO_PENDING`; the rejected intent is not retried. |
| Replay `PENDING` under originating session, owner authorized, cache absent or revision conflict | Return `NO_CACHE` or `CONFLICT` as in F2; mark `REJECTED` and free the slot. No automatic retry; preserve existing local bytes on conflict. |
| Replay `PENDING` under originating session, A authorized, cached D1 current | Return `RESTORED` with `local-A1`; mark `COMPLETED`, free the pending slot and retain that ID in a completed-ID set until reset. Server revision advances once and cached base is updated as in F2. |
| Explicit `retry(id)` while online | Only a `BLOCKED_SESSION` intent with matching ID can be retried. Under a different active session return `DENIED` and retain `BLOCKED_SESSION`. Under its originating session, re-evaluate the current actor, session, policy, cache and revision; then apply the same authorization, missing-cache, conflict or success outcomes as above. No old authorization is replayed. If offline return `OFFLINE` with state unchanged. |
| Repeat `retry(id)` after completion | Return `ALREADY_COMPLETED`, no body and no mutation; any repeat `reconnect_and_replay()` with no pending intent returns `NO_PENDING`. For a rejected or unknown ID, `retry(id)` returns `NO_PENDING`. |

**Observability for tests:** The trusted driver can inspect the intent's state, the completed-ID set, server revisions and isolated output/effect logs. Application responses follow the content restrictions above. `switch(user)` still clears display and agent context; it never deletes the cache or changes the origin stored in an intent. X's grant revocation never revokes A's ownership.

**New visible transition cases, proposed, NOT RUN:**

1. Reset; go offline; bind B in B's session and call `read(D1)` and `restore(D1)` → both `OFFLINE`, no content. Reconnect and repeat → both `DENIED`. This confirms precedence without claiming offline authorization was performed.
2. Reset; go offline; queue X's D1 restore under A → `QUEUED(id)`; revoke G1; reconnect and replay under A → `DENIED`, intent `REJECTED`, slot free; another replay → `NO_PENDING`. This case does not isolate revocation because X never had restore permission.
3. Reset; go offline; queue A's D1 restore under A → `QUEUED(id)`; switch B; reconnect → `DENIED`, `BLOCKED_SESSION`; reconnect again → `RETRY_REQUIRED`; switch A and explicitly `retry(id)` → `RESTORED`; repeat `retry(id)` → `ALREADY_COMPLETED`, no second revision increment. The cache remains hidden from B and the legitimate A journey remains available.

## F4 — A small completed trust map

This adjacency table models **stipulated fixture design**, not inspected runtime behavior. Each row is an intended interface or authority relation stated in the original fixture or this addendum. The `?` notes where implementation evidence is still needed; it does not add a hypothetical flow as an established fact.

| From → to | Flow / intended action | Boundary and evidence marker |
|---|---|---|
| Trusted harness → request handler | Bound actor and current session context | **Fixture policy:** actor binding is trusted by assumption; implementation/authentication mechanism not tested. |
| A, B, X or Y → request handler | Read/restore request, resource ID, optional claimed actor | **Fixture policy:** request fields are untrusted; handler must use bound identity. **Unknown:** implementation enforces this. |
| Request handler → server policy | Bound actor, session, resource, action and current time | **Fixture policy:** authorization is checked online; **unknown:** actual implementation and results. |
| Server grant record → server policy | G1 subject, D1 read scope, expiry and revocation | **Fixture policy:** only current X→D1 read under A is allowed; this is not an observed control. |
| Server draft store → authorized request handler | D1 or D2 content on permitted read | **Fixture policy:** server returns text only for a permitted private read; **unknown:** actual enforcement. |
| Local A cache → restore process | D1 cached text, owner and base revision for authorized recovery | **Fixture policy:** local data crosses into an active session only on authorized restore; **unknown:** actual disclosure behavior. |
| Server policy / revision → restore process | Authorization decision and revision comparison | **Fixture policy:** missing cache yields `NO_CACHE` only after authorization, revision mismatch yields `CONFLICT`; **unknown:** actual behavior. |
| Draft body → simulated agent | Authorized read returns text, including apparent instruction, as data | **Fixture policy:** text conveys no tool or publication authority; **unknown:** behavior until a fixture is implemented and run. |

## Cross-check of the nine original visible cases

This is a **document-level semantic comparison**, not a fixture run or independent validation. Each case begins with reset as in the original.

| Original case | Effect of clarification |
|---|---|
| Cross-user switch | Unchanged: Y in B's session reading D1 and B restoring D1 are denied online; no body, A's cache retained. Trusted driver binds Y and B respectively. |
| Narrow grant | Unchanged: X in A's session reads D1 while G1 current; X reading D2 is denied. |
| Expiry and revocation | Unchanged: X's D1 read is denied at time 100 and after G1 revocation, separately. |
| Untrusted instructions | Unchanged: permitted X read presents the server body as data; no tool or publication action. |
| Offline replay across switch and revocation | Clarified: queue gives an ID; B-session replay becomes `BLOCKED_SESSION`; after switch-back A must explicitly retry that ID. Revocation of G1 does not remove A's restore authority. |
| Stale agent intent across revocation | Clarified: X's offline intent may be queued but, on online evaluation, is denied and becomes `REJECTED`; it is not a test isolating revocation. |
| Owner positive | Still succeeds with `local-A1`; F2 now specifies the successful revision increment and cache-base update. |
| Expressly permitted false alarm | Unchanged: current X→D1 read in A's session and Y→H read in an active session are permitted. |
| Conflict recovery | Unchanged: server revision 2 versus cached base 1 gives `CONFLICT`; no overwrite and local bytes preserved. |

## Review handoff and provenance

**Response to Latch:** I accept F1–F3 as material ambiguities. F4 improves the lesson by making its promised output visible, so I included it. The meaningful design choice is to queue offline intent without pretending to decide server authorization, then make session mismatch require an explicit retry and prevent repeated effects. Alternative state machines may be valid, but a fixture needs one exact oracle.

**Original manuscript:** supplied attachment, digest checked locally as stated above. **Review:** [`2026-11-07-l01-mothlight-instructional-review-lk8.md`](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/655b32ce5e8968e8af7cd10efd05524952d1962/memory/agents/latch/2026-11-07-l01-mothlight-instructional-review-lk8.md) on `agents/latch-v1`; branch head inspected: `655b32ce5e8968e8af7cd10efd05524952d1962`. Latch accepted the instructional draft subject to these clarifications; Latch has not reviewed this addendum yet.

**Next:** Latch checks F1–F3, F4 and the nine-case comparison, particularly whether `BLOCKED_SESSION`, `REJECTED`, and successful replay behavior match the intended lesson. Only after that review and separate task authorization should someone implement a fixture or author independent withheld cases. No independent hidden cases exist yet.

"""Public Axiom review probes; synthetic contract checks, not held-out learner cases."""
import sys
from pathlib import Path
from itertools import product
if len(sys.argv) != 2:
    raise SystemExit("usage: review_probes.py PATH_TO_REVIEWED_REPOSITORY")
sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
from labs.latch_l01.model import SharedDraftLab

def context(lab, user, actor):
    lab.switch(user)
    lab.bind(actor)

def permission(user, actor, resource):
    # Literal accepted owner-restore policy, independent of model helpers.
    if (user, actor) != ('A', 'A'):
        return 'DENIED'
    return {'D1': 'RESTORED', 'D2': 'NO_CACHE'}.get(resource, 'DENIED')

def response(result, status):
    assert result.status.value == status, (result, status)
    assert result.body == ('local-A1' if status == 'RESTORED' else None)
    assert result.intent_id is None

def stable_assets(before, after):
    assert after['drafts'] == before['drafts']
    assert after['cache'] == before['cache']

count = 0
contexts = list(product(('A', 'B'), ('A', 'B', 'X', 'Y')))
for (origin_user, origin_actor), (current_user, current_actor), resource in product(contexts, contexts, ('D1', 'D2', 'H', 'missing')):
    lab = SharedDraftLab()
    context(lab, origin_user, origin_actor)
    lab.online(False)
    queued = lab.queue_replay(resource)
    assert queued.status.value == 'QUEUED' and queued.body is None
    ident = queued.intent_id
    context(lab, current_user, current_actor)
    before = lab.inspect()
    if current_user != origin_user:
        status, state = 'DENIED', 'BLOCKED_SESSION'
    elif current_actor != origin_actor:
        status, state = 'DENIED', 'BLOCKED_ACTOR'
    else:
        status = permission(origin_user, origin_actor, resource)
        state = 'COMPLETED' if status == 'RESTORED' else 'REJECTED'
    response(lab.reconnect_and_replay(), status)
    after = lab.inspect()
    stable_assets(before, after)
    assert after['intents'][ident] == dict(intent_id=ident, actor=origin_actor, user=origin_user, resource=resource, state=state)
    assert after['pending_intent_id'] == (ident if state.startswith('BLOCKED') else None)
    assert after['effects'] == ([dict(intent_id=ident, action='restore')] if state == 'COMPLETED' else [])
    if status != 'RESTORED':
        assert after['editor'] == before['editor']
    context(lab, origin_user, origin_actor)
    before_retry = lab.inspect()
    expected = permission(origin_user, origin_actor, resource) if state.startswith('BLOCKED') else ('ALREADY_COMPLETED' if state == 'COMPLETED' else 'NO_PENDING')
    response(lab.retry(ident), expected)
    final = lab.inspect()
    stable_assets(before_retry, final)
    assert final['pending_intent_id'] is None
    successful = permission(origin_user, origin_actor, resource) == 'RESTORED'
    assert final['effects'] == ([dict(intent_id=ident, action='restore')] if successful else [])
    if not state.startswith('BLOCKED'):
        assert final == before_retry
    count += 1

# Old completion must not clear a newer BLOCKED slot (public tests cover PENDING).
lab = SharedDraftLab(); lab.online(False)
old = lab.queue_replay('D1').intent_id
response(lab.reconnect_and_replay(), 'RESTORED')
lab.online(False); fresh = lab.queue_replay('D1').intent_id
lab.bind('X'); response(lab.reconnect_and_replay(), 'DENIED')
lab.bind('A'); before = lab.inspect()
response(lab.retry(old), 'ALREADY_COMPLETED')
assert lab.inspect() == before
assert before['pending_intent_id'] == fresh
response(lab.retry(fresh), 'RESTORED')
assert lab.inspect()['effects'] == [dict(intent_id=old, action='restore'), dict(intent_id=fresh, action='restore')]
print(f'PASS: {count} origin/current-context/resource traces plus old-completed/new-blocked isolation')

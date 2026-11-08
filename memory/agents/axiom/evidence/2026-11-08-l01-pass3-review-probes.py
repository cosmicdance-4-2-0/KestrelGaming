"""Public Axiom Pass-3 review evidence, not hidden learner evaluation."""
import io
import json
import sys
from contextlib import ExitStack, redirect_stdout
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

if len(sys.argv) != 2:
    raise SystemExit('usage: review_probes.py PATH_TO_REVIEWED_REPOSITORY')
sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
from labs.latch_l01.model import SharedDraftLab, Result, Status
from labs.latch_l01.surface import ApplicationSurface, Reply
from labs.latch_l01.visible_cases import run_visible_cases
from labs.latch_l01 import __main__ as cli

class StringSubclass(str):
    pass

class DictSubclass(dict):
    pass

class NoCoercion:
    def __str__(self):
        raise AssertionError('request data must not be coerced')

bad_types = [None, [], {}, 1, True, 1.5, b'D1', ('D1',), StringSubclass('D1'), NoCoercion()]
requests = [(x, 'INVALID_REQUEST') for x in (None, [], (), 'read', 1, True, DictSubclass(action='read', resource='D1'))]
requests += [({}, 'INVALID_REQUEST'), ({'action': None}, 'INVALID_REQUEST'),
             ({'action': StringSubclass('read'), 'resource': 'D1'}, 'INVALID_REQUEST'),
             ({StringSubclass('action'): 'read', 'resource': 'D1'}, 'INVALID_REQUEST'),
             ({1: 'read'}, 'INVALID_REQUEST')]
for action, field in [('read','resource'), ('restore','resource'), ('queue_replay','resource'), ('retry','intent_id')]:
    requests.append(({'action':action}, 'INVALID_REQUEST'))
    for value in bad_types:
        requests.append(({'action':action, field:value}, 'INVALID_REQUEST'))
for action in ['read','restore']:
    for value in bad_types[1:]:
        requests.append(({'action':action,'resource':'D1','claimed_actor':value}, 'INVALID_REQUEST'))
for action in ['inspect','inspect_effects','bind','switch','reset','online','advance','revoke','set_server_text','set_server_revision','__dict__','unknown']:
    requests.append(({'action':action, 'resource':[], 'actor':'A'}, 'UNSUPPORTED_ACTION'))
for action in ['read','restore','queue_replay','retry','reconnect_and_replay','tool','publish']:
    envelope = {'action':action, 'actor':'A'}
    if action in ['read','restore','queue_replay']:
        envelope['resource']='D1'
    elif action=='retry':
        envelope['intent_id']='unknown'
    requests.append((envelope, 'INVALID_REQUEST'))
for action in ['tool','publish']:
    requests.append(({'action':action}, 'DENIED'))

def setup(mode):
    lab=SharedDraftLab()
    if mode in ['offline','invalid_context','full','blocked','completed']:
        lab.online(False)
    if mode in ['full','blocked','completed']:
        lab.queue_replay('D1')
    if mode=='blocked':
        lab.bind('X'); lab.reconnect_and_replay()
    if mode=='completed':
        lab.reconnect_and_replay()
    if mode=='invalid_context':
        lab.bind(None)
    return lab

count=0
for mode in ['online','offline','invalid_context','full','blocked','completed']:
    for payload, expected in requests:
        lab=setup(mode);surface=ApplicationSurface(lab)
        before=lab.inspect(); effects=surface.inspect_effects()
        with ExitStack() as stack:
            calls=[stack.enter_context(patch.object(lab, name, wraps=getattr(lab,name)))
                   for name in ['read','restore','queue_replay','retry','reconnect_and_replay']]
            actual=surface.dispatch(payload)
            assert actual==Reply(expected),(mode,type(payload),actual,expected)
            assert all(call.call_count==0 for call in calls)
        assert lab.inspect()==before
        assert surface.inspect_effects()==effects
        count+=1
print('PASS:',count,'shape/unsupported/deny-only requests: zero model calls and no mutation')

class DenyReads(SharedDraftLab):
    def read(self, resource, claimed_actor=None):
        return Result(Status.DENIED)

class EmptyReads(SharedDraftLab):
    def read(self, resource, claimed_actor=None):
        return replace(super().read(resource,claimed_actor), body=None)

class WriteOnRestore(SharedDraftLab):
    def restore(self, resource, claimed_actor=None):
        result=super().restore(resource,claimed_actor)
        if result.status==Status.RESTORED:
            self._drafts[resource]=replace(self._drafts[resource],body=result.body)
        return result

class QueuedWriteOnly(SharedDraftLab):
    def _execute_intent(self,intent,block_on_mismatch):
        result=super()._execute_intent(intent,block_on_mismatch)
        if result.status==Status.RESTORED:
            self._drafts[intent.resource]=replace(self._drafts[intent.resource],body=result.body)
        return result

for factory in [DenyReads,EmptyReads,WriteOnRestore]:
    outcomes=run_visible_cases(factory)
    assert len(outcomes)==16 and any(not c.passed for c in outcomes)
    for json_mode in [False,True]:
        with patch.object(cli,'run_visible_cases',lambda:run_visible_cases(factory)):
            with redirect_stdout(io.StringIO()) as output:
                code=cli.main(['--json'] if json_mode else [])
        assert code==1
        if json_mode:
            data=json.loads(output.getvalue());assert not data['successful'] and data['failed']>0
        else:
            assert 'FAIL ' in output.getvalue()
    print('PASS: runner and both CLI modes reject',factory.__name__)

def raises():
    raise RuntimeError('reviewer synthetic case error')
for factory in [raises]:
    cases=run_visible_cases(factory)
    assert len(cases)==16 and all(not c.passed and c.error for c in cases)
    with patch.object(cli,'run_visible_cases',lambda:run_visible_cases(factory)):
        with redirect_stdout(io.StringIO()) as output:
            assert cli.main(['--json'])==1
    assert all(c['error'] for c in json.loads(output.getvalue())['cases'])
with patch.object(cli,'run_visible_cases',return_value=[]):
    with redirect_stdout(io.StringIO()) as output:
        assert cli.main(['--json'])==1
assert not json.loads(output.getvalue())['successful']
print('PASS: case errors retained; empty run fails closed')

# Characterize an additional public-runner coverage gap, without changing the model.
cases=run_visible_cases(QueuedWriteOnly)
assert len(cases)==16 and all(c.passed for c in cases)
lab=QueuedWriteOnly();before=lab.inspect()['drafts'];lab.online(False);lab.queue_replay('D1');lab.reconnect_and_replay()
assert lab.inspect()['drafts']!=before
print('OBSERVED COVERAGE LIMIT: queued-only server-write mutant passes all 16 public cases')
for mode in [[], ['--json']]:
    with patch.object(cli, 'run_visible_cases', lambda: run_visible_cases(QueuedWriteOnly)):
        with redirect_stdout(io.StringIO()) as output:
            code = cli.main(mode)
    assert code == 0
    if mode:
        data = json.loads(output.getvalue())
        assert data['successful'] and (data['passed'], data['failed']) == (16, 0)
print('OBSERVED: text and JSON CLI both exit 0 for queued-only server-write mutant')

# The older focused regression already protects this invariant; distinguish that
# protection from the standalone teaching runner observation above.
import unittest
sys.path.insert(0, str(Path(sys.argv[1]).resolve() / 'tests'))
import test_latch_l01_replay as replay_tests
with patch.object(replay_tests, 'SharedDraftLab', QueuedWriteOnly):
    case = replay_tests.SharedDraftReplayTests('test_success_has_one_local_effect_no_server_or_cache_write')
    result = unittest.TextTestRunner(stream=io.StringIO()).run(unittest.TestSuite([case]))
assert len(result.failures) == 1 and not result.errors
print('PASS: existing Pass-2 regression rejects that mutant as expected')

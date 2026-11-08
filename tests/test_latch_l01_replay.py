"""Public pass-2 transition controls; expected outcomes come from the contract."""

import unittest

from labs.latch_l01.model import Result, SharedDraftLab, Status


class SharedDraftReplayTests(unittest.TestCase):
    def setUp(self):
        self.lab = SharedDraftLab()

    def context(self, user, actor):
        self.lab.switch(user)
        self.lab.bind(actor)

    def queue(self, resource="D1"):
        self.lab.online(False)
        result = self.lab.queue_replay(resource)
        self.assertEqual(result.status, Status.QUEUED)
        self.assertIsNone(result.body)
        self.assertIsNotNone(result.intent_id)
        return result.intent_id

    def unchanged(self, operation, expected):
        before = self.lab.inspect()
        self.assertEqual(operation(), expected)
        self.assertEqual(self.lab.inspect(), before)

    def assets(self):
        state = self.lab.inspect()
        return {key: state[key] for key in ("drafts", "cache", "editor", "effects")}

    def test_queue_stores_immutable_origin_without_reading_text(self):
        self.lab.bind("X")
        before = self.assets()
        intent_id = self.queue()
        state = self.lab.inspect()
        self.assertEqual(state["pending_intent_id"], intent_id)
        self.assertEqual(state["intents"][intent_id], {
            "intent_id": intent_id, "actor": "X", "user": "A",
            "resource": "D1", "state": "PENDING"})
        self.assertEqual(self.assets(), before)
        # Inspection is detached, so even trusted view edits do not rewrite origin.
        state["intents"][intent_id]["actor"] = "A"
        self.lab.bind("A")
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["actor"], "X")

    def test_queue_guards_online_before_full_and_never_allocate_on_refusal(self):
        self.unchanged(lambda: self.lab.queue_replay("D1"), Result(Status.NOT_OFFLINE))
        intent_id = self.queue()
        self.unchanged(lambda: self.lab.queue_replay("D2"), Result(Status.QUEUE_FULL))
        self.lab.online(True)
        self.unchanged(lambda: self.lab.queue_replay("D2"), Result(Status.NOT_OFFLINE))
        self.assertEqual(self.lab.inspect()["pending_intent_id"], intent_id)

    def test_online_pending_retry_is_ineligible_but_automatic_replay_survives(self):
        intent_id = self.queue()
        self.lab.online(True)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "PENDING")
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.NO_PENDING))
        self.assertEqual(self.lab.reconnect_and_replay(),
                         Result(Status.RESTORED, "local-A1"))
        self.assertEqual(self.lab.inspect()["completed_ids"], [intent_id])

    def test_success_has_one_local_effect_no_server_or_cache_write(self):
        intent_id = self.queue()
        before = self.lab.inspect()
        self.assertEqual(self.lab.reconnect_and_replay(),
                         Result(Status.RESTORED, "local-A1"))
        after = self.lab.inspect()
        self.assertEqual(after["drafts"], before["drafts"])
        self.assertEqual(after["cache"], before["cache"])
        self.assertEqual(after["editor"],
                         {"resource": "D1", "body": "local-A1", "unsent": True})
        self.assertEqual(after["effects"], [{"intent_id": intent_id, "action": "restore"}])
        self.assertEqual(after["intents"][intent_id]["state"], "COMPLETED")
        self.assertIsNone(after["pending_intent_id"])
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.ALREADY_COMPLETED))
        self.unchanged(self.lab.reconnect_and_replay, Result(Status.NO_PENDING))

    def test_session_mismatch_precedes_actor_mismatch_and_retains_cache(self):
        intent_id = self.queue()
        self.context("B", "Y")
        before = self.assets()
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.DENIED))
        self.assertEqual(self.assets(), before)
        state = self.lab.inspect()
        self.assertEqual(state["intents"][intent_id]["state"], "BLOCKED_SESSION")
        self.assertEqual(state["pending_intent_id"], intent_id)
        self.unchanged(self.lab.reconnect_and_replay, Result(Status.RETRY_REQUIRED))

    def test_returning_to_origin_requires_explicit_retry(self):
        intent_id = self.queue()
        self.context("B", "B")
        self.lab.reconnect_and_replay()
        self.context("A", "A")
        self.unchanged(self.lab.reconnect_and_replay, Result(Status.RETRY_REQUIRED))
        self.assertEqual(self.lab.retry(intent_id), Result(Status.RESTORED, "local-A1"))

    def test_automatic_actor_mismatch_blocks_then_origin_can_retry(self):
        intent_id = self.queue()
        self.lab.bind("X")
        before = self.assets()
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.DENIED))
        self.assertEqual(self.assets(), before)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "BLOCKED_ACTOR")
        self.unchanged(self.lab.reconnect_and_replay, Result(Status.RETRY_REQUIRED))
        self.lab.bind("A")
        self.assertEqual(self.lab.retry(intent_id), Result(Status.RESTORED, "local-A1"))

    def test_cross_actor_retry_cannot_launder_owner_authority(self):
        intent_id = self.queue()
        self.context("B", "B")
        self.lab.reconnect_and_replay()
        self.context("A", "X")
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.DENIED))
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "BLOCKED_SESSION")
        self.lab.bind("A")
        self.assertEqual(self.lab.retry(intent_id), Result(Status.RESTORED, "local-A1"))

    def test_cross_session_retry_retains_existing_blocked_state(self):
        intent_id = self.queue()
        self.lab.bind("X")
        self.lab.reconnect_and_replay()
        self.context("B", "A")  # Correct origin actor, wrong current user.
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.DENIED))
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "BLOCKED_ACTOR")

    def test_agent_intent_can_queue_but_cannot_restore_after_reconnect(self):
        self.lab.bind("X")
        intent_id = self.queue()
        self.lab.revoke()
        self.lab.advance(100)
        before = self.assets()
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.DENIED))
        self.assertEqual(self.assets(), before)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "REJECTED")
        self.assertIsNone(self.lab.inspect()["pending_intent_id"])
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.NO_PENDING))
        self.unchanged(self.lab.reconnect_and_replay, Result(Status.NO_PENDING))
        # This cannot isolate revocation: X never had restore permission.

    def test_owner_intent_survives_agent_revocation_and_expiry(self):
        intent_id = self.queue()
        self.lab.revoke()
        self.lab.advance(100)
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.RESTORED, "local-A1"))
        self.assertEqual(self.lab.inspect()["completed_ids"], [intent_id])

    def test_missing_cache_is_authorized_terminal_result_and_frees_slot(self):
        intent_id = self.queue("D2")
        before = self.assets()
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.NO_CACHE))
        self.assertEqual(self.assets(), before)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "REJECTED")
        self.assertIsNone(self.lab.inspect()["pending_intent_id"])
        self.assertNotEqual(self.queue(), intent_id)

    def test_revision_change_before_reconnect_rejects_without_losing_work(self):
        intent_id = self.queue()
        self.lab.set_server_revision("D1", 2)
        before = self.assets()
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.CONFLICT))
        self.assertEqual(self.assets(), before)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "REJECTED")
        self.assertIsNone(self.lab.inspect()["pending_intent_id"])

    def test_blocked_retry_revalidates_revision_before_any_recovery(self):
        intent_id = self.queue()
        self.context("B", "B")
        self.lab.reconnect_and_replay()
        self.lab.set_server_revision("D1", 2)
        self.context("A", "A")
        before = self.assets()
        self.assertEqual(self.lab.retry(intent_id), Result(Status.CONFLICT))
        self.assertEqual(self.assets(), before)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "REJECTED")

    def test_unknown_resource_is_not_authorized_by_earlier_queue(self):
        intent_id = self.queue("missing")
        before = self.assets()
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.DENIED))
        self.assertEqual(self.assets(), before)
        self.assertEqual(self.lab.inspect()["intents"][intent_id]["state"], "REJECTED")

    def test_rejected_agent_intent_does_not_prevent_fresh_owner_intent(self):
        self.lab.bind("X")
        old = self.queue()
        self.lab.reconnect_and_replay()
        self.lab.bind("A")
        fresh = self.queue()
        self.assertNotEqual(fresh, old)
        self.lab.online(True)
        self.unchanged(lambda: self.lab.retry(old), Result(Status.NO_PENDING))
        self.assertEqual(self.lab.inspect()["pending_intent_id"], fresh)
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.RESTORED, "local-A1"))

    def test_completed_retry_requires_origin_actor_and_session(self):
        intent_id = self.queue()
        self.lab.reconnect_and_replay()
        for user, actor in (("A", "X"), ("B", "B"), ("B", "A")):
            self.context(user, actor)
            self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.DENIED))

    def test_completed_retry_does_not_reinstall_cleared_editor(self):
        intent_id = self.queue()
        self.lab.reconnect_and_replay()
        self.context("B", "B")
        self.assertIsNone(self.lab.inspect()["editor"])
        self.context("A", "A")
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.ALREADY_COMPLETED))
        self.assertIsNone(self.lab.inspect()["editor"])

    def test_completed_retry_does_not_consume_another_pending_intent(self):
        old = self.queue()
        self.lab.reconnect_and_replay()
        fresh = self.queue()
        self.lab.online(True)
        self.unchanged(lambda: self.lab.retry(old), Result(Status.ALREADY_COMPLETED))
        self.assertEqual(self.lab.inspect()["pending_intent_id"], fresh)
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.RESTORED, "local-A1"))
        self.assertEqual(self.lab.inspect()["effects"], [
            {"intent_id": old, "action": "restore"},
            {"intent_id": fresh, "action": "restore"}])

    def test_offline_retry_precedes_unknown_pending_blocked_and_completed(self):
        pending = self.queue()
        self.unchanged(lambda: self.lab.retry(pending), Result(Status.OFFLINE))
        self.unchanged(lambda: self.lab.retry("unknown"), Result(Status.OFFLINE))
        self.lab.bind("X")
        self.lab.reconnect_and_replay()
        self.lab.online(False)
        self.unchanged(lambda: self.lab.retry(pending), Result(Status.OFFLINE))
        self.lab.bind("A")
        self.lab.online(True)
        self.lab.retry(pending)
        self.lab.online(False)
        self.unchanged(lambda: self.lab.retry(pending), Result(Status.OFFLINE))

    def test_blocked_slot_limit_preserves_direct_owner_recovery(self):
        self.lab.bind("X")
        intent_id = self.queue()
        self.lab.bind("A")
        self.lab.reconnect_and_replay()
        self.unchanged(lambda: self.lab.retry(intent_id), Result(Status.DENIED))
        self.assertEqual(self.lab.restore("D1"), Result(Status.RESTORED, "local-A1"))
        self.lab.online(False)
        self.unchanged(lambda: self.lab.queue_replay("D1"), Result(Status.QUEUE_FULL))
        self.lab.online(True)
        self.lab.bind("X")
        self.assertEqual(self.lab.retry(intent_id), Result(Status.DENIED))
        self.assertIsNone(self.lab.inspect()["pending_intent_id"])

    def test_invalid_context_precedes_all_replay_driver_requests(self):
        intent_id = self.queue()
        self.lab.bind(None)
        for call in (lambda: self.lab.queue_replay("D1"),
                     self.lab.reconnect_and_replay, lambda: self.lab.retry(intent_id)):
            self.unchanged(call, Result(Status.INVALID_CONTEXT))

    def test_reconnect_without_pending_sets_online_and_has_no_other_effect(self):
        self.lab.online(False)
        expected = self.lab.inspect()
        expected["online"] = True
        self.assertEqual(self.lab.reconnect_and_replay(), Result(Status.NO_PENDING))
        self.assertEqual(self.lab.inspect(), expected)
        self.unchanged(lambda: self.lab.retry("unknown"), Result(Status.NO_PENDING))

    def test_reset_clears_intents_effects_and_restores_id_sequence(self):
        initial = self.lab.inspect()
        old = self.queue()
        self.lab.reconnect_and_replay()
        self.queue("D2")
        self.lab.reset()
        self.assertEqual(self.lab.inspect(), initial)
        # IDs are unique within one reset epoch; reset restores the full fixture.
        self.assertEqual(self.queue(), old)


if __name__ == "__main__":
    unittest.main()

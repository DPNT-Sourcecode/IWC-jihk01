from __future__ import annotations

import unittest
from unittest.mock import patch

from .utils import call_dequeue, call_enqueue, call_size, iso_ts, run_queue

from solutions.IWC.task_types import TaskSubmission
from solutions.IWC.queue_solution_legacy import Priority, Queue

def test_enqueue_size_dequeue_flow() -> None:
    run_queue([
        call_enqueue("companies_house", 1, iso_ts(delta_minutes=0)).expect(1),
        call_size().expect(1),
        call_dequeue().expect("companies_house", 1),
    ])


def test_task_already_in_queue() -> None:
    run_queue([
        call_enqueue("companies_house", 1, iso_ts(delta_minutes=0)).expect(1),
        call_enqueue("companies", 1, iso_ts(delta_minutes=0)).expect(2),
        call_enqueue("companies_house", 1, iso_ts(delta_minutes=0)).expect(2),
        call_enqueue("companies_house", 2, iso_ts(delta_minutes=0)).expect(3),
    ])

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

        self.t1 = TaskSubmission(
            provider="companies_house",
            user_id=3,
            timestamp=iso_ts(delta_minutes=0),
            metadata={"priority": Priority.NORMAL}
        )

        self.t2 = TaskSubmission(
            provider="companies",
            user_id=3,
            timestamp=iso_ts(delta_minutes=0),
            metadata={"priority": Priority.NORMAL}
        )

    def test_maintain_schedule_order(self) -> None:
        self.assertEqual(self.t1.provider, "companies_house")
        self.assertNotEqual(self.t2.provider, "companies_house")

        self.queue.enqueue(self.t1)
        self.queue.enqueue(self.t2)

        # this is a hacky test but here I am going to simulate the order being shuffled
        # as happens in dequeue due to the 3 rule
        queue_shuffled = [self.queue._queue[1], self.queue._queue[0]]
        with patch.object(self.queue, "_queue", new=queue_shuffled):

            self.assertEqual(self.queue.dequeue().provider, "companies_house")   # should be t1












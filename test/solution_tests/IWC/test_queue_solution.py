from __future__ import annotations

from .utils import call_dequeue, call_enqueue, call_size, iso_ts, run_queue

from solutions.IWC.task_types import TaskSubmission
from solutions.IWC.queue_solution_entrypoint import QueueSolutionEntrypoint
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


def test_maintain_schedule_order() -> None:
    queue = Queue()

    t1 = TaskSubmission(
        provider="companies_house",
        user_id=3,
        timestamp=iso_ts(delta_minutes=0),
        metadata={"priority": Priority.NORMAL}
    )

    t2 = TaskSubmission(
        provider="companies",
        user_id=3,
        timestamp=iso_ts(delta_minutes=0),
        metadata={"priority": Priority.NORMAL}
    )

    queue.enqueue(t1)
    queue.enqueue(t2)

    # this is a hacky test but here I am going to simulate the order being shuffled
    # as happens in dequeue due to the 3 rule
    queue_shuffled = [queue._queue[1], queue._queue[0]]
    from unittest.mock import patch,
    with patch.object(queue, "_queue")









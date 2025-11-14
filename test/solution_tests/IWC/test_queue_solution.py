from __future__ import annotations

from .utils import call_dequeue, call_enqueue, call_size, iso_ts, run_queue

from solutions.IWC.queue_solution_legacy import Queue


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
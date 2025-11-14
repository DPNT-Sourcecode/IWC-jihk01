"""Extremely small queue placeholder for the IWC challenge."""

from __future__ import annotations

from solutions.IWC.task_types import TaskDispatch, TaskSubmission


class Queue:
    """Naive FIFO queue backed by a Python list."""

    def __init__(self) -> None:
        self._tasks: list[TaskSubmission] = []

    def enqueue(self, item: TaskSubmission) -> int:
        self._tasks.append(item)
        return self.size

    def dequeue(self) -> TaskDispatch | None:
        if not self._tasks:
            return None
        task = self._tasks.pop(0)
        return TaskDispatch(provider=task.provider, user_id=task.user_id)

    @property
    def size(self) -> int:
        return len(self._tasks)

    def purge(self) -> bool:
        self._tasks.clear()
        return True

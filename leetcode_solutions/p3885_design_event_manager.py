import unittest
from heapq import heappop, heappush

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class EventManager:

    def __init__(self, events: list[list[int]]):
        self.polled = set()
        self.heap = []
        self.actual_priorities = {}
        for event_id, priority in events:
            self.actual_priorities[event_id] = priority
            heappush(self.heap, (-priority, event_id))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.actual_priorities[eventId] = newPriority
        heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        if not self.heap:
            return -1
        priority, event_id = heappop(self.heap)
        while (
            event_id in self.polled
            or self.actual_priorities[event_id] != -priority
        ):
            if not self.heap:
                return -1
            priority, event_id = heappop(self.heap)
        self.polled.add(event_id)
        return event_id


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": EventManager,
            "cls_init_args": [[[5, 7], [2, 7], [9, 4]]],
            "class_methods": [
                "pollHighest",
                "updatePriority",
                "pollHighest",
                "pollHighest",
            ],
            "args": [[], [9, 7], [], []],
            "expected": [2, None, 5, 9],
        },
        {
            "class": EventManager,
            "cls_init_args": [[[4, 1], [7, 2]]],
            "class_methods": ["pollHighest", "pollHighest", "pollHighest"],
            "args": [[], [], []],
            "expected": [7, 4, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

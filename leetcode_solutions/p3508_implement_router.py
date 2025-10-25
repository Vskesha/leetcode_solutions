import unittest
from collections import defaultdict, deque
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.queue = deque()
        self.destinations = defaultdict(SortedList)
        self.packets = set()

    def _pop_old_packet(self) -> tuple | None:
        if self.queue:
            packet = self.queue.popleft()
            self.packets.remove(packet)
            self.destinations[packet[1]].remove(packet[2])
            return packet

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packets:
            return False

        self.packets.add((source, destination, timestamp))
        self.queue.append((source, destination, timestamp))
        self.destinations[destination].add(timestamp)

        if len(self.queue) > self.memory_limit:
            self._pop_old_packet()

        return True

    def forwardPacket(self) -> List[int]:
        packet = self._pop_old_packet()
        return list(packet) if packet else []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destinations[destination]
        start_index = timestamps.bisect_left(startTime)
        end_index = timestamps.bisect_right(endTime)
        return end_index - start_index


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null, true, false = None, True, False
    test_cases = [
        {
            "class": Router,
            "cls_init_args": [3],
            "class_methods": [
                "addPacket",
                "addPacket",
                "addPacket",
                "addPacket",
                "addPacket",
                "forwardPacket",
                "addPacket",
                "getCount",
            ],
            "args": [
                [1, 4, 90],
                [2, 5, 90],
                [1, 4, 90],
                [3, 5, 95],
                [4, 5, 105],
                [],
                [5, 2, 110],
                [5, 100, 110],
            ],
            "expected": [
                true,
                true,
                false,
                true,
                true,
                [2, 5, 90],
                true,
                1,
            ],
        },
        {
            "class": Router,
            "cls_init_args": [2],
            "class_methods": ["addPacket", "forwardPacket", "forwardPacket"],
            "args": [[7, 4, 90], [], []],
            "expected": [true, [7, 4, 90], []],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from heapq import heappop, heappush
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        free = SortedList(range(len(times)))
        stimes = sorted((fr, to, i) for i, (fr, to) in enumerate(times))
        ends = []

        for fr, to, i in stimes:
            while ends and ends[0][0] <= fr:
                free.add(heappop(ends)[1])
            seat = free.pop(0)
            if i == targetFriend:
                return seat
            heappush(ends, (to, seat))


class Solution2:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        stimes = sorted((fr, to, i) for i, (fr, to) in enumerate(times))
        free, ends = [], []
        nxt = 0

        for fr, to, i in stimes:
            while ends and ends[0][0] <= fr:
                heappush(free, (heappop(ends)[1]))
            if free:
                seat = heappop(free)
            else:
                seat = nxt
                nxt += 1
            if i == targetFriend:
                return seat
            heappush(ends, (to, seat))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestChair"] * 2,
            "kwargs": [
                dict(times=[[1, 4], [2, 3], [4, 6]], targetFriend=1),
                dict(times=[[3, 10], [1, 5], [2, 6]], targetFriend=0),
            ],
            "expected": [1, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from heapq import heapify, heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = [(t, t, 2) for t in workerTimes]
        heapify(heap)
        for _ in range(mountainHeight):
            tt, t, r = heappop(heap)
            heappush(heap, (tt + t * r, t, r + 1))
        return tt


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minNumberOfSeconds"] * 3,
            "kwargs": [
                dict(mountainHeight = 4, workerTimes = [2,1,1]),
                dict(mountainHeight = 10, workerTimes = [3,2,2,4]),
                dict(mountainHeight = 5, workerTimes = [1]),
            ],
            "expected": [3, 12, 15],
        },
    ]


if __name__ == '__main__':
    unittest.main()

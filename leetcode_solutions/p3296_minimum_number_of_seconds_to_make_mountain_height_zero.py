import unittest
from heapq import heapify, heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        right = workerTimes[0] * mountainHeight * (mountainHeight + 1) // 2
        left = 1

        while left < right:
            mid = (left + right) // 2
            if (
                sum(
                    int((2 * mid / wt + 0.25) ** 0.5 - 0.5)
                    for wt in workerTimes
                )
                >= mountainHeight
            ):
                right = mid
            else:
                left = mid + 1

        return left


class Solution2:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        heap = [(t, t, 2) for t in workerTimes]
        heapify(heap)
        for _ in range(mountainHeight):
            tt, t, r = heappop(heap)
            heappush(heap, (tt + t * r, t, r + 1))
        return tt


class Solution3:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        heap = []

        for i, wt in enumerate(workerTimes):
            heappush(heap, (wt, i, 2))

        for _ in range(mountainHeight - 1):
            wt, i, k = heappop(heap)
            heappush(heap, (wt + workerTimes[i] * k, i, k + 1))

        return heap[0][0]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minNumberOfSeconds"] * 3,
            "kwargs": [
                dict(mountainHeight=4, workerTimes=[2, 1, 1]),
                dict(mountainHeight=10, workerTimes=[3, 2, 2, 4]),
                dict(mountainHeight=5, workerTimes=[1]),
            ],
            "expected": [3, 12, 15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

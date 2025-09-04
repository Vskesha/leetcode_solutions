import unittest
from heapq import heapify, heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heappop(heap)
            p += 1
            t += 1
            heappush(heap, (p / t - (p + 1) / (t + 1), p, t))

        avg = sum(p / t for _, p, t in heap) / len(classes)
        return avg


class Solution2:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        for pas, tot in classes:
            diff = pas / tot - (pas + 1) / (tot + 1)
            heappush(heap, (diff, pas, tot))

        for _ in range(extraStudents):
            _, pas, tot = heappop(heap)
            pas += 1
            tot += 1
            diff = pas / tot - (pas + 1) / (tot + 1)
            heappush(heap, (diff, pas, tot))

        return sum(pas / tot for _, pas, tot in heap) / len(heap)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxAverageRatio"] * 2,
            "kwargs": [
                dict(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2),
                dict(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4),
            ],
            "expected": [0.78333, 0.53485],
            "assert_methods": ["assertAlmostEqual5"] * 2,
        },
    ]

    def assertAlmostEqual5(self, actual, expected):
        self.assertAlmostEqual(actual, expected, places=5)


if __name__ == "__main__":
    unittest.main()

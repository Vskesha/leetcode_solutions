import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prow = points[0]

        for i in range(1, m):
            row = points[i]
            mr = prow.copy()
            for j in range(n - 2, -1, -1):
                mr[j] = max(mr[j], mr[j + 1] - 1)
            pm = 0
            for j in range(n):
                pm = max(prow[j], pm - 1)
                row[j] += max(mr[j], pm)
            prow = row
        return max(prow)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxPoints"] * 3,
            "kwargs": [
                dict(points=[[1, 2, 3], [1, 5, 1], [3, 1, 1]]),
                dict(points=[[1, 5], [2, 3], [4, 2]]),
                dict(
                    points=[
                        [4, 4, 2, 2, 1],
                        [5, 5, 2, 1, 2],
                        [3, 1, 5, 5, 2],
                        [3, 2, 0, 0, 3],
                    ]
                ),
            ],
            "expected": [9, 11, 15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

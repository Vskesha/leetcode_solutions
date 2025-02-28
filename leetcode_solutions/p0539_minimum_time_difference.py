import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        minutes.append(minutes[0] + 1440)
        return min(b - a for a, b in pairwise(minutes))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findMinDifference"] * 2,
            "kwargs": [
                dict(timePoints=["23:59", "00:00"]),
                dict(timePoints=["00:00", "23:59", "00:00"]),
            ],
            "expected": [1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

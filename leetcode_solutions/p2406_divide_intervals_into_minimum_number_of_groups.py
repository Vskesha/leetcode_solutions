import unittest
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ends = [inf]
        for fr, to in intervals:
            if ends[0] < fr:
                heappop(ends)
            heappush(ends, to)
        return len(ends) - 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minGroups"] * 2,
            "kwargs": [
                dict(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]),
                dict(intervals=[[1, 3], [5, 6], [8, 10], [11, 13]]),
            ],
            "expected": [3, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

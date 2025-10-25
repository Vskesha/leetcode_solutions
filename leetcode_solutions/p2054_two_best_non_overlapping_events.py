import unittest
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        ongoing, ended = [], [(0, 0)]
        ans = 0

        for st, end, val in events:
            heappush(ongoing, (end, val))
            while ongoing[0][0] < st:
                pend, pval = heappop(ongoing)
                heappush(ended, (-pval, pend))
            ans = max(ans, val - ended[0][0])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxTwoEvents"] * 3,
            "kwargs": [
                dict(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]),
                dict(events=[[1, 3, 2], [4, 5, 2], [1, 5, 5]]),
                dict(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]]),
            ],
            "expected": [4, 5, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()

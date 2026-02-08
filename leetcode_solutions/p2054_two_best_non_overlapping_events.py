import unittest
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ongoing = []

        ans = max(value for _, _, value in events)
        max_ended = 0
        events.sort(key=lambda x: x[0])

        for start, end, value in events:
            while ongoing and ongoing[0][0] < start:
                max_ended = max(max_ended, heappop(ongoing)[1])
            ans = max(ans, value + max_ended)
            heappush(ongoing, (end, value))

        return ans


class Solution2:
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

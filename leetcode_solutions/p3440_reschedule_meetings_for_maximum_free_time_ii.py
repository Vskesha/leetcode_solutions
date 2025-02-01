import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        gap = [startTime[0]]
        for i in range(1, n):
            gap.append(startTime[i] - endTime[i - 1])
        gap.append(eventTime - endTime[-1])
        dur = [b - a for a, b in zip(startTime, endTime)]

        ans = max(a + b for a, b in pairwise(gap))

        mg = 0
        for i in range(n):
            if dur[i] <= mg:
                ans = max(ans, gap[i] + dur[i] + gap[i + 1])
            mg = max(mg, gap[i])
        mg = 0
        for i in range(n - 1, -1, -1):
            if dur[i] <= mg:
                ans = max(ans, gap[i] + dur[i] + gap[i + 1])
            mg = max(mg, gap[i + 1])

        return ans
class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxFreeTime"] * 4,
            "kwargs": [
                dict(eventTime = 5, startTime = [1,3], endTime = [2,5]),
                dict(eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]),
                dict(eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]),
                dict(eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]),
            ],
            "expected": [2, 7, 6, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

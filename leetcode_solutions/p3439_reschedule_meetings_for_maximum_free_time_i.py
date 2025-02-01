import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        dur = [startTime[0]]
        for i in range(1, n):
            dur.append(startTime[i] - endTime[i - 1])
        dur.append(eventTime - endTime[-1])

        ws = 0
        for i in range(k):
            ws += dur[i]
        ans = 0
        for i, j in zip(range(k, n + 1), range(n + 1)):
            ws += dur[i]
            ans = max(ans, ws)
            ws -= dur[j]
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxFreeTime"] * 3,
            "kwargs": [
                dict(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]),
                dict(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]),
                dict(
                    eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]
                ),
            ],
            "expected": [2, 6, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

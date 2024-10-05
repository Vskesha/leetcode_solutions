import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [-inf] * 4
        for n in b:
            for i in range(3, 0, -1):
                dp[i] = max(dp[i], dp[i - 1] + n * a[i])
            dp[0] = max(dp[0], n * a[0])
        return dp[3]


class Solution2:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [-inf] * 5
        dp[0] = 0
        for n in b:
            for i in range(4, 0, -1):
                dp[i] = max(dp[i], dp[i - 1] + n * a[i - 1])
        return dp[4]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxScore"] * 2,
            "kwargs": [
                dict(a=[3, 2, 5, 6], b=[2, -6, 4, -5, -3, 2, -7]),
                dict(a=[-1, 4, 5, -2], b=[-5, -1, -3, -2, -4]),
            ],
            "expected": [26, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

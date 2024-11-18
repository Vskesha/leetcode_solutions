import unittest
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n

        for i in range(k - 1, -1, -1):
            ndp = [0] * n
            for curr in range(n):
                ndp[curr] = stayScore[i][curr] + dp[curr]
                for dest in range(n):
                    ndp[curr] = max(ndp[curr], travelScore[curr][dest] + dp[dest])
            dp = ndp

        return max(dp)


class Solution2:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        @cache
        def dp(curr, i) -> int:
            if i == k:
                return 0
            score = stayScore[i][curr] + dp(curr, i + 1)
            for dest in range(n):
                move = travelScore[curr][dest] + dp(dest, i + 1)
                score = max(score, move)
            return score

        return max(dp(curr, 0) for curr in range(n))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxScore"] * 2,
            "kwargs": [
                dict(n=2, k=1, stayScore=[[2, 3]], travelScore=[[0, 2], [1, 0]]),
                dict(n=3, k=2, stayScore=[[3, 4, 2], [2, 1, 2]], travelScore=[[0, 2, 1], [2, 0, 4], [3, 2, 0]]),
            ],
            "expected": [3, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()

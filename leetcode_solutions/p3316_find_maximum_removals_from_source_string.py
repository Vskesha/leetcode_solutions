import unittest
from functools import cache
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        ti = set(targetIndices)
        ls, lp = len(source), len(pattern)

        @cache
        def dp(i, j) -> int:
            if j == -1:
                return 0
            if i == -1:
                return inf
            if source[i] != pattern[j]:
                return dp(i - 1, j)
            if i not in ti:
                return dp(i - 1, j - 1)
            return min(dp(i - 1, j), dp(i - 1, j - 1) + 1)

        return len(ti) - dp(ls - 1, lp - 1)


class Solution1:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        ti = set(targetIndices)
        ls, lp = len(source), len(pattern)

        dp = [[0] * (lp + 1) for _ in range(ls + 1)]
        for j in range(lp):
            dp[-1][j] = inf

        for i in range(ls):
            for j in range(lp):
                if source[i] != pattern[j]:
                    dp[i][j] = dp[i - 1][j]
                elif i not in ti:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + 1)

        return len(ti) - dp[ls - 1][lp - 1]


class Solution2:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        ti = set(targetIndices)
        ls, lp = len(source), len(pattern)

        dp = [inf] * lp
        dp[0] = int(0 in ti) if source[0] == pattern[0] else inf

        for i in range(1, ls):
            ndp = [0] * lp
            for j in range(lp):
                prev = dp[j - 1] if j else 0
                if source[i] != pattern[j]:
                    ndp[j] = dp[j]
                elif i not in ti:
                    ndp[j] = prev
                else:
                    ndp[j] = min(dp[j], prev + 1)
            dp = ndp

        return len(ti) - dp[-1]


class Solution3:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        ti = set(targetIndices)
        ls, lp = len(source), len(pattern)

        dp = [[0] * (lp) for _ in range(ls)]
        dp[0][0] = int(0 in ti) if source[0] == pattern[0] else inf
        for j in range(1, lp):
            dp[0][j] = inf
        for i in range(1, ls):
            if source[i] != pattern[0]:
                dp[i][0] = dp[i - 1][0]
            elif i not in ti:
                dp[i][0] = 0
            else:
                dp[i][0] = min(dp[i - 1][0], 1)

        for i in range(1, ls):
            for j in range(1, lp):
                if source[i] != pattern[j]:
                    dp[i][j] = dp[i - 1][j]
                elif i not in ti:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + 1)

        return len(ti) - dp[-1][-1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxRemovals"] * 4,
            "kwargs": [
                dict(source="abbaa", pattern="aba", targetIndices=[0, 1, 2]),
                dict(source="bcda", pattern="d", targetIndices=[0, 3]),
                dict(source="dda", pattern="dda", targetIndices=[0, 1, 2]),
                dict(source="yeyeykyded", pattern="yeyyd", targetIndices=[0, 2, 3, 4]),
            ],
            "expected": [1, 2, 0, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

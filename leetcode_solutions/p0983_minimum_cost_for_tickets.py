import unittest
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ld = len(days)
        dp = [0] * (ld + 1)

        for di in range(ld - 1, -1, -1):
            d = days[di]
            ci = di + 1
            dp[di] = dp[ci] + costs[0]
            d += 7
            while ci < ld and days[ci] < d:
                ci += 1
            dp[di] = min(dp[di], dp[ci] + costs[1])
            d += 23
            while ci < ld and days[ci] < d:
                ci += 1
            dp[di] = min(dp[di], dp[ci] + costs[2])

        return dp[0]


class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ld = len(days)

        @cache
        def dp(di: int) -> int:
            if di == ld:
                return 0
            d = days[di]
            di += 1
            res1 = dp(di) + costs[0]
            d += 7
            while di < ld and days[di] < d:
                di += 1
            res7 = dp(di) + costs[1]
            d += 23
            while di < ld and days[di] < d:
                di += 1
            res30 = dp(di) + costs[2]
            ans = min(res1, res7, res30)
            return ans

        res = dp(0)
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["mincostTickets"] * 2,
            "kwargs": [
                dict(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]),
                dict(
                    days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
                    costs=[2, 7, 15],
                ),
            ],
            "expected": [11, 17],
        },
    ]


if __name__ == "__main__":
    unittest.main()

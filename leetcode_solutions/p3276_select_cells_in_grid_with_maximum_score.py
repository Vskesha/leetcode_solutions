import unittest
from collections import defaultdict
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid)
        mmask = 2**m - 1

        vals = defaultdict(set)
        for i, row in enumerate(grid):
            for v in row:
                vals[v].add(i)

        vkeys = sorted(vals.keys(), reverse=True)
        lvk = len(vkeys)

        @cache
        def dp(i, mask):
            if i == lvk:
                return 0
            if mask == mmask:
                return 0

            while i < len(vkeys):
                key = vkeys[i]
                taken = False
                ans = 0
                for r in vals[key]:
                    if mask & (1 << r):
                        continue
                    taken = True
                    curr = key + dp(i + 1, mask + (1 << r))
                    ans = max(ans, curr)
                if taken:
                    return ans
                else:
                    i += 1

            return 0

        return dp(0, 0)


class Solution2:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)

        vals = defaultdict(set)
        for i, row in enumerate(grid):
            for v in row:
                vals[v].add(i)

        dp = defaultdict(int, {0: 0})

        for v in sorted(vals)[::-1]:
            for mask in list(dp):
                sc = dp[mask] + v
                for r in vals[v]:
                    if not mask & (1 << r) and dp[mask + (1 << r)] < sc:
                        dp[mask + (1 << r)] = sc

        return max(dp.values())


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxScore"] * 2,
            "kwargs": [
                dict(grid=[[1, 2, 3], [4, 3, 2], [1, 1, 1]]),
                dict(grid=[[8, 7, 6], [8, 3, 2]]),
            ],
            "expected": [8, 15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

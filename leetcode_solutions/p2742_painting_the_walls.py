import unittest
from functools import lru_cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n - 1, -1, -1):
            new_dp = [0] * (n + 1)
            for rem in range(1, n + 1):
                new_dp[rem] = min(
                    dp[rem], dp[max(rem - time[i] - 1, 0)] + cost[i]
                )
            dp = new_dp

        return dp[n]


class Solution1:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[n] = [float("inf")] * (n + 1)
        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for rem in range(1, n + 1):
                paint = dp[i + 1][max(rem - time[i] - 1, 0)] + cost[i]
                notpaint = dp[i + 1][rem]
                dp[i][rem] = min(paint, notpaint)

        return dp[0][n]


class Solution2:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @lru_cache(None)
        def dp(i, rem):
            if rem <= 0:
                return 0
            if i == n:
                return float("inf")

            with_painter = dp(i + 1, rem - time[i] - 1) + cost[i]
            without_painter = dp(i + 1, rem)
            return min(with_painter, without_painter)

        return dp(0, n)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["paintWalls"] * 2,
            "kwargs": [
                dict(cost=[1, 2, 3, 2], time=[1, 2, 3, 2]),
                dict(cost=[2, 3, 4, 2], time=[1, 1, 1, 1]),
            ],
            "expected": [3, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print('Test 1 ... ', end='')
#     assert sol.paintWalls(cost=[1, 2, 3, 2], time=[1, 2, 3, 2]) == 3
#     print('ok')
#
#     print('Test 1 ... ', end='')
#     assert sol.paintWalls(cost=[2, 3, 4, 2], time=[1, 1, 1, 1]) == 4
#     print('ok')


# if __name__ == '__main__':
#     test()

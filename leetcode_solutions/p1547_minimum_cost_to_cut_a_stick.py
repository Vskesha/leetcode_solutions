import unittest
from functools import lru_cache
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted([0] + cuts + [n])
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for width in range(2, m):
            for left in range(0, m - width):
                right = left + width
                dp[left][right] = dp[left + 1][right]
                for mid in range(left + 2, right):
                    curr = dp[left][mid] + dp[mid][right]
                    dp[left][right] = min(dp[left][right], curr)
                dp[left][right] += cuts[right] - cuts[left]

        return dp[0][m - 1]


class Solution2:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache
        def cost(left, right):
            if right - left == 1:
                return 0
            min_cost = min(
                cost(left, mid) + cost(mid, right)
                for mid in range(left + 1, right)
            )
            return min_cost + cuts[right] - cuts[left]

        cuts = sorted([0] + cuts + [n])
        return cost(0, len(cuts) - 1)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_cost_1(self):
        print("Test minCost 1... ", end="")
        self.assertEqual(self.sol.minCost(n=7, cuts=[1, 3, 4, 5]), 16)
        print("OK")

    def test_min_cost_2(self):
        print("Test minCost 2... ", end="")
        self.assertEqual(self.sol.minCost(n=9, cuts=[5, 6, 1, 4, 2]), 22)
        print("OK")

    def test_min_cost_3(self):
        print("Test minCost 3... ", end="")
        self.assertEqual(self.sol.minCost(n=5, cuts=[3, 1, 4]), 10)
        print("OK")


if __name__ == "__main__":
    unittest.main()

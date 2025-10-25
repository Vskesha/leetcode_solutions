import unittest
from functools import cache
from typing import List


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        mod = 10**9 + 7
        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(minProfit)]

        for gr, pr in zip(group, profit):
            for p in range(minProfit, -1, -1):
                for g in range(n, gr - 1, -1):
                    dp[p][g] = (dp[p][g] + dp[max(0, p - pr)][g - gr]) % mod

        return dp[minProfit][n]


class Solution2:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        mod = 10**9 + 7

        @cache
        def dp(i, p, n):
            if n < 0:
                return 0
            if i == -1:
                if p > 0:
                    return 0
                else:
                    return 1
                # return 0 if p > 0 else 1
            ans = dp(i - 1, p - profit[i], n - group[i])
            ans = (ans + dp(i - 1, p, n)) % mod
            return ans

        return dp(len(profit) - 1, minProfit, n)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_profitable_schemes_1(self):
        print("Test profitableSchemes 1... ", end="")
        self.assertEqual(
            self.sol.profitableSchemes(
                n=5, minProfit=3, group=[2, 2], profit=[2, 3]
            ),
            2,
        )
        print("OK")

    def test_profitable_schemes_2(self):
        print("Test profitableSchemes 2... ", end="")
        self.assertEqual(
            self.sol.profitableSchemes(
                n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]
            ),
            7,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

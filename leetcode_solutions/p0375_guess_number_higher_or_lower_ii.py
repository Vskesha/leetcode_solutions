import unittest
from functools import cache
from math import inf


class Solution:
    def getMoneyAmount(self, n: int) -> int:

        @cache
        def dp(l, r) -> int:
            if l >= r:
                return 0
            ans = inf
            for m in range((l + r) // 2, r):
                res = max(dp(l, m - 1), dp(m + 1, r))
                ans = min(ans, res + m)
            return ans

        return dp(1, n)


class Solution2:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(l, r) -> int:
            if l >= r:
                return 0
            ans = inf
            for m in range(l, r + 1):
                res = max(dp(l, m - 1), dp(m + 1, r))
                ans = min(ans, res + m)
            return ans

        return dp(1, n)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_getMoneyAmount_1(self):
        print("Test getMoneyAmount 1... ", end="")
        self.assertEqual(16, self.sol.getMoneyAmount(n=10))
        print("OK")

    def test_getMoneyAmount_2(self):
        print("Test getMoneyAmount 2... ", end="")
        self.assertEqual(0, self.sol.getMoneyAmount(n=1))
        print("OK")

    def test_getMoneyAmount_3(self):
        print("Test getMoneyAmount 3... ", end="")
        self.assertEqual(1, self.sol.getMoneyAmount(n=2))
        print("OK")


if __name__ == "__main__":
    unittest.main()

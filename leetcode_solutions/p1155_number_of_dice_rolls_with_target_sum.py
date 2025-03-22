import unittest
from functools import cache, lru_cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(n, k, target):
            if n > target or n * k < target:
                return 0
            if n == target or n * k == target:
                return 1
            if n == 1:
                return 0 if target > k else 1
            ans = 0
            for ck in range(1, k + 1):
                ans = (ans + dp(n - 1, k, target - ck)) % mod
            return ans

        return dp(n, k, target)


class Solution0:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dp(n, target):
            if n == target or target == n * k:
                return 1
            if target < n or target > n * k:
                return 0
            res = 0
            for i in range(1, k + 1):
                res += dp(n - 1, target - i)
                res %= mod
            return res

        return dp(n, target)


class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dp(n, target):
            if n == target or target == n * k:
                return 1
            if target < n or target > n * k:
                return 0
            res = 0
            for i in range(1, k + 1):
                res = (res + dp(n - 1, target - i)) % mod
            return res

        return dp(n, target)


class Solution2:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(n, t):
            if t <= 0:
                return 0
            if n == 1:
                return 0 if t > k else 1
            ans = 0
            for i in range(1, k + 1):
                ans = (ans + dp(n - 1, t - i)) % MOD
            return ans

        return dp(n, target)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numRollsToTarget_1(self):
        print("Test numRollsToTarget 1 ... ", end="")
        self.assertEqual(1, self.sol.numRollsToTarget(n=1, k=6, target=3))
        print("OK")

    def test_numRollsToTarget_2(self):
        print("Test numRollsToTarget 2 ... ", end="")
        self.assertEqual(6, self.sol.numRollsToTarget(n=2, k=6, target=7))
        print("OK")

    def test_numRollsToTarget_3(self):
        print("Test numRollsToTarget 3 ... ", end="")
        self.assertEqual(222616187, self.sol.numRollsToTarget(n=30, k=30, target=500))
        print("OK")


if __name__ == "__main__":
    unittest.main()

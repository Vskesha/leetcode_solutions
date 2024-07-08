import unittest
from functools import lru_cache
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(n + m - 2, n - 1)


# recursive dp solution
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        s = m + n - 1
        res = 1
        for i in range(1, min(m, n)):
            res = res * (s - i) // i
        return res


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dp(m, n):
            if not (m and n):
                return 1
            return dp(m - 1, n) + dp(m, n - 1)

        return dp(m - 1, n - 1)


# iterative dp solution
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_unique_paths_1(self):
        print("Test uniquePaths 1... ", end="")
        self.assertEqual(self.sol.uniquePaths(m=3, n=7), 28)
        print("OK")

    def test_unique_paths_2(self):
        print("Test uniquePaths 2... ", end="")
        self.assertEqual(self.sol.uniquePaths(m=3, n=2), 3)
        print("OK")


if __name__ == "__main__":
    unittest.main()

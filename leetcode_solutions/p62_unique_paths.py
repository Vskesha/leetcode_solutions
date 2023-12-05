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


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.uniquePaths(m=3, n=7) == 28
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.uniquePaths(m=3, n=2) == 3
    print('ok')


if __name__ == '__main__':
    test()

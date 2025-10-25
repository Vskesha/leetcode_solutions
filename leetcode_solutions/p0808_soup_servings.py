from collections import defaultdict
from functools import lru_cache


# recursive solution
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4500:
            return 1

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (
                dp(a - 100, b)
                + dp(a - 75, b - 25)
                + dp(a - 50, b - 50)
                + dp(a - 25, b - 75)
            ) / 4

        return dp(n, n)


# iterative solution
class Solution2:
    def soupServings(self, n: int) -> float:
        if n > 4500:
            return 1

        m = (n - 1) // 25 + 2
        dp = defaultdict(dict)

        for i in range(4):
            for j in range(3):
                dp[-i][-j] = 0.5

        for i in range(1, m):
            dp[i][0] = dp[i][-1] = dp[i][-2] = 0
            dp[0][i] = dp[-1][i] = dp[-2][i] = dp[-3][i] = 1
            for j in range(1, i + 1):
                dp[i][j] = (
                    dp[i - 4][j]
                    + dp[i - 3][j - 1]
                    + dp[i - 2][j - 2]
                    + dp[i - 1][j - 3]
                ) / 4
                dp[j][i] = (
                    dp[j - 4][i]
                    + dp[j - 3][i - 1]
                    + dp[j - 2][i - 2]
                    + dp[j - 1][i - 3]
                ) / 4
        return dp[m - 1][m - 1]


def main():
    sol = Solution()
    print("0.62500 ===", sol.soupServings(n=50))
    print("0.71875 ===", sol.soupServings(n=100))
    print("??????? ===", sol.soupServings(n=4500))


if __name__ == "__main__":
    main()

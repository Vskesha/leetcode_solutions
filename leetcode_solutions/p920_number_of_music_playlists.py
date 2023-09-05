from functools import lru_cache


# recursive solution
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dp(i, j):
            if not (i or j):
                return 1
            if not j or not i:
                return 0
            ans = dp(i - 1, j - 1) * (n - j + 1)
            if j > k:
                ans += dp(i - 1, j) * (j - k)
            return ans % mod

        return dp(goal, n)


#iterative solution
class Solution2:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 1_000_000_007
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j - 1] * (n - j + 1) % mod
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                dp[i][j] %= mod

        return dp[goal][n]


def main():
    sol = Solution()
    print('6 ===', sol.numMusicPlaylists(n=3, goal=3, k=1))
    print('6 ===', sol.numMusicPlaylists(n=2, goal=3, k=0))
    print('2 ===', sol.numMusicPlaylists(n=2, goal=3, k=1))


if __name__ == '__main__':
    main()

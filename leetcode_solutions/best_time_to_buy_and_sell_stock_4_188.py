class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if k == 0:
            return 0

        dp = [[1000, 0] for _ in range(k + 1)]

        for price in prices:
            for i in range(1, k + 1):
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                dp[i][1] = max(dp[i][1], price - dp[i][0])

        return dp[k][1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))

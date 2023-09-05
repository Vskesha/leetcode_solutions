from functools import lru_cache


# recursive dp solution
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if not (i or j):
                return 1
            return dp(i - 1, j) + dp(i, j - 1)

        return dp(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
# iterative dp solution
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            if obstacleGrid[i][0]:
                break
            else:
                dp[i][0] = 1

        for j in range(m):
            if obstacleGrid[0][j]:
                break
            else:
                dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


def main():
    sol = Solution()
    print('2 ===', sol.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print('1 ===', sol.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))


if __name__ == '__main__':
    main()

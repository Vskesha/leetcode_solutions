import unittest
from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1

        for i, row in enumerate(obstacleGrid):
            if row[0]:
                dp[0] = 0
            for j in range(1, n):
                if row[j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]
        return dp[-1]


class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        obstacleGrid[0][0] = 1
        for i, row in enumerate(obstacleGrid):
            for j, obs in enumerate(row):
                if obs:
                    if i or j:
                        obstacleGrid[i][j] = 0
                else:
                    if i:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if j:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]


# recursive dp solution
class Solution2:
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
class Solution3:
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


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_unique_path_with_obstacles_1(self):
        print("Test uniquePathsWithObstacles 1... ", end="")
        self.assertEqual(
            self.sol.uniquePathsWithObstacles(
                obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            ),
            2,
        )
        print("OK")

    def test_unique_path_with_obstacles_2(self):
        print("Test uniquePathsWithObstacles 2... ", end="")
        self.assertEqual(
            self.sol.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]), 1
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

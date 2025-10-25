import unittest
from functools import cache
from math import inf
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        prev = [0] * n
        for row in matrix:
            row[0] += min(prev[:2])
            for j in range(1, n - 1):
                row[j] += min(prev[j - 1 : j + 2])
            row[-1] += min(prev[-2:])
            prev = row
        return min(prev)


class Solution0:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            matrix[i][0] += min(matrix[i - 1][:2])
            for j in range(1, n - 1):
                matrix[i][j] += min(matrix[i - 1][j - 1 : j + 2])
            matrix[i][-1] += min(matrix[i - 1][-2:])

        return min(matrix[-1])


class Solution1:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        dp = [0] * n

        for row in matrix:
            ndp = []
            ndp.append(min(dp[:2]) + row[0])
            for j in range(1, n - 1):
                ndp.append(min(dp[j - 1 : j + 2]) + row[j])
            ndp.append(min(dp[-2:]) + row[-1])
            dp = ndp
        return min(dp)


class Solution2:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @cache
        def dp(i, j):
            if j == -1 or j == n:
                return inf
            if i == m:
                return 0
            return (
                min(dp(i + 1, dj) for dj in range(j - 1, j + 2)) + matrix[i][j]
            )

        return min(dp(0, j) for j in range(n))


class Solution3:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1, n):
            matrix[i][0] += min(matrix[i - 1][:2])
            for j in range(1, n):
                matrix[i][j] += min(matrix[i - 1][j - 1 : j + 2])

        return min(matrix[-1])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_falling_path_sum_1(self):
        print("Test minFallingPathSum 1... ", end="")
        self.assertEqual(
            self.sol.minFallingPathSum(
                matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]
            ),
            13,
        )
        print("OK")

    def test_min_falling_path_sum_2(self):
        print("Test minFallingPathSum 2... ", end="")
        self.assertEqual(
            self.sol.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]), -59
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

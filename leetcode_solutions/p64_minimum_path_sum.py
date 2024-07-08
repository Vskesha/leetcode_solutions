import unittest
from itertools import accumulate
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid[0] = list(accumulate(grid[0]))
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_path_sum_1(self):
        print("Test minPathSum 1... ", end="")
        self.assertEqual(self.sol.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        print("OK")

    def test_min_path_sum_2(self):
        print("Test minPathSum 2... ", end="")
        self.assertEqual(self.sol.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]), 12)
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        n3 = n * 3
        g = [[1] * n3 for _ in range(n3)]

        for i in range(0, n3, 3):
            for j in range(0, n3, 3):
                ch = grid[i // 3][j // 3]
                if ch == "/":
                    g[i][j + 2] = g[i + 1][j + 1] = g[i + 2][j] = 0
                elif ch == "\\":
                    g[i][j] = g[i + 1][j + 1] = g[i + 2][j + 2] = 0

        def dfs(i, j):
            if i == -1 or j == -1 or i == n3 or j == n3 or g[i][j] == 0:
                return
            g[i][j] = 0
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                dfs(ni, nj)

        ans = 0
        for i in range(n3):
            for j in range(n3):
                if g[i][j]:
                    dfs(i, j)
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_regions_by_slashes1(self):
        print("Test regionsBySlashes 1 ... ", end="")
        self.assertEqual(self.sol.regionsBySlashes(grid=[" /", "/ "]), 2)
        print("OK")

    def test_regions_by_slashes2(self):
        print("Test regionsBySlashes 2 ... ", end="")
        self.assertEqual(self.sol.regionsBySlashes(grid=[" /", "  "]), 1)
        print("OK")

    def test_regions_by_slashes3(self):
        print("Test regionsBySlashes 3 ... ", end="")
        self.assertEqual(self.sol.regionsBySlashes(grid=["/\\", "\\/"]), 5)
        print("OK")


if __name__ == "__main__":
    unittest.main()

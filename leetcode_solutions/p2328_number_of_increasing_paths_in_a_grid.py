import unittest
from functools import cache
from itertools import pairwise
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]

        @cache
        def dfs(i, j) -> int:
            ans = 1
            for di, dj in pairwise(dirs):
                di, dj = di + i, dj + j
                if 0 <= di < m and 0 <= dj < n:
                    if grid[i][j] > grid[di][dj]:
                        ans = (ans + dfs(di, dj)) % mod

            return ans

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod


class Solution2:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(grid)
        m = len(grid[0])

        aux = [[1] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        def dfs(i, j) -> int:
            if not visited[i][j]:
                for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                    if 0 <= y < n and 0 <= x < m and grid[i][j] > grid[y][x]:
                        aux[i][j] += dfs(y, x) % mod
                visited[i][j] = True
            return aux[i][j]

        return sum(dfs(i, j) for i in range(n) for j in range(m)) % mod


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_count_paths_1(self):
        print("Test countPaths 1... ", end="")
        self.assertEqual(self.sol.countPaths(grid=[[1, 1], [3, 4]]), 8)
        print("OK")

    def test_count_paths_2(self):
        print("Test countPaths 2... ", end="")
        self.assertEqual(self.sol.countPaths(grid=[[1], [2]]), 3)
        print("OK")


if __name__ == "__main__":
    unittest.main()

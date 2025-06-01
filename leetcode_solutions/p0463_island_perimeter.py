import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def islandPerimeter(self, grid):
        row = len(grid)
        col = len(grid[0])
        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if not (i and grid[i - 1][j]):
                        ans += 2
                    if not (j and grid[i][j - 1]):
                        ans += 2

        return ans


class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def borders(i, j):
            return (
                (i == 0 or grid[i - 1][j] == 0)
                + (j == 0 or grid[i][j - 1] == 0)
                + (i == m - 1 or grid[i + 1][j] == 0)
                + (j == n - 1 or grid[i][j + 1] == 0)
            )

        res = 0

        for i, row in enumerate(grid):
            for j, is_land in enumerate(row):
                if is_land:
                    res += borders(i, j)

        return res


class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def borders(i, j):
            ans = 0
            if i == 0 or grid[i - 1][j] == 0:
                ans += 1
            if j == 0 or grid[i][j - 1] == 0:
                ans += 1
            if i == m - 1 or grid[i + 1][j] == 0:
                ans += 1
            if j == n - 1 or grid[i][j + 1] == 0:
                ans += 1
            return ans

        res = 0
        for i, row in enumerate(grid):
            for j, is_land in enumerate(row):
                if is_land:
                    res += borders(i, j)

        return res


class Solution3:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 2 if grid[0][0] == 1 else 0

        for i in range(1, m):
            ans += grid[i][0]
            ans += grid[i][0] != grid[i - 1][0]

        for j in range(1, n):
            ans += grid[0][j]
            ans += grid[0][j] != grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                ans += grid[i][j] != grid[i - 1][j]
                ans += grid[i][j] != grid[i][j - 1]

        for i in range(m):
            ans += grid[i][n - 1]

        for j in range(n):
            ans += grid[m - 1][j]

        return ans


class Solution4:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        perimetr = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue

                bfs = deque([(i, j)])
                visited[i][j] = True
                while bfs:
                    i, j = bfs.popleft()
                    for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                            if not visited[ni][nj]:
                                visited[ni][nj] = True
                                bfs.append((ni, nj))
                        else:
                            perimetr += 1

                return perimetr


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["islandPerimeter"] * 3,
            "kwargs": [
                dict(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]),
                dict(grid=[[1]]),
                dict(grid=[[1, 0]]),
            ],
            "expected": [16, 4, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test_island_perimeter():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert (
#         sol.islandPerimeter(
#             grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
#         )
#         == 16
#     )
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.islandPerimeter(grid=[[1]]) == 4
#     print("OK")
#
#     print("Test 3... ", end="")
#     assert sol.islandPerimeter(grid=[[1, 0]]) == 4
#     print("OK")


# if __name__ == "__main__":
#     test_island_perimeter()

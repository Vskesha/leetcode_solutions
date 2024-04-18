from typing import List


class Solution:
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


def test_island_perimeter():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.islandPerimeter(
            grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        )
        == 16
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.islandPerimeter(grid=[[1]]) == 4
    print("OK")

    print("Test 3... ", end="")
    assert sol.islandPerimeter(grid=[[1, 0]]) == 4
    print("OK")


if __name__ == "__main__":
    test_island_perimeter()

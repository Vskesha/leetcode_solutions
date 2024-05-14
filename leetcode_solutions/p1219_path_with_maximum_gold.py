from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neibs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j) -> int:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            res = max(dfs(i + di, j + dj) for di, dj in neibs) + val
            grid[i][j] = val
            return res

        res = 0
        tot = sum(sum(row) for row in grid)
        for i in range(m):
            for j in range(n):
                nn = sum(
                    0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] != 0
                    for di, dj in neibs
                )
                if nn < 3:
                    res = max(res, dfs(i, j))
                    if res == tot:
                        return res

        return res


class Solution2:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neibs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j) -> int:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            res = max(dfs(i + di, j + dj) for di, dj in neibs) + val
            grid[i][j] = val
            return res

        return max(dfs(i, j) for i in range(m) for j in range(n))


def test_get_maximum_gold():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]) == 24
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.getMaximumGold(
            grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        )
        == 28
    )
    print("OK")


if __name__ == "__main__":
    test_get_maximum_gold()

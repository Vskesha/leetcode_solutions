from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mr = [max(row) for row in grid]
        mc = [max(grid[i][j] for i in range(n)) for j in range(n)]
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(mr[i], mc[j]) - grid[i][j]
        return ans


class Solution2:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mr, mc = [0] * n, [0] * n
        for i, row in enumerate(grid):
            for j, b in enumerate(row):
                mr[i] = max(mr[i], b)
                mc[j] = max(mc[j], b)

        ans = 0
        for i, row in enumerate(grid):
            mri = mr[i]
            for j, b in enumerate(row):
                ans += min(mri, mc[j]) - b
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.maxIncreaseKeepingSkyline(
            grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        )
        == 35
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.maxIncreaseKeepingSkyline(grid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        == 0
    )
    print("OK")


if __name__ == "__main__":
    test()

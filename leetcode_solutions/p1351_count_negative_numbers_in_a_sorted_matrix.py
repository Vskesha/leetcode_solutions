from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = cols = len(grid[0])
        ans = 0
        for row in grid:
            l = 0
            while l < r:
                m = (l + r) // 2
                if row[m] < 0:
                    r = m
                else:
                    l = m + 1
            ans += cols - r
        return ans


class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        j = m = len(grid[0]) - 1
        ans = 0
        for row in grid:
            while j >= 0 and row[j] < 0:
                j -= 1
            ans += m - j
        return ans


class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        res = 0
        for i in range(h):
            j = w
            while j > 0 and grid[i][j - 1] < 0:
                j -= 1
            res += (w - j) * (h - i)
            w = j
            if not w:
                break
        return res


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.countNegatives(
            grid=[
                [4, 3, 2, -1],
                [3, 2, 1, -1],
                [1, 1, -1, -2],
                [-1, -1, -2, -3],
            ]
        )
        == 8
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.countNegatives(grid=[[3, 2], [1, 0]]) == 0
    print("OK")


if __name__ == "__main__":
    test()

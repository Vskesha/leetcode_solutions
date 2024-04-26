from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        def two_smallest(arr: list):
            s = ss = float("inf")
            for num in arr:
                if num < s:
                    s, ss = num, s
                elif num < ss:
                    ss = num
            return s, ss

        for i in range(1, n):
            s, ss = two_smallest(grid[i - 1])
            for j in range(n):
                grid[i][j] += ss if grid[i - 1][j] == s else s

        return min(grid[-1])


def test_min_falling_path_sum():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
    print("OK")

    print("Test 2... ", end="")
    assert sol.minFallingPathSum(grid=[[7]]) == 7
    print("OK")


if __name__ == "__main__":
    test_min_falling_path_sum()

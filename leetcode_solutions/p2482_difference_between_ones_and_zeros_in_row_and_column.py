from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid[0]), len(grid)
        mn = m + n
        r = [sum(row) for row in grid]
        c = [sum(col) for col in zip(*grid)]
        return [[(r[i] + c[j]) * 2 - mn for j in range(m)] for i in range(n)]


class Solution2:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid[0]), len(grid)
        mn = m + n
        rows, cols = [0] * n, [0] * m
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                rows[i] += el
                cols[j] += el

        diffs = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                diffs[i][j] = (rows[i] + cols[j]) * 2 - mn

        return diffs


def test():
    sol = Solution()

    print("Test 1... ", end="")
    for a, b in zip(
        sol.onesMinusZeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]]),
        [[0, 0, 4], [0, 0, 4], [-2, -2, 2]],
    ):
        assert a == b
    print("OK")

    print("Test 2... ", end="")
    for a, b in zip(
        sol.onesMinusZeros(grid=[[1, 1, 1], [1, 1, 1]]), [[5, 5, 5], [5, 5, 5]]
    ):
        assert a == b
    print("OK")


if __name__ == "__main__":
    test()

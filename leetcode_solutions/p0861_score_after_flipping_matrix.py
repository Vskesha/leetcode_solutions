from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        tot = [0] * n
        for row in grid:
            if row[0]:
                for j in range(n):
                    tot[j] += row[j]
            else:
                for j in range(n):
                    tot[j] += 1 - row[j]

        res = 0
        pow2 = 1
        for val in reversed(tot):
            val = max(val, m - val)
            res += val * pow2
            pow2 *= 2

        return res


class Solution2:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        tot = [0] * n
        for row in grid:
            first = row[0]
            for j, val in enumerate(row):
                tot[j] += val if first else not val
        return sum(max(val, m - val) * 2 ** (n - i - 1) for i, val in enumerate(tot))


class Solution3:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return sum(max(val, m - val) * 2 ** (n - i - 1) for i, val in
                   enumerate([sum(row[j] if row[0] else not row[j] for row in grid) for j in range(n)]))


def test_matrix_score():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39
    print("OK")

    print("Test 2... ", end="")
    assert sol.matrixScore(grid=[[0]]) == 1
    print("OK")


if __name__ == "__main__":
    test_matrix_score()

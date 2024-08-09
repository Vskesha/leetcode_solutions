import unittest
from itertools import product
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        dirs = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0))
        seq = "2943816729438167 7618349276183492"
        ans = 0

        for i, j in product(range(len(grid) - 2), range(len(grid[0]) - 2)):
            if grid[i + 1][j + 1] == 5 and grid[i][j + 1] % 2:
                ans += "".join(str(grid[i + di][j + dj]) for di, dj in dirs) in seq

        return ans


class Solution1:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 2, len(grid[0]) - 2
        ans = 0

        for i in range(m):
            for j in range(n):
                vals = {grid[i + di][j + dj] for di in range(3) for dj in range(3)}
                if len(vals) < 9 or any((v > 9) or (v < 1) for v in vals):
                    continue
                sm = sum(grid[i][j : j + 3])
                if (
                    sum(grid[i + 1][j : j + 3]) == sm
                    and sum(grid[i + 2][j : j + 3]) == sm
                    and sum(grid[di][j] for di in range(i, i + 3)) == sm
                    and sum(grid[di][j + 1] for di in range(i, i + 3)) == sm
                    and sum(grid[di][j + 2] for di in range(i, i + 3)) == sm
                    and sum(grid[i + dij][j + dij] for dij in range(3)) == sm
                    and sum(grid[i + dij][j + 2 - dij] for dij in range(3)) == sm
                ):
                    ans += 1

        return ans


class Solution2:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 2, len(grid[0]) - 2
        ans = 0

        for i, j in product(range(m), range(n)):
            vals, rs, cs = set(), [0] * 3, [0] * 3

            for di, dj in product(range(3), repeat=2):
                v = grid[i + di][j + dj]
                if v < 1 or v > 9 or v in vals:
                    break
                vals.add(v)
                rs[di] += v
                cs[dj] += v
            else:
                d1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                d2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
                if (
                    d1 == d2
                    and rs[0] == rs[1] == rs[2]
                    and cs[0] == cs[1] == cs[2]
                    and rs[0] == cs[0] == d1
                ):
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_numMagicSquaresInside_1(self):
        print("Test numMagicSquaresInside 1... ", end="")
        self.assertEqual(
            self.sol.numMagicSquaresInside(
                grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
            ),
            1,
        )
        print("OK")

    def test_numMagicSquaresInside_2(self):
        print("Test numMagicSquaresInside 2... ", end="")
        self.assertEqual(self.sol.numMagicSquaresInside(grid=[[8]]), 0)
        print("OK")

    def test_numMagicSquaresInside_3(self):
        print("Test numMagicSquaresInside 3... ", end="")
        self.assertEqual(
            self.sol.numMagicSquaresInside(
                grid=[
                    [3, 2, 9, 2, 7],
                    [6, 1, 8, 4, 2],
                    [7, 5, 3, 2, 7],
                    [2, 9, 4, 9, 6],
                    [4, 3, 8, 2, 5],
                ]
            ),
            1,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

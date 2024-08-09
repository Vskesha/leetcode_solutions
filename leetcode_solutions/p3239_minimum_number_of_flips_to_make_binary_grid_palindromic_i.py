import unittest
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        return min(
            sum(row[i] != row[~i] for row in grid for i in range(len(grid[0]) // 2)),
            sum(col[i] != col[~i] for col in zip(*grid) for i in range(len(grid) // 2)),
        )


class Solution2:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rans = 0

        for row in grid:
            for i in range(n // 2):
                if row[i] != row[~i]:
                    rans += 1

        cans = 0
        for col in zip(*grid):
            for i in range(m // 2):
                if col[i] != col[~i]:
                    cans += 1

        return min(rans, cans)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minFlips_1(self):
        print("Test minFlips 1... ", end="")
        self.assertEqual(2, self.sol.minFlips(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
        print("OK")

    def test_minFlips_2(self):
        print("Test minFlips 2... ", end="")
        self.assertEqual(1, self.sol.minFlips(grid=[[0, 1], [0, 1], [0, 0]]))
        print("OK")

    def test_minFlips_3(self):
        print("Test minFlips 3... ", end="")
        self.assertEqual(0, self.sol.minFlips(grid=[[1], [0]]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from itertools import pairwise
from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        r, c, n, sp = rStart, cStart, rows * cols, 2
        dirs = (1, 0, -1, 0, 1)
        ans = [[rStart, cStart]]

        while len(ans) < n:
            c += 1
            r -= 1
            for dr, dc in pairwise(dirs):
                for _ in range(sp):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
            sp += 2

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameCoords(
        self, coords1: List[List[int]], coords2: List[List[int]]
    ) -> None:
        self.assertEqual(len(coords1), len(coords2))
        for coord1, coord2 in zip(coords1, coords2):
            self.assertListEqual(coord1, coord2)

    def test_spiralMatrixIII_1(self):
        print("Test spiralMatrixIII 1... ", end="")
        self.assertSameCoords(
            self.sol.spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0),
            [[0, 0], [0, 1], [0, 2], [0, 3]],
        )
        print("OK")

    def test_spiralMatrixIII_2(self):
        print("Test spiralMatrixIII 2... ", end="")
        self.assertSameCoords(
            self.sol.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4),
            [
                [1, 4],
                [1, 5],
                [2, 5],
                [2, 4],
                [2, 3],
                [1, 3],
                [0, 3],
                [0, 4],
                [0, 5],
                [3, 5],
                [3, 4],
                [3, 3],
                [3, 2],
                [2, 2],
                [1, 2],
                [0, 2],
                [4, 5],
                [4, 4],
                [4, 3],
                [4, 2],
                [4, 1],
                [3, 1],
                [2, 1],
                [1, 1],
                [0, 1],
                [4, 0],
                [3, 0],
                [2, 0],
                [1, 0],
                [0, 0],
            ],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

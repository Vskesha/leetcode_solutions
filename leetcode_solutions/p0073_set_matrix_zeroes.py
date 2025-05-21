import unittest
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zrows = set()
        zcols = set()
        m, n = len(matrix), len(matrix[0])

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if not val:
                    zrows.add(i)
                    zcols.add(j)

        for i in zrows:
            for j in range(n):
                matrix[i][j] = 0

        for j in zcols:
            for i in range(m):
                matrix[i][j] = 0


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_setZeroes_1(self):
        print("Test 1. Solution.setZeroes ... ", end="")
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.solution.setZeroes(matrix)
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        for row1, row2 in zip(matrix, expected):
            self.assertListEqual(row1, row2)
        print("OK")

    def test_setZeroes_2(self):
        print("Test 2. Solution.setZeroes ... ", end="")
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        self.solution.setZeroes(matrix)
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        for row1, row2 in zip(matrix, expected):
            self.assertListEqual(row1, row2)
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix[0])
        n = len(matrix)

        for i in range(n):
            curr = matrix[i][0]
            y, x = i + 1, 1
            while y < n and x < m:
                if matrix[y][x] != curr:
                    return False
                y += 1
                x += 1

        for j in range(1, m):
            curr = matrix[0][j]
            y, x = 1, j + 1
            while y < n and x < m:
                if matrix[y][x] != curr:
                    return False
                y += 1
                x += 1

        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_toeplitz_matrix_1(self):
        print('Test isToeplitzMatrix 1... ', end='')
        self.assertTrue(self.sol.isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
        print('OK')

    def test_is_toeplitz_matrix_2(self):
        print('Test isToeplitzMatrix 2... ', end='')
        self.assertFalse(self.sol.isToeplitzMatrix(matrix=[[1, 2], [2, 2]]))
        print('OK')


if __name__ == '__main__':
    unittest.main()

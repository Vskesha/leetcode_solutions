import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n

        while i < m and j > 0:
            if matrix[i][j - 1] > target:
                j -= 1
            elif matrix[i][j - 1] == target:
                return True
            else:
                i += 1

        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        j = n

        for i in range(m):
            j = bisect_left(matrix[i], target, hi=j)
            if j < n and matrix[i][j] == target:
                return True
        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_search_matrix1(self):
        print("Test searchMatrix 1 ... ", end="")
        self.assertTrue(
            self.sol.searchMatrix(
                matrix=[
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                target=5,
            )
        )
        print("OK")

    def test_search_matrix2(self):
        print("Test searchMatrix 2 ... ", end="")
        self.assertFalse(
            self.sol.searchMatrix(
                matrix=[
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                target=20,
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

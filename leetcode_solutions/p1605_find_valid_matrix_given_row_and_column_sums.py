import unittest
from typing import List


class Solution:
    def restoreMatrix(
        self, rowSum: List[int], colSum: List[int]
    ) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        grid = [[0] * n for _ in range(m)]
        r = c = 0

        while r < m and c < n:
            if rowSum[r] > colSum[c]:
                grid[r][c] = colSum[c]
                rowSum[r] -= colSum[c]
                c += 1
            else:
                grid[r][c] = rowSum[r]
                colSum[c] -= rowSum[r]
                r += 1

        return grid


class Solution1:
    def restoreMatrix(
        self, rowSum: List[int], colSum: List[int]
    ) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        grid = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                grid[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= grid[r][c]
                colSum[c] -= grid[r][c]

        return grid


class Solution2:
    def restoreMatrix(
        self, rowSum: List[int], colSum: List[int]
    ) -> List[List[int]]:
        m = len(colSum)
        n = len(rowSum)
        mat = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            if rowSum[i] < colSum[j]:
                mat[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i += 1
            else:
                mat[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j += 1

        return mat


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertRowColumnSumEqual(
        self,
        matrix: List[List[int]],
        rowSum: List[int],
        colSum: List[int],
    ):
        self.assertListEqual(rowSum, [sum(row) for row in matrix])
        self.assertListEqual(colSum, [sum(col) for col in zip(*matrix)])

    def test_restoreMatrix_1(self):
        print("Test restoreMatrix 1... ", end="")
        rowSum = [3, 8]
        colSum = [4, 7]
        rowSumCopy, colSumCopy = rowSum.copy(), colSum.copy()
        matrix = self.sol.restoreMatrix(rowSum, colSum)
        self.assertRowColumnSumEqual(matrix, rowSumCopy, colSumCopy)
        print("OK")

    def test_restoreMatrix_2(self):
        print("Test restoreMatrix 2... ", end="")
        rowSum = [5, 7, 10]
        colSum = [8, 6, 8]
        rowSumCopy, colSumCopy = rowSum.copy(), colSum.copy()
        matrix = self.sol.restoreMatrix(rowSum, colSum)
        self.assertRowColumnSumEqual(matrix, rowSumCopy, colSumCopy)
        print("OK")


if __name__ == "__main__":
    unittest.main()

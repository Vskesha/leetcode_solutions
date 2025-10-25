import unittest
from typing import List


class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> List[List[int]]:

        def get_indexes(conditions, k):
            income = [0] * (k + 1)
            adj = [[] for _ in range(k + 1)]
            for a, b in conditions:
                adj[a].append(b)
                income[b] += 1
            row_order = [i for i in range(1, k + 1) if not income[i]]
            i = 0
            while i < len(row_order):
                curr = row_order[i]
                for neib in adj[curr]:
                    income[neib] -= 1
                    if not income[neib]:
                        row_order.append(neib)
                i += 1
            if len(row_order) != k:
                return None
            return {n: i for i, n in enumerate(row_order)}

        row_indexes = get_indexes(rowConditions, k)
        if not row_indexes:
            return []
        col_indexes = get_indexes(colConditions, k)
        if not col_indexes:
            return []

        matrix = [[0] * k for _ in range(k)]
        for n in range(1, k + 1):
            matrix[row_indexes[n]][col_indexes[n]] = n

        return matrix


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertMatrixSatisfiesConditions(
        self,
        matrix: List[List[int]],
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> None:
        lm = len(matrix)
        rindex = {
            matrix[i][j]: i
            for i in range(lm)
            for j in range(lm)
            if matrix[i][j]
        }
        cindex = {
            matrix[i][j]: j
            for i in range(lm)
            for j in range(lm)
            if matrix[i][j]
        }
        for a, b in rowConditions:
            self.assertLess(rindex[a], rindex[b])
        for a, b in colConditions:
            self.assertLess(cindex[a], cindex[b])

    def test_buildMatrix_1(self):
        print("Test buildMatrix 1... ", end="")
        k = 3
        rowConditions = [[1, 2], [3, 2]]
        colConditions = [[2, 1], [3, 2]]
        matrix = self.sol.buildMatrix(k, rowConditions, colConditions)
        self.assertMatrixSatisfiesConditions(
            matrix, rowConditions, colConditions
        )
        print("OK")

    def test_buildMatrix_2(self):
        print("Test buildMatrix 2... ", end="")
        k = 3
        rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
        colConditions = [[2, 1]]
        matrix = self.sol.buildMatrix(k, rowConditions, colConditions)
        self.assertListEqual([], matrix)
        print("OK")


if __name__ == "__main__":
    unittest.main()

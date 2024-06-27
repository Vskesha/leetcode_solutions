import unittest
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = sum(row[i] + row[~i] for i, row in enumerate(mat))
        i, r = divmod(len(mat), 2)
        if r:
            ans -= mat[i][i]
        return ans


class Solution2:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        lm = len(mat) // 2
        res = 0
        for i in range(lm):
            res += sum([mat[i][i], mat[-i - 1][i], mat[i][-i - 1], mat[-i - 1][-i - 1]])
        if len(mat) % 2:
            res += mat[lm][lm]
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_diagonal_sum_1(self):
        print("Test diagonalSum 1... ", end="")
        self.assertEqual(
            self.sol.diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25
        )
        print("OK")

    def test_diagonal_sum_2(self):
        print("Test diagonalSum 2... ", end="")
        self.assertEqual(
            self.sol.diagonalSum(
                mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
            ),
            8,
        )
        print("OK")

    def test_diagonal_sum_3(self):
        print("Test diagonalSum 3... ", end="")
        self.assertEqual(self.sol.diagonalSum(mat=[[5]]), 5)
        print("OK")


if __name__ == "__main__":
    unittest.main()

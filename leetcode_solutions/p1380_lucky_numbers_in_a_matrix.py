import unittest
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(r) for r in matrix} & {max(c) for c in zip(*matrix)})


class Solution2:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = set(min(row) for row in matrix)
        cols = set(max(col) for col in zip(*matrix))
        lucky = rows & cols
        return list(lucky)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_luckyNumbers_1(self):
        print("Test luckyNumbers 1... ", end="")
        self.assertListEqual(
            [15], self.sol.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]])
        )
        print("OK")

    def test_luckyNumbers_2(self):
        print("Test luckyNumbers 2... ", end="")
        self.assertListEqual(
            [12],
            self.sol.luckyNumbers(
                matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
            ),
        )
        print("OK")

    def test_luckyNumbers_3(self):
        print("Test luckyNumbers 3... ", end="")
        self.assertListEqual([7], self.sol.luckyNumbers(matrix=[[7, 8], [1, 2]]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

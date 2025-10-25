import unittest
from itertools import product
from typing import Iterable, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(nums: Iterable) -> bool:
            nums = [int(c) for c in nums if c.isdigit()]
            return len(set(nums)) == len(nums)

        for row in board:
            if not is_valid(row):
                return False

        for col in zip(*board):
            if not is_valid(col):
                return False

        for si, sj in product(range(0, 9, 3), repeat=2):
            sq = [
                board[i][j]
                for i, j in product(range(si, si + 3), range(sj, sj + 3))
            ]
            if not is_valid(sq):
                return False

        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                d = int(board[r][c])
                s = r // 3 * 3 + c // 3

                if d in rows[r] or d in cols[c] or d in sqrs[s]:
                    return False

                rows[r].add(d)
                cols[c].add(d)
                sqrs[s].add(d)

        return True


class Solution3:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            digits = [d for d in row if d != "."]
            if len(digits) != len(set(digits)):
                return False

        for col in zip(*board):
            digits = [d for d in col if d != "."]
            if len(digits) != len(set(digits)):
                return False

        for sr in range(0, 9, 3):
            for sc in range(0, 9, 3):
                digits = [
                    board[i][j]
                    for i in range(sr, sr + 3)
                    for j in range(sc, sc + 3)
                    if board[i][j] != "."
                ]
                if len(digits) != len(set(digits)):
                    return False

        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_valid_sudoku_1(self):
        print("Test isValidSudoku 1... ", end="")
        self.assertTrue(
            self.sol.isValidSudoku(
                board=[
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )
        print("OK")

    def test_is_valid_sudoku_2(self):
        print("Test isValidSudoku 2... ", end="")
        self.assertFalse(
            self.sol.isValidSudoku(
                board=[
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

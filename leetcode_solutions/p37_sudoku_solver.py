from copy import deepcopy
from itertools import product
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def reduce_allowed(i, j, allowed):
            val = allowed[i][j].pop()

            for y in range(9):
                allowed[y][j].discard(val)
            for x in range(9):
                allowed[i][x].discard(val)
            si = i // 3 * 3
            sj = j // 3 * 3
            for y in range(si, si + 3):
                for x in range(sj, sj + 3):
                    allowed[y][x].discard(val)

            allowed[i][j].add(val)

        def backtrack(allowed, left) -> bool:
            if not left:
                for i, j in product(range(9), repeat=2):
                    board[i][j] = allowed[i][j].pop()
                return True

            min_len = 10
            min_i, min_j = 0, 0
            for i, j in product(range(9), repeat=2):
                if (i, j) in left and len(allowed[i][j]) < min_len:
                    min_len = len(allowed[i][j])
                    if min_len == 1:
                        left.remove((i, j))
                        reduce_allowed(i, j, allowed)
                        return backtrack(allowed, left)
                    min_i, min_j = i, j

            if min_len == 0:
                return False

            i, j = min_i, min_j

            for val in allowed[i][j]:
                new_left = left.copy()
                new_left.remove((i, j))
                new_allowed = deepcopy(allowed)
                new_allowed[i][j] = {val}
                reduce_allowed(i, j, new_allowed)
                if backtrack(new_allowed, new_left):
                    return True

            return False

        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        sqrs = {i: set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                sq = i // 3 * 3 + j // 3
                d = board[i][j]
                if d == ".":
                    continue
                rows[i].add(d)
                cols[j].add(d)
                sqrs[sq].add(d)

        allowed = [[set()] * 9 for _ in range(9)]
        left = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    sq = i // 3 * 3 + j // 3
                    allowed[i][j] = set("123456789").difference(
                        rows[i] | cols[j] | sqrs[sq]
                    )
                    left.append((i, j))
                else:
                    allowed[i][j] = set(board[i][j])

        backtrack(allowed, left)


class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_taken_in_rows_cols_sqrs():
            rows = {i: set() for i in range(9)}
            cols = {i: set() for i in range(9)}
            sqrs = {i: set() for i in range(9)}

            for i in range(9):
                for j in range(9):
                    sq = i // 3 * 3 + j // 3
                    d = board[i][j]
                    if d == ".":
                        continue
                    rows[i].add(d)
                    cols[j].add(d)
                    sqrs[sq].add(d)

            return rows, cols, sqrs

        def create_allowed_sets(rows, cols, sqrs):
            allowed = [[set()] * 9 for _ in range(9)]

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        sq = i // 3 * 3 + j // 3
                        allowed[i][j] = set("123456789").difference(
                            rows[i] | cols[j] | sqrs[sq]
                        )
                    else:
                        allowed[i][j] = set(board[i][j])

            return allowed

        def get_min_set_coords(allowed, left):
            min_len = 10
            min_i, min_j = 0, 0
            for i in range(9):
                for j in range(9):
                    if (i, j) in left and len(allowed[i][j]) < min_len:
                        min_len = len(allowed[i][j])
                        min_i, min_j = i, j

            return min_i, min_j, min_len

        def reduce_allowed(i, j, allowed):
            val = allowed[i][j].pop()

            for y in range(9):
                allowed[y][j].discard(val)
            for x in range(9):
                allowed[i][x].discard(val)
            si = i // 3 * 3
            sj = j // 3 * 3
            for y in range(si, si + 3):
                for x in range(sj, sj + 3):
                    allowed[y][x].discard(val)

            allowed[i][j].add(val)

        def fill_board(allowed):
            for i, j in product(range(9), repeat=2):
                board[i][j] = allowed[i][j].pop()

        def backtrack(allowed, left) -> bool:
            if not left:
                fill_board(allowed)
                return True

            i, j, min_len = get_min_set_coords(allowed, left)

            if min_len == 0:
                return False

            if min_len == 1:
                left.remove((i, j))
                reduce_allowed(i, j, allowed)
                return backtrack(allowed, left)

            for val in allowed[i][j]:
                new_left = left.copy()
                new_left.remove((i, j))
                new_allowed = deepcopy(allowed)
                new_allowed[i][j] = {val}
                reduce_allowed(i, j, new_allowed)
                if backtrack(new_allowed, new_left):
                    return True

            return False

        rows, cols, sqrs = get_taken_in_rows_cols_sqrs()
        allowed = create_allowed_sets(rows, cols, sqrs)

        left = [(i, j) for i, j in product(range(9), repeat=2) if board[i][j] == "."]

        backtrack(allowed, left)


class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        sqrs = {i: set() for i in range(9)}

        def fill_sets():
            for i in range(9):
                for j in range(9):
                    sq = i // 3 * 3 + j // 3
                    d = board[i][j]
                    if d == ".":
                        continue
                    rows[i].add(d)
                    cols[j].add(d)
                    sqrs[sq].add(d)

        fill_sets()

        def backtrack(c):
            if c == 81:
                return True

            i, j = divmod(c, 9)
            sq = i // 3 * 3 + j // 3

            if board[i][j] != ".":
                return backtrack(c + 1)

            allowed = set("123456789").difference(rows[i] | cols[j] | sqrs[sq])

            for d in allowed:
                board[i][j] = d
                rows[i].add(d)
                cols[j].add(d)
                sqrs[sq].add(d)

                if backtrack(c + 1):
                    return True

                board[i][j] = "."
                rows[i].remove(d)
                cols[j].remove(d)
                sqrs[sq].remove(d)

            return False

        backtrack(0)


class Solution3:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        sqrs = {i: set() for i in range(9)}

        def fill_board():
            for i in range(9):
                for j in range(9):
                    sq = i // 3 * 3 + j // 3
                    d = board[i][j]
                    if d == ".":
                        continue
                    rows[i].add(d)
                    cols[j].add(d)
                    sqrs[sq].add(d)

        fill_board()

        def can_place(i, j, sq, d) -> bool:
            return d not in rows[i] and d not in cols[j] and d not in sqrs[sq]

        def place(i, j, sq, d):
            board[i][j] = d
            rows[i].add(d)
            cols[j].add(d)
            sqrs[sq].add(d)

        def remove(i, j, sq, d):
            board[i][j] = "."
            rows[i].remove(d)
            cols[j].remove(d)
            sqrs[sq].remove(d)

        def backtrack(c):
            if c == 81:
                return True

            i, j = divmod(c, 9)
            sq = i // 3 * 3 + j // 3

            if board[i][j] != ".":
                return backtrack(c + 1)

            for d in map(str, range(1, 10)):
                if can_place(i, j, sq, d):
                    place(i, j, sq, d)
                    if backtrack(c + 1):
                        return True
                    remove(i, j, sq, d)

            return False

        backtrack(0)


def verify_sudoku(board):
    all_digits = set("123456789")
    for row in board:
        assert set(row) == all_digits
    for col in zip(*board):
        assert set(col) == all_digits
    for sq in range(9):
        sqr, sqc = divmod(sq, 3)
        si, sj = sqr * 3, sqc * 3
        sqset = {board[i][j] for i in range(si, si + 3) for j in range(sj, sj + 3)}
        assert sqset == all_digits


def test_solve_sudoku():
    sol = Solution()

    print("Test 1... ", end="")
    board = [
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
    sol.solveSudoku(board=board)
    verify_sudoku(board)
    print("OK")

    print("Test 2... ", end="")
    board = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ]
    sol.solveSudoku(board=board)
    verify_sudoku(board)
    print("OK")


if __name__ == "__main__":
    test_solve_sudoku()

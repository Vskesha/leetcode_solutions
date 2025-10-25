from collections import Counter
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board[0]), len(board)
        values = Counter()

        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    for neib in (
                        (i - 1, j - 1),
                        (i - 1, j),
                        (i - 1, j + 1),
                        (i, j + 1),
                        (i + 1, j + 1),
                        (i + 1, j),
                        (i + 1, j - 1),
                        (i, j - 1),
                    ):
                        values[neib] += 1

        for i in range(n):
            for j in range(m):
                if values[(i, j)] == 3:
                    board[i][j] = 1
                elif values[(i, j)] < 2 or values[(i, j)] > 3:
                    board[i][j] = 0


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    print("ok")
    print("Test 2 ... ", end="")
    board = [[1, 1], [1, 0]]
    sol.gameOfLife(board)
    assert board == [[1, 1], [1, 1]]
    print("ok")


if __name__ == "__main__":
    test()

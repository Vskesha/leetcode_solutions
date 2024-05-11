from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"

        field = [[None] * 3 for _ in range(3)]

        i = 1
        for row, col in moves:
            field[row][col] = i
            if (
                (field[row][0] == field[row][1] == field[row][2])
                or (field[0][col] == field[1][col] == field[2][col])
                or (row == col and field[0][0] == field[1][1] == field[2][2])
                or (row + col == 2 and field[0][2] == field[1][1] == field[2][0])
            ):
                return "A" if i else "B"
            i = 1 - i

        return "Draw" if len(moves) == 9 else "Pending"


def test_tictactoe():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == "A"
    print("OK")

    print("Test 2... ", end="")
    assert sol.tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == "B"
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.tictactoe(
            moves=[
                [0, 0],
                [1, 1],
                [2, 0],
                [1, 0],
                [1, 2],
                [2, 1],
                [0, 1],
                [0, 2],
                [2, 2],
            ]
        )
        == "Draw"
    )
    print("OK")


if __name__ == "__main__":
    test_tictactoe()

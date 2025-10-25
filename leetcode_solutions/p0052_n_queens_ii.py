class Solution:
    def __init__(self):
        self.cols = set()
        self.dia1 = set()
        self.dia2 = set()

    def can_place(self, r, c) -> bool:
        return (
            c not in self.cols
            and r - c not in self.dia1
            and r + c not in self.dia2
        )

    def place(self, r, c) -> None:
        self.cols.add(c)
        self.dia1.add(r - c)
        self.dia2.add(r + c)

    def remove(self, r, c) -> None:
        self.cols.remove(c)
        self.dia1.remove(r - c)
        self.dia2.remove(r + c)

    def totalNQueens(self, n: int) -> int:
        return self.backtrack(0, n)

    def backtrack(self, r, n) -> int:
        if r == n:
            return 1

        tot = 0
        for c in range(n):
            if self.can_place(r, c):
                self.place(r, c)
                tot += self.backtrack(r + 1, n)
                self.remove(r, c)

        return tot


def test_total_n_queens():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.totalNQueens(n=1) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.totalNQueens(n=4) == 2
    print("OK")


if __name__ == "__main__":
    test_total_n_queens()

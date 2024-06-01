from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def btr(r, oc, comb, rows, ans):
            if r:
                for c in range(n):
                    st = {c, r - c + n * 2, r + c + n * 3}
                    if not st.intersection(oc):
                        oc.update(st)
                        comb.append(c)
                        btr(r - 1, oc, comb, rows, ans)
                        comb.pop()
                        oc.difference_update(st)
            else:
                ans.append([rows[c] for c in comb])

        ans = []
        btr(n, set(), [], ["." * i + "Q" + "." * (n - i - 1) for i in range(n)], ans)

        return ans


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, dia1, dia2 = set(), set(), set()
        rows = ["." * i + "Q" + "." * (n - i - 1) for i in range(n)]
        ans, comb = [], []

        def btr(r):
            if r == n:
                ans.append(comb.copy())
                return

            for c in range(n):
                d1, d2 = r - c, r + c
                if c in cols or d1 in dia1 or d2 in dia2:
                    continue
                cols.add(c)
                dia1.add(d1)
                dia2.add(d2)
                comb.append(rows[c])
                btr(r + 1)
                comb.pop()
                dia2.remove(d2)
                dia1.remove(d1)
                cols.remove(c)

        btr(0)
        return ans


def test_solve_n_queens():
    sol = Solution()

    print("Test 1... ", end="")
    ans = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    for comb in sol.solveNQueens(n=4):
        assert comb in ans
    print("OK")

    print("Test 2... ", end="")
    ans = [["Q"]]
    for comb in sol.solveNQueens(n=1):
        assert comb in ans
    print("OK")


if __name__ == "__main__":
    test_solve_n_queens()

import unittest
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        co, ro = n % 2, m % 2
        mr, mc = grid[m // 2], [grid[r][n // 2] for r in range(m)]

        ans = 0
        for r in range(m // 2):
            for c in range(n // 2):
                ts = grid[r][c] + grid[~r][c] + grid[r][~c] + grid[~r][~c]
                ans += min(ts, 4 - ts)

        ans += co * ro * grid[m // 2][n // 2]

        mans = sum(
            [
                ro * sum(mr[c] != mr[~c] for c in range(n // 2)),
                co * sum(mc[r] != mc[~r] for r in range(m // 2)),
            ]
        )
        if mans:
            return ans + mans

        msum = ro * sum(mr) + co * sum(mc) - ro * co * grid[m // 2][n // 2] * 2

        return ans if msum % 4 == 0 else ans + 2


class Solution1:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        co, ro = n % 2, m % 2
        mr, mc = grid[m // 2], [grid[r][n // 2] for r in range(m)]
        ans = (
            sum(
                min(
                    ts := grid[r][c]
                    + grid[~r][c]
                    + grid[r][~c]
                    + grid[~r][~c],
                    4 - ts,
                )
                for r in range(m // 2)
                for c in range(n // 2)
            )
            + co * ro * grid[m // 2][n // 2]
        )
        mans = ro * sum(mr[c] != mr[~c] for c in range(n // 2)) + co * sum(
            mc[r] != mc[~r] for r in range(m // 2)
        )
        return (
            ans + mans
            if mans
            else (
                ans + 2
                if (
                    ro * sum(mr)
                    + co * sum(mc)
                    - ro * co * grid[m // 2][n // 2] * 2
                )
                % 4
                else ans
            )
        )


class Solution2:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        for r in range(m // 2):
            for c in range(n // 2):
                ts = grid[r][c] + grid[~r][c] + grid[r][~c] + grid[~r][~c]
                ans += min(ts, 4 - ts)
        oddcols, oddrows = n % 2, m % 2

        if oddcols and oddrows:
            ans += grid[m // 2][n // 2]

        mrow = grid[m // 2]
        mcol = [grid[r][n // 2] for r in range(m)]

        mans = 0
        if oddrows:
            mans += sum(mrow[c] != mrow[~c] for c in range(n // 2))
        if oddcols:
            mans += sum(mcol[r] != mcol[~r] for r in range(m // 2))
        if mans:
            return ans + mans

        msum = 0
        if oddrows:
            msum += sum(mrow)
        if oddcols:
            msum += sum(mcol)
        if oddrows and oddcols:
            msum -= 2 * grid[m // 2][n // 2]

        return ans if msum % 4 == 0 else ans + 2


class Solution3:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        co, ro = n % 2, m % 2

        ans = 0
        for r in range(m // 2):
            for c in range(n // 2):
                ts = grid[r][c] + grid[~r][c] + grid[r][~c] + grid[~r][~c]
                ans += min(ts, 4 - ts)
        if co and ro and grid[m // 2][n // 2]:
            ans += 1

        zsd = [0, 0, 0]
        if ro:
            mr = grid[m // 2]
            for c in range(n // 2):
                zsd[mr[c] + mr[~c]] += 1
        if co:
            mc = [grid[r][n // 2] for r in range(m)]
            for r in range(m // 2):
                zsd[mc[r] + mc[~r]] += 1

        return ans + zsd[1] if zsd[1] else ans + 2 if zsd[2] % 2 else ans


class Solution4:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        co, ro = n % 2, m % 2

        ans = 0
        for r in range(m // 2):
            for c in range(n // 2):
                ts = grid[r][c] + grid[~r][c] + grid[r][~c] + grid[~r][~c]
                ans += min(ts, 4 - ts)
        if co and ro and grid[m // 2][n // 2]:
            ans += 1

        single = 0
        dividesby4 = True
        if ro:
            mr = grid[m // 2]
            for c in range(n // 2):
                if mr[c] != mr[~c]:
                    single += 1
                elif mr[c] == 1:
                    dividesby4 = not dividesby4
        if co:
            mc = [grid[r][n // 2] for r in range(m)]
            for r in range(m // 2):
                if mc[r] != mc[~r]:
                    single += 1
                elif mc[r] == 1:
                    dividesby4 = not dividesby4

        return ans + single if single else ans if dividesby4 else ans + 2


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minFlips_1(self):
        print("Test minFlips 1... ", end="")
        self.assertEqual(
            3, self.sol.minFlips(grid=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        )
        print("OK")

    def test_minFlips_2(self):
        print("Test minFlips 2... ", end="")
        self.assertEqual(2, self.sol.minFlips(grid=[[0, 1], [0, 1], [0, 0]]))
        print("OK")

    def test_minFlips_3(self):
        print("Test minFlips 3... ", end="")
        self.assertEqual(2, self.sol.minFlips(grid=[[1], [1]]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

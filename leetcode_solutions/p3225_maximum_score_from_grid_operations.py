import unittest
from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        lg = len(grid)
        acc = [list(accumulate(col, initial=0)) for col in zip(*grid)]
        """
        vep -- max value excluding previous column
        vip -- max value including previous column
        vec -- max value excluding current column
        vic -- max value including current column
        """
        vep = vip = vic = [0] * (lg + 1)
        for j in range(1, lg):
            vec = [0] * (lg + 1)
            vic = [0] * (lg + 1)
            for pb in range(lg + 1):
                for cb in range(lg + 1):
                    pv = acc[j - 1][cb] - acc[j - 1][pb] if cb > pb else 0
                    cv = acc[j][pb] - acc[j][cb] if cb < pb else 0
                    pmax = max(pv + vep[pb], vip[pb])
                    vec[cb] = max(vec[cb], pmax)
                    vic[cb] = max(vic[cb], cv + pmax)
            vep, vip = vec, vic

        return max(vic)


class Solution1:
    def maximumScore(self, grid: List[List[int]]) -> int:
        @lru_cache(1000)
        def d1(u: bool, s: int) -> int:
            if s == n - 1:
                return 0
            if not u:
                return max(d2(u, s, 0, c) + d1(not u, c) for c in range(s + 1, n))
            return max(d2(u, s, n - 1, c - 1) + d1(not u, c) for c in range(s + 1, n))

        @lru_cache(1000)
        def d2(u: bool, s: int, r: int, c: int) -> int:
            if r == n or r == -1 or c == s:
                return 0
            if u:
                return max(d2(u, s, r - 1, c) + grid[r][c], d2(u, s, r, c - 1))
            return max(d2(u, s, r, c - 1), d2(u, s, r + 1, c) + grid[r][c])

        n = len(grid)
        return d1(True, -1)


class Solution2:
    def maximumScore(self, grid: List[List[int]]) -> int:
        @lru_cache(1000)
        def peak(s: int) -> int:
            if s == n - 1:
                return 0
            return max(slope_down(s, n - 1, c - 1) + valley(c) for c in range(s + 1, n))

        @lru_cache(1000)
        def valley(s: int) -> int:
            if s == n - 1:
                return 0
            return max(slope_up(s, 0, c) + peak(c) for c in range(s + 1, n))

        @lru_cache(1000)
        def slope_up(stcol: int, row: int, col: int) -> int:
            if row == n or col == stcol:
                return 0
            return max(
                slope_up(stcol, row, col - 1),
                slope_up(stcol, row + 1, col) + grid[row][col],
            )

        @lru_cache(1000)
        def slope_down(stcol: int, row: int, col: int) -> int:
            if row == -1 or col == stcol:
                return 0
            return max(
                slope_down(stcol, row - 1, col) + grid[row][col],
                slope_down(stcol, row, col - 1),
            )

        n = len(grid)
        return peak(-1)


class Solution3:
    def maximumScore(self, grid: List[List[int]]) -> int:
        @lru_cache(1000)
        def peak(col: int) -> int:
            if col == n - 1:
                return 0
            ans = 0
            for vcol in range(col + 1, n):
                res = slope_down(col, n - 1, vcol - 1) + valley(vcol)
                ans = max(ans, res)
            return ans

        @lru_cache(1000)
        def valley(col: int) -> int:
            if col == n - 1:
                return 0
            ans = 0
            for pcol in range(col + 1, n):
                res = slope_up(col + 1, 0, pcol) + peak(pcol)
                ans = max(ans, res)
            return ans

        @lru_cache(1000)
        def slope_up(stcol: int, row: int, col: int) -> int:
            if row == n:
                return 0
            down = slope_up(stcol, row + 1, col) + grid[row][col]
            if col == stcol:
                return down
            left = slope_up(stcol, row, col - 1)
            return max(left, down)

        @lru_cache(1000)
        def slope_down(stcol: int, row: int, col: int) -> int:
            if row == -1 or col == stcol:
                return 0
            up = slope_down(stcol, row - 1, col) + grid[row][col]
            left = slope_down(stcol, row, col - 1)
            return max(up, left)

        n = len(grid)
        return peak(-1)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maximumScore_1(self):
        print("Test maximumScore 1... ", end="")
        self.assertEqual(
            11,
            self.sol.maximumScore(
                grid=[
                    [0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 0],
                    [0, 1, 0, 0, 0],
                    [5, 0, 0, 3, 0],
                    [0, 0, 0, 0, 2],
                ]
            ),
        )
        print("OK")

    def test_maximumScore_2(self):
        print("Test maximumScore 2... ", end="")
        self.assertEqual(
            94,
            self.sol.maximumScore(
                grid=[
                    [10, 9, 0, 0, 15],
                    [7, 1, 0, 8, 0],
                    [5, 20, 0, 11, 0],
                    [0, 0, 0, 1, 2],
                    [8, 12, 1, 10, 3],
                ]
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

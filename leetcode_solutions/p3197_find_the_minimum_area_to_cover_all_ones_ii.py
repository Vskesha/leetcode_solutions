import unittest
from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        ra = [list(accumulate(r, initial=0)) for r in grid]
        ca = [list(accumulate(c, initial=0)) for c in zip(*grid)]

        @cache
        def shrink(l, r, t, b):
            while ra[t][r + 1] == ra[t][l]:
                t += 1
            while ra[b][r + 1] == ra[b][l]:
                b -= 1
            while ca[l][b + 1] == ca[l][t]:
                l += 1
            while ca[r][b + 1] == ca[r][t]:
                r -= 1
            return l, r, t, b

        @cache
        def dp(l, r, t, b, d) -> int:
            l, r, t, b = shrink(l, r, t, b)
            if d == 1:
                return (r - l + 1) * (b - t + 1)
            ma = float("inf")
            for j in range(l, r):
                ma = min(ma, dp(l, j, t, b, 1) + dp(j + 1, r, t, b, d - 1))
                ma = min(ma, dp(l, j, t, b, d - 1) + dp(j + 1, r, t, b, 1))
            for i in range(t, b):
                ma = min(ma, dp(l, r, t, i, 1) + dp(l, r, i + 1, b, d - 1))
                ma = min(ma, dp(l, r, t, i, d - 1) + dp(l, r, i + 1, b, 1))
            return ma

        return dp(0, len(grid[0]) - 1, 0, len(grid) - 1, 3)


class Solution2:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def area(l, r, t, b):
            l, r, t, b = shrink(l, r, t, b)
            return (r - l + 1) * (b - t + 1)

        @cache
        def shrink(l, r, t, b):
            while l < r and 1 not in [grid[i][l] for i in range(t, b + 1)]:
                l += 1
            while r > l and 1 not in [grid[i][r] for i in range(t, b + 1)]:
                r -= 1
            while t < b and 1 not in [grid[t][j] for j in range(l, r + 1)]:
                t += 1
            while t < b and 1 not in [grid[b][j] for j in range(l, r + 1)]:
                b -= 1
            return l, r, t, b

        def min_area_vertical_split(l, r, t, b):
            if l == r:
                return area(l, r, t, b) + 1
            return min(
                area(l, j, t, b) + area(j + 1, r, t, b) for j in range(l, r)
            )

        def min_area_horizontal_split(l, r, t, b):
            if t == b:
                return area(l, r, t, b) + 1
            return min(
                area(l, r, t, i) + area(l, r, i + 1, b) for i in range(t, b)
            )

        l, r, t, b = shrink(0, len(grid[0]) - 1, 0, len(grid) - 1)
        sq = float("inf")

        for i in range(t, b):
            bnd1, bnd2 = shrink(l, r, t, i), shrink(l, r, i + 1, b)
            av1 = area(*bnd1)
            av23h = min_area_vertical_split(*bnd2)
            av23v = min_area_horizontal_split(*bnd2)
            av12h = min_area_vertical_split(*bnd1)
            av3 = area(*bnd2)
            sq = min((sq, av1 + av23h, av1 + av23v, av12h + av3))

        for j in range(l, r):
            bnd1, bnd2 = shrink(l, j, t, b), shrink(j + 1, r, t, b)
            ah1 = area(*bnd1)
            ah23h = min_area_vertical_split(*bnd2)
            ah23v = min_area_horizontal_split(*bnd2)
            ah12v = min_area_horizontal_split(*bnd1)
            ah3 = area(*bnd2)
            sq = min((sq, ah1 + ah23h, ah1 + ah23v, ah12v + ah3))

        return sq


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimum_sum_1(self):
        print("Test minimumSum 1... ", end="")
        self.assertEqual(self.sol.minimumSum(grid=[[1, 0, 1], [1, 1, 1]]), 5)
        print("OK")

    def test_minimum_sum_2(self):
        print("Test minimumSum 2... ", end="")
        self.assertEqual(
            self.sol.minimumSum(grid=[[1, 0, 1, 0], [0, 1, 0, 1]]), 5
        )
        print("OK")

    def test_minimum_sum_3(self):
        print("Test minimumSum 3... ", end="")
        self.assertEqual(
            self.sol.minimumSum(
                grid=[[0, 0, 0], [0, 0, 0], [1, 1, 1], [0, 0, 0]]
            ),
            3,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

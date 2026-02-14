import unittest
from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        ra = [list(accumulate(r, initial=0)) for r in grid]
        ca = [list(accumulate(c, initial=0)) for c in zip(*grid)]

        @cache
        def shrink(left, right, top, bottom):
            while ra[top][right + 1] == ra[top][left]:
                top += 1
            while ra[bottom][right + 1] == ra[bottom][left]:
                bottom -= 1
            while ca[left][bottom + 1] == ca[left][top]:
                left += 1
            while ca[right][bottom + 1] == ca[right][top]:
                right -= 1
            return left, right, top, bottom

        @cache
        def dp(left, right, top, bottom, d) -> int:
            left, right, top, bottom = shrink(left, right, top, bottom)
            if d == 1:
                return (right - left + 1) * (bottom - top + 1)
            ma = float("inf")
            for j in range(left, right):
                ma = min(
                    ma,
                    dp(left, j, top, bottom, 1)
                    + dp(j + 1, right, top, bottom, d - 1),
                )
                ma = min(
                    ma,
                    dp(left, j, top, bottom, d - 1)
                    + dp(j + 1, right, top, bottom, 1),
                )
            for i in range(top, bottom):
                ma = min(
                    ma,
                    dp(left, right, top, i, 1)
                    + dp(left, right, i + 1, bottom, d - 1),
                )
                ma = min(
                    ma,
                    dp(left, right, top, i, d - 1)
                    + dp(left, right, i + 1, bottom, 1),
                )
            return ma

        return dp(0, len(grid[0]) - 1, 0, len(grid) - 1, 3)


class Solution2:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def area(left, right, top, bottom):
            left, right, top, bottom = shrink(left, right, top, bottom)
            return (right - left + 1) * (bottom - top + 1)

        @cache
        def shrink(left, right, top, bottom):
            while left < right and 1 not in [
                grid[i][left] for i in range(top, bottom + 1)
            ]:
                left += 1
            while right > left and 1 not in [
                grid[i][right] for i in range(top, bottom + 1)
            ]:
                right -= 1
            while top < bottom and 1 not in [
                grid[top][j] for j in range(left, right + 1)
            ]:
                top += 1
            while top < bottom and 1 not in [
                grid[bottom][j] for j in range(left, right + 1)
            ]:
                bottom -= 1
            return left, right, top, bottom

        def min_area_vertical_split(left, right, top, bottom):
            if left == right:
                return area(left, right, top, bottom) + 1
            return min(
                area(left, j, top, bottom) + area(j + 1, right, top, bottom)
                for j in range(left, right)
            )

        def min_area_horizontal_split(left, right, top, bottom):
            if top == bottom:
                return area(left, right, top, bottom) + 1
            return min(
                area(left, right, top, i) + area(left, right, i + 1, bottom)
                for i in range(top, bottom)
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

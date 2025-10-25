import unittest
from functools import cache
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        aw = list(accumulate(weights))
        lw = len(weights)

        def can_convey(w):
            d = 1
            wd = w
            for i in range(lw):
                if aw[i] > wd:
                    wd = aw[i - 1] + w
                    d += 1
            return d <= days

        lw = len(weights)
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if can_convey(mid):
                r = mid
            else:
                l = mid + 1

        return l


class Solution1:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lw = len(weights)
        aw = list(accumulate(weights, initial=0))

        @cache
        def dp(i, d):
            if i == lw:
                return 0
            if d == 1:
                return aw[lw] - aw[i]
            ans = inf
            for j in range(i + 1, lw):
                cs = aw[j] - aw[i]
                if cs >= ans:
                    break
                res = max(cs, dp(j, d - 1))
                ans = min(ans, res)
            return ans

        return dp(0, days)


class Solution2:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(w):
            d = i = 0
            while i < lw:
                cs = 0
                while i < lw and cs + weights[i] <= w:
                    cs += weights[i]
                    i += 1
                d += 1
            return d

        lw = len(weights)
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if days_needed(mid) <= days:
                r = mid
            else:
                l = mid + 1

        return l


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_shipWithinDays_1(self):
        print("Test shipWithinDays 1 ... ", end="")
        self.assertEqual(
            15,
            self.sol.shipWithinDays(
                weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5
            ),
        )
        print("OK")

    def test_shipWithinDays_2(self):
        print("Test shipWithinDays 2 ... ", end="")
        self.assertEqual(
            6, self.sol.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3)
        )
        print("OK")

    def test_shipWithinDays_3(self):
        print("Test shipWithinDays 3 ... ", end="")
        self.assertEqual(
            3, self.sol.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4)
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

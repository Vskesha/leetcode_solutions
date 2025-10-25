import unittest
from heapq import heapify, heappop
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        lb = len(bloomDay)
        if len(bloomDay) < m * k:
            return -1

        di = iter(sorted(zip(bloomDay, range(lb))))
        starts, ends = {}, {}
        d = boq = 0

        while boq < m:
            d, i = next(di)
            ldist, lboq = ends.get(i - 1, (0, 0))
            rdist, rboq = starts.get(i + 1, (0, 0))
            cdist = ldist + rdist + 1
            cboq = cdist // k
            starts[i - ldist] = ends[i + rdist] = (cdist, cboq)
            boq += cboq - lboq - rboq

        return d


class Solution1:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        lb = len(bloomDay)
        if len(bloomDay) < m * k:
            return -1

        di = sorted(zip(bloomDay, range(lb)))
        starts, ends = {}, {}
        ans = 0

        for d, i in di:
            ldist = ends.get(i - 1, 0)
            rdist = starts.get(i + 1, 0)
            dist = ldist + rdist + 1
            starts[i - ldist] = dist
            ends[i + rdist] = dist
            ans += dist // k - ldist // k - rdist // k
            if ans >= m:
                return d


class Solution2:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def bouquets_on_day(x: int, k: int, bloomDay: List[int]) -> int:
            curr = ans = 0

            for i, b in enumerate(bloomDay):
                if b > x:
                    ans += curr // k
                    curr = 0
                else:
                    curr += 1
            ans += curr // k

            return ans

        l, r = 0, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if bouquets_on_day(mid, k, bloomDay) < m:
                l = mid + 1
            else:
                r = mid

        return r


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_days(self):
        print("Test minDays 1 ... ", end="")
        self.assertEqual(
            self.sol.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1), 3
        )
        print("OK")

    def test_min_days_2(self):
        print("Test minDays 2 ... ", end="")
        self.assertEqual(
            self.sol.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2), -1
        )
        print("OK")

    def test_min_days_3(self):
        print("Test minDays 3 ... ", end="")
        self.assertEqual(
            self.sol.minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3), 12
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def diff_h(rods: list[int]) -> dict[int, int]:
            dh = {0: 0}
            for rod in rods:
                for d, h in list(dh.items()):
                    dh[d + rod] = max(dh.get(d + rod, 0), h)
                    dh[abs(d - rod)] = max(dh.get(abs(d - rod), 0), h + min(d, rod))
            return dh

        d1, d2 = diff_h(rods[: len(rods) // 2]), diff_h(rods[len(rods) // 2 :])
        return max(v1 + d2[k1] + k1 for k1, v1 in d1.items() if k1 in d2)


class Solution1:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        hh = sum(rods) // 2 + 1
        for r in rods:
            for d, h in dp.copy().items():
                nd = d + r
                if nd < hh:
                    dp[nd] = max(dp.get(nd, 0), h)
                nd, h = (d - r, h + r) if r < d else (r - d, h + d)
                if nd < hh:
                    dp[nd] = max(dp.get(nd, 0), h)
        return dp[0]


class Solution2:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = Counter()
        dp[0] = 0
        for r in rods:
            ndp = dp.copy()
            for d, h in ndp.items():
                dp[d + r] = max(dp[d + r], h)
                if r < d:
                    dp[d - r] = max(dp[d - r], h + r)
                else:
                    dp[r - d] = max(dp[r - d], h + d)
        return dp[0]


class Solution3:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            for d, r in list(dp.items()):
                dp[d + rod] = max(dp.get(d + rod, 0), r + rod)
                if d > rod:
                    dp[d - rod] = max(dp.get(d - rod, 0), r)
                else:
                    dp[rod - d] = max(dp.get(rod - d, 0), r - d + rod)
        return dp[0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_tallest_billboard_1(self):
        print("Test tallestBillboard 1... ", end="")
        self.assertEqual(self.sol.tallestBillboard([1, 2, 3, 6]), 6)
        print("OK")

    def test_tallest_billboard_2(self):
        print("Test tallestBillboard 2... ", end="")
        self.assertEqual(self.sol.tallestBillboard(rods=[1, 2, 3, 4, 5, 6]), 10)
        print("OK")


if __name__ == "__main__":
    unittest.main()

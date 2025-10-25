import unittest
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nc = sorted(zip(nums, cost))
        il, ir = 0, len(nc) - 1
        cl, cr = nc[0][1], nc[-1][1]
        ans = 0

        while il < ir:
            if cl < cr:
                ans += (nc[il + 1][0] - nc[il][0]) * cl
                il += 1
                cl += nc[il][1]
            else:
                ans += (nc[ir][0] - nc[ir - 1][0]) * cr
                ir -= 1
                cr += nc[ir][1]

        return ans


class Solution2:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        left, right = min(nums), max(nums) + 1
        while left < right:
            m = (left + right) // 2
            curr = sum(cost[i] * abs(m - nums[i]) for i in range(n))
            nxt = sum(cost[i] * abs(m + 1 - nums[i]) for i in range(n))

            if nxt > curr:
                right = m
            else:
                left = m + 1

        return sum(cost[i] * abs(nums[i] - left) for i in range(n))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_cost_1(self):
        print("Test minCost 1... ", end="")
        self.assertEqual(
            self.sol.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]), 8
        )
        print("OK")

    def test_min_cost_2(self):
        print("Test minCost 2... ", end="")
        self.assertEqual(
            self.sol.minCost(nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]), 0
        )
        print("OK")

    def test_min_cost_3(self):
        print("Test minCost 3... ", end="")
        self.assertEqual(
            self.sol.minCost(
                nums=[
                    735103,
                    366367,
                    132236,
                    133334,
                    808160,
                    113001,
                    49051,
                    735598,
                    686615,
                    665317,
                    999793,
                    426087,
                    587000,
                    649989,
                    509946,
                    743518,
                ],
                cost=[
                    724182,
                    447415,
                    723725,
                    902336,
                    600863,
                    287644,
                    13836,
                    665183,
                    448859,
                    917248,
                    397790,
                    898215,
                    790754,
                    320604,
                    468575,
                    825614,
                ],
            ),
            1907611126748,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

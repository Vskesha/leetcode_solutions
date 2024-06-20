import unittest
from functools import cache
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)

        @cache
        def dp(i, s):
            if s == k:
                return pow(2, n - i, mod)
            if i == n or s > k:
                return 0
            return (2 * dp(i + 1, s) + dp(i + 1, s + nums[i])) % mod

        return dp(0, 0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_sum_of_power_1(self):
        print("Test sumOfPower 1... ", end="")
        self.assertEqual(self.sol.sumOfPower(nums=[1, 2, 3], k=3), 6)
        print("OK")

    def test_sum_of_power_2(self):
        print("Test sumOfPower 2... ", end="")
        self.assertEqual(self.sol.sumOfPower(nums=[2, 3, 3], k=5), 4)
        print("OK")

    def test_sum_of_power_3(self):
        print("Test sumOfPower 3... ", end="")
        self.assertEqual(self.sol.sumOfPower(nums=[1, 2, 3], k=7), 0)
        print("OK")


if __name__ == "__main__":
    unittest.main()

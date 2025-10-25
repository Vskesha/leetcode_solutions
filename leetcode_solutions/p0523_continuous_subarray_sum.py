import unittest
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods, mod = {0: -1}, 0

        for i, n in enumerate(nums):
            mod = (mod + n) % k
            if mod not in mods:
                mods[mod] = i
            elif i > mods[mod] + 1:
                return True

        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_check_subarray_sum1(self):
        print("Test checkSubarraySum 1 ... ", end="")
        self.assertTrue(self.sol.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
        print("OK")

    def test_check_subarray_sum2(self):
        print("Test checkSubarraySum 2 ... ", end="")
        self.assertTrue(self.sol.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
        print("OK")

    def test_check_subarray_sum3(self):
        print("Test checkSubarraySum 3 ... ", end="")
        self.assertFalse(
            self.sol.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13)
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

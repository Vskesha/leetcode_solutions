import unittest
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans, k, i, ln = 0, 1, 0, len(nums)

        while k <= n:
            if i == ln or nums[i] > k:
                ans += 1
                k += k
            else:
                k += nums[i]
                i += 1

        return ans


class Solution2:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans, k, i, ln = 0, 1, 0, len(nums)

        while k <= n:
            if i < ln and nums[i] <= k:
                k += nums[i]
                i += 1
            else:
                ans += 1
                k += k

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_min_patches_1(self):
        print("Test minPatches 1 ... ", end="")
        self.assertEqual(self.sol.minPatches(nums=[1, 3], n=6), 1)
        print("OK")

    def test_min_patches_2(self):
        print("Test minPatches 2 ... ", end="")
        self.assertEqual(self.sol.minPatches(nums=[1, 5, 10], n=20), 2)
        print("OK")


if __name__ == "__main__":
    unittest.main()

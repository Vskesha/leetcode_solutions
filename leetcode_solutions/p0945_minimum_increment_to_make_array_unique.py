import unittest
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans, k = 0, 0
        for n in sorted(nums):
            if k > n:
                ans += k - n
                k += 1
            else:
                k = n + 1
        return ans


class Solution2:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans, k = 0, 0
        for n in sorted(nums):
            k = max(k, n)
            ans += k - n
            k += 1
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_min_increment_for_unique_1(self):
        print("Test minIncrementForUnique 1 ... ", end="")
        self.assertEqual(self.sol.minIncrementForUnique(nums=[1, 2, 2]), 1)
        print("OK")

    def test_min_increment_for_unique_2(self):
        print("Test minIncrementForUnique 2 ... ", end="")
        self.assertEqual(self.sol.minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]), 6)
        print("OK")


if __name__ == "__main__":
    unittest.main()

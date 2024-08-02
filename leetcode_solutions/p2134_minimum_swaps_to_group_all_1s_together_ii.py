import unittest
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = nums.count(1)
        ln = len(nums)
        if not n or n == ln:
            return 0
        ans = z = nums[:n].count(0)
        nums.extend(nums)
        for st, end in zip(range(ln - 1), range(n, ln * 2)):
            z += (nums[end] == 0) - (nums[st] == 0)
            ans = min(ans, z)
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minSwaps_1(self):
        print("Test minSwaps 1... ", end="")
        self.assertEqual(1, self.sol.minSwaps(nums=[0, 1, 0, 1, 1, 0, 0]))
        print("OK")

    def test_minSwaps_2(self):
        print("Test minSwaps 2... ", end="")
        self.assertEqual(2, self.sol.minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0]))
        print("OK")

    def test_minSwaps_3(self):
        print("Test minSwaps 3... ", end="")
        self.assertEqual(0, self.sol.minSwaps(nums=[1, 1, 0, 0, 1]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m

        return l


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_findPeakElement_1(self):
        print("Test findPeakElement 1... ", end="")
        self.assertEqual(2, self.sol.findPeakElement(nums=[1, 2, 3, 1]))
        print("OK")

    def test_findPeakElement_2(self):
        print("Test findPeakElement 2... ", end="")
        self.assertIn(self.sol.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]), [1, 5])
        print("OK")


if __name__ == "__main__":
    unittest.main()

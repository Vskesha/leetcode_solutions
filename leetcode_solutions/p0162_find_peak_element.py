import unittest
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


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
        self.assertIn(
            self.sol.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]), [1, 5]
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

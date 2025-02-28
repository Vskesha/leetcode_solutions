import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return True if target in nums else False


class Solution1:
    def search(self, nums: list[int], target: int) -> bool:
        ln = len(nums)
        left, right = 0, ln - 1

        while left <= right:
            if right - left < 10:
                for i in range(left, right + 1):
                    if nums[i] == target:
                        return True
                return False
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[middle] > nums[left]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < nums[left]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                while left < ln and nums[left] == nums[middle]:
                    left += 1
                while right >= 0 and nums[right] == nums[middle]:
                    right -= 1

        return False


class Solution2:
    def search(self, nums: list[int], target: int) -> bool:
        ln = len(nums)
        if ln == 1:
            return nums[0] == target

        piv = 1
        while piv < ln - 1 and nums[piv] >= nums[piv - 1]:
            piv += 1

        if target > nums[0]:
            l, r = 1, piv
        elif target < nums[0]:
            l, r = piv, ln - 1
        else:
            return True

        idx = bisect_left(nums, target, lo=l, hi=r)
        return nums[idx] == target


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_search_1(self):
        print("Test search 1... ", end="")
        self.assertTrue(self.sol.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
        print("OK")

    def test_search_2(self):
        print("Test search 2... ", end="")
        self.assertFalse(self.sol.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
        print("OK")

    def test_search_3(self):
        print("Test search 3... ", end="")
        self.assertFalse(self.sol.search(nums=[1, 1], target=0))
        print("OK")


if __name__ == "__main__":
    unittest.main()

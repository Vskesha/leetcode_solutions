import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ln = len(nums)
        l, r = 0, ln - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return r + 1


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for n in nums:
            if n != val:
                nums[k] = n
                k += 1

        return k


class Solution3:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            elif nums[right] == val:
                right -= 1
            else:
                nums[left] = nums[right]
                right -= 1
        return left


class Solution4:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertEqualListBeginning(self, beginning: List[int], nums: List[int]):
        self.assertSetEqual(set(beginning), set(nums[: len(beginning)]))

    def test_remove_element_1(self):
        print("Test removeElement 1... ", end="")
        nums = [3, 2, 2, 3]
        val = 3
        expected = [2, 2]
        self.assertEqual(len(expected), self.sol.removeElement(nums, val))
        self.assertEqualListBeginning(expected, nums)
        print("OK")

    def test_remove_element_2(self):
        print("Test removeElement 2... ", end="")
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 1, 4, 0, 3]
        self.assertEqual(len(expected), self.sol.removeElement(nums, val))
        self.assertEqualListBeginning(expected, nums)
        print("OK")


if __name__ == "__main__":
    unittest.main()

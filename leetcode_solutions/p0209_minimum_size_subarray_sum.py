import unittest
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        curr_sum = 0
        min_len = len(nums) + 1
        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_len = min(min_len, end - start + 1)
                curr_sum -= nums[start]
                start += 1
        return 0 if min_len > len(nums) else min_len


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        min_length = len(nums) + 1
        sum_sub = 0
        left = 0
        for i, right in enumerate(nums):
            sum_sub += right
            while sum_sub >= target:
                min_length = min(min_length, i - left + 1)
                sum_sub -= nums[left]
                left += 1

        return min_length


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_sub_array_len_1(self):
        print("Test minSubArrayLen 1... ", end="")
        self.assertEqual(
            self.sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]), 2
        )
        print("OK")

    def test_min_sub_array_len_2(self):
        print("Test minSubArrayLen 2... ", end="")
        self.assertEqual(self.sol.minSubArrayLen(target=4, nums=[1, 4, 4]), 1)
        print("OK")

    def test_min_sub_array_len_3(self):
        print("Test minSubArrayLen 3... ", end="")
        self.assertEqual(
            self.sol.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]),
            0,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

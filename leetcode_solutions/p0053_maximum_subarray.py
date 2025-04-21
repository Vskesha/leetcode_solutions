import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = ans = 0

        for n in nums:
            acc += n
            if acc < 0:
                acc = 0
            elif acc > ans:
                ans = acc

        return ans or max(nums)


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if max_sum < curr_sum:
                max_sum = curr_sum
            if curr_sum <= 0:
                curr_sum = 0
        return max_sum


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxSubArray"] * 3,
            "kwargs": [
                dict(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]),
                dict(nums=[1]),
                dict(nums=[5, 4, -1, 7, 8]),
            ],
            "expected": [6, 1, 23],
        },
    ]


if __name__ == "__main__":
    unittest.main()

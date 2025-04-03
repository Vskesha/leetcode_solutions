import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highestSeen = 0
        highestDiff = 0
        ans = 0
        for num in nums:
            if highestDiff * num > ans:
                ans = highestDiff * num
            if highestSeen - num > highestDiff:
                highestDiff = highestSeen - num
            if num > highestSeen:
                highestSeen = num
        return ans


class Solution2:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = ans = max_diff = 0

        for n in nums:
            ans = max(ans, n * max_diff)
            max_diff = max(max_diff, max_val - n)
            max_val = max(max_val, n)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumTripletValue"] * 3,
            "kwargs": [
                dict(nums=[12, 6, 1, 2, 7]),
                dict(nums=[1, 10, 3, 4, 19]),
                dict(nums=[1, 2, 3]),
            ],
            "expected": [77, 133, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

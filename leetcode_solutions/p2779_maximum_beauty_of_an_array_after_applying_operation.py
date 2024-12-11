import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ln = len(nums)
        ei = 0
        k *= 2
        ans = 1

        for i, n in enumerate(nums):
            while ei < ln and nums[ei] <= n + k:
                ei += 1
            ans = max(ans, ei - i)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumBeauty"] * 2,
            "kwargs": [
                dict(nums=[4, 6, 1, 2], k=2),
                dict(nums=[1, 1, 1, 1], k=10),
            ],
            "expected": [3, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

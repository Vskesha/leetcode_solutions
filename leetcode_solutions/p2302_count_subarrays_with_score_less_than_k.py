import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = i = csum = wlen = 0

        for n in nums:
            csum += n
            wlen += 1
            while csum * wlen >= k:
                csum -= nums[i]
                wlen -= 1
                i += 1
            ans += wlen

        return ans


class Solution2:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = i = csum = 0

        for j, n in enumerate(nums, 1):
            csum += n
            while csum * (j - i) >= k:
                csum -= nums[i]
                i += 1
            ans += j - i

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSubarrays"] * 2,
            "kwargs": [
                dict(nums=[2, 1, 4, 3, 5], k=10),
                dict(nums=[1, 1, 1], k=5),
            ],
            "expected": [6, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

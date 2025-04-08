import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        nums.sort()
        ans = [[n] for n in nums]

        for i in range(ln):
            for j in range(i):
                if not nums[i] % nums[j]:
                    curr = ans[j] + [nums[i]]
                    ans[i] = max(ans[i], curr, key=len)

        return max(ans, key=len)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestDivisibleSubset"] * 2,
            "kwargs": [
                dict(nums = [1,2,3]),
                dict(nums = [1,2,4,8]),
            ],
            "expected": [
                [1, 2],
                [1, 2, 4, 8],
            ],
            "assert_methods": ["assertSameLengthSubset"],
        },
    ]

    def assertSameLengthSubset(self, actual, expected):
        return len(actual) == len(expected)


if __name__ == "__main__":
    unittest.main()

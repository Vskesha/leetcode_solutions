import math
import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1
        return sum(num * math.comb(n, k) % 10 for k, num in enumerate(nums)) % 10


class Solution1:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(a + b) % 10 for a, b in pairwise(nums)]
        return nums[0]


class Solution2:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]


class Solution3:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums) - 1
        for k, num in enumerate(nums):
            res = (res + num * math.comb(n, k) % 10) % 10
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["triangularSum"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 3, 4, 5]),
                dict(nums=[5]),
            ],
            "expected": [8, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

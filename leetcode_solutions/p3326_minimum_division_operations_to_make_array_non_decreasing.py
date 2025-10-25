import unittest
from functools import lru_cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1] = self.findNum(nums[i], nums[i - 1])
                if nums[i - 1] == -1:
                    return -1
                ans += 1
        return ans

    @lru_cache(2000)
    def findNum(self, n1, n2):
        for i in range(2, n1 + 1):
            if n2 % i == 0:
                return i
        return -1


class Solution2:
    def minOperations(self, nums: List[int]) -> int:
        ln = len(nums)
        ops = 0

        for i in range(ln - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            for d in range(2, min(nums[i + 1], int(nums[i] ** 2)) + 1):
                if nums[i] % d == 0:
                    nums[i] = d
                    ops += 1
                    break
            else:
                return -1

        return ops


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 3,
            "kwargs": [
                dict(nums=[25, 7]),
                dict(nums=[7, 7, 6]),
                dict(nums=[1, 1, 1, 1]),
            ],
            "expected": [1, -1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

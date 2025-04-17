import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    res += 1
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPairs"] * 2,
            "kwargs": [
                dict(nums = [3,1,2,2,2,1,3], k = 2),
                dict(nums = [1,2,3,4], k = 1),
            ],
            "expected": [4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

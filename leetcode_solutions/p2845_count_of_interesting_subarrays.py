import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countInterestingSubarrays(
            self, nums: List[int], modulo: int, k: int
    ) -> int:
        n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countInterestingSubarrays"] * 2,
            "kwargs": [
                dict(nums=[3, 2, 4], modulo=2, k=1),
                dict(nums=[3, 1, 9, 6], modulo=3, k=0),
            ],
            "expected": [3, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

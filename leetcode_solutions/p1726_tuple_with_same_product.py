import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = Counter()
        for i in range(len(nums)):
            for j in range(i):
                cnt[nums[i] * nums[j]] += 1
        return sum(v * (v - 1) for v in cnt.values()) * 4


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["tupleSameProduct"] * 2,
            "kwargs": [
                dict(nums=[2, 3, 4, 6]),
                dict(nums=[1, 2, 4, 5, 10]),
            ],
            "expected": [8, 16],
        },
    ]


if __name__ == "__main__":
    unittest.main()

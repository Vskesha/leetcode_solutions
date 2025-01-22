import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ns = Counter(nums)
        sm = sum(nums)
        nums.sort(reverse=True)
        for n in nums:
            ns[n] -= 1
            csm = sm - n
            if csm % 2 == 0 and ns[csm // 2]:
                return n
            ns[n] += 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getLargestOutlier"] * 3,
            "kwargs": [
                dict(nums=[2, 3, 5, 10]),
                dict(nums=[-2, -1, -3, -6, 4]),
                dict(nums=[1, 1, 1, 1, 1, 5, 5]),
            ],
            "expected": [10, 4, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

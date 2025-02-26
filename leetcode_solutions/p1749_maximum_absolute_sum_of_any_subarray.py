import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = cps = cns = 0

        for n in nums:
            cps = max(0, cps + n)
            cns = min(0, cns + n)
            ans = max(ans, cps, -cns)

        return ans

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxAbsoluteSum"] * 2,
            "kwargs": [
                dict(nums = [1,-3,2,3,-4]),
                dict(nums = [2,-5,1,-4,3,-2]),
            ],
            "expected": [5, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()

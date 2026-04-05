import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        return [nums[(i + nums[i]) % ln] for i in range(ln)]


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["constructTransformedArray"] * 2,
            "kwargs": [
                dict(nums=[3, -2, 1, 1]),
                dict(nums=[-1, 4, -1]),
            ],
            "expected": [[1, 1, 1, 3], [-1, -1, 4]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

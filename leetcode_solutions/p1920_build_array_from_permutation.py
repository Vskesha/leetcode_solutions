import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            # "cls_init_args": [],
            # "cls_init_kwargs": dict(),
            "class_methods": ["buildArray"] * 2,
            # "args": [[], ],
            "kwargs": [
                dict(nums=[0, 2, 1, 5, 3, 4]),
                dict(nums=[5, 0, 1, 2, 3, 4]),
            ],
            "expected": [[0, 1, 2, 4, 5, 3], [4, 5, 0, 1, 2, 3]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

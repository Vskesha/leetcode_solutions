import unittest
from functools import reduce, cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mor = reduce(lambda a, b: a | b, nums)

        @cache
        def dp(i: int, cor: int) -> int:
            if i == -1:
                return int(cor == mor)
            without = dp(i - 1, cor)
            with_ni = dp(i - 1, cor | nums[i])
            return without + with_ni

        return dp(len(nums) - 1, 0)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countMaxOrSubsets"] * 3,
            "kwargs": [
                dict(nums=[3, 1]),
                dict(nums=[2, 2, 2]),
                dict(nums=[3, 2, 1, 5]),
            ],
            "expected": [2, 7, 6],
        },
    ]


if __name__ == "__main__":
    unittest.main()

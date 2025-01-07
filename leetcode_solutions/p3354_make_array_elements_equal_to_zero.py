import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ls = sum(nums)
        cs = ans = 0

        for n in nums:
            if not n:
                d = abs(cs - ls)
                if d < 2:
                    ans += 2 - d
            cs += n
            ls -= n

        return ans


class Solution2:
    def countValidSelections(self, nums: List[int]) -> int:
        acc = list(accumulate(nums, initial=0))
        ans = 0

        for i, n in enumerate(nums):
            if not n:
                before = acc[i]
                after = acc[-1] - before
                diff = abs(before - after)
                if diff == 0:
                    ans += 2
                elif diff == 1:
                    ans += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countValidSelections"] * 2,
            "kwargs": [
                dict(nums=[1, 0, 2, 0, 3]),
                dict(nums=[2, 3, 4, 0, 4, 1, 0]),
            ],
            "expected": [2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

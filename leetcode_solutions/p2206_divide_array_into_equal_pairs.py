import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        return all(v % 2 == 0 for v in cnt.values())


class Solution2:
    def divideArray(self, nums: List[int]) -> bool:
        paired = set()
        for n in nums:
            if n in paired:
                paired.remove(n)
            else:
                paired.add(n)
        return not paired


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["divideArray"] * 2,
            "kwargs": [
                dict(nums=[3, 2, 3, 2, 2, 2]),
                dict(nums=[1, 2, 3, 4]),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

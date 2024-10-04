import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        k = len(nums) / 3
        return [n for n, c in cnt.items() if c > k]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["majorityElement"] * 3,
            "kwargs": [
                dict(nums=[3, 2, 3]),
                dict(nums=[1]),
                dict(nums=[1, 2]),
            ],
            "expected": [[3], [1], [1, 2]],
            "assert_methods": ["assertListEqual"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

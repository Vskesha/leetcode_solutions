import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, equal, bigger = [], [], []
        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                bigger.append(n)
            else:
                equal.append(n)

        smaller.extend(equal)
        smaller.extend(bigger)

        return smaller


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["pivotArray"] * 2,
            "kwargs": [
                dict(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10),
                dict(nums=[-3, 4, 3, 2], pivot=2),
            ],
            "expected": [
                [9, 5, 3, 10, 10, 12, 14],
                [-3, 2, 4, 3],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

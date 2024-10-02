import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {k: i for i, k in enumerate(sorted(set(arr)), 1)}
        return [rank[n] for n in arr]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["arrayRankTransform"] * 3,
            "kwargs": [
                dict(arr=[40, 10, 20, 30]),
                dict(arr=[100, 100, 100]),
                dict(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]),
            ],
            "expected": [
                [4, 1, 2, 3],
                [1, 1, 1],
                [5, 3, 4, 2, 8, 6, 7, 1, 3],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

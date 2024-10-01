import operator
import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = list(accumulate(arr, operator.xor, initial=0))
        return [acc[l] ^ acc[r + 1] for l, r in queries]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["xorQueries"] * 2,
            "kwargs": [
                dict(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]),
                dict(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]),
            ],
            "expected": [[2, 7, 14, 8], [8, 0, 4, 4]],
        },
    ]


if __name__ == "__main__":
    unittest.main()

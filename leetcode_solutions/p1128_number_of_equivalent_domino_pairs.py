import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter((a, b) if a < b else (b, a) for a, b in dominoes)
        return sum(v * (v - 1) for v in cnt.values()) // 2


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numEquivDominoPairs"] * 2,
            "kwargs": [
                dict(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]),
                dict(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]),
            ],
            "expected": [1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

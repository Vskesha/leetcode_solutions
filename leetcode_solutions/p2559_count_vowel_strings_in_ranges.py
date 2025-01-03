import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vw = {"a", "e", "i", "o", "u"}
        acc = list(
            accumulate([int(w[0] in vw and w[-1] in vw) for w in words], initial=0)
        )
        return [acc[ri + 1] - acc[li] for li, ri in queries]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["vowelStrings"] * 2,
            "kwargs": [
                dict(
                    words=["aba", "bcb", "ece", "aa", "e"],
                    queries=[[0, 2], [1, 4], [1, 1]],
                ),
                dict(words=["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]]),
            ],
            "expected": [[2, 3, 0], [3, 2, 1]],
        },
    ]


if __name__ == "__main__":
    unittest.main()

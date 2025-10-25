import unittest
from heapq import nlargest, nsmallest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        edges = sorted(
            [weights[i] + weights[i - 1] for i in range(1, len(weights))]
        )
        return sum(edges[-i - 1] - edges[i] for i in range(k - 1))


class Solution2:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = [x + y for x, y in pairwise(weights)]
        return sum(nlargest(k - 1, pairs)) - sum(nsmallest(k - 1, pairs))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["putMarbles"] * 2,
            "kwargs": [
                dict(weights=[1, 3, 5, 1], k=2),
                dict(weights=[1, 3], k=2),
            ],
            "expected": [4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

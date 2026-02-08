import unittest
from collections import defaultdict
from itertools import pairwise, product
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        top = defaultdict(list)
        for a, b, c in allowed:
            top[(a, b)].append(c)

        def dfs(row):
            if len(row) == 1:
                return True

            possibles = []
            for pair in pairwise(row):
                possibles.append(top[pair])

            for upper in product(*possibles):
                if dfs(upper):
                    return True

            return False

        return dfs(tuple(bottom))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["pyramidTransition"] * 2,
            "kwargs": [
                dict(bottom="BCD", allowed=["BCC", "CDE", "CEA", "FFF"]),
                dict(
                    bottom="AAAA", allowed=["AAB", "AAC", "BCD", "BBE", "DEF"]
                ),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

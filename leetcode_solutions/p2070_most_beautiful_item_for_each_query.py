import unittest
from bisect import bisect_right
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = [pr for pr, _ in items]
        accb = list(accumulate([b for _, b in items], initial=0, func=max))
        return [accb[bisect_right(prices, pr)] for pr in queries]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumBeauty"] * 3,
            "kwargs": [
                dict(items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]),
                dict(items=[[1, 2], [1, 2], [1, 3], [1, 4]], queries=[1]),
                dict(items=[[10, 1000]], queries=[5]),
            ],
            "expected": [[2, 4, 5, 5, 6, 6], [4], [0]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

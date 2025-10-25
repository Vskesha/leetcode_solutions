import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}

        ans = []
        for b, c in queries:
            pc = balls.get(b, 0)
            balls[b] = c
            if pc:
                colors[pc] -= 1
                if not colors[pc]:
                    del colors[pc]
            colors[c] = colors.get(c, 0) + 1
            ans.append(len(colors))

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["queryResults"] * 2,
            "kwargs": [
                dict(limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]),
                dict(
                    limit=4, queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
                ),
            ],
            "expected": [[1, 2, 2, 3], [1, 2, 2, 3, 4]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

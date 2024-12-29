import unittest
from collections import defaultdict
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        lh = len(heights)
        res = [-1] * len(queries)
        quer2 = defaultdict(list)

        for qi, (i, j) in enumerate(queries):
            if i > j:
                i, j = j, i
            if i == j or heights[j] > heights[i]:
                res[qi] = j
            else:
                quer2[j].append((heights[i], qi))

        stack = []
        for i in range(lh - 1, -1, -1):
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            stack.append((heights[i], i))
            if i in quer2:
                for h, qi in quer2[i]:
                    if h < stack[0][0]:
                        li, ri = 0, len(stack) - 1
                        while li < ri:
                            mi = (li + ri + 1) // 2
                            if stack[mi][0] <= h:
                                ri = mi - 1
                            else:
                                li = mi
                        res[qi] = stack[li][1]

        return res


class Solution2:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        lh = len(heights)
        res = [-1] * len(queries)
        quer2 = []

        for qi, (i, j) in enumerate(queries):
            if i > j:
                i, j = j, i
            if i == j or heights[j] > heights[i]:
                res[qi] = j
            else:
                quer2.append((j, heights[i], qi))

        quer2.sort(reverse=True)
        stack, pj = [(inf, -1)], lh - 1

        for j, h, qi in quer2:
            for i in range(pj, j, -1):
                while stack[-1][0] <= heights[i]:
                    stack.pop()
                stack.append((heights[i], i))
            pj = j
            li, ri = 0, len(stack) - 1
            while li < ri:
                mi = (li + ri + 1) // 2
                if stack[mi][0] > h:
                    li = mi
                else:
                    ri = mi - 1
            res[qi] = stack[li][1]

        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["leftmostBuildingQueries"] * 2,
            "kwargs": [
                dict(
                    heights=[6, 4, 8, 5, 2, 7],
                    queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]],
                ),
                dict(
                    heights=[5, 3, 8, 2, 6, 1, 4, 6],
                    queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
                ),
            ],
            "expected": [[2, 5, -1, 5, 2], [7, 6, -1, 4, 6]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

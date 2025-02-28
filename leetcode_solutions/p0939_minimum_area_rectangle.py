import unittest
from collections import defaultdict
from itertools import pairwise
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        groups = defaultdict(set)
        for x, y in points:
            groups[x].add(y)

        ma = inf
        absc = sorted(x for x in groups if len(groups[x]) > 1)
        for i in range(1, len(absc)):
            x2 = absc[i]
            gr2 = groups[x2]
            for j in range(i):
                x1 = absc[j]
                ords = groups[x1] & gr2
                if len(ords) > 1:
                    dy = min(b - a for a, b in pairwise(sorted(ords)))
                    ma = min(ma, dy * (x2 - x1))

        return 0 if ma == inf else ma


class Solution2:
    def minAreaRect(self, points: List[List[int]]) -> int:
        lp = len(points)
        pset = {tuple(p) for p in points}
        ans = inf
        for i in range(1, lp):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in pset and (x2, y1) in pset:
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return 0 if ans == inf else ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minAreaRect"] * 2,
            "kwargs": [
                dict(points=[[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]),
                dict(points=[[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]),
            ],
            "expected": [4, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

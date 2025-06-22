import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        xs = defaultdict(list)
        ys = defaultdict(list)

        for x, y in coords:
            xs[x].append(y)
            ys[y].append(x)

        maxx, minx, maxy, miny = max(xs), min(xs), max(ys), min(ys)
        ans = 0

        for x, lst in xs.items():
            side = max(lst) - min(lst)
            ans = max(ans, side * (maxx - x), side * (x - minx))

        for y, lst in ys.items():
            side = max(lst) - min(lst)
            ans = max(ans, side * (maxy - y), side * (y - miny))

        return ans or -1


class Solution2:
    def maxArea(self, coords: List[List[int]]) -> int:
        xs = defaultdict(list)
        ys = defaultdict(list)

        for x, y in coords:
            xs[x].append(y)
            ys[y].append(x)

        maxx = max(xs)
        minx = min(xs)
        maxy = max(ys)
        miny = min(ys)

        ans = -1
        for x, xys in xs.items():
            if len(xys) == 1:
                continue
            side = max(xys) - min(xys)
            height = maxx - x
            if height:
                ans = max(ans, side * height)
            height = x - minx
            if height:
                ans = max(ans, side * height)

        for y, yxs in ys.items():
            if len(yxs) == 1:
                continue
            side = max(yxs) - min(yxs)
            height = maxy - y
            if height:
                ans = max(ans, side * height)
            height = y - miny
            if height:
                ans = max(ans, side * height)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxArea"] * 2,
            "kwargs": [
                dict(coords=[[1, 1], [1, 2], [3, 2], [3, 3]]),
                dict(coords=[[1, 1], [2, 2], [3, 3]]),
            ],
            "expected": [2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        ln = len(bottomLeft)
        mside = 0

        rects = sorted((*bl, *tr) for bl, tr in zip(bottomLeft, topRight))

        for i, (x1, y1, x2, y2) in enumerate(rects):
            if min(x2 - x1, y2 - y1) <= mside:
                continue
            j = i + 1
            while j < ln and rects[j][0] < x2:
                if rects[j][1] >= y2 or rects[j][3] <= y1:
                    j += 1
                    continue
                ms = min(
                    min(rects[j][2], x2) - rects[j][0],
                    min(rects[j][3], y2) - max(rects[j][1], y1),
                )
                if ms > mside:
                    mside = ms
                j += 1

        return mside**2


class Solution3:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        max_area = 0
        ln = len(bottomLeft)
        for i in range(1, ln):
            for j in range(i):
                if (
                    bottomLeft[i][0] >= topRight[j][0]
                    or bottomLeft[j][0] >= topRight[i][0]
                    or bottomLeft[i][1] >= topRight[j][1]
                    or bottomLeft[j][1] >= topRight[i][1]
                ):
                    continue
                xl = max(bottomLeft[i][0], bottomLeft[j][0])
                xr = min(topRight[i][0], topRight[j][0])
                yb = max(bottomLeft[i][1], bottomLeft[j][1])
                yt = min(topRight[i][1], topRight[j][1])

                if (area := min(xr - xl, yt - yb) ** 2) > max_area:
                    max_area = area

        return max_area


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestSquareArea"] * 4,
            "kwargs": [
                dict(
                    bottomLeft=[[1, 1], [2, 2], [3, 1]],
                    topRight=[[3, 3], [4, 4], [6, 6]],
                ),
                dict(
                    bottomLeft=[[1, 1], [1, 3], [1, 5]],
                    topRight=[[5, 5], [5, 7], [5, 9]],
                ),
                dict(
                    bottomLeft=[[1, 1], [2, 2], [1, 2]],
                    topRight=[[3, 3], [4, 4], [3, 4]],
                ),
                dict(
                    bottomLeft=[[1, 1], [3, 3], [3, 1]],
                    topRight=[[2, 2], [4, 4], [4, 2]],
                ),
            ],
            "expected": [1, 4, 1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

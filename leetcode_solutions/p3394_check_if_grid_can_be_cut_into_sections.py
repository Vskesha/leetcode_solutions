import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort()
        xm = rectangles[0][2]
        sep = 0
        for x1, y1, x2, y2 in rectangles:
            if x1 >= xm:
                if sep:
                    return True
                sep += 1
            xm = max(xm, x2)

        rectangles.sort(key=lambda x: x[1])
        xm = rectangles[0][3]
        sep = 0
        for x1, y1, x2, y2 in rectangles:
            if y1 >= xm:
                if sep:
                    return True
                sep += 1
            xm = max(xm, y2)

        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkValidCuts"] * 3,
            "kwargs": [
                dict(n=5, rectangles=[[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]),
                dict(n=4, rectangles=[[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]),
                dict(n=4, rectangles=[[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from bisect import bisect_left
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        mx, my = coordinates[k]
        low = [(x, y) for x, y in coordinates if x < mx and y < my]
        hi = [(x, y) for x, y in coordinates if x > mx and y > my]

        def lpath(coords):
            if not coords:
                return 0
            coords.sort(key=lambda x: (x[0], -x[1]))
            lis = [coords[0][1]]
            for _, y in coords:
                if y > lis[-1]:
                    lis.append(y)
                else:
                    lis[bisect_left(lis, y)] = y
            return len(lis)

        ans = lpath(low) + lpath(hi) + 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxPathLength"] * 2,
            "kwargs": [
                dict(
                    coordinates=[[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], k=1
                ),
                dict(coordinates=[[2, 1], [7, 0], [5, 6]], k=2),
            ],
            "expected": [3, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()

        for iv in intervals:
            if result and result[-1][1] >= iv[0]:
                result[-1][1] = max(result[-1][1], iv[1])
            else:
                result.append(iv)

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["merge"] * 2,
            "kwargs": [
                dict(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]),
                dict(intervals=[[1, 4], [4, 5]]),
            ],
            "expected": [[[1, 6], [8, 10], [15, 18]], [[1, 5]]],
            "assert_methods": ["assertSameIntervals"] * 2,
        },
    ]

    def assertSameIntervals(self, iv1: List[List[int]], iv2: List[List[int]]):
        self.assertEqual(len(iv1), len(iv2))
        self.assertSetEqual(set(tuple(iv) for iv in iv1), set(tuple(iv) for iv in iv2))


if __name__ == "__main__":
    unittest.main()

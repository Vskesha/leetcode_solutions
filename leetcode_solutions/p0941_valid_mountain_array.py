import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        la = len(arr)
        if la < 3 or arr[0] >= arr[1] or arr[la - 1] >= arr[la - 2]:
            return False
        li = 0
        while li < la - 1 and arr[li] < arr[li + 1]:
            li += 1
        ri = la - 1
        while ri > 0 and arr[ri] < arr[ri - 1]:
            ri -= 1
        return li == ri


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["validMountainArray"] * 3,
            "kwargs": [
                dict(arr=[2, 1]),
                dict(arr=[3, 5, 5]),
                dict(arr=[0, 3, 2, 1]),
            ],
            "expected": [False, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

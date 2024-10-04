import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        la = len(arr)
        if la < 3 or arr[0] >= arr[1] or arr[la - 1] >= arr[la - 2]:
            return False
        l = 0
        while l < la - 1 and arr[l] < arr[l + 1]:
            l += 1
        r = la - 1
        while r > 0 and arr[r] < arr[r - 1]:
            r -= 1
        return l == r


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

import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        la = len(arr)
        ls = la - 1
        while ls and arr[ls] >= arr[ls - 1]:
            ls -= 1
        if not ls:
            return 0
        ans = inf
        prev = 0
        for i, n in enumerate(arr):
            while ls < la and arr[ls] < prev:
                ls += 1
            ans = min(ans, ls - i)
            if n < prev:
                break
            prev = n
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findLengthOfShortestSubarray"] * 4,
            "kwargs": [
                dict(arr=[6, 3, 10, 11, 15, 20, 13, 3, 18, 12]),
                dict(arr=[1, 2, 3, 10, 4, 2, 3, 5]),
                dict(arr=[5, 4, 3, 2, 1]),
                dict(arr=[1, 2, 3]),
            ],
            "expected": [8, 3, 4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

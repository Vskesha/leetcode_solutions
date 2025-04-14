import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        la = len(arr)

        for k in range(2, la):
            for j in range(1, k):
                if abs(arr[j] - arr[k]) > b:
                    continue
                for i in range(j):
                    ans += abs(arr[i] - arr[j]) <= a and abs(arr[i] - arr[k]) <= c

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countGoodTriplets"] * 2,
            "kwargs": [
                dict(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3),
                dict(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1),
            ],
            "expected": [4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

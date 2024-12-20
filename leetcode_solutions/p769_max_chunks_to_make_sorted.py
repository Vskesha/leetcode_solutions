import unittest
from itertools import accumulate
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mins = list(accumulate(arr[::-1], min))
        maxs = list(accumulate(arr, max, initial=0))
        return sum(a <= b for a, b in zip(maxs, reversed(mins)))


class Solution1:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return sum(
            a <= b
            for a, b in zip(
                accumulate(arr, max, initial=0),
                reversed(list(accumulate(reversed(arr), min))),
            )
        )


class Solution2:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        la = len(arr)
        mins = arr.copy()
        for i in range(la - 2, -1, -1):
            mins[i] = min(arr[i], mins[i + 1])
        mins.append(inf)

        ans = cm = 0
        for i, n in enumerate(arr):
            cm = max(cm, n)
            if cm <= mins[i + 1]:
                ans += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxChunksToSorted"] * 2,
            "kwargs": [
                dict(arr=[4, 3, 2, 1, 0]),
                dict(arr=[1, 0, 2, 3, 4]),
            ],
            "expected": [1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

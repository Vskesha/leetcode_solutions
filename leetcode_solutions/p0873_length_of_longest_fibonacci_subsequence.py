import unittest
from bisect import bisect_left
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fibs = {}
        ans = 0

        for i, n in enumerate(arr):
            fibs[n] = {}
            for j in range(bisect_left(arr, n // 2 + 1), i):
                prev = arr[j]
                prev2 = n - prev
                if prev2 in fibs:
                    fibs[n][prev] = fibs[prev].get(prev2, 2) + 1
                    ans = max(ans, fibs[n][prev])

        return ans

class Solution2:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fibs = defaultdict(list)
        ans = 0
        for i, n in enumerate(arr):
            for lst, ln in fibs[n]:
                fibs[lst + n].append((n, ln + 1))
                ans = max(ans, ln + 1)
            for j in range(i):
                fibs[arr[j] + n].append((n, 2))

        return ans


class Solution3:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fibs = defaultdict(list)
        for i, n in enumerate(arr):
            for lst, ln in fibs[n]:
                fibs[lst + n].append((n, ln + 1))
            for j in range(i):
                fibs[arr[j] + n].append((n, 2))

        ans = 0
        for fiblist in fibs.values():
            for _, ln in fiblist:
                ans = max(ans, ln)

        return ans if ans > 2 else 0


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lenLongestFibSubseq"] * 2,
            "kwargs": [
                dict(arr=[1, 2, 3, 4, 5, 6, 7, 8]),
                dict(arr=[1, 3, 7, 11, 12, 14, 18]),
            ],
            "expected": [5, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

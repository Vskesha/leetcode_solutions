import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def diff(i, j):
            if cnts[i] != cnts[j]:
                return False
            d = 0
            for a, b in zip(ns[i], ns[j]):
                if a != b:
                    d += 1
                    if d > 2:
                        return False
            return True

        ml = len(str(max(nums)))
        ns = [str(n).zfill(ml) for n in nums]
        cnts = [Counter(n) for n in ns]
        ln = len(ns)

        ans = 0
        for i in range(1, ln):
            for j in range(i):
                ans += diff(i, j)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPairs"] * 3,
            "kwargs": [
                dict(nums=[3, 12, 30, 17, 21]),
                dict(nums=[1, 1, 1, 1, 1]),
                dict(nums=[123, 231]),
            ],
            "expected": [2, 10, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

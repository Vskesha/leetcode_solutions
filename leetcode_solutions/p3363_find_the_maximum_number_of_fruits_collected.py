import unittest
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        for i in range(1, n - 1):
            for j in range(max(i + 1, n - i - 1), n):
                mpv = 0
                for pj in range(max(n - i, j - 1), min(n, j + 2)):
                    mpv = max(mpv, fruits[i - 1][pj])
                fruits[i][j] += mpv
        ans += fruits[-2][-1]

        for j in range(1, n - 1):
            for i in range(max(j + 1, n - j - 1), n):
                mph = 0
                for pi in range(max(n - j, i - 1), min(n, i + 2)):
                    mph = max(mph, fruits[pi][j - 1])
                fruits[i][j] += mph
        ans += fruits[-1][-2]

        return ans


class Solution2:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0

        @cache
        def ver(i, j):
            if j < i or j < n - i - 1 or j == n or i < 0:
                return 0
            return fruits[i][j] + max(
                ver(i - 1, j - 1), ver(i - 1, j), ver(i - 1, j + 1)
            )

        @cache
        def hor(i, j):
            if i < j or i < n - j - 1 or i == n or j < 0:
                return 0
            return fruits[i][j] + max(
                hor(i - 1, j - 1), hor(i, j - 1), hor(i + 1, j - 1)
            )

        ans += ver(n - 1, n - 1)
        ans += hor(n - 1, n - 1)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxCollectedFruits"] * 2,
            "kwargs": [
                dict(
                    fruits=[
                        [1, 2, 3, 4],
                        [5, 6, 8, 7],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16],
                    ]
                ),
                dict(fruits=[[1, 1], [1, 1]]),
            ],
            "expected": [100, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

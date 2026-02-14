import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def get_z_arr(s: str, p: str) -> List[int]:
            p += s
            z = [0] * lt
            left, r = 0, 0
            for i in range(1, lt):
                if i > r:
                    left = r = i
                    while r < lt and p[r] == p[r - left]:
                        r += 1
                    z[i] = r - left
                    r -= 1
                else:
                    k = i - left
                    if z[k] < r - i + 1:
                        z[i] = z[k]
                    else:
                        left = i
                        while r < lt and p[r] == p[r - left]:
                            r += 1
                        z[i] = r - left
                        r -= 1
            return z

        ls, lp = len(s), len(pattern)
        lt = ls + lp
        z1 = get_z_arr(s, pattern)
        z2 = get_z_arr(s[::-1], pattern[::-1])

        for i in range(lp, ls + 1):
            if z1[i] + z2[lt - i] >= lp - 1:
                return i - lp

        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minStartingIndex"] * 5,
            "kwargs": [
                dict(s="abcdefg", pattern="bcdffg"),
                dict(s="ababbababa", pattern="bacaba"),
                dict(s="abcd", pattern="dba"),
                dict(s="dde", pattern="d"),
                dict(s="gghghh", pattern="hh"),
            ],
            "expected": [1, 4, -1, 0, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

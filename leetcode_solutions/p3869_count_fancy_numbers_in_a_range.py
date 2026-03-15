import unittest
from functools import cache
from itertools import pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        hs = str(r)
        n = len(hs)
        ls = str(l).zfill(n)

        def is_fancy(n):
            return (
                n < 10
                or all(a < b for a, b in pairwise(str(n)))
                or all(a > b for a, b in pairwise(str(n)))
            )

        @cache
        def dp(i, lf, hf, sm, f1, f2, prv):
            if i >= n:
                return int(f1 or f2 or is_fancy(sm))

            lw = int(ls[i]) if lf else 0
            hi = int(hs[i]) if hf else 9

            return sum(
                dp(
                    i + 1,
                    lf and j == lw,
                    hf and j == hi,
                    sm + j,
                    not sm or (prv < j and f1),
                    not sm or (prv > j and f2),
                    j,
                )
                for j in range(lw, hi + 1)
            )

        res = dp(0, 1, 1, 0, True, True, 0)

        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countFancy"] * 3,
            "kwargs": [
                dict(l=8, r=10),
                dict(l=12340, r=12341),
                dict(l=123456788, r=123456788),
            ],
            "expected": [3, 1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

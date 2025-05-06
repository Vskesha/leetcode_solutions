import unittest
from functools import cache

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        ae = be = bu = 1
        au = 0

        for _ in range(n - 1):
            nbe = (be + ae + 2 * au) % mod
            nbu = (be + bu) % mod
            ae, au, be, bu = be, bu, nbe, nbu

        return be


class Solution2:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(left: int, equal: int) -> int:
            if left < 0:
                return 0

            if left <= 0:
                return equal

            if equal:
                dh = dp(left - 2, 1)
                dv = dp(left - 1, 1)
                t = dp(left - 2, 0)
                ans = (dh + dv + 2 * t) % mod
                return ans

            d = dp(left - 1, 0)
            t = dp(left - 1, 1)
            ans = (d + t) % mod
            return ans

        return dp(n, 1)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            # "cls_init_args": [],
            # "cls_init_kwargs": dict(),
            "class_methods": ["numTilings"] * 2,
            # "args": [[], ],
            "kwargs": [
                dict(n=3),
                dict(n=1),
            ],
            "expected": [5, 1],
            # "assert_methods": ["assertMethod"] * n,
        },
    ]


if __name__ == "__main__":
    unittest.main()

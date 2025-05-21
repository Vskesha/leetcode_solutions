import unittest
from collections import Counter, defaultdict
from itertools import pairwise, product

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        m3 = 3**m

        valid = {}
        for mask in range(m3):
            colors = []
            num = mask
            for _ in range(m):
                colors.append(num % 3)
                num //= 3
            if all(a != b for a, b in pairwise(colors)):
                valid[mask] = colors

        adj = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if all(color1[i] != color2[i] for i in range(m)):
                    adj[mask1].append(mask2)

        dp = [int(mask in valid) for mask in range(m3)]
        for _ in range(n - 1):
            ndp = [0] * m3
            for mask in range(m3):
                for mask2 in adj[mask]:
                    ndp[mask] = (ndp[mask] + dp[mask2]) % mod
            dp = ndp

        return sum(dp) % mod


class Solution2:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        valid = [
            "".join(mask)
            for mask in product("RGB", repeat=m)
            if all(a != b for a, b in pairwise(mask))
        ]
        adj = {
            mask: [mask2 for mask2 in valid if all(a != b for a, b in zip(mask, mask2))]
            for mask in valid
        }
        dp = {mask: 1 for mask in valid}
        for _ in range(n - 1):
            dp = {mask: sum(dp[mask2] for mask2 in adj[mask]) % mod for mask in valid}
        return sum(dp.values()) % mod


class Solution3:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7

        valid = [
            "".join(mask)
            for mask in product("RGB", repeat=m)
            if all(a != b for a, b in pairwise(mask))
        ]
        adj = {
            mask: [mask2 for mask2 in valid if all(a != b for a, b in zip(mask, mask2))]
            for mask in valid
        }

        dp = Counter(valid)
        for _ in range(n - 1):
            ndp = Counter()
            for mask in valid:
                for mask2 in adj[mask]:
                    ndp[mask] = (ndp[mask] + dp[mask2]) % mod
            dp = ndp

        return sum(dp.values()) % mod


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["colorTheGrid"] * 3,
            "kwargs": [
                dict(m=1, n=1),
                dict(m=1, n=2),
                dict(m=5, n=5),
            ],
            "expected": [3, 6, 580986],
        },
    ]


if __name__ == "__main__":
    unittest.main()

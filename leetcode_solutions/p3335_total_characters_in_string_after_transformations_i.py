import unittest

import numpy as np

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        for _ in range(t):
            cnt = [cnt[i - 1] for i in range(26)]
            cnt[1] = (cnt[1] + cnt[0]) % mod

        return sum(cnt) % mod


class Solution2:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        base = np.zeros((26, 26), dtype=object)
        cur = np.eye(26, dtype=object)
        for i in range(25):
            base[i][i + 1] = 1
        base[25][0] = base[25][1] = 1
        while t:
            if t & 1 > 0:
                cur = cur.dot(base) % mod
            base = base.dot(base) % mod
            t >>= 1
        data = cur.sum(axis=1) % mod
        return sum(data[ord(ch) - 97] for ch in s) % mod


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lengthAfterTransformations"] * 2,
            "kwargs": [
                dict(s="abcyy", t=2),
                dict(s="azbk", t=1),
            ],
            "expected": [7, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from functools import reduce
from typing import List

import numpy as np

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lengthAfterTransformations(
        self, s: str, t: int, nums: List[int]
    ) -> int:
        mod = 10**9 + 7
        orda = ord("a")
        base = np.zeros((26, 26), dtype=object)
        curr = np.eye(26, dtype=object)
        for i, n in enumerate(nums):
            for sh in range(1, n + 1):
                base[i][(i + sh) % 26] = 1
        while t:
            if t % 2:
                curr = curr.dot(base) % mod
            t //= 2
            base = base.dot(base) % mod
        # base = np.linalg.matrix_power(base, t)
        data = curr.sum(axis=1) % mod
        cnt = Counter(s)
        ans = (
            sum(data[ord(ch) - orda] * v % mod for ch, v in cnt.items()) % mod
        )
        return ans


class Solution1:
    def lengthAfterTransformations(
        self, s: str, t: int, nums: List[int]
    ) -> int:
        sh = ord("a")
        mod = 10**9 + 7

        v = [0] * 26
        for ch in s:
            v[ord(ch) - sh] += 1

        m = [[0] * 26 for _ in range(26)]
        for i, val in enumerate(nums):
            for j in range(i + 1, i + nums[i] + 1):
                m[i][j % 26] = 1

        def mult(a, b):
            m, k, n = len(a), len(b), len(b[0])
            res = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    for ki in range(k):
                        res[i][j] = (res[i][j] + a[i][ki] * b[ki][j]) % mod

            return res

        def power(a, t):
            if t == 1:
                return a
            res = power(mult(a, a), t // 2)
            if t % 2:
                res = mult(res, a)
            return res

        resv = mult([v], power(m, t))
        ans = reduce(lambda x, y: (x + y) % mod, resv[0])
        return ans


class Solution2:
    def lengthAfterTransformations(
        self, s: str, t: int, nums: List[int]
    ) -> int:
        mod = 10**9 + 7
        base = np.zeros((26, 26), dtype=object)
        cur = np.eye(26, dtype=object)
        for i, v in enumerate(nums):
            for j in range(i + 1, i + v + 1):
                base[i][j % 26] = 1
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
                dict(
                    s="abcyy",
                    t=2,
                    nums=[
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        2,
                    ],
                ),
                dict(
                    s="azbk",
                    t=1,
                    nums=[
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                        2,
                    ],
                ),
            ],
            "expected": [7, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()

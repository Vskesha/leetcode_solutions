import unittest
from collections import Counter, deque

import numpy as np

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        prev = 1
        dp = deque([1] * 25)
        for _ in range(t):
            dp.append((prev + dp[0]) % mod)
            prev = dp.popleft()
        dp.appendleft(prev)
        return sum(dp[ord(ch) - 97] * v % mod for ch, v in Counter(s).items()) % mod


class Solution1:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = [1] * (t + 26)
        for i in range(26, len(dp)):
            dp[i] = (dp[i - 26] + dp[i - 25]) % 1_000_000_007
        ans = 0
        cnt = Counter(s)
        for k, v in cnt.items():
            ans = (ans + v * dp[(ord(k) - 97) + t]) % 1_000_000_007
        return ans


class Solution2:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        oa = ord("a")
        base = np.zeros((26, 26), dtype=object)
        for i in range(25):
            base[i][i + 1] = 1
        base[25][0] = base[25][1] = 1
        base = np.linalg.matrix_power(base, t)
        data = base.sum(axis=1) % mod
        return sum(data[ord(ch) - oa] * v % mod for ch, v in Counter(s).items()) % mod


class Solution3:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        for _ in range(t):
            cnt = [cnt[i - 1] for i in range(26)]
            cnt[1] = (cnt[1] + cnt[0]) % mod

        return sum(cnt) % mod


class Solution4:
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

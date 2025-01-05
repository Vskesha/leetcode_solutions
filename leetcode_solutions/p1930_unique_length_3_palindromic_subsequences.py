import unittest
from bisect import bisect_left
from collections import defaultdict

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indices = defaultdict(list)
        for i, ch in enumerate(s):
            indices[ch].append(i)
        ans = 0
        vals = list(indices.values())
        for ids1 in vals:
            if len(ids1) < 2:
                continue
            fo, lo = ids1[0] + 1, ids1[-1]
            for ids2 in vals:
                i = bisect_left(ids2, fo)
                if i < len(ids2) and ids2[i] < lo:
                    ans += 1
        return ans


class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        counts = []
        fi = [-1] * 26
        li = [-1] * 26
        cnt = [0] * 26

        for i, ch in enumerate(s):
            chi = ord(ch) - 97
            if fi[chi] == -1:
                fi[chi] = i
            li[chi] = i
            cnt[chi] += 1
            counts.append(cnt.copy())

        ans = 0
        for chi in range(26):
            i, j = fi[chi], li[chi]
            if j > i + 1:
                for a, b in zip(counts[i], counts[j - 1]):
                    ans += (b - a) > 0

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPalindromicSubsequence"] * 3,
            "kwargs": [
                dict(s="aabca"),
                dict(s="adc"),
                dict(s="bbcbaba"),
            ],
            "expected": [3, 0, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        d = Counter()
        for c in s:
            d[c] += 1
            while d[c] == k:
                d[s[l]] -= 1
                l += 1
            ans += l
        return ans


class Solution2:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        ans = 0
        i = 0

        for ch in s:
            cnt[ch] += 1
            if max(cnt.values()) < k:
                continue
            while True:
                cnt[s[i]] -= 1
                if max(cnt.values()) < k:
                    cnt[s[i]] += 1
                    break
                i += 1
            ans += i + 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfSubstrings"] * 2,
            "kwargs": [
                dict(s="abacb", k=2),
                dict(s="abcde", k=1),
            ],
            "expected": [4, 15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

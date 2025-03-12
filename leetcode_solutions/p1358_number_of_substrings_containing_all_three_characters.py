import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i, j = 0, 0
        ls = len(s)
        cnt = {"a": 0, "b": 0, "c": 0}
        ans = 0
        while j < ls:
            cnt[s[j]] += 1
            if all(cnt.values()):
                cnt[s[j]] -= 1
                break
            j += 1
        while j < ls:
            cnt[s[j]] += 1
            while cnt[s[i]] > 1:
                cnt[s[i]] -= 1
                i += 1
            ans += i + 1
            j += 1

        return ans


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        i = ans = 0
        cnt = Counter()
        for ch in s:
            cnt[ch] += 1
            while cnt[s[i]] > 1:
                cnt[s[i]] -= 1
                i += 1
            if len(cnt) == 3:
                ans += i + 1

        return ans


class Solution3:
    def numberOfSubstrings(self, s: str) -> int:
        i, j = 0, 0
        ls = len(s)
        cnt = {}
        ans = 0

        while j < ls and len(cnt) < 3:
            cnt[s[j]] = cnt.get(s[j], 0) + 1
            j += 1

        if len(cnt) < 3:
            return 0
        j -= 1
        cnt[s[j]] -= 1

        while j < ls:
            cnt[s[j]] += 1
            while cnt[s[i]] > 1:
                cnt[s[i]] -= 1
                i += 1
            ans += i + 1
            j += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfSubstrings"] * 3,
            "kwargs": [
                dict(s="abcabc"),
                dict(s="aaacb"),
                dict(s="abc"),
            ],
            "expected": [10, 3, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

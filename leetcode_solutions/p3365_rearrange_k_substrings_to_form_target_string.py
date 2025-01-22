import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s) % k:
            return False
        k = len(s) // k
        cnts = Counter(s[i : i + k] for i in range(0, len(s), k))
        cntt = Counter(t[i : i + k] for i in range(0, len(t), k))
        return cnts == cntt


class Solution2:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s) % k:
            return False
        k = len(s) // k
        cnt = Counter(s[i : i + k] for i in range(0, len(s), k))
        for i in range(0, len(t), k):
            part = t[i : i + k]
            if not cnt[part]:
                return False
            cnt[part] -= 1
        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isPossibleToRearrange"] * 3,
            "kwargs": [
                dict(s="abcd", t="cdab", k=2),
                dict(s="aabbcc", t="bbaacc", k=3),
                dict(s="aabbcc", t="bbaacc", k=2),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

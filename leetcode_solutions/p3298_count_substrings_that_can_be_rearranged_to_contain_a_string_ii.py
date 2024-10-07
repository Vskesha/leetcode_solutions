import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt2 = Counter(word2)
        ln1, ln2 = len(word1), len(word2)
        i = st = 0

        while i < ln1 and ln2:
            if cnt2[word1[i]] > 0:
                cnt2[word1[i]] -= 1
                ln2 -= 1
            i += 1
        if ln2:
            return 0
        i -= 1
        ans = ln1 - i
        cnt1, cnt2 = Counter(word1[:i]), Counter(word2)
        for end in range(i, len(word1)):
            cnt1[word1[end]] += 1
            while cnt1[word1[st]] > cnt2[word1[st]]:
                cnt1[word1[st]] -= 1
                st += 1
                ans += ln1 - end
        return ans


class Solution2:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt2 = Counter(word2)
        ln1, ln2 = len(word1), len(word2)
        i = st = ans = 0

        while i < ln1 and ln2:
            if cnt2[word1[i]] > 0:
                cnt2[word1[i]] -= 1
                ln2 -= 1
            i += 1
        if ln2:
            return 0
        i -= 1
        cnt1, cnt2 = Counter(word1[:i]), Counter(word2)
        ost = -1
        for end in range(i, len(word1)):
            cnt1[word1[end]] += 1
            while cnt1[word1[st]] > cnt2[word1[st]]:
                cnt1[word1[st]] -= 1
                st += 1
            ans += (ln1 - end) * (st - ost)
            ost = st
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["validSubstringCount"] * 3,
            "kwargs": [
                dict(word1="bcca", word2="abc"),
                dict(word1="abcabc", word2="abc"),
                dict(word1="abcabc", word2="aaabc"),
            ],
            "expected": [1, 10, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

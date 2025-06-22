import unittest
from collections import Counter
from itertools import accumulate

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        freq = sorted(cnt.values())
        acc = list(accumulate(freq, initial=0))
        ans = len(word)
        bi, lf = 0, len(freq)

        for i, fr in enumerate(freq):
            fr += k
            while bi < lf and freq[bi] <= fr:
                bi += 1
            del_total = acc[i] + acc[-1] - acc[bi] - fr * (lf - bi)
            if del_total < ans:
                ans = del_total

        return ans


class Solution2:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        freq = sorted(cnt.values())
        acc = list(accumulate(freq, initial=0))

        ans = len(word)
        bi, lf = 0, len(freq)

        for i, fr in enumerate(freq):
            del_before = acc[i]
            while bi < lf and freq[bi] <= fr + k:
                bi += 1
            num_bigger = lf - bi
            del_after = acc[-1] - acc[bi] - (fr + k) * num_bigger
            del_total = del_before + del_after
            if del_total < ans:
                ans = del_total

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumDeletions"] * 3,
            "kwargs": [
                dict(word="aabcaba", k=0),
                dict(word="dabdcbdcdcd", k=2),
                dict(word="aaabaaa", k=2),
            ],
            "expected": [3, 2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

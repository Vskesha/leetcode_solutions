import unittest
from collections import Counter
from itertools import groupby

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestBalanced(self, s: str) -> int:
        ls = len(s)
        max_single_len = 0

        for k, gr in groupby(s):
            lgr = len(list(gr))
            if lgr > max_single_len:
                max_single_len = lgr

        if max_single_len == ls:
            return max_single_len

        def get_two_chars_strings(ss):
            sti = 0
            scnt = {"a": 0, "b": 0, "c": 0}
            for eni, sch in enumerate(ss):
                scnt[sch] += 1
                if 0 not in scnt.values():
                    yield ss[sti:eni]
                    while 0 not in scnt.values():
                        scnt[ss[sti]] -= 1
                        sti += 1
            yield ss[sti:]

        max_double_len = 0
        for s2 in get_two_chars_strings(s):
            diffs = {0: -1}
            ch1, ch2 = set(s2)
            cnt = Counter()
            for i, ch in enumerate(s2):
                cnt[ch] += 1
                diff = cnt[ch1] - cnt[ch2]
                if diff in diffs:
                    pi = diffs[diff]
                    max_double_len = max(max_double_len, i - pi)
                else:
                    diffs[diff] = i

        if max_double_len > ls * 2 / 3:
            return max_double_len

        max_triple_len = 0
        diffs = {(0, 0): -1}
        cnt = Counter()

        for i, ch in enumerate(s):
            cnt[ch] += 1
            diff = (cnt["a"] - cnt["b"], cnt["b"] - cnt["c"])
            if diff in diffs:
                pi = diffs[diff]
                max_triple_len = max(max_triple_len, i - pi)
            else:
                diffs[diff] = i

        return max(max_single_len, max_double_len, max_triple_len)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestBalanced"] * 4,
            "kwargs": [
                dict(s="abbac"),
                dict(s="aabcc"),
                dict(s="aba"),
                dict(s="ccaca"),
            ],
            "expected": [4, 3, 2, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

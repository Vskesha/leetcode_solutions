import unittest
from itertools import groupby

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        for k, gr in groupby(word):
            lg = len(list(gr))
            while lg > 9:
                comp += "9" + k
                lg -= 9
            comp += str(lg) + k
        return comp


class Solution2:
    def compressedString(self, word: str) -> str:
        i = 0
        comp = ""
        lw = len(word)

        while i < lw:
            ch = word[i]
            cnt = 0
            while i < lw and cnt < 9 and word[i] == ch:
                i += 1
                cnt += 1
            comp += str(cnt) + ch

        return comp


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["compressedString"] * 2,
            "kwargs": [
                dict(word="abcde"),
                dict(word="aaaaaaaaaaaaaabb"),
            ],
            "expected": ["1a1b1c1d1e", "9a5a2b"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

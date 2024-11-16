import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        prefix = ""
        for ch in target:
            for n in range(ord("a"), ord(ch) + 1):
                ans.append(prefix + chr(n))
            prefix += ch
        return ans


class Solution2:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        s = []
        for i, ch in enumerate(target):
            s.append("a")
            ans.append("".join(s))
            while s[-1] != ch:
                s[-1] = chr(ord(s[-1]) + 1)
                ans.append("".join(s))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["stringSequence"] * 2,
            "kwargs": [
                dict(target="abc"),
                dict(target="he"),
            ],
            "expected": [
                ["a", "aa", "ab", "aba", "abb", "abc"],
                ["a", "b", "c", "d", "e", "f", "g", "h", "ha", "hb", "hc", "hd", "he"],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

import string
import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ds = {ch: ch for ch in string.ascii_lowercase}

        def find(ch):
            if ds[ch] == ch:
                return ch
            ds[ch] = find(ds[ch])
            return ds[ch]

        for ch1, ch2 in zip(s1, s2):
            root1 = find(ch1)
            root2 = find(ch2)
            if root1 < root2:
                ds[root2] = root1
            elif root1 > root2:
                ds[root1] = root2

        return "".join(find(ch) for ch in baseStr)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestEquivalentString"] * 3,
            "kwargs": [
                dict(s1="parker", s2="morris", baseStr="parser"),
                dict(s1="hello", s2="world", baseStr="hold"),
                dict(s1="leetcode", s2="programs", baseStr="sourcecode"),
            ],
            "expected": ["makkek", "hdld", "aauaaaaada"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

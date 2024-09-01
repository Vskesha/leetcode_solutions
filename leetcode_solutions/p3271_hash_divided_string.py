import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        return "".join(
            chr(sum(ord(ch) - 97 for ch in s[i : i + k]) % 26 + 97)
            for i in range(0, len(s), k)
        )


class Solution2:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        orda = ord("a")

        for i in range(0, len(s), k):
            h = 0
            for j in range(i, i + k):
                h += ord(s[j]) - orda
            res += chr(h % 26 + orda)

        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["stringHash"] * 2,
            "kwargs": [
                dict(s="abcd", k=2),
                dict(s="mxz", k=3),
            ],
            "expected": ["bf", "i"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

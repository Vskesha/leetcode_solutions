import unittest
from itertools import pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def modifyString(self, s: str) -> str:
        res, ls = list(s), len(s)

        for i in range(ls):
            if res[i] == "?":
                res[i] = (
                    {"a", "b", "c"}
                    .difference(
                        {
                            res[i - 1] if i else "?",
                            res[i + 1] if i < ls - 1 else "?",
                        }
                    )
                    .pop()
                )

        return "".join(res)


class Solution2:
    def modifyString(self, s: str) -> str:
        rp = "abc"
        prev = "?"
        nxt = s[0]
        res = []
        for i in range(1, len(s)):
            ch = nxt
            nxt = s[i]
            if ch == "?":
                for r in rp:
                    if r != prev and r != nxt:
                        ch = r
                        break
            res.append(ch)
            prev = ch
        if s[-1] == "?":
            if not res or res[-1] == "b":
                res.append("a")
            else:
                res.append("b")
        else:
            res.append(s[-1])

        return "".join(res)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["modifyString"] * 2,
            "kwargs": [
                dict(s="?zs"),
                dict(s="ubv?w"),
            ],
            "expected": ["azs", "ubvaw"],
            "assert_methods": ["asseertNoConsecutiveRepeatingCharacters"] * 2,
        },
    ]

    def asseertNoConsecutiveRepeatingCharacters(self, s1: str, s2: str):
        self.assertEqual(len(s1), len(s2))
        for a, b in pairwise(s1):
            self.assertNotEqual(a, b)
        for a, b in pairwise(s2):
            self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()

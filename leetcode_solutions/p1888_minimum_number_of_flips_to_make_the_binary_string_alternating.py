import unittest
from itertools import accumulate, cycle

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minFlips(self, s: str) -> int:
        ls = len(s)

        if ls % 2 == 0:
            ch = sum(a != b for a, b in zip(s, cycle("01")))
            return min(ch, ls - ch)

        chs = list(
            accumulate(
                (int(a != b) for a, b in zip(s, cycle("01"))), initial=0
            )
        )

        gch = chs[-1]
        return min(
            min(i + gch - ch - ch, ls - i - gch + ch + ch)
            for i, ch in enumerate(chs)
        )


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minFlips"] * 3,
            "kwargs": [
                dict(s="111000"),
                dict(s="010"),
                dict(s="1110"),
            ],
            "expected": [2, 0, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

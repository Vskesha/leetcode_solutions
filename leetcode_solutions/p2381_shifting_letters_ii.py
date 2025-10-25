import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shs = [0] * (len(s) + 1)
        for i, j, d in shifts:
            d = d or -1
            shs[i] += d
            shs[j + 1] -= d

        return "".join(
            chr((ord(ch) - 97 + sh) % 26 + 97)
            for ch, sh in zip(s, accumulate(shs))
        )


class Solution2:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shs = [0] * (len(s) + 1)

        for i, j, d in shifts:
            d = d * 2 - 1
            shs[i] += d
            shs[j + 1] -= d

        ans = []
        sh = 0
        for i, ch in enumerate(s):
            sh = sh + shs[i]
            chi = ord(ch) - 97
            chi = (chi + sh) % 26
            ans.append(chr(chi + 97))

        return "".join(ans)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["shiftingLetters"] * 2,
            "kwargs": [
                dict(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]),
                dict(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]]),
            ],
            "expected": ["ace", "catz"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

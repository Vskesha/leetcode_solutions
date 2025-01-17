import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        acc_next = list(accumulate(nextCost * 2, initial=0))
        acc_prev = list(accumulate(previousCost * 2, initial=0))
        ans = 0
        for a, b in zip(s, t):
            ia, ib = ord(a) - 97, ord(b) - 97
            if ia < ib:
                fowd = acc_next[ib] - acc_next[ia]
                ia += 26
                back = acc_prev[ia + 1] - acc_prev[ib + 1]
            else:
                back = acc_prev[ia + 1] - acc_prev[ib + 1]
                ib += 26
                fowd = acc_next[ib] - acc_next[ia]
            ans += min(back, fowd)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["shiftDistance"] * 2,
            "kwargs": [
                dict(
                    s="abab",
                    t="baba",
                    nextCost=[
                        100,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    previousCost=[
                        1,
                        100,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                ),
                dict(
                    s="leet",
                    t="code",
                    nextCost=[
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                    ],
                    previousCost=[
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                    ],
                ),
            ],
            "expected": [2, 31],
        },
    ]


if __name__ == "__main__":
    unittest.main()

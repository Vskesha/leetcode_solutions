import unittest
from bisect import bisect_right
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        return bisect_right(acc := list(accumulate(chalk)), k % acc[-1])


class Solution2:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        acc = list(accumulate(chalk))
        tot = acc[-1]
        rem = k % tot
        ans = bisect_right(acc, rem)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["chalkReplacer"] * 2,
            "kwargs": [
                dict(chalk=[5, 1, 5], k=22),
                dict(chalk=[3, 4, 1, 2], k=25),
            ],
            "expected": [0, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from itertools import pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def binaryGap(self, n: int) -> int:
        ans = pi = 0
        for i, b in enumerate(bin(n)[2:]):
            if b == "1":
                ans = max(ans, i - pi)
                pi = i
        return ans


# fmt: off
class Solution2:
    def binaryGap(self, n: int) -> int:
        return max((j - i for i, j in pairwise(k for k, b in enumerate(bin(n)) if b == "1")), default=0)  # noqa
# fmt: on


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["binaryGap"] * 3,
            "kwargs": [
                dict(n=22),
                dict(n=8),
                dict(n=5),
            ],
            "expected": [2, 0, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

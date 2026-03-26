import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        mt = 0
        ans = 0
        for pos, sp in sorted(zip(position, speed), reverse=True):
            cmt = (target - pos) / sp
            if cmt > mt:
                mt = cmt
                ans += 1
        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["carFleet"] * 3,
            "kwargs": [
                dict(
                    target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]
                ),
                dict(target=10, position=[3], speed=[3]),
                dict(target=100, position=[0, 2, 4], speed=[4, 2, 1]),
            ],
            "expected": [3, 1, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

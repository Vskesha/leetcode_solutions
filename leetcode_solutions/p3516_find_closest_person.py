import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x - z), abs(y - z)
        return 1 if d1 < d2 else 2 if d1 > d2 else 0


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findClosest"] * 3,
            "kwargs": [
                dict(x=2, y=7, z=4),
                dict(x=2, y=5, z=6),
                dict(x=1, y=5, z=3),
            ],
            "expected": [1, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

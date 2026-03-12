import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int("".join("1" if d == "0" else "0" for d in bin(n)[2:]), 2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["bitwiseComplement"] * 2,
            "kwargs": [
                dict(n=5),
                dict(n=7),
                dict(n=10),
            ],
            "expected": [2, 0, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

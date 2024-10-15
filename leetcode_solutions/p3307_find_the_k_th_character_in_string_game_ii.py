import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lo = len(operations)
        ls = pow(2, lo)
        shift = 0

        while k > 1:
            ls //= 2
            lo -= 1
            if k > ls:
                k -= ls
                shift += operations[lo]

        return chr(shift % 26 + 97)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["kthCharacter"] * 3,
            "kwargs": [
                dict(k=5, operations=[0, 0, 0]),
                dict(k=10, operations=[0, 1, 0, 1]),
                dict(
                    k=100000000000000,
                    operations=[
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
            "expected": ["a", "b", "e"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

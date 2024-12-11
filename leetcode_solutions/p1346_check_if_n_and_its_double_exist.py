import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if n in seen:
                return True
            seen.add(n * 2)
            if not n % 2:
                seen.add(n // 2)
        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkIfExist"] * 2,
            "kwargs": [
                dict(arr=[10, 2, 5, 3]),
                dict(arr=[3, 1, 7, 11]),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

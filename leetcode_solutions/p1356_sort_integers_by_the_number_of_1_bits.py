import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


class Solution2:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sortByBits"] * 2,
            "kwargs": [
                dict(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]),
                dict(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
            ],
            "expected": [
                [0, 1, 2, 4, 8, 3, 5, 6, 7],
                [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

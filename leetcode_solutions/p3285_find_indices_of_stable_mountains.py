import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["stableMountains"] * 3,
            "kwargs": [
                dict(height=[1, 2, 3, 4, 5], threshold=2),
                dict(height=[10, 1, 10, 1, 10], threshold=3),
                dict(height=[10, 1, 10, 1, 10], threshold=10),
            ],
            "expected": [[3, 4], [1, 3], []],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

import math
import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        total_operations = 0
        for left, right in queries:
            power4 = int(math.log(left, 4)) + 1
            end = pow(4, power4)
            single_operations = 0

            while end <= right:
                elements = end - left
                single_operations += elements * power4
                power4 += 1
                left = end
                end *= 4
            elements = right - left + 1
            single_operations += elements * power4

            total_operations += (single_operations + 1) // 2

        return total_operations


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 3,
            "kwargs": [
                dict(queries = [[1,2],[2,4]]),
                dict(queries = [[2,6]]),
                dict(queries = [[13,16]]),
            ],
            "expected": [3, 4, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

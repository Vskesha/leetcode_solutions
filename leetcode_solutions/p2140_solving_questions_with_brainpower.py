import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        lq = len(questions)
        result = [0] * lq
        result[-1] = questions[-1][0]

        for i in range(lq - 2, -1, -1):
            points, skip = questions[i]
            j = i + skip + 1
            if j >= lq:
                result[i] = max(result[i + 1], points)
            else:
                result[i] = max(result[i + 1], points + result[j])

        return result[0]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["mostPoints"] * 3,
            "kwargs": [
                dict(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]),
                dict(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]),
                dict(questions=[[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]]),
            ],
            "expected": [5, 7, 79],
        },
    ]


if __name__ == "__main__":
    unittest.main()

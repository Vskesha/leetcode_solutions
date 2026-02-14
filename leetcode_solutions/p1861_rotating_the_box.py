import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box[0])
        st, ob = "#", "*"

        for row in box:
            ri = n - 1
            for li in range(n - 1, -1, -1):
                if row[li] == st:
                    row[li] = row[ri]
                    row[ri] = st
                    ri -= 1
                elif row[li] == ob:
                    ri = li - 1

        return list(map(list, zip(*box[::-1])))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["rotateTheBox"] * 3,
            "kwargs": [
                dict(box=[["#", ".", "#"]]),
                dict(box=[["#", ".", "*", "."], ["#", "#", "*", "."]]),
                dict(
                    box=[
                        ["#", "#", "*", ".", "*", "."],
                        ["#", "#", "#", "*", ".", "."],
                        ["#", "#", "#", ".", "#", "."],
                    ]
                ),
            ],
            "expected": [
                [["."], ["#"], ["#"]],
                [["#", "."], ["#", "#"], ["*", "*"], [".", "."]],
                [
                    [".", "#", "#"],
                    [".", "#", "#"],
                    ["#", "#", "*"],
                    ["#", "*", "."],
                    ["#", ".", "*"],
                    ["#", ".", "."],
                ],
            ],
            "assert_methods": ["assertBoxEqual"] * 3,
        },
    ]

    def assertBoxEqual(
        self, actual: List[List[int]], expected: List[List[int]]
    ) -> None:
        self.assertEqual(len(actual), len(expected))
        for a, b in zip(actual, expected):
            self.assertListEqual(a, b)


if __name__ == "__main__":
    unittest.main()

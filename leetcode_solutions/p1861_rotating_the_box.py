import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        st, ob, em = "#", "*", "."

        for row in box:
            r = n - 1
            for l in range(n - 1, -1, -1):
                if row[l] == st:
                    row[l] = row[r]
                    row[r] = st
                    r -= 1
                elif row[l] == ob:
                    r = l - 1

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

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        nines, left = divmod(sum, 9)
        if nines == num:
            return "9" * nines
        return "9" * nines + str(left) + "0" * (num - nines - 1)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxSumOfSquares"] * 3,
            "kwargs": [
                dict(num=2, sum=3),
                dict(num=2, sum=17),
                dict(num=1, sum=10),
            ],
            "expected": ["30", "98", ""],
        },
    ]


if __name__ == "__main__":
    unittest.main()

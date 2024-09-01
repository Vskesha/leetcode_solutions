import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = str(num1).zfill(4)
        num2 = str(num2).zfill(4)
        num3 = str(num3).zfill(4)

        res = ""
        for ns in zip(num1, num2, num3):
            res += min(ns)

        res = res.lstrip("0")

        return int(res) if res else 0


class Solution2:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        vals = [str(x).zfill(4) for x in (num1, num2, num3)]
        return int("".join(map(min, zip(*vals))))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["generateKey"] * 3,
            "kwargs": [
                dict(num1=1, num2=10, num3=1000),
                dict(num1=987, num2=879, num3=798),
                dict(num1=1, num2=2, num3=3),
            ],
            "expected": [0, 777, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join("0" if x == "1" else "1" for x in bin(num)[2:]), 2)


class Solution1:
    def findComplement(self, num: int) -> int:
        return int("".join(str(1 - int(x)) for x in bin(num)[2:]), 2)


class Solution2:
    def findComplement(self, num: int) -> int:
        res = 0
        p = 1
        while num:
            num, m = divmod(num, 2)
            res += (1 - m) * p
            p *= 2
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findComplement"] * 2,
            "kwargs": [
                dict(num=5),
                dict(num=1),
            ],
            "expected": [2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

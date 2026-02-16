import unittest
from itertools import zip_longest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        add = 0

        for x, y in zip_longest(
            map(int, reversed(a)), map(int, reversed(b)), fillvalue=0
        ):
            add, cur = divmod(x + y + add, 2)
            res.append(cur)

        if add:
            res.append(add)

        return "".join(map(str, reversed(res)))


class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        for a, b in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry, bit = divmod(int(a) + int(b) + carry, 2)
            res.append(str(bit))
        if carry:
            res.append("1")
        return "".join(reversed(res))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["addBinary"] * 2,
            "kwargs": [
                dict(a="11", b="1"),
                dict(a="1010", b="1011"),
            ],
            "expected": ["100", "10101"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

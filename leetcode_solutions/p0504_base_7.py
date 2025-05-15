import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = num < 0
        if negative:
            num = -num
        ans = []
        while num:
            ans.append(str(num % 7))
            num //= 7
        if negative:
            ans.append("-")
        return "".join(reversed(ans)) or "0"


class Solution2:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"
        ans = []
        if num < 0:
            num = -num
            ans.append("-")
        d = 1
        while d <= num:
            d *= 7
        d //= 7
        while d:
            ans.append(str(num // d))
            num %= d
            d //= 7

        return "".join(ans)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["convertToBase7"] * 2,
            "kwargs": [
                dict(num=100),
                dict(num=-7),
            ],
            "expected": ["202", "-10"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

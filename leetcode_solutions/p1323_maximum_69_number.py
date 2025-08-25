import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


class Solution2:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        i = str_num.find("6")
        return int(str_num if i == -1 else str_num[:i] + "9" + str_num[i + 1:])


class Solution3:
    def maximum69Number (self, num: int) -> int:
        seen = False
        result = []
        for digit in str(num):
            if digit == "6" and not seen:
                result.append("9")
                seen = True
            else:
                result.append(digit)
        return int("".join(result))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximum69Number"] * 3,
            "kwargs": [
                dict(num = 9669),
                dict(num = 9996),
                dict(num = 9999),
            ],
            "expected": [9969, 9999, 9999],
        },
    ]


if __name__ == "__main__":
    unittest.main()

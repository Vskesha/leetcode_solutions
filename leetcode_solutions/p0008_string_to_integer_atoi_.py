import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        its = iter(s)
        res = []

        for ch in its:
            if ch != " ":
                break

        if ch in "+-":
            res.append(ch)
            ch = next(its, "z")

        while ch.isdigit():
            res.append(ch)
            ch = next(its, "z")

        if not res:
            return 0
        if not res[-1].isdigit():
            return 0

        number = int("".join(res))

        p2 = pow(2, 31)
        if number < -p2:
            return -p2
        if number >= p2:
            return p2 - 1
        return number


class Solution2:
    def myAtoi(self, s: str) -> int:
        result = []

        for ch in s:
            if ch.isdigit():
                result.append(ch)
            elif ch in "+-":
                if result:
                    break
                result.append(ch)
            elif ch == " ":
                if result:
                    break
            else:
                break

        if not result:
            return 0
        if not result[-1].isdigit():
            return 0

        number = int("".join(result))

        mn = pow(2, 31)
        if number < -mn:
            return -mn
        if number > mn - 1:
            return mn - 1
        return number


class Solution3:
    def myAtoi(self, s: str) -> int:
        sign = ""
        number = ""
        i, l = 0, len(s)
        while i < l and s[i] == " ":
            i += 1
        if i < l and (s[i] == "+" or s[i] == "-"):
            sign = s[i]
            i += 1
        while i < l and s[i].isnumeric():
            number += s[i]
            i += 1
        if number:
            x = int(sign + number)
        else:
            return 0
        if x < -(2**31):
            return -(2**31)
        if x > 2**31 - 1:
            return 2**31 - 1
        return x


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["myAtoi"] * 5,
            "kwargs": [
                dict(s="42"),
                dict(s=" -042"),
                dict(s="1337c0d3"),
                dict(s="0-1"),
                dict(s="words and 987"),
            ],
            "expected": [42, -42, 1337, 0, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

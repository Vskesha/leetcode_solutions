import unittest
from fractions import Fraction
from math import gcd

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def fractionAddition(self, expression: str) -> str:
        ans, st = Fraction(), 0
        for i in range(1, len(expression)):
            if expression[i] in "+-":
                ans += Fraction(expression[st:i])
                st = i
        ans += Fraction(expression[st:])
        return f"{ans.numerator}/{ans.denominator}"


class Solution1:
    def fractionAddition(self, expression: str) -> str:
        nom, nom1, den, den1 = 0, 0, 1, 1
        st = 0
        for i in range(1, len(expression)):
            ch = expression[i]
            if ch == "/":
                nom1 = int(expression[st:i])
                st = i + 1
            elif ch == "+" or ch == "-":
                den1 = int(expression[st:i])
                st = i
                nom, den = nom * den1 + nom1 * den, den * den1
        den1 = int(expression[st:])
        nom, den = nom * den1 + nom1 * den, den * den1
        gd = gcd(nom, den)
        nom, den = nom // gd, den // gd

        return f"{nom}/{den}"


class Solution2:
    def fractionAddition(self, expression: str) -> str:
        ans = Fraction()
        st = 0
        for i in range(1, len(expression)):
            if expression[i] in "+-":
                expr = expression[st:i]
                fr = Fraction(expr)
                ans += fr
                st = i
        expr = expression[st:]
        fr = Fraction(expr)
        ans += fr
        ans = f"{ans.numerator}/{ans.denominator}"
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["fractionAddition"] * 3,
            "args": [
                [],
            ],
            "kwargs": [
                dict(expression="-1/2+1/2"),
                dict(expression="-1/2+1/2+1/3"),
                dict(expression="1/3-1/2"),
            ],
            "expected": ["0/1", "1/3", "-1/6"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

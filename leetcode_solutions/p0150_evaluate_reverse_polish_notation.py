import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                x = st.pop()
                st[-1] += x
            elif t == "-":
                x = st.pop()
                st[-1] -= x
            elif t == "*":
                x = st.pop()
                st[-1] *= x
            elif t == "/":
                x = st.pop()
                sign = (st[-1] < 0) ^ (x < 0)
                st[-1] = abs(st[-1]) // abs(x)
                if sign:
                    st[-1] *= -1
            else:
                st.append(int(t))

        return st[-1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class":  Solution,
            "class_methods": ["evalRPN"] * 3,
            "kwargs": [
                dict(tokens=["2", "1", "+", "3", "*"]),
                dict(tokens=["4", "13", "5", "/", "+"]),
                dict(
                    tokens=[
                        "10",
                        "6",
                        "9",
                        "3",
                        "+",
                        "-11",
                        "*",
                        "/",
                        "*",
                        "17",
                        "+",
                        "5",
                        "+",
                    ]
                ),
            ],
            "expected": [9, 6, 22],
        },
    ]


if __name__ == "__main__":
    unittest.main()

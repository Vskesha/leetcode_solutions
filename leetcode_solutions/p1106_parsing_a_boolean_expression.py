import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return True if expression[0] == "t" else False
        if expression[0] == "!":
            return not self.parseBoolExpr(expression[2:-1])

        exps, exp, op = [], "", 0
        for ch in expression[2:-1]:
            if ch == "," and op == 0:
                exps.append(exp)
                exp = ""
            else:
                exp += ch
                if ch == "(":
                    op += 1
                elif ch == ")":
                    op -= 1
        exps.append(exp)

        if expression[0] == "&":
            return all(self.parseBoolExpr(exp) for exp in exps)
        return any(self.parseBoolExpr(exp) for exp in exps)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["parseBoolExpr"] * 4,
            "kwargs": [
                dict(expression="&(|(f))"),
                dict(expression="|(f,f,f,t)"),
                dict(expression="!(&(f,t))"),
                dict(expression="|(&(t,f,t),!(t))"),
            ],
            "expected": [False, True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

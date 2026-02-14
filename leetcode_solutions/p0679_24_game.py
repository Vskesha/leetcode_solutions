import unittest
from functools import cache, reduce
from itertools import permutations, product
from math import inf, isclose
from operator import add, mul, sub, truediv
from typing import List


def div(x, y):
    return reduce(truediv, (x, y)) if y else inf


ops = (add, sub, mul, div)


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        operations = (
            lambda x, y: x + y,
            lambda x, y: x - y,
            lambda x, y: x * y,
            lambda x, y: (x / y) if y else inf,
        )

        @cache
        def dfs(*args) -> bool:
            if len(args) == 1:
                return isclose(args[0], 24)

            for a, b, *c in permutations(args):
                for operation in operations:
                    if dfs(operation(a, b), *c):
                        return True

            return False

        return dfs(*cards)


class Solution2:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(c: list) -> bool:
            if len(c) < 2:
                return isclose(c[0], 24)

            for p in set(permutations(c)):
                for num in {reduce(op, p[:2]) for op in ops}:
                    if dfs([num] + list(p[2:])):
                        return True

            return False

        return dfs(cards)


class Solution3:
    def judgePoint24(self, cards: List[int]) -> bool:
        for n1, n2, n3, n4 in permutations(cards, r=4):
            for op1, op2, op3 in product("+-*/", repeat=3):
                for expression in (
                    f"{n1} {op1} {n2} {op2} {n3} {op3} {n4}",
                    f"({n1} {op1} {n2}) {op2} {n3} {op3} {n4}",
                    f"({n1} {op1} {n2} {op2} {n3}) {op3} {n4}",
                    f"{n1} {op1} ({n2} {op2} {n3}) {op3} {n4}",
                    f"{n1} {op1} ({n2} {op2} {n3} {op3} {n4})",
                    f"{n1} {op1} {n2} {op2} ({n3} {op3} {n4})",
                    f"({n1} {op1} {n2}) {op2} ({n3} {op3} {n4})",
                    f"(({n1} {op1} {n2}) {op2} {n3}) {op3} {n4}",
                    f"({n1} {op1} ({n2} {op2} {n3})) {op3} {n4}",
                    f"{n1} {op1} (({n2} {op2} {n3}) {op3} {n4})",
                    f"{n1} {op1} ({n2} {op2} ({n3} {op3} {n4}))",
                ):
                    try:
                        result = round(eval(expression), 1)
                        # print(expression, "=", result)
                        if result == 24.0:
                            return True
                    except ZeroDivisionError:
                        pass
        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_judge_point_24_1(self):
        print("Test judgePoint24 1 ... ", end="")
        self.assertTrue(self.sol.judgePoint24([4, 1, 8, 7]))
        print("OK")

    def test_judge_point_24_2(self):
        print("Test judgePoint24 2 ... ", end="")
        self.assertFalse(self.sol.judgePoint24([1, 2, 1, 2]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

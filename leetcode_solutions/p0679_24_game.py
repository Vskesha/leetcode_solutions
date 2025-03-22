import unittest
from functools import reduce
from itertools import permutations
from math import inf, isclose
from operator import add, mul, sub, truediv
from typing import List

div = lambda x, y: reduce(truediv, (x, y)) if y else inf
ops = (add, sub, mul, div)


class Solution:
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

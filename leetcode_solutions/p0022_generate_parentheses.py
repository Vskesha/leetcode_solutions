import unittest
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = ["()"]
        for _ in range(n - 1):
            new = set()
            for comb in result:
                for i in range(len(comb) + 1):
                    new.add(comb[:i] + "()" + comb[i:])
            result = list(new)
        return result


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def gp(n, o, c, s):
            if n == o == c:
                return [s]
            r = []
            if o < n:
                r.extend(gp(n, o + 1, c, s + "("))
            if c < o:
                r.extend(gp(n, o, c + 1, s + ")"))
            return r

        return gp(n, 0, 0, "")


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def contains_all_combinations(self, list1, list2):
        return set(list1) == set(list2)

    def test_generate_parenthesis_1(self):
        print("Test generateParenthesis 1 ... ", end="")
        self.assertTrue(
            self.contains_all_combinations(
                self.sol.generateParenthesis(n=3),
                ["((()))", "(()())", "(())()", "()(())", "()()()"],
            )
        )
        print("OK")

    def test_generate_parenthesis_2(self):
        print("Test generateParenthesis 2 ... ", end="")
        self.assertTrue(
            self.contains_all_combinations(self.sol.generateParenthesis(n=1), ["()"])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        lf = len(formula)

        while i < lf:
            el = formula[i]
            if el.isupper():
                n = 0
                i += 1
                while i < lf and formula[i].islower():
                    el += formula[i]
                    i += 1
                while i < lf and formula[i].isdigit():
                    n = n * 10 + int(formula[i])
                    i += 1
                n = n or 1
                stack[-1][el] += n
            elif el == "(":
                stack.append(Counter())
                i += 1
            elif el == ")":
                i += 1
                n = 0
                while i < lf and formula[i].isdigit():
                    n = n * 10 + int(formula[i])
                    i += 1
                n = n or 1
                cnt = stack.pop()
                stack[-1] += {el: q * n for el, q in cnt.items()}
        cnt = stack.pop()
        ans = ""
        for el in sorted(cnt.keys()):
            ans += el
            if cnt[el] != 1:
                ans += str(cnt[el])
        return ans


class Solution2:
    def countOfAtoms(self, formula: str) -> str:
        def add():
            k = number or 1
            if closed:
                last_counter = stack.pop()
                for elem, quantity in last_counter.items():
                    stack[-1][elem] += quantity * k
            elif element:
                stack[-1][element] += k

        stack = [Counter()]
        number, element = 0, ""
        closed = False

        for c in formula + "A":
            if c.isupper():
                add()
                number, element, closed = 0, c, False
            elif c.isdigit():
                number = number * 10 + int(c)
            elif c == "(":
                add()
                number, element, closed = 0, "", False
                stack.append(Counter())
            elif c == ")":
                add()
                number, element, closed = 0, "", True
            else:
                element += c

        c = stack[-1]
        return "".join(
            el if c[el] == 1 else el + str(c[el]) for el in sorted(c.keys())
        )


class Solution3:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        lf = len(formula)

        while i < lf:
            if formula[i] == "(":
                stack.append(Counter())
                i += 1
            elif formula[i] == ")":
                counter = stack.pop()
                i += 1
                st = i
                while i < lf and formula[i].isdigit():
                    i += 1
                n = int(formula[st:i] or 1)
                for el, qty in counter.items():
                    stack[-1][el] += qty * n
            else:
                el = formula[i]
                i += 1
                while i < lf and formula[i].islower():
                    el += formula[i]
                    i += 1
                st = i
                while i < lf and formula[i].isdigit():
                    i += 1
                n = int(formula[st:i] or 1)
                stack[-1][el] += n

        c = stack[-1]
        return "".join(
            el + str(c[el]) if c[el] > 1 else el for el in sorted(c.keys())
        )


class TestSolution(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.sol = Solution()

    def test_count_of_atoms(self):
        print("Test countOfAtoms 1... ", end="")
        self.assertEqual(self.sol.countOfAtoms(formula="H2O"), "H2O")
        print("OK")

    def test_count_of_atoms_2(self):
        print("Test countOfAtoms 2... ", end="")
        self.assertEqual(self.sol.countOfAtoms(formula="Mg(OH)2"), "H2MgO2")
        print("OK")

    def test_count_of_atoms_3(self):
        print("Test countOfAtoms 3... ", end="")
        self.assertEqual(
            self.sol.countOfAtoms(formula="K4(ON(SO3)2)2"), "K4N2O14S4"
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

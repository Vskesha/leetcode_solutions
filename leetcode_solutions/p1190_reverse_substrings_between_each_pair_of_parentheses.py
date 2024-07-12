import unittest


class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = [""]
        for c in s:
            if c == "(":
                st.append("")
            elif c == ")":
                prev = st.pop()[::-1]
                st[-1] += prev
            else:
                st[-1] += c
        return st.pop()


class Solution2:
    def reverseParentheses(self, s: str) -> str:
        st = [[]]
        for c in s:
            if c == "(":
                st.append([])
            elif c == ")":
                prev = st.pop()[::-1]
                st[-1].extend(prev)
            else:
                st[-1].append(c)
        return "".join(st[0])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_reverse_parentheses_1(self):
        print("Test reverseParentheses 1... ", end="")
        self.assertEqual(self.sol.reverseParentheses(s="(abcd)"), "dcba")
        print("OK")

    def test_reverse_parentheses_2(self):
        print("Test reverseParentheses 2... ", end="")
        self.assertEqual(self.sol.reverseParentheses(s="(u(love)i)"), "iloveu")
        print("OK")

    def test_reverse_parentheses_3(self):
        print("Test reverseParentheses 3... ", end="")
        self.assertEqual(self.sol.reverseParentheses(s="(ed(et(oc))el)"), "leetcode")
        print("OK")


if __name__ == "__main__":
    unittest.main()

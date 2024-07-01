import unittest


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


class Solution2:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_make_good_1(self):
        print("Test makeGood 1... ", end="")
        self.assertEqual(self.sol.makeGood(s="leEeetcode"), "leetcode")
        print("OK")

    def test_make_good_2(self):
        print("Test makeGood 2... ", end="")
        self.assertEqual(self.sol.makeGood(s="abBAcC"), "")
        print("OK")


if __name__ == "__main__":
    unittest.main()

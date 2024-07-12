import unittest


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s
        return ""


class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        ls = len(s)

        for i in range((ls - 1) // 2, -1, -1):
            for j in range(2):
                l, r = i, i + j
                while l >= 0 and r < ls and s[l] == s[r]:
                    l, r = l - 1, r + 1
                if l == -1:
                    return s[r:][::-1] + s


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_shortest_palindrome_1(self):
        print("Test shortestPalindrome 1... ", end="")
        self.assertEqual(self.sol.shortestPalindrome(s="aacecaaa"), "aaacecaaa")
        print("OK")

    def test_shortest_palindrome_2(self):
        print("Test shortestPalindrome 2... ", end="")
        self.assertEqual(self.sol.shortestPalindrome(s="abcd"), "dcbabcd")
        print("OK")

    def test_shortest_palindrome_3(self):
        print("Test shortestPalindrome 3... ", end="")
        self.assertEqual(self.sol.shortestPalindrome(s="abbacd"), "dcabbacd")
        print("OK")


if __name__ == "__main__":
    unittest.main()

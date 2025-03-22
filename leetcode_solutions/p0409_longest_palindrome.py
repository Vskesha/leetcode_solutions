import unittest
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = len(s)
        has_odd = 0
        for c, q in Counter(s).items():
            if q % 2:
                has_odd = 1
                ans -= 1
        return ans + has_odd


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_longest_palindrome1(self):
        print("Test longestPalindrome 1 ... ", end="")
        self.assertEqual(self.sol.longestPalindrome(s="abccccdd"), 7)
        print("OK")

    def test_longest_palindrome2(self):
        print("Test longestPalindrome 2 ... ", end="")
        self.assertEqual(self.sol.longestPalindrome(s="a"), 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()

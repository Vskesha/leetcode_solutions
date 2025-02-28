import unittest


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_repeatedSubstringPattern_1(self):
        print("Test repeatedSubstringPattern 1... ", end="")
        self.assertTrue(self.sol.repeatedSubstringPattern("abab"))
        print("OK")

    def test_repeatedSubstringPattern_2(self):
        print("Test repeatedSubstringPattern 2... ", end="")
        self.assertFalse(self.sol.repeatedSubstringPattern("aba"))
        print("OK")

    def test_repeatedSubstringPattern_3(self):
        print("Test repeatedSubstringPattern 3... ", end="")
        self.assertTrue(self.sol.repeatedSubstringPattern("abcabcabcabc"))
        print("OK")


if __name__ == "__main__":
    unittest.main()

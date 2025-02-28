import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_reverse_words1(self):
        print("Test reverseWords 1... ", end="")
        self.assertEqual(self.sol.reverseWords(s="the sky is blue"), "blue is sky the")
        print("OK")

    def test_reverse_words2(self):
        print("Test reverseWords 2... ", end="")
        self.assertEqual(self.sol.reverseWords(s="  hello world  "), "world hello")
        print("OK")

    def test_reverse_words3(self):
        print("Test reverseWords 3... ", end="")
        self.assertEqual(self.sol.reverseWords(s="a good   example"), "example good a")
        print("OK")


if __name__ == "__main__":
    unittest.main()

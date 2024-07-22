import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        ans = ""

        for i in range(ls):
            for r in range(i, i + 2):
                l = i
                while l >= 0 and r < ls and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > len(ans):
                    ans = s[l + 1 : r]

        return ans


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        max_len = 0
        start, stop = 0, 0
        for i in range(ls):
            for d in range(2):
                b, e = i, i + d
                while b >= 0 and e < ls and s[b] == s[e]:
                    b -= 1
                    e += 1
                b += 1
                if max_len < e - b:
                    max_len = e - b
                    start, stop = b, e

        return s[start:stop]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_longestPalindrome_1(self):
        print("Test longestPalindrome 1 ... ", end="")
        self.assertEqual("bab", self.sol.longestPalindrome(s="babad"))
        print("OK")

    def test_longestPalindrome_2(self):
        print("Test longestPalindrome 2 ... ", end="")
        self.assertEqual("bb", self.sol.longestPalindrome(s="cbbd"))
        print("OK")


if __name__ == "__main__":
    unittest.main()

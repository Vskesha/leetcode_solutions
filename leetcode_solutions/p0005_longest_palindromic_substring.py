import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        ans = ""

        for i in range(ls):
            for ri in range(i, i + 2):
                li = i
                while li >= 0 and ri < ls and s[li] == s[ri]:
                    li -= 1
                    ri += 1
                if ri - li - 1 > len(ans):
                    ans = s[li + 1 : ri]

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

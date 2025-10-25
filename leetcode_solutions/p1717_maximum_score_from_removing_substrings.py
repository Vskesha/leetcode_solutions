import unittest


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pr = npr = ans = 0
        c1, c2 = "a", "b"
        if y > x:
            c1, c2 = c2, c1
            y, x = x, y

        for c in s:
            if c == c1:
                pr += 1
            elif c == c2:
                if pr:
                    pr -= 1
                    ans += x
                else:
                    npr += 1
            else:
                ans += min(pr, npr) * y
                pr = npr = 0
        ans += min(pr, npr) * y

        return ans


class Solution2:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = i = 0
        ls = len(s)
        c1 = "a"
        if y > x:
            c1 = "b"
            y, x = x, y

        while i < ls:
            pr = npr = 0
            while i < ls and s[i] in "ab":
                if s[i] == c1:
                    pr += 1
                elif pr:
                    pr -= 1
                    ans += x
                else:
                    npr += 1
                i += 1
            ans += min(pr, npr) * y
            while i < ls and s[i] not in "ab":
                i += 1

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maximum_gain_1(self):
        print("Test maximumGain 1... ", end="")
        self.assertEqual(self.sol.maximumGain(s="cdbcbbaaabab", x=4, y=5), 19)
        print("OK")

    def test_maximum_gain_2(self):
        print("Test maximumGain 2... ", end="")
        self.assertEqual(
            self.sol.maximumGain(s="aabbaaxybbaabb", x=5, y=4), 20
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

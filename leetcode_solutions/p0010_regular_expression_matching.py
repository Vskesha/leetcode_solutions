import unittest
from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        def eq(ch1: str, ch2: str) -> bool:
            return ch1 == ch2 or ch2 == "."

        @lru_cache(None)
        def dfs(i: int, j: int) -> bool | None:
            if j == -1:
                return i == -1

            elif i == -1:
                return dfs(i, j - 2) if p[j] == "*" else False

            elif p[j] == "*":
                if dfs(i, j - 2):
                    return True
                if eq(s[i], p[j - 1]) and dfs(i - 1, j):
                    return True

            elif eq(s[i], p[j]) and dfs(i - 1, j - 1):
                return True
            else:
                return False

        return dfs(len(s) - 1, len(p) - 1)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_match_1(self) -> None:
        print("Test isMatch 1... ", end="")
        self.assertFalse(self.sol.isMatch(s="aa", p="a"))
        print("OK")

    def test_is_match_2(self) -> None:
        print("Test isMatch 2... ", end="")
        self.assertTrue(self.sol.isMatch(s="aa", p="a*"))
        print("OK")

    def test_is_match_3(self) -> None:
        print("Test isMatch 3... ", end="")
        self.assertTrue(self.sol.isMatch(s="ab", p=".*"))
        print("OK")

    def test_is_match_4(self) -> None:
        print("Test isMatch 4... ", end="")
        self.assertTrue(self.sol.isMatch(s="aab", p="c*a*b"))
        print("OK")


if __name__ == "__main__":
    unittest.main()

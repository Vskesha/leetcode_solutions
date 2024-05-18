from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def eq(ch1, ch2):
            return ch1 == ch2 or ch2 == "."

        @lru_cache(None)
        def dfs(i, j) -> bool:

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


def test_is_match():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.isMatch(s="aa", p="a") is False
    print("OK")

    print("Test 2... ", end="")
    assert sol.isMatch(s="aa", p="a*") is True
    print("OK")

    print("Test 3... ", end="")
    assert sol.isMatch(s="ab", p=".*") is True
    print("OK")

    print("Test 4... ", end="")
    assert sol.isMatch(s="aab", p="c*a*b") is True
    print("OK")


if __name__ == "__main__":
    test_is_match()

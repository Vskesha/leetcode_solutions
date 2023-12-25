from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        a, b = 1, 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] in "12":
                    a, b = b, a
                else:
                    return 0
            elif 10 < int(s[i - 1] + s[i]) < 27:
                a, b = b, a + b
            else:
                a, b = b, b

        return b


class Solution2:
    def numDecodings(self, s: str) -> int:
        ls = len(s)
        dp = [1] * (ls + 1)
        if s[0] == "0":
            return 0

        for i in range(1, ls):
            if s[i] == "0":
                if s[i - 1] in "12":
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            elif 10 < int(s[i - 1] + s[i]) < 27:
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]

        return dp[-1]


class Solution3:
    def numDecodings(self, s: str) -> int:
        ls = len(s)
        dp = [0] * ls

        if s[0] == "0":
            return 0
        dp[0] = 1

        if ls > 1:
            if s[1] != "0":
                dp[1] += 1
            if 9 < int(s[:2]) < 27:
                dp[1] += 1

        for i in range(2, ls):
            if s[i] != "0":
                dp[i] += dp[i - 1]
            if 9 < int(s[i - 1 : i + 1]) < 27:
                dp[i] += dp[i - 2]

        return dp[-1]


class Solution4:
    def numDecodings(self, s: str) -> int:
        ls = len(s)

        @cache
        def dp(i):
            if i == 1:
                return int(s[0] != "0")
            if not i:
                return 1
            if s[i - 1] == "0":
                if s[i - 2] in "12":
                    return dp(i - 2)
                else:
                    return 0
            elif 10 < int(s[i - 2 : i]) < 27:
                return dp(i - 2) + dp(i - 1)
            else:
                return dp(i - 1)

        return dp(ls)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numDecodings(s="12") == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.numDecodings(s="226") == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.numDecodings(s="06") == 0
    print("OK")

    print("Test 4... ", end="")
    assert sol.numDecodings(s="2101") == 1
    print("OK")


if __name__ == "__main__":
    test()

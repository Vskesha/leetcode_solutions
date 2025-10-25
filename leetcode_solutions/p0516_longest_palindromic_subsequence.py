class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ls = len(s)
        rs = s[::-1]
        dp = [0] * (ls + 1)

        for i in range(ls):
            new = [0]
            for j in range(ls):
                if s[i] == rs[j]:
                    new.append(dp[j] + 1)
                else:
                    new.append(max(dp[j + 1], new[-1]))
            dp = new

        return dp[-1]


class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        ls = len(s)
        rs = s[::-1]
        dp = [0] * (ls + 1)

        for i in range(ls):
            new = [0]
            for j in range(ls):
                new.append(
                    dp[j] + 1 if s[i] == rs[j] else max(dp[j + 1], new[-1])
                )
            dp = new

        return dp[-1]


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.longestPalindromeSubseq(s="bbbab") == 4
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.longestPalindromeSubseq(s="cbbd") == 2
    print("ok")


if __name__ == "__main__":
    test()

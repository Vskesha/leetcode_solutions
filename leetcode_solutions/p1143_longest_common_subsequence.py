class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lt1, lt2 = len(text1), len(text2)
        dp = [0] * (lt2 + 1)
        for i in range(lt1):
            ndp = [0]
            for j in range(lt2):
                if text1[i] == text2[j]:
                    ndp.append(dp[j] + 1)
                else:
                    ndp.append(max(ndp[-1], dp[j + 1]))
            dp = ndp
        return dp[-1]


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        t = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1):
            for j in range(n2):
                t[i + 1][j + 1] = (
                    t[i][j] + 1
                    if text1[i] == text2[j]
                    else max(t[i + 1][j], t[i][j + 1])
                )

        return t[-1][-1]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.longestCommonSubsequence(text1="abcde", text2="ace") == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.longestCommonSubsequence(text1="abc", text2="abc") == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.longestCommonSubsequence(text1="abc", text2="def") == 0
    print("OK")


if __name__ == "__main__":
    test()

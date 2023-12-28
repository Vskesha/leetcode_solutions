from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        e = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4

        @cache
        def f(i, k):
            if i < 0:
                return 0
            r = f(i - 1, k - 1) if k else 9e9
            x = 0
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    x += 1
                elif k == 0:
                    return r
                else:
                    k -= 1
                r = min(r, f(j - 1, k) + e(x))
            return r

        return f(len(s) - 1, k)


class Solution1:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    if j - del_ >= 0:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[l - 1][j - del_]
                            + 1
                            + (
                                3
                                if cnt >= 100
                                else 2
                                if cnt >= 10
                                else 1
                                if cnt >= 2
                                else 0
                            ),
                        )

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]


class Solution2:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        ls = len(s)
        inf = float("inf")

        @cache
        def dp(k, i, pr, lgr):
            if k < 0:
                return inf
            if ls - i <= k:
                return pr + len(lgr)

            without = dp(k - 1, i + 1, pr, lgr)

            if not lgr:
                lgr = s[i]
            elif lgr[0] == s[i]:
                num = 2 if len(lgr) == 1 else int(lgr[1:]) + 1
                lgr = s[i] + str(num)
            else:
                pr += len(lgr)
                lgr = s[i]

            with_ch = dp(k, i + 1, pr, lgr)

            return min(with_ch, without)

        return dp(k, 0, 0, "")


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.getLengthOfOptimalCompression(s="aaabcccd", k=2) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.getLengthOfOptimalCompression(s="aabbaa", k=2) == 2
    print("OK")

    print("Test 3... ", end="")
    assert sol.getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0)
    print("OK")


if __name__ == "__main__":
    test()

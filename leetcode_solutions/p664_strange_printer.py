from functools import lru_cache


# iterative solution
class Solution:
    def strangePrinter(self, s: str) -> int:
        ls = len(s)
        dp = [[0] * ls for _ in range(ls)]

        for ln in range(0, ls):
            for l in range(0, ls - ln):
                r = l + ln
                for j in range(l, r):
                    if s[j] != s[r]:
                        break
                else:
                    dp[l][r] = 0
                    continue

                dp[l][r] = min(dp[j][i] + dp[i + 1][r] for i in range(j, r)) + 1

        return dp[0][ls - 1] + 1


# recursive dp solution
class Solution2:
    def strangePrinter(self, s: str) -> int:

        @lru_cache(None)
        def dp(l, r):
            for j in range(l, r):
                if s[j] != s[r]:
                    break
            else:
                return 0

            min_turn = min(dp(j, i) + dp(i + 1, r) for i in range(j, r))

            return min_turn + 1

        return 1 + dp(0, len(s) - 1)


def main():
    sol = Solution()
    print('2 ===', sol.strangePrinter(s="aaabbb"))
    print('2 ===', sol.strangePrinter(s="aba"))


if __name__ == '__main__':
    main()

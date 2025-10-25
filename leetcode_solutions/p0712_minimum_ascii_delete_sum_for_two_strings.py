# iterative solution
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        l1, l2 = len(s1), len(s2)

        ords1 = [ord(c) for c in s1]
        ords2 = [ord(c) for c in s2]

        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1):
            dp[i + 1][0] = dp[i][0] + ords1[i]
        for j in range(l2):
            dp[0][j + 1] = dp[0][j] + ords2[j]

        for i in range(l1):
            for j in range(l2):
                if ords1[i] == ords2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(
                        dp[i + 1][j] + ords2[j], dp[i][j + 1] + ords1[i]
                    )

        return dp[l1][l2]


def main():
    sol = Solution()
    print("231 ===", sol.minimumDeleteSum(s1="sea", s2="eat"))
    print("403 ===", sol.minimumDeleteSum(s1="delete", s2="leet"))
    print("116 ===", sol.minimumDeleteSum(s1="at", s2="a"))
    print("116 ===", sol.minimumDeleteSum(s1="a", s2="at"))


if __name__ == "__main__":
    main()

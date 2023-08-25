from functools import cache


# iterative dp solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        if l2 > l1:
            s1, l1, s2, l2 = s2, l2, s1, l1

        dp = [False] * (l2 + 1)
        dp[0] = True
        j = 0
        while j < l2 and s2[j] == s3[j]:
            dp[j + 1] = True
            j += 1

        for i in range(l1):
            new_dp = [False] * (l2 + 1)
            new_dp[0] = dp[0] and s1[i] == s3[i]
            for j in range(1, l2 + 1):
                new_dp[j] = (dp[j] and s1[i] == s3[i + j]) or (new_dp[j - 1] and s2[j - 1] == s3[i + j])
            dp = new_dp

        return dp[l2]


# recursive dp solution
class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        @cache
        def dp(i, j) -> bool:
            if i + j == l3:
                return True
            return ((i < l1 and s1[i] == s3[i + j] and dp(i + 1, j)) or
                    (j < l2 and s2[j] == s3[i + j] and dp(i, j + 1)))

        return dp(0, 0)


def main():
    sol = Solution()
    assert sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
    print('Test 1 ... ok')
    assert sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
    print('Test 2 ... ok')
    assert sol.isInterleave(s1="", s2="", s3="")


if __name__ == '__main__':
    main()

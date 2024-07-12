import unittest
from difflib import SequenceMatcher
from functools import cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1) + 1, len(str2) + 1
        i1, i2, ans = n1 - 1, n2 - 1, ""
        str1, str2 = str1.rjust(n1), str2.rjust(n2)
        dp = [[0] * n2 for _ in range(n1)]

        for i1 in range(1, n1):
            for i2 in range(1, n2):
                if str1[i1] == str2[i2]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

        while i1 | i2:
            if not i1 * i2:
                ans += str1[i1] if i1 else str2[i2]
                i2 -= bool(i2)
                i1 -= bool(i1)
            elif str1[i1] == str2[i2]:
                ans += str1[i1]
                i1 -= 1
                i2 -= 1
            elif dp[i1][i2] == dp[i1 - 1][i2]:
                ans += str1[i1]
                i1 -= 1
            else:  # dp[i1][i2] == dp[i1][i2-1]
                ans += str2[i2]
                i2 -= 1
        return ans[::-1]


class Solution2:  # MLE
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        strs = [[""] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(len(str1) + 1):
            for j in range(len(str2) + 1):
                if i == 0:
                    strs[i][j] = str2[:j]
                elif j == 0:
                    strs[i][j] = str1[:i]
                elif str1[i - 1] == str2[j - 1]:
                    strs[i][j] = strs[i - 1][j - 1] + str1[i - 1]
                else:
                    strs[i][j] = min(
                        strs[i - 1][j] + str1[i - 1],
                        strs[i][j - 1] + str2[j - 1],
                        key=len,
                    )
        return strs[-1][-1]


class Solution3:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        matches = SequenceMatcher(None, str1, str2).get_matching_blocks()
        result = ""
        p = (0, 0, 0)  # previous match
        for m in matches:
            result += (
                str1[p[0] + p[2] : m[0]]
                + str2[p[1] + p[2] : m[1]]
                + str1[m[0] : m[0] + m[2]]
            )
            p = m
        return result


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_shortest_common_supersequence_1(self):
        print("Test shortestCommonSupersequence 1... ", end="")
        self.assertEqual(
            len(self.sol.shortestCommonSupersequence(str1="abac", str2="cab")), 5
        )
        print("OK")

    def test_shortest_common_supersequence_2(self):
        print("Test shortestCommonSupersequence 2... ", end="")
        self.assertEqual(
            len(self.sol.shortestCommonSupersequence(str1="aaaaaaaa", str2="aaaaaaaa")),
            8,
        )
        print("OK")

    def test_shortest_common_supersequence_3(self):
        print("Test shortestCommonSupersequence 3... ", end="")
        self.assertEqual(
            len(self.sol.shortestCommonSupersequence(str1="bcacaaab", str2="bbabaccc")),
            13,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

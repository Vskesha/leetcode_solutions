import unittest
from functools import cache


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        ls = len(s)
        k = str(k)
        lk = len(k)
        dp = [0] * (ls + 1)
        dp[-1] = 1
        msk = max(-1, ls - lk)

        for i in range(ls - 1, msk, -1):
            if s[i] != "0":
                for j in range(i + 1, ls + 1):
                    dp[i] = (dp[i] + dp[j]) % mod

        for i in range(msk, -1, -1):
            if s[i] != "0":
                for j in range(i + 1, i + lk):
                    dp[i] = (dp[i] + dp[j]) % mod
                if s[i:i + lk] <= k:
                    dp[i] = (dp[i] + dp[i + lk]) % mod

        return dp[0]


class Solution1:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        ls = len(s)
        k = str(k)
        lk = len(k)
        dp = [0] * (ls + 1)
        dp[-1] = 1

        for i in range(ls - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            for j in range(i + 1, min(ls + 1, i + lk)):
                dp[i] = (dp[i] + dp[j]) % mod
            mx = s[i : i + lk]
            if len(mx) == lk and mx <= k:
                dp[i] = (dp[i] + dp[i + lk]) % mod

        return dp[0]


class Solution2:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        ls = len(s)
        k = str(k)
        lk = len(k)

        @cache
        def dp(i) -> int:
            if i == ls:
                return 1
            if s[i] == "0":
                return 0
            ans = 0
            for j in range(i + 1, min(ls + 1, i + lk)):
                ans = (ans + dp(j)) % mod
            mx = s[i : i + lk]
            if len(mx) == lk and mx <= k:
                ans = (ans + dp(i + lk)) % mod
            return ans

        return dp(0)


class Solution3:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        ls = len(s)

        @cache
        def dp(i) -> int:
            if i == ls:
                return 1
            if s[i] == "0":
                return 0
            ans = n = 0
            for j in range(i, ls):
                n = n * 10 + int(s[j])
                if n > k:
                    break
                ans = (ans + dp(j + 1)) % mod
            return ans

        return dp(0)


class Solution4:
    def numberOfArrays(self, s: str, k: int) -> int:
        l = len(s)
        ml = len(str(k))
        dp = [1] + [0] * l
        for i in range(1, l + 1):
            for w in range(1, min(i, ml) + 1):
                if s[i - w] != "0" and (w < ml or int(s[i - w : i]) <= k):
                    dp[i] += dp[i - w]
                    dp[i] %= 1000000007
        return dp[l]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_number_of_arrays_1(self):
        print("Test numberOfArrays 1... ", end="")
        self.assertEqual(self.sol.numberOfArrays(s="1000", k=10000), 1)
        print("OK")

    def test_number_of_arrays_2(self):
        print("Test numberOfArrays 2... ", end="")
        self.assertEqual(self.sol.numberOfArrays(s="1000", k=10), 0)
        print("OK")

    def test_number_of_arrays_3(self):
        print("Test numberOfArrays 3... ", end="")
        self.assertEqual(self.sol.numberOfArrays(s="1317", k=2000), 8)
        print("OK")

    def test_number_of_arrays_4(self):
        print("Test numberOfArrays 4... ", end="")
        self.assertEqual(self.sol.numberOfArrays(s="1234567890", k=90), 34)
        print("OK")


if __name__ == "__main__":
    unittest.main()

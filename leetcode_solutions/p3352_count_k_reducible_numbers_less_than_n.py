import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        ls = len(s)
        ops = [0] * (ls + 1)
        for n in range(2, ls + 1):
            ops[n] = ops[n.bit_count()] + 1

        fact = [1] * ls
        for i in range(2, ls):
            fact[i] = fact[i - 1] * i % mod

        ifact = [1] * ls
        ifact[ls - 1] = pow(fact[ls - 1], mod - 2, mod)
        for i in range(ls - 1, 2, -1):
            ifact[i - 1] = (ifact[i] * i) % mod

        ans = -1
        tb = 0
        for i, b in enumerate(s, 1):
            if b == "1":
                ln = ls - i
                for bc in range(ln + 1):
                    if ops[tb + bc] < k:
                        ans = (
                            ans + fact[ln] * ifact[bc] * ifact[ln - bc]
                        ) % mod
                tb += 1

        return ans


# Time Limit Exceeded
class Solution5:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        ls = len(s)

        def combs(pref: str, zeros: int, ones: int) -> list[str]:
            if not (zeros or ones):
                return [pref]
            ans = []
            if zeros:
                ans.extend(combs(pref + "0", zeros - 1, ones))
            if ones:
                ans.extend(combs(pref + "1", zeros, ones - 1))
            return ans

        def dp(bn: str, k: int) -> int:
            if len(bn) == ls and bn >= s:
                return 0
            if not k:
                return 1
            n = int(bn, 2)
            if n >= ls:
                return 1
            ans = 1
            zeros = 1 if n == 1 else 0
            while n + zeros <= ls:
                for comb in combs("1", zeros, n - 1):
                    ans += dp(comb, k - 1)
                    ans %= mod
                zeros += 1
            return ans

        ans = dp("1", k)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countKReducibleNumbers"] * 3,
            "kwargs": [
                dict(s="111", k=1),
                dict(s="1000", k=2),
                dict(s="1", k=3),
            ],
            "expected": [3, 6, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

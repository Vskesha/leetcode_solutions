import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    mod = 10**9 + 7
    max_n = 100_000
    fact = [1] * (max_n + 1)
    inv = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    inv[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % mod

    def nCr_mod(self, n, r):
        if r < 0 or r > n:
            return 0
        num = self.fact[n]
        den = (self.inv[r] * self.inv[n - r]) % self.mod
        return (num * den) % self.mod

    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        left_max = min(pos, k)
        rc = n - pos - 1
        right_max = min(rc, k)
        left_min = max(0, k - right_max)

        ans = 0
        for am in range(left_min, left_max + 1):
            lcomb = self.nCr_mod(pos, am)
            rcomb = self.nCr_mod(rc, k - am)
            cmb = (lcomb * rcomb) % self.mod
            ans = (ans + cmb) % self.mod

        return (ans * 2) % self.mod


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countVisiblePeople"] * 3,
            "kwargs": [
                dict(n=3, pos=1, k=0),
                dict(n=3, pos=2, k=1),
                dict(n=1, pos=0, k=0),
            ],
            "expected": [2, 4, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

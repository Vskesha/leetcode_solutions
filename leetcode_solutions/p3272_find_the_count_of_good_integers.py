import unittest
from collections import Counter
from math import factorial

from leetcode_solutions._test_meta import TestMeta


class Solution:
    fact = [1] * 11
    for i in range(2, 11):
        fact[i] = fact[i - 1] * i

    def countGoodIntegers(self, n: int, k: int) -> int:
        n2 = (n + 1) // 2
        st = n % 2
        seen = set()
        ans = 0

        for fh in range(10 ** (n2 - 1), 10**n2):
            sfh = str(fh)
            sn = sfh + sfh[::-1][st:]
            if int(sn) % k == 0:
                key = tuple(sorted(sn))
                if key in seen:
                    continue
                seen.add(key)
                cnt = Counter(sn)
                combs = self.fact[n - 1] * (n - cnt["0"])
                for val in cnt.values():
                    combs //= self.fact[val]
                ans += combs

        return ans


class Solution2:
    def countGoodIntegers(self, n: int, k: int) -> int:
        n2 = (n + 1) // 2
        st = n % 2
        seen = set()
        ans = 0

        for fh in range(10 ** (n2 - 1), 10**n2):
            sfh = str(fh)
            sn = sfh + sfh[::-1][st:]
            if int(sn) % k == 0:
                key = "".join(sorted(sn))
                if key in seen:
                    continue
                seen.add(key)
                cnt = Counter(sn)
                combs = factorial(n - 1) * (n - cnt["0"])
                for val in cnt.values():
                    combs //= factorial(val)
                ans += combs

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countGoodIntegers"] * 3,
            "kwargs": [
                dict(n=3, k=5),
                dict(n=1, k=4),
                dict(n=5, k=6),
            ],
            "expected": [27, 2, 2468],
        },
    ]


if __name__ == "__main__":
    unittest.main()

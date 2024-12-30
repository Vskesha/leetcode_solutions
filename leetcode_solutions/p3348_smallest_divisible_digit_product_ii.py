import unittest
from math import gcd

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        def complement(size, needed):
            ans = []
            for d in range(9, 1, -1):
                while needed % d == 0:
                    ans.append(d)
                    needed //= d
            if len(ans) < size:
                ans.extend([1] * (size - len(ans)))
            return "".join(map(str, reversed(ans)))

        tg = t
        for p in [2, 3, 5, 7]:
            while tg % p == 0:
                tg //= p
        if tg > 1:
            return "-1"

        ln = len(num)
        needs = [0] * (ln + 1)
        needs[0] = t
        for i, n in enumerate(map(int, num)):
            if not n:
                break
            needs[i + 1] = needs[i] // gcd(needs[i], n)
        if needs[-1] == 1:
            return num

        zi = num.find("0") % ln
        for i in range(zi, -1, -1):
            d = int(num[i])
            size = ln - i - 1
            for nd in range(d + 1, 10):
                compl = complement(size, needs[i] // gcd(needs[i], nd))
                if len(compl) == size:
                    res = num[:i] + str(nd) + compl
                    return res

        ans = complement(ln + 1, t)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestNumber"] * 3,
            "kwargs": [
                dict(num="26", t=9),
                dict(num="1234", t=256),
                dict(num="12355", t=50),
                dict(num="11111", t=26),
            ],
            "expected": ["29", "1488", "12355", "-1"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

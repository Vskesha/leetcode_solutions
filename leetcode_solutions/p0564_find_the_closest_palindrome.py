import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        ln = len(n)
        if ln == 1:
            return str(int(n) - 1)

        od = ln % 2
        sns = []

        sfh = n[: (ln + 1) // 2]
        sns.append(sfh + sfh[len(sfh) - od - 1 :: -1])
        fh = int(sfh)
        sfh = str(fh - 1)
        sns.append(sfh + sfh[len(sfh) - od - 1 :: -1])
        sfh = str(fh + 1)
        sns.append(sfh + sfh[len(sfh) - od - 1 :: -1])
        sns.append("9" * (ln - 1))
        sns.append("1" + "0" * (ln - 1) + "1")

        num = int(n)
        ans = min(sns, key=lambda x: (num == (k := int(x)), abs(k - num), k))

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["nearestPalindromic"] * 2,
            "kwargs": [
                dict(n="123"),
                dict(n="1"),
            ],
            "expected": ["121", "034"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

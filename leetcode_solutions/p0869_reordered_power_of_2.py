import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    powers = set()
    pw = 1
    while pw <= 10**9:
        cnt = Counter(str(pw))
        combination = []
        for i in range(10):
            combination.append(cnt[str(i)])
        powers.add(tuple(combination))
        pw *= 2

    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        tpl = tuple(cnt[str(i)] for i in range(10))
        return tpl in self.powers


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["reorderedPowerOf2"] * 2,
            "kwargs": [
                dict(n=1),
                dict(n=10),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

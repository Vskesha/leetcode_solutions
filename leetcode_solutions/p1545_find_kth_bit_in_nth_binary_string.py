import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ls = 1
        while ls < k:
            ls = 2 * ls + 1
        k -= 1
        changes = 0
        while ls > 1:
            ls = ls // 2
            if k == ls:
                changes += 1
                break
            elif k > ls:
                k = 2 * ls - k
                changes += 1
        return str(changes % 2)


class Solution2:
    def findKthBit(self, n: int, k: int) -> str:
        s = [0]
        while len(s) < k:
            s.extend([1] + [1 - n for n in reversed(s)])
        return str(s[k - 1])


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findKthBit"] * 2,
            "kwargs": [
                dict(n=3, k=1),
                dict(n=4, k=11),
            ],
            "expected": ["0", "1"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

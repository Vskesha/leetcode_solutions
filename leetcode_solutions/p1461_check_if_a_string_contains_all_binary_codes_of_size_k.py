import unittest

from leetcode_solutions._test_meta import TestMeta

# fmt: off
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return 2 ** k == len(set(int(s[i : i + k], 2) for i in range(len(s) - k + 1)))  #noqa
# fmt: on


class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ls = len(s)
        if ls <= k:
            return False

        nums = set()
        n = 0
        n2 = 2 ** (k - 1)
        for i in range(k - 1):
            n = n * 2 + int(s[i])
        for i, j in zip(range(k - 1, ls), range(ls)):
            n = n * 2 + int(s[i])
            nums.add(n)
            if s[j] == "1":
                n -= n2
        return len(nums) == 2**k


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["hasAllCodes"] * 3,
            "kwargs": [
                dict(s="00110110", k=2),
                dict(s="0110", k=1),
                dict(s="0110", k=2),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

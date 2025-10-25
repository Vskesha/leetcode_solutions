import unittest
from string import ascii_lowercase

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        ls = len(s)
        fwd = [set() for _ in range(ls)]
        bck = [set() for _ in range(ls)]
        famounts = [0] * ls
        bamounts = [0] * ls

        letters = set()
        amount = 0
        for i, ch in enumerate(s):
            fwd[i] = letters.copy()
            famounts[i] = amount
            if len(letters) == k and ch not in letters:
                letters = {ch}
                amount += 1
            else:
                letters.add(ch)

        letters = set()
        amount = 0
        for i in range(ls - 1, -1, -1):
            ch = s[i]
            bck[i] = letters.copy()
            bamounts[i] = amount
            if len(letters) == k and ch not in letters:
                letters = {ch}
                amount += 1
            else:
                letters.add(ch)

        result = 0
        for i in range(ls):
            for ch in ascii_lowercase:
                if (
                    len(fwd[i]) == k
                    and len(bck[i]) == k
                    and ch not in fwd[i]
                    and ch not in bck[i]
                ):
                    amount = famounts[i] + bamounts[i] + 3
                    result = max(result, amount)
                    break
                elif len(fwd[i] | bck[i] | {ch}) <= k:
                    amount = 1
                    result = max(result, amount)
                else:
                    amount = 2
                    result = max(result, amount)

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxPartitionsAfterOperations"] * 3,
            "kwargs": [
                dict(s = "accca", k = 2),
                dict(s = "aabaab", k = 3),
                dict(s = "xxyz", k = 1),
            ],
            "expected": [3, 1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

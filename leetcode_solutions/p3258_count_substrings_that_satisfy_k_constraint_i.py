import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = {"0": 0, "1": 0}
        st = ans = 0
        for i, ch in enumerate(s):
            cnt[ch] += 1
            while cnt["0"] > k and cnt["1"] > k:
                cnt[s[st]] -= 1
                st += 1
            ans += i - st + 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countKConstraintSubstrings"] * 3,
            "kwargs": [
                dict(s="10101", k=1),
                dict(s="1010101", k=2),
                dict(s="11111", k=1),
            ],
            "expected": [12, 25, 15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

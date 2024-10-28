import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ls = len(s)

        def dp(i: int, seen: set) -> int:
            if i == ls:
                return 0
            ans = 0
            cs = ""
            j = i
            while j < ls - ans:
                cs += s[j]
                if cs not in seen:
                    seen.add(cs)
                    res = dp(j + 1, seen) + 1
                    ans = max(ans, res)
                    seen.remove(cs)
                j += 1
            return ans

        ans = dp(0, set())
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxUniqueSplit"] * 4,
            "kwargs": [
                dict(s="ababccc"),
                dict(s="aba"),
                dict(s="aa"),
                dict(s="wwwzfvedwfvhsww"),
            ],
            "expected": [5, 2, 1, 11],
        },
    ]


if __name__ == "__main__":
    unittest.main()

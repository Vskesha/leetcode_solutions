import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        op = pow(2, n - 1)
        if k > op * 3:
            return ""

        ss = {"d": "abc", "a": "bc", "b": "ac", "c": "ab"}
        prev = "d"
        ans = []
        for _ in range(n):
            part = (k - 1) // op
            k = k - op * part
            op //= 2

            curr = ss[prev][part]
            ans.append(curr)
            prev = curr

        return "".join(ans)

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getHappyString"] * 3,
            "kwargs": [
                dict(n = 1, k = 3),
                dict(n = 1, k = 4),
                dict(n = 3, k = 9),
            ],
            "expected": ["c", "", "cab"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        sm = s.count("1")
        for i in range(len(s) - 1):
            sm += int(s[i]) * (-2) + 1
            ans = max(ans, sm)
        return ans


class Solution1:
    def maxScore(self, s: str) -> int:
        b = -1
        o = z = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                z += 1
                b = max(b, z - o)
            else:
                o += 1
        o += int(s[-1])
        return o + b


class Solution2:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = ans = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, ones + zeros)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxScore"] * 3,
            "kwargs": [
                dict(s="011101"),
                dict(s="00111"),
                dict(s="1111"),
            ],
            "expected": [5, 5, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

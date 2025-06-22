import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxDistance"] * 2,
            "kwargs": [
                dict(s="NWSE", k=1),
                dict(s="NSWWEW", k=3),
            ],
            "expected": [3, 6],
        },
    ]


if __name__ == "__main__":
    unittest.main()

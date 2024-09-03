import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = "".join(str(ord(c) - 96) for c in s)

        for _ in range(k):
            n = str(sum(map(int, n)))

        return int(n)


class Solution2:
    def getLucky(self, s: str, k: int) -> int:
        n = int("".join(str(ord(c) - 96) for c in s))
        while k and n > 9:
            n = sum(map(int, str(n)))
            k -= 1
        return n


class Solution3:
    def getLucky(self, s: str, k: int) -> int:
        n = int("".join(str(ord(c) - 96) for c in s))
        while k and n > 9:
            nn = 0
            while n:
                n, d = divmod(n, 10)
                nn += d
            n = nn
            k -= 1
        return n


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getLucky"] * 3,
            "kwargs": [
                dict(s="iiii", k=1),
                dict(s="leetcode", k=2),
                dict(s="zbax", k=2),
            ],
            "expected": [36, 6, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()

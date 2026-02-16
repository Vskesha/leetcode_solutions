import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = ans * 2 + n % 2
            n //= 2
        return ans


class Solution1:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        return int(b[::-1] + "0" * (32 - len(b)), 2)


class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["reverseBits"] * 2,
            "kwargs": [
                dict(n=43261596),
                dict(n=2147483644),
            ],
            "expected": [964176192, 1073741822],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    pbc = [0] * 1_000_001
    cnt = 0
    for n in range(1, 1_000_001):
        if n.bit_count() in primes:
            cnt += 1
        pbc[n] = cnt

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return self.pbc[right] - self.pbc[left - 1]


class Solution2:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(n.bit_count() in primes for n in range(left, right + 1))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPrimeSetBits"] * 2,
            "kwargs": [
                dict(left=6, right=10),
                dict(left=10, right=15),
            ],
            "expected": [4, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

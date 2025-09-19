import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    SIZE = 100_001
    PRIMES = []

    sieve = [True] * SIZE
    sieve[0] = sieve[1] = False
    for number in range(2, SIZE):
        if sieve[number]:
            PRIMES.append(number)
            for multiple in range(number**2, SIZE, number):
                sieve[multiple] = False

    DIVISORS = [None] * SIZE
    DIVISORS[0] = DIVISORS[1] = {}

    def get_primes(self, number: int) -> dict | None:
        if self.DIVISORS[number] is None:
            if self.sieve[number]:
                self.DIVISORS[number] = {number: 1}
            else:
                for prime in self.PRIMES:
                    if number % prime == 0:
                        primes = self.get_primes(number // prime)
                        primes[prime] = primes.get(prime, 0) + 1
                        self.DIVISORS[number] = primes
                        break

        return self.DIVISORS[number].copy()

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.append(self.get_primes(num))
            while len(res) > 1 and any(key in res[-2] for key in res[-1]):
                for key, value in res[-1].items():
                    if res[-2].get(key, 0) < value:
                        res[-2][key] = value
                res.pop()

        res = [self.get_num_from(primes) for primes in res]
        return res

    def get_num_from(self, primes: dict) -> int:
        num = 1
        for key, value in primes.items():
            num *= pow(key, value)
        return num


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["replaceNonCoprimes"] * 3,
            "kwargs": [
                dict(nums=[6, 4, 3, 2, 7, 6, 2]),
                dict(nums=[2, 2, 1, 1, 3, 3, 3]),
                dict(nums=[287, 41, 49, 287, 899, 23, 23, 20677, 5, 825]),
            ],
            "expected": [
                [12, 7, 6],
                [2, 1, 1, 3],
                [2009, 20677, 825],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

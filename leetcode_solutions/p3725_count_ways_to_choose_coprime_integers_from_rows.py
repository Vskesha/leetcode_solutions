import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        max_val = max(max(row) for row in mat)
        ways = [1] * (max_val + 1)

        for row in mat:
            count = [0] * (max_val + 1)
            for num in row:
                divisor = 1
                while divisor * divisor <= num:
                    if num % divisor == 0:
                        count[divisor] += 1
                        if divisor != num // divisor:
                            count[num // divisor] += 1
                    divisor += 1

            for divisor in range(1, max_val + 1):
                ways[divisor] = (ways[divisor] * count[divisor]) % MOD

        mu = [0] * (max_val + 1)
        mu[1] = 1

        for i in range(1, max_val + 1):
            for j in range(2 * i, max_val + 1, i):
                mu[j] -= mu[i]

        result = 0
        for divisor in range(1, max_val + 1):
            result = (result + mu[divisor] * ways[divisor]) % MOD

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countCoprime"] * 2,
            "kwargs": [
                dict(mat=[[1, 2], [3, 4]]),
                dict(mat=[[2, 2], [2, 2]]),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

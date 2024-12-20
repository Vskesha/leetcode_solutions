import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                j = stack.pop()
                prices[j] -= p
            stack.append(i)

        return prices


class Solution2:
    def finalPrices(self, prices: List[int]) -> List[int]:
        lp = len(prices)
        ans = []

        for i, p in enumerate(prices):
            j = i + 1
            while j < lp and prices[j] > p:
                j += 1
            ans.append(p if j == lp else p - prices[j])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["finalPrices"] * 3,
            "kwargs": [
                dict(prices=[8, 4, 6, 2, 3]),
                dict(prices=[1, 2, 3, 4, 5]),
                dict(prices=[10, 1, 1, 6]),
            ],
            "expected": [[4, 2, 4, 2, 3], [1, 2, 3, 4, 5], [9, 0, 1, 6]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

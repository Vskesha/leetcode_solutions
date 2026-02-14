import unittest
from heapq import heapify, heappop, heapreplace
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if sum((q - 1) // mid + 1 for q in quantities) > n:
                left = mid + 1
            else:
                right = mid
        return right


class Solution2:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        heap = [(-q, q, 1) for q in quantities]
        heapify(heap)

        for _ in range(n - len(quantities)):
            _, q, k = heap[0]
            heapreplace(heap, (-q / (k + 1), q, k + 1))

        _, q, k = heappop(heap)
        return (q - 1) // k + 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimizedMaximum"] * 3,
            "kwargs": [
                dict(n=6, quantities=[11, 6]),
                dict(n=7, quantities=[15, 10, 10]),
                dict(n=1, quantities=[100000]),
            ],
            "expected": [3, 5, 100000],
        },
    ]


if __name__ == "__main__":
    unittest.main()

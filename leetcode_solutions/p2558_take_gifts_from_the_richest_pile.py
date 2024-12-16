import unittest
from heapq import heapify, heappush, heappop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapify(heap)
        for _ in range(k):
            heappush(heap, -int((-heappop(heap)) ** 0.5))
        return -sum(heap)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["pickGifts"] * 2,
            "kwargs": [
                dict(gifts=[25, 64, 9, 4, 100], k=4),
                dict(gifts=[1, 1, 1, 1], k=4),
            ],
            "expected": [29, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

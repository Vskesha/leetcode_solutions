import unittest
from heapq import heapify, heapreplace
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        ans = 0

        for _ in range(k):
            ans -= heap[0]
            heapreplace(heap, -((-heap[0] - 1) // 3 + 1))

        return ans


class Solution2:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        ans = 0

        for i in range(k):
            if heap[0] == -1:
                return ans + k - i
            ans -= heap[0]
            heapreplace(heap, -((-heap[0] - 1) // 3 + 1))

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxKelements"] * 2,
            "kwargs": [
                dict(nums=[10, 10, 10, 10, 10], k=5),
                dict(nums=[1, 10, 3, 3, 3], k=3),
            ],
            "expected": [50, 17],
        },
    ]


if __name__ == "__main__":
    unittest.main()

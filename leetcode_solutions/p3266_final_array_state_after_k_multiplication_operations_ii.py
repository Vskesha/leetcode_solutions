import unittest
from heapq import heapify, heappushpop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums

        mod = 10**9 + 7
        ln = len(nums)
        max_val = max(nums)
        heap = [(v, i) for i, v in enumerate(nums)]
        heapify(heap)

        counter = 0
        while counter < k:
            v, i = heap[0]
            v *= multiplier
            if v <= max_val:
                heappushpop(heap, (v, i))
                counter += 1
            else:
                break

        heap.sort()
        op, add = divmod(k - counter, ln)

        ans = [0] * ln
        for j, (v, i) in enumerate(heap):
            p = pow(multiplier, op + int(j < add), mod)
            ans[i] = (v * p) % mod

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getFinalState"] * 4,
            "kwargs": [
                dict(nums=[2, 1, 3, 5, 6], k=5, multiplier=2),
                dict(nums=[100000, 2000], k=2, multiplier=1000000),
                dict(nums=[1, 2, 5], k=1, multiplier=2),
                dict(nums=[4, 2, 4], k=3, multiplier=2),
            ],
            "expected": [[8, 4, 6, 5, 6], [999999307, 999999993], [2, 2, 5], [8, 8, 4]],
            "assert_methods": ["assertListEqual"] * 4,
        },
    ]


if __name__ == "__main__":
    unittest.main()

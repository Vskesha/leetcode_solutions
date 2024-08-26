import unittest
from heapq import heapify, heappop, heappush, heappushpop
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


class Solution1:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(v, i) for i, v in enumerate(nums)]
        heapify(h)

        for _ in range(k):
            v, i = heappop(h)
            v *= multiplier
            heappush(h, (v, i))

        ans = [0] * len(nums)
        for v, i in h:
            ans[i] = v

        return ans


class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [[v, i] for i, v in enumerate(nums)]
        heapify(h)

        for _ in range(k):
            vi = heappop(h)
            vi[0] *= multiplier
            heappush(h, vi)

        ans = [0] * len(nums)
        for v, i in h:
            ans[i] = v

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getFinalState"] * 2,
            "kwargs": [
                dict(nums=[2, 1, 3, 5, 6], k=5, multiplier=2),
                dict(nums=[1, 2], k=3, multiplier=4),
            ],
            "expected": [[8, 4, 6, 5, 6], [16, 8]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

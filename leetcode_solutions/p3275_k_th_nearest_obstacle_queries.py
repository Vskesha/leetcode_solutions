import unittest
from heapq import heappop, heappush, heappushpop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans, heap = [], []
        for i, (x, y) in enumerate(queries):
            heappush(heap, -abs(x) - abs(y))
            if len(heap) > k:
                heappop(heap)
            ans.append(-heap[0] if len(heap) == k else -1)
        return ans


class Solution2:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        lq = len(queries)
        ans = [-1] * lq

        if lq < k:
            return ans

        heap = []
        for i in range(k):
            x, y = queries[i]
            d = abs(x) + abs(y)
            heappush(heap, -d)

        ans[k - 1] = -heap[0]

        for i in range(k, lq):
            x, y = queries[i]
            d = abs(x) + abs(y)
            heappushpop(heap, -d)
            ans[i] = -heap[0]

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["resultsArray"] * 2,
            "kwargs": [
                dict(queries=[[1, 2], [3, 4], [2, 3], [-3, 0]], k=2),
                dict(queries=[[5, 5], [4, 4], [3, 3]], k=1),
            ],
            "expected": [[-1, 7, 5, 3], [10, 8, 6]],
            "assert_methods": ["assertListEqual"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

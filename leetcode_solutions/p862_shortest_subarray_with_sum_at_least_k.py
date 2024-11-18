import unittest
from collections import deque
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        heap = []
        ans = ln + 1
        curr = 0

        for i, n in enumerate(nums):
            curr += n
            if curr >= k:
                ans = min(ans, i + 1)
            while heap and curr - heap[0][0] >= k:
                ans = min(ans, i - heappop(heap)[1])
            heappush(heap, (curr, i))

        return ans if ans <= ln else -1


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        q = deque([(0, -1)])
        ans = ln + 1
        curr = 0

        for i, n in enumerate(nums):
            curr += n
            while q and q[-1][0] >= curr:
                q.pop()
            q.append((curr, i))
            while q and curr - q[0][0] >= k:
                ans = min(ans, i - q.popleft()[1])

        return ans if ans <= ln else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["shortestSubarray"] * 4,
            "kwargs": [
                dict(nums=[17, 85, 93, -45, -21], k=150),
                dict(nums=[1], k=1),
                dict(nums=[1, 2], k=4),
                dict(nums=[2, -1, 2], k=3),
            ],
            "expected": [2, 1, -1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

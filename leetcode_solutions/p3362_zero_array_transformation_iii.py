import unittest
from heapq import heapify, heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        heapify(queries)
        taken, prep = [], []

        for i, n in enumerate(nums):
            while queries and queries[0][0] <= i:
                _, r = heappop(queries)
                heappush(prep, -r)
            while taken and taken[0] < i:
                heappop(taken)
            while prep and len(taken) < n:
                r = -heappop(prep)
                if r < i:
                    prep.clear()
                    break
                heappush(taken, r)
            if len(taken) < n:
                return -1

        return len(prep)


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        heapify(queries)
        taken, prepared = [], []

        for i, n in enumerate(nums):
            while queries and queries[0][0] <= i:
                _, r = heappop(queries)
                heappush(prepared, -r)
            while taken and taken[0] < i:
                heappop(taken)
            while prepared and prepared[0] <= -i and len(taken) < n:
                heappush(taken, -heappop(prepared))
            if len(taken) < n:
                return -1

        return len(prepared)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxRemoval"] * 4,
            "kwargs": [
                dict(nums=[0, 0, 3], queries=[[0, 2], [1, 1], [0, 0], [0, 0]]),
                dict(nums=[2, 0, 2], queries=[[0, 2], [0, 2], [1, 1]]),
                dict(
                    nums=[1, 1, 1, 1], queries=[[1, 3], [0, 2], [1, 3], [1, 2]]
                ),
                dict(nums=[1, 2, 3, 4], queries=[[0, 3]]),
            ],
            "expected": [-1, 1, 2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

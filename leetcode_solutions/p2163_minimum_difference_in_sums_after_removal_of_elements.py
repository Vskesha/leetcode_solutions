import unittest
from heapq import heappush, heappushpop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        ln = len(nums) // 3
        diffs = []

        heap = []
        for i in range(ln):
            heappush(heap, -nums[i])

        cur_sum = -sum(heap)
        diffs.append(cur_sum)

        for i in range(ln, 2 * ln):
            num = -nums[i]
            if heap[0] < num:
                cur_sum += heappushpop(heap, num) - num
            diffs.append(cur_sum)

        heap = []
        for i in range(ln * 2, ln * 3):
            heappush(heap, nums[i])

        j = ln
        cur_sum = sum(heap)
        diffs[j] -= cur_sum

        for i in range(ln * 2 - 1, ln - 1, -1):
            j -= 1
            num = nums[i]
            if heap[0] < num:
                cur_sum += num - heappushpop(heap, num)
            diffs[j] -= cur_sum

        return min(diffs)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumDifference"] * 2,
            "kwargs": [
                dict(nums=[3, 1, 2]),
                dict(nums=[7, 9, 5, 8, 1, 3]),
            ],
            "expected": [-1, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from heapq import heapify, heappushpop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        while len(nums) < k:
            nums.append(-float("inf"))
        self.heap = nums[:k]
        heapify(self.heap)
        for i in range(k, len(nums)):
            heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        heappushpop(self.heap, val)
        return self.heap[0]


class KthLargest2:
    def __init__(self, k: int, nums: list[int]):
        self.nums = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)

        if val > self.nums[-1] or len(self.nums) < self.k:
            left, right = 0, len(self.nums)
            while left < right:
                mid = (left + right) // 2
                if self.nums[mid] >= val:
                    left = mid + 1
                else:
                    right = mid
            self.nums.insert(left, val)
            while len(self.nums) > self.k:
                self.nums.pop()
        return self.nums[-1]


class TestKthLargest(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": KthLargest,
            "cls_init_args": [3, [4, 5, 8, 2]],
            "class_methods": ["add", "add", "add", "add", "add"],
            "args": [[3], [5], [10], [9], [4]],
            "expected": [4, 5, 5, 8, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()

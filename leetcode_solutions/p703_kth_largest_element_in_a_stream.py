import unittest
from heapq import heapify, heappushpop
from typing import List


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
            l, r = 0, len(self.nums)
            while l < r:
                mid = (l + r) // 2
                if self.nums[mid] >= val:
                    l = mid + 1
                else:
                    r = mid
            self.nums.insert(l, val)
            while len(self.nums) > self.k:
                self.nums.pop()
        return self.nums[-1]


class TestKthLargest(unittest.TestCase):
    def test_kth_largest(self):
        print("Testing KthLargest ...")

        commands = ["KthLargest", "add", "add", "add", "add", "add"]
        args = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
        expected = [None, 4, 5, 5, 8, 8]

        kth = KthLargest(*args[0])

        for i in range(1, len(commands)):
            print(f"    Test {i}... ", end="")
            res = getattr(kth, commands[i])(*args[i])
            self.assertEqual(res, expected[i])
            print("OK")

        print("Test PASSED!")


if __name__ == "__main__":
    unittest.main()

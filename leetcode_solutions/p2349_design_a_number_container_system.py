import unittest
from collections import defaultdict
from heapq import heappop, heappush

from leetcode_solutions._test_meta import TestMeta


class NumberContainers:

    def __init__(self):
        self.inds = {}
        self.nums = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.inds[index] = number
        heap = self.nums[number]
        heappush(heap, index)

    def find(self, number: int) -> int:
        heap = self.nums[number]
        while heap and self.inds[heap[0]] != number:
            heappop(heap)
        return heap[0] if heap else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null = None
    test_cases = [
        {
            "class": NumberContainers,
            "class_methods": [
                "find",
                "change",
                "change",
                "change",
                "change",
                "find",
                "change",
                "find",
            ],
            "args": [[10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]],
            "expected": [-1, null, null, null, null, 1, null, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

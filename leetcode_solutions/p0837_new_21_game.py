import unittest
from collections import deque
from functools import cache

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        ones = min(n - k + 1, maxPts)
        queue = deque([1] * ones + [0] * (maxPts - ones))
        win_sum = sum(queue)

        for _ in range(k):
            prev = win_sum / maxPts
            win_sum -= queue.pop()
            win_sum += prev
            queue.appendleft(prev)

        return queue[0]


class Solution2:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        @cache
        def probability(points):
            if points >= k:
                return int(points <= n)
            return sum(probability(points + i) for i in range(1, maxPts + 1)) / maxPts

        return probability(0)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["new21Game"] * 4,
            "kwargs": [
                dict(n=10, k=1, maxPts=10),
                dict(n=6, k=1, maxPts=10),
                dict(n=21, k=17, maxPts=10),
                dict(n=185, k=183, maxPts=2),
            ],
            "expected": [1.00000, 0.60000, 0.73278, 1.00000],
            "assert_methods": ["assertAlmostEqualFivePlaces"] * 4,
        },
    ]

    def assertAlmostEqualFivePlaces(self, first, second):
        self.assertAlmostEqual(first, second, places=5)


if __name__ == "__main__":
    unittest.main()

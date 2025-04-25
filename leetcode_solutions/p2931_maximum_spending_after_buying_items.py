import unittest
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:

        m = len(values)
        heap = []

        for i in range(m):
            j = len(values[i]) - 1
            heappush(heap, (values[i][j], i, j))

        ans = 0
        mul = 1
        while heap:
            val, i, j = heappop(heap)
            ans += val * mul
            mul += 1
            if j:
                heappush(heap, (values[i][j - 1], i, j - 1))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxSpending"] * 2,
            "kwargs": [
                dict(values=[[8, 5, 2], [6, 4, 1], [9, 7, 3]]),
                dict(values=[[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]),
            ],
            "expected": [285, 386],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print('Test 1... ', end='')
#     assert sol.maxSpending(values=[[8, 5, 2], [6, 4, 1], [9, 7, 3]]) == 285
#     print('ok')
#
#     print('Test 1... ', end='')
#     assert sol.maxSpending(values=[[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]) == 386
#     print('ok')


# if __name__ == '__main__':
#     test()

import unittest
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def unmarkedSumArray(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        tsum = sum(nums)

        heap = []
        for i, n in enumerate(nums):
            heappush(heap, (n, i))

        deleted = set()
        ans = []
        for idx, q in queries:
            if idx not in deleted:
                deleted.add(idx)
                tsum -= nums[idx]

            while heap and q:
                n, i = heappop(heap)
                if i not in deleted:
                    deleted.add(i)
                    q -= 1
                    tsum -= n

            ans.append(tsum)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["unmarkedSumArray"] * 2,
            "kwargs": [
                dict(
                    nums=[1, 2, 2, 1, 2, 3, 1],
                    queries=[[1, 2], [3, 3], [4, 2]],
                ),
                dict(nums=[1, 4, 2, 3], queries=[[0, 1]]),
            ],
            "expected": [[8, 3, 0], [7]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test_unmarked_sum_array():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.unmarkedSumArray(
#         nums=[1, 2, 2, 1, 2, 3, 1], queries=[[1, 2], [3, 3], [4, 2]]
#     ) == [8, 3, 0]
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.unmarkedSumArray(nums=[1, 4, 2, 3], queries=[[0, 1]]) == [7]
#     print("OK")


# if __name__ == "__main__":
#     test_unmarked_sum_array()

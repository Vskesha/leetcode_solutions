import unittest
from collections import defaultdict
from heapq import heapify, heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        min_pos = inf
        amount = 0
        max_neg = -inf
        sum_pos = sum(nums)

        for n in nums:
            diff = (n ^ k) - n
            if diff >= 0:
                if diff < min_pos:
                    min_pos = diff
                amount += 1
                sum_pos += diff
            elif diff > max_neg:
                max_neg = diff

        if amount % 2 == 0:
            return sum_pos
        return max(sum_pos - min_pos, sum_pos + max_neg)


class Solution1:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        diffs = sorted(((n ^ k) - n for n in nums), reverse=True)
        pairs = (diffs[i] + diffs[i + 1] for i in range(0, len(diffs) - 1, 2))
        return sum(nums) + sum(p for p in pairs if p > 0)


class Solution2:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        ans = sum(nums)
        cost = sorted(((n ^ k) - n for n in nums), reverse=True)

        for i in range(0, len(cost) - 1, 2):
            d = cost[i] + cost[i + 1]
            if d > 0:
                ans += d
            else:
                break

        return ans


class Solution3:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        ans = sum(nums)
        heap = [n - (n ^ k) for n in nums]
        heapify(heap)

        fm, sm = -heappop(heap), -heappop(heap)
        while fm + sm > 0:
            ans += fm + sm
            heappush(heap, fm)
            heappush(heap, sm)
            fm, sm = -heappop(heap), -heappop(heap)

        return ans


class Solution4:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        self.ans = sum(nums)

        cost = [(n ^ k) - n for n in nums]

        graph = defaultdict(set)
        for fr, to in edges:
            graph[fr].add(to)
            graph[to].add(fr)

        def dfs(node, parent):
            graph[node].discard(parent)

            if not graph[node]:
                return

            heap = [-cost[node]]
            for child in graph[node]:
                dfs(child, node)
                heappush(heap, -cost[child])

            while True:
                fm = -heappop(heap)
                sm = -heappop(heap)
                if fm + sm > 0:
                    self.ans += fm + sm
                    heappush(heap, fm)
                    heappush(heap, sm)
                else:
                    cost[node] = fm
                    return

        dfs(0, -1)
        return self.ans


class Solution5:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        heap = [n - (n ^ k) for n in nums]
        heapify(heap)
        ans = sum(nums)

        while len(heap) > 1:
            d = -heappop(heap) - heappop(heap)
            if d > 0:
                ans += d
            else:
                break

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumValueSum"] * 5,
            "kwargs": [
                dict(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]),
                dict(nums=[2, 3], k=7, edges=[[0, 1]]),
                dict(
                    nums=[7, 7, 7, 7, 7, 7],
                    k=3,
                    edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],
                ),
                dict(
                    nums=[5, 8, 4, 6, 3, 8],
                    k=7,
                    edges=[[2, 0], [2, 1], [2, 3], [2, 4], [2, 5]],
                ),
                dict(
                    nums=[0, 1, 2, 0, 1, 2, 5, 0, 2],
                    k=3,
                    edges=[
                        [0, 1],
                        [0, 2],
                        [0, 3],
                        [3, 4],
                        [3, 5],
                        [3, 6],
                        [5, 7],
                        [5, 8],
                    ],
                ),
            ],
            "expected": [6, 9, 42, 48, 25],
        },
    ]


if __name__ == "__main__":
    unittest.main()


# def timeit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"{func.__name__} took {end - start} seconds")
#         return result
#
#     return wrapper


# @timeit
# def test_maximum_value_sum():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.maximumValueSum(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]) == 6
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.maximumValueSum(nums=[2, 3], k=7, edges=[[0, 1]]) == 9
#     print("OK")
#
#     print("Test 3... ", end="")
#     assert (
#             sol.maximumValueSum(
#                 nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
#             )
#             == 42
#     )
#     print("OK")
#
#     print("Test 4... ", end="")
#     assert (
#             sol.maximumValueSum(
#                 nums=[5, 8, 4, 6, 3, 8], k=7, edges=[[2, 0], [2, 1], [2, 3], [2, 4], [2, 5]]
#             )
#             == 48
#     )
#     print("OK")
#
#     print("Test 5... ", end="")
#     assert (
#             sol.maximumValueSum(
#                 nums=[0, 1, 2, 0, 1, 2, 5, 0, 2],
#                 k=3,
#                 edges=[[0, 1], [0, 2], [0, 3], [3, 4], [3, 5], [3, 6], [5, 7], [5, 8]],
#             )
#             == 25
#     )
#     print("OK")

# if __name__ == "__main__":
#     test_maximum_value_sum()

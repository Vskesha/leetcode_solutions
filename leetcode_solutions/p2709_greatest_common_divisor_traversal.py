import math
import unittest
from collections import defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False

        nums = sorted(nums, reverse=True)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    nums[j] *= nums[i]
                    break
            else:
                return False
        return True


class Solution2:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        ln = len(nums)
        prime2index = defaultdict(list)
        index2prime = {}

        for i in range(ln):
            index2prime[i] = self.factors(nums[i])
            for factor in index2prime[i]:
                prime2index[factor].append(i)

        bfs = deque([0])
        visited_indices = set([0])
        visited_primes = set()

        while bfs:
            ci = bfs.popleft()
            for factor in index2prime[ci]:
                if factor in visited_primes:
                    continue
                for i in prime2index[factor]:
                    if i in visited_indices:
                        continue
                    bfs.append(i)
                    visited_indices.add(i)
                visited_primes.add(factor)

        return len(visited_indices) == ln

    def factors(self, num: int) -> set:
        ans = set()
        divisor = 2
        while num > 1:
            if num % divisor == 0:
                ans.add(divisor)
                num //= divisor
            else:
                divisor += 1
        return ans


class DisjointSet:
    def __init__(self, n):
        self.root = list(range(n))
        self.groups = n

    def find(self, node):
        # if node == self.root[node]:
        #     return node
        # self.root[node] = self.find(self.root[node])
        # return self.root[node]
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.groups -= 1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution3:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        ln = len(nums)
        ds = DisjointSet(ln)
        primes = list(map(self.factors, nums))
        for j in range(1, ln):
            for i in range(j):
                if ds.connected(i, j):
                    continue
                if primes[i] & primes[j]:
                    ds.union(i, j)
        return ds.groups == 1

    def factors(self, num: int) -> set:
        ans = set()
        divisor = 2
        while num > 1:
            if num % divisor == 0:
                ans.add(divisor)
                num //= divisor
            else:
                divisor += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canTraverseAllPairs"] * 3,
            "kwargs": [
                dict(nums=[2, 3, 6]),
                dict(nums=[3, 9, 5]),
                dict(nums=[4, 3, 12, 8]),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.canTraverseAllPairs(nums=[2, 3, 6]) is True
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.canTraverseAllPairs(nums=[3, 9, 5]) is False
#     print("OK")
#
#     print("Test 3... ", end="")
#     assert sol.canTraverseAllPairs(nums=[4, 3, 12, 8]) is True
#     print("OK")


# if __name__ == "__main__":
#     test()

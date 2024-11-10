import unittest
from collections import deque
from heapq import heappushpop, heappush
from typing import Optional, List

from leetcode_solutions._test_meta import TestMeta


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        self.dfs(root, heap, k)
        return heap[0] if len(heap) == k else -1

    def dfs(self, node, heap, k) -> int:
        if not node:
            return 0
        left = self.dfs(node.left, heap, k)
        right = self.dfs(node.right, heap, k)
        if left == right:
            ans = left + right + 1
            if len(heap) == k:
                heappushpop(heap, ans)
            else:
                heappush(heap, ans)
            return ans
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def array_to_tree(arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root

    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["kthLargestPerfectSubtree"] * 3,
            "kwargs": [
                dict(root=array_to_tree([5, 3, 6, 5, 2, 5, 7, 1, 8, null, null, 6, 8]), k=2),
                dict(root=array_to_tree([1, 2, 3, 4, 5, 6, 7]), k=1),
                dict(root=array_to_tree([1, 2, 3, null, 4]), k=3),
            ],
            "expected": [3, 7, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import deque
from heapq import heappush, heappushpop
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        lvls = []

        bfs = deque([root])
        while bfs:
            cs = 0
            for _ in range(len(bfs)):
                node = bfs.popleft()
                cs += node.val
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            if len(lvls) == k:
                heappushpop(lvls, cs)
            else:
                heappush(lvls, cs)

        return lvls[0] if len(lvls) == k else -1


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

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["kthLargestLevelSum"] * 2,
            "kwargs": [
                dict(root=array_to_tree([5, 8, 9, 2, 1, 3, 7, 4, 6]), k=2),
                dict(root=array_to_tree([1, 2, None, 3]), k=1),
            ],
            "expected": [13, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

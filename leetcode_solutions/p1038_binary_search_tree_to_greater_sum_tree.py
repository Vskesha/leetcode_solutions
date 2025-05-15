# Definition for a binary tree node.
import unittest
from collections import deque
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"



class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, gs):
            if not node:
                return gs
            node.val += dfs(node.right, gs)
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root


class Solution1:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def dfs(node) -> int:
            if node.right:
                dfs(node.right)
            total[0] += node.val
            node.val = total[0]
            if node.left:
                dfs(node.left)

        total = [0]
        dfs(root)
        return root


class Solution2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        gs = 0

        def dfs(node):
            nonlocal gs
            if node.right:
                dfs(node.right)
            gs += node.val
            node.val = gs
            if node.left:
                dfs(node.left)

        dfs(root)
        return root


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def list_to_tree(arr: List[int]) -> Optional[TreeNode]:
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
            "class_methods": ["bstToGst"] * 2,
            "kwargs": [
                dict(root=list_to_tree([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8])),
                dict(root=list_to_tree([0,null,1])),
            ],
            "expected": [
                list_to_tree([30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]),
                list_to_tree([1,null,1])
            ],
            "assert_methods": ["assertTreeEqual"] * 2,
        },
    ]

    def assertTreeEqual(self, actual, expected):
        if actual and expected:
            self.assertEqual(actual.val, expected.val)
            self.assertTreeEqual(actual.left, expected.left)
            self.assertTreeEqual(actual.right, expected.right)
        else:
            self.assertIsNone(actual)
            self.assertIsNone(expected)


if __name__ == "__main__":
    unittest.main()

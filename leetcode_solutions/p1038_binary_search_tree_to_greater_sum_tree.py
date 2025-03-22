# Definition for a binary tree node.
import unittest
from collections import deque
from typing import List, Optional


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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def list_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
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

    def tree_to_list(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        arr = [root]
        i = li = 0

        while i < len(arr):
            node = arr[i]
            if node:
                arr.append(node.left)
                arr.append(node.right)
                arr[i] = node.val
                li = i
            i += 1

        return arr[: li + 1]

    def test_bst_to_gst_1(self):
        print("Test bstToGst 1... ", end="")
        null = None
        root = [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]
        expected = [
            30,
            36,
            21,
            36,
            35,
            26,
            15,
            null,
            null,
            null,
            33,
            null,
            null,
            null,
            8,
        ]
        self.assertListEqual(
            self.tree_to_list(self.sol.bstToGst(self.list_to_tree(root))), expected
        )
        print("OK")

    def test_bst_to_gst_2(self):
        print("Test bstToGst 2... ", end="")
        null = None
        root = [0, null, 1]
        expected = [1, null, 1]
        self.assertListEqual(
            self.tree_to_list(self.sol.bstToGst(self.list_to_tree(root))), expected
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

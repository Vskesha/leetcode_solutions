# Definition for a binary tree node.
import unittest
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.ans = False

        def dfs(node, parent, lvl):
            if not node:
                return None
            if node.val == x or node.val == y:
                return parent, lvl
            left = dfs(node.left, node, lvl + 1)
            right = dfs(node.right, node, lvl + 1)
            if left and right:
                if left[0] != right[0] and left[1] == right[1]:
                    self.ans = True
                return None
            return left or right

        dfs(root, None, 0)
        return self.ans


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        path, xpath, ypath = [], [], []

        def dfs(node):
            if not node:
                return
            if node.val == x:
                xpath.extend(path)
                return
            if node.val == y:
                ypath.extend(path)
                return
            path.append(node)
            dfs(node.left)
            dfs(node.right)
            path.pop()

        dfs(root)
        if not (xpath and ypath):
            return False
        if len(xpath) != len(ypath):
            return False
        return xpath[-1] != ypath[-1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

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

    def test_isCousins_1(self):
        print("Test isCousins 1... ", end="")
        root = [1, 2, 3, 4]
        x = 4
        y = 3
        root = self.list_to_tree(root)
        self.assertFalse(self.sol.isCousins(root, x, y))
        print("OK")

    def test_isCousins_2(self):
        print("Test isCousins 2... ", end="")
        null = None
        root = [1, 2, 3, null, 4, null, 5]
        x = 5
        y = 4
        root = self.list_to_tree(root)
        self.assertTrue(self.sol.isCousins(root, x, y))
        print("OK")

    def test_isCousins_3(self):
        print("Test isCousins 3... ", end="")
        null = None
        root = [1, 2, 3, null, 4]
        x = 2
        y = 3
        root = self.list_to_tree(root)
        self.assertFalse(self.sol.isCousins(root, x, y))
        print("OK")


if __name__ == "__main__":
    unittest.main()

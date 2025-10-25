import unittest
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def array_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
        """
        Make a tree from an array.
        """
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        queue = deque([root])
        try:
            while queue:
                node = queue.popleft()
                val = next(vals)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                val = next(vals)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        except StopIteration:
            pass

        return root

    def assertIsBST(self, root: Optional[TreeNode]):
        """
        Check if a tree is a BST.
        """
        if not root:
            self.assertIsNone(root)
        if root.left:
            self.assertLess(root.left.val, root.val)
            self.assertIsBST(root.left)
        if root.right:
            self.assertGreater(root.right.val, root.val)
            self.assertIsBST(root.right)

    def test_insert_into_bst_1(self):
        print("Test insertIntoBST 1... ", end="")
        root = [4, 2, 7, 1, 3]
        val = 5
        root = self.array_to_tree(root)
        self.assertIsBST(root)
        root = self.sol.insertIntoBST(root, val)
        self.assertIsBST(root)
        print("OK")

    def test_insert_into_bst_2(self):
        print("Test insertIntoBST 2... ", end="")
        root = [40, 20, 60, 10, 30, 50, 70]
        val = 25
        root = self.array_to_tree(root)
        self.assertIsBST(root)
        root = self.sol.insertIntoBST(root, val)
        self.assertIsBST(root)
        print("OK")

    def test_insert_into_bst_3(self):
        print("Test insertIntoBST 3... ", end="")
        null = None
        root = [4, 2, 7, 1, 3, null, null, null, null, null, null]
        val = 5
        root = self.array_to_tree(root)
        self.assertIsBST(root)
        root = self.sol.insertIntoBST(root, val)
        self.assertIsBST(root)
        print("OK")


if __name__ == "__main__":
    unittest.main()

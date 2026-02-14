from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# it's my solution
class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                break

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            while node.left and node.left.val < low:
                node.left = node.left.right
            dfs(node.left)
            while node.right and node.right.val > high:
                node.right = node.right.left
            dfs(node.right)

        dfs(root)

        return root


# it's not my solution
class Solution2:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return root
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

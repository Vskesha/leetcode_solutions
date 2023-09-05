# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:

        def dfs(p, q):
            if p.val != q.val:
                return False
            if p.left or q.left:
                return dfs(p.left, q.left)
            if p.right or q.right:
                return dfs(p.right, q.right)
            return True

        return dfs(p, q)

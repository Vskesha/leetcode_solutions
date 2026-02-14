from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        bfs = [(root, 0)]
        i = 0
        while i < len(bfs):
            curr, lvl = bfs[i]
            if curr.left:
                curr.left.parent = curr
                bfs.append((curr.left, lvl + 1))
            if curr.right:
                curr.right.parent = curr
                bfs.append((curr.right, lvl + 1))
            i += 1

        max_lvl = bfs[-1][1]
        while i and bfs[i - 1][1] == max_lvl:
            i -= 1

        deepest = [node for node, lvl in bfs[i:]]

        while not all(node == deepest[0] for node in deepest):
            deepest = [node.parent for node in deepest]

        return deepest[0]

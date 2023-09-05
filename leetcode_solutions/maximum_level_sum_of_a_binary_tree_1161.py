from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        bfs = deque([root])
        level, ans = 0, 0
        max_sum = float('-inf')
        while bfs:
            level += 1
            curr_sum = 0
            for _ in range(len(bfs)):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                curr_sum += node.val
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level
        return ans
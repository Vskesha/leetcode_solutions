from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:

        ans = []
        bfs = deque([(root, 1)])

        while bfs:
            node, idx = bfs.popleft()

            if not node:
                continue

            if idx == len(ans):
                ans[-1] = max(ans[-1], node.val)
            else:
                ans.append(node.val)

            bfs.append((node.left, idx + 1))
            bfs.append((node.right, idx + 1))

        return ans
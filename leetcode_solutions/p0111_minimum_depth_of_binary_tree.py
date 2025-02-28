from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        bfs = deque([(root, 1)])

        while bfs:
            curr, depth = bfs.popleft()
            if not (curr.left or curr.right):
                return depth
            if curr.left:
                bfs.append((curr.left, depth + 1))
            if curr.right:
                bfs.append((curr.right, depth + 1))


def main():
    sol = Solution()
    



if __name__ == '__main__':
    main()

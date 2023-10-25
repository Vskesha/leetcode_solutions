from itertools import zip_longest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def inorder(node):
            if not node:
                return
            if not (node.left or node.right):
                yield node.val
            yield from inorder(node.left)
            yield from inorder(node.right)

        for a, b in zip_longest(inorder(root1), inorder(root2)):
            if a != b:
                return False
        return True


class Solution1:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def inorder(node):
            if not node:
                return
            if not (node.left or node.right):
                yield node.val
            yield from inorder(node.left)
            yield from inorder(node.right)

        return list(inorder(root1)) == list(inorder(root2))


class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []

        def traverse(node, lst):
            if not node.left and not node.right:
                lst.append(node.val)
                return
            if node.left:
                traverse(node.left, lst)
            if node.right:
                traverse(node.right, lst)

        traverse(root1, leaves1)
        traverse(root2, leaves2)

        return leaves1 == leaves2


def test():
    sol = Solution()


if __name__ == '__main__':
    test()

from collections import deque
from functools import wraps
from itertools import zip_longest
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
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
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def inorder(node):
            if not node:
                return
            if not (node.left or node.right):
                yield node.val
            yield from inorder(node.left)
            yield from inorder(node.right)

        return list(inorder(root1)) == list(inorder(root2))


class Solution2:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
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


def sol_decor(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def leafSimilar(
            self, root1: Optional[List], root2: Optional[List]
        ) -> bool:
            root1 = self.list2tree(root1)
            root2 = self.list2tree(root2)
            return self.original.leafSimilar(root1, root2)

        def list2tree(self, arr: Optional[List]) -> Optional[TreeNode]:
            if not arr:
                return None

            vals = iter(arr)
            root = TreeNode(next(vals))
            que = deque([root])

            while que:
                node = que.popleft()
                val = next(vals, None)
                if val is not None:
                    node.left = TreeNode(val)
                    que.append(node.left)
                val = next(vals, None)
                if val is not None:
                    node.right = TreeNode(val)
                    que.append(node.right)

            return root

    return Wrapper


def test():
    null = None
    sol = sol_decor(Solution)()

    print("Test 1... ", end="")
    assert (
        sol.leafSimilar(
            root1=[3, 5, 1, 6, 2, 9, 8, null, null, 7, 4],
            root2=[
                3,
                5,
                1,
                6,
                7,
                4,
                2,
                null,
                null,
                null,
                null,
                null,
                null,
                9,
                8,
            ],
        )
        is True
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.leafSimilar(root1=[1, 2, 3], root2=[1, 3, 2]) is False
    print("OK")


if __name__ == "__main__":
    test()

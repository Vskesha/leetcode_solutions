from collections import deque
from functools import wraps
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def diameterOfBinaryTree(self, root: Optional[List]) -> int:
            root = self.list2tree(root)
            return self.original.diameterOfBinaryTree(root)

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


@sol_decorator
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return 0, 0
            d1, h1 = dfs(node.left)
            d2, h2 = dfs(node.right)
            d = h1 + h2
            return max([d, d1, d2]), max(h1, h2) + 1

        return dfs(root)[0]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.diameterOfBinaryTree(root=[1, 2, 3, 4, 5]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.diameterOfBinaryTree(root=[1, 2]) == 1
    print("OK")


if __name__ == "__main__":
    test()

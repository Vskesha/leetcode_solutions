from collections import deque
from functools import wraps
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol_decor(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

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

        def maxAncestorDiff(self, root: Optional[List]) -> int:
            root = self.list2tree(root)
            return self.original.maxAncestorDiff(root)

    return Wrapper


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, low, high):
            if not node:
                return
            if node.val < low:
                low = node.val
                self.ans = max(self.ans, high - low)
            elif node.val > high:
                high = node.val
                self.ans = max(self.ans, high - low)
            dfs(node.left, low, high)
            dfs(node.right, low, high)

        dfs(root, root.val, root.val)

        return self.ans


def test():
    null = None
    sol = sol_decor(Solution)()

    print("Test 1... ", end="")
    assert (
        sol.maxAncestorDiff(
            root=[8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]
        )
        == 7
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxAncestorDiff(root=[1, null, 2, null, 0, 3]) == 3
    print("OK")


if __name__ == "__main__":
    test()

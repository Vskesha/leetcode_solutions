from bisect import bisect_left, bisect_right
from collections import deque
from functools import wraps
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dp(node):
            if not node:
                return 0
            ans = 0
            if low <= node.val <= high:
                ans += node.val
            return dp(node.left) + dp(node.right) + ans

        return dp(root)


class Solution1:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node, vals):
            if not node:
                return
            if node.val > low:
                inorder(node.left, vals)
            if low <= node.val <= high:
                vals.append(node.val)
            if node.val < high:
                inorder(node.right, vals)

        vals = []
        inorder(root, vals)

        return sum(vals)


class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node, vals):
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)

        vals = []
        inorder(root, vals)

        li = bisect_left(vals, low)
        ri = bisect_right(vals, high)
        return sum(vals[li:ri])


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def rangeSumBST(self, root: Optional[List], low: int, high: int) -> int:
            root = self.list2tree(nums=root)
            return self.original.rangeSumBST(root=root, low=low, high=high)

        def list2tree(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            vals = iter(nums)
            root = TreeNode(val=next(vals))
            que = deque([root])

            while que:
                node = que.popleft()
                val = next(vals, None)
                if val is not None:
                    node.left = TreeNode(val=val)
                    que.append(node.left)
                val = next(vals, None)
                if val is not None:
                    node.right = TreeNode(val=val)
                    que.append(node.right)

            return root

    return Wrapper


def test():
    null = None
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.rangeSumBST(root=[10, 5, 15, 3, 7, null, 18], low=7, high=15) == 32
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.rangeSumBST(root=[10, 5, 15, 3, 7, 13, 18, 1, null, 6], low=6, high=10)
        == 23
    )
    print("OK")


if __name__ == "__main__":
    test()

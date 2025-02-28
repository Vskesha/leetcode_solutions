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

        def sumNumbers(self, root: Optional[List]) -> int:
            root = self.list2tree(root)
            return self.original.sumNumbers(root)

        def list2tree(self, nums: Optional[List]) -> Optional[TreeNode]:
            if not nums:
                return None

            vals = iter(nums)
            root = TreeNode(next(vals))
            queue = deque([root])

            while queue:
                node = queue.popleft()
                val = next(vals, None)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                val = next(vals, None)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)

            return root

    return Wrapper


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num=0) -> int:
            if not node:
                return 0
            cnum = num * 10 + node.val
            if node.left or node.right:
                return dfs(node.left, cnum) + dfs(node.right, cnum)
            return cnum

        return dfs(root)


def test_sum_numbers():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.sumNumbers(root=[1, 2, 3]) == 25
    print("OK")

    print("Test 2... ", end="")
    assert sol.sumNumbers(root=[4, 9, 0, 5, 1]) == 1026
    print("OK")


if __name__ == "__main__":
    test_sum_numbers()

from collections import deque
from functools import wraps
from typing import List, Optional


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

        def pseudoPalindromicPaths(self, root: Optional[List]) -> int:
            root = self.list2tree(nums=root)
            return self.original.pseudoPalindromicPaths(root)

        def list2tree(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            vals = iter(nums)
            root = TreeNode(val=next(vals))
            queue = deque([root])

            while queue:
                node = queue.popleft()
                val = next(vals, None)
                if val is not None:
                    node.left = TreeNode(val=val)
                    queue.append(node.left)
                val = next(vals, None)
                if val is not None:
                    node.right = TreeNode(val=val)
                    queue.append(node.right)

            return root

    return Wrapper


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], bitmask: int) -> int:
            bitmask = bitmask ^ 1 << node.val
            if node.left:
                if node.right:
                    return dfs(node.left, bitmask) + dfs(node.right, bitmask)
                else:
                    return dfs(node.left, bitmask)
            else:
                if node.right:
                    return dfs(node.right, bitmask)
                else:
                    return 1 if not bitmask or bin(bitmask).count("1") == 1 else 0

        return dfs(root, 0)


def test():
    null = None
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.pseudoPalindromicPaths(root=[2, 3, 1, 3, 1, null, 1]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.pseudoPalindromicPaths(
            root=[2, 1, 1, 1, 3, null, null, null, null, null, 1]
        )
        == 1
    )
    print("OK")

    print("Test 3... ", end="")
    assert sol.pseudoPalindromicPaths(root=[9]) == 1
    print("OK")


if __name__ == "__main__":
    test()

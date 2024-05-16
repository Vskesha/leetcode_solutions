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

        def evaluateTree(self, root: Optional[List]) -> bool:
            root = self.list2tree(root)
            return self.original.evaluateTree(root)

        def list2tree(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            vals = iter(nums)
            root = TreeNode(next(vals))
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


@sol_decorator
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


def test_evaluate_tree():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.evaluateTree(root=[2, 1, 3, null, null, 0, 1]) is True  # noqa
    print("OK")

    print("Test 2... ", end="")
    assert sol.evaluateTree(root=[0]) is False  # noqa
    print("OK")


if __name__ == "__main__":
    test_evaluate_tree()

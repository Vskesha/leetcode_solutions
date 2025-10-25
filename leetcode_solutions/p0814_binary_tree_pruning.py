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

        def pruneTree(self, root: List) -> List:
            root = self.list_to_tree(root)
            result = self.original.pruneTree(root)
            return self.tree_to_list(result)

        def list_to_tree(self, arr: List) -> Optional[TreeNode]:
            if not arr:
                return None

            vals = iter(arr)
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

        def tree_to_list(self, root: Optional[TreeNode]) -> List:
            if not root:
                return []

            arr, i, li = [root], 0, 0

            while i < len(arr):
                node = arr[i]
                if node:
                    arr.append(node.left)
                    arr.append(node.right)
                    li = i
                    arr[i] = node.val
                i += 1

            return arr[: li + 1]

    return Wrapper


@sol_decorator
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.left or root.right or root.val:
            return root
        else:
            return None


def test_prune_tree():
    null = None
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.pruneTree(root=[1, null, 0, 0, 1]) == [
        1,
        null,
        0,
        null,
        1,
    ]  # noqa
    print("OK")

    print("Test 2... ", end="")
    assert sol.pruneTree(root=[1, 0, 1, 0, 0, 0, 1]) == [
        1,
        null,
        1,
        null,
        1,
    ]  # noqa
    print("OK")

    print("Test 3... ", end="")
    assert sol.pruneTree(root=[1, 1, 0, 1, 1, 0, 1, 0]) == [
        1,
        1,
        0,
        1,
        1,
        null,
        1,
    ]  # noqa
    print("OK")


if __name__ == "__main__":
    test_prune_tree()

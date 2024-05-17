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

        def removeLeafNodes(
                self, root: Optional[List], target: int
        ) -> Optional[List]:
            root = self.list2tree(root)
            result = self.original.removeLeafNodes(root, target)
            return self.tree2list(result)

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

        def tree2list(self, root: Optional[TreeNode]) -> Optional[List]:
            arr = []
            if not root:
                return arr

            arr.append(root)
            i = li = 0

            while i < len(arr):
                node = arr[i]
                if node is not None:
                    arr.append(node.left)
                    arr.append(node.right)
                    arr[i] = node.val
                    li = i
                i += 1

            return arr[:li + 1]

    return Wrapper


@sol_decorator
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root


def test_remove_leaf_nodes():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.removeLeafNodes(root=[1, 2, 3, 2, null, 2, 4], target=2) == [
        1,
        null,
        3,
        null,
        4,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeLeafNodes(root=[1, 3, 3, 3, 2], target=3) == [1, 3, null, null, 2]
    print("OK")

    print("Test 3... ", end="")
    assert sol.removeLeafNodes(root=[1, 2, null, 2, null, 2], target=2) == [1]
    print("OK")


if __name__ == "__main__":
    test_remove_leaf_nodes()

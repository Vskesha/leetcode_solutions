from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Decorator:
    def __init__(self, original):
        self.original = original

    def __call__(self, *args, **kwargs):
        instance = self.original(*args, **kwargs)
        self.originalSmallestFromLeaf = instance.smallestFromLeaf
        instance.smallestFromLeaf = self.smallestFromLeaf
        return instance

    def smallestFromLeaf(self, root: Optional[List]) -> str:
        root = self.list_to_tree(root)
        return self.originalSmallestFromLeaf(root)

    def list_to_tree(self, arr: Optional[List]) -> TreeNode:
        if not arr:
            return None

        vals = iter(arr)
        root = TreeNode(next(vals))
        q = deque([root])
        while q:
            node = q.popleft()
            val = next(vals, None)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(vals, None)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)

        return root


@Decorator
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, suffix):
            ch = chr(node.val + 97)
            suffix = ch + suffix

            if node.left:
                if node.right:
                    left = dfs(node.left, suffix)
                    right = dfs(node.right, suffix)
                    if left + suffix < right + suffix:
                        return left + ch
                    else:
                        return right + ch
                else:
                    return dfs(node.left, suffix) + ch
            else:
                if node.right:
                    return dfs(node.right, suffix) + ch
                else:
                    return ch

        return dfs(root, "")


def test_smallest_from_leaf():
    sol = Solution()
    null = None

    print("Test 1... ", end="")
    assert sol.smallestFromLeaf(root=[0, 1, 2, 3, 4, 3, 4]) == "dba"
    print("OK")

    print("Test 2... ", end="")
    assert sol.smallestFromLeaf(root=[25, 1, 3, 1, 3, 0, 2]) == "adz"
    print("OK")

    print("Test 3... ", end="")
    assert sol.smallestFromLeaf(root=[2, 2, 1, null, 1, 0, null, 0]) == "abc"
    print("OK")


if __name__ == "__main__":
    test_smallest_from_leaf()
